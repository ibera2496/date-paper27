#!/usr/bin/env bash
# ============================================================
#  date/compile.sh -- dual-mode build of the single-file working copy
#    main.pdf            clean submission copy (showcomments=false)
#    main-comments.pdf   annotated review copy (showcomments=true)
#  Same mechanism as the parent tree's compile.sh: flips the
#  showcomments line in comments.tex with sed, restores it on exit.
#  USAGE:  bash compile.sh          (both PDFs + page counts)
#          bash compile.sh clean    (clean PDF only, fastest)
# ============================================================
set -e
cd "$(dirname "$0")"
DRIVER="main"
TOGGLE_FILE="comments.tex"

flip () {
    sed "/compile\.sh targets/s/{showcomments}{[a-z]*}/{showcomments}{$1}/" \
        "$TOGGLE_FILE" > "$TOGGLE_FILE.tmp"
    mv "$TOGGLE_FILE.tmp" "$TOGGLE_FILE"
}
trap 'flip false' EXIT

run_latex () {   # $1 = jobname
    pdflatex -interaction=nonstopmode -jobname="$1" "$DRIVER".tex > /dev/null 2>&1 || true
    bibtex "$1" > /dev/null 2>&1 || true
    pdflatex -interaction=nonstopmode -jobname="$1" "$DRIVER".tex > /dev/null 2>&1 || true
    pdflatex -interaction=nonstopmode -jobname="$1" "$DRIVER".tex > /dev/null 2>&1 || true
    [ -f "$1.pdf" ] || { echo "ERROR: $1.pdf not produced -- see $1.log" >&2; exit 1; }
}

flip false; run_latex "main"
if [ "${1:-}" != "clean" ]; then
    flip true; run_latex "main-comments"; flip false
fi

echo "Page counts:"
for f in main.pdf main-comments.pdf; do
    [ -f "$f" ] && echo "  $f: $(pdfinfo "$f" | awk '/^Pages/{print $2}') pages"
done
echo "Warnings (clean build):"
grep -E "LaTeX Warning: (Reference|Citation)|Overfull \\\\hbox \([0-9.]+pt" main.log | sed 's/^/  /' | head -20
echo "  $(grep -c 'Overfull' main.log) overfull boxes total"
