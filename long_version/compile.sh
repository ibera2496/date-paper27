#!/usr/bin/env bash
# ============================================================
#  compile.sh -- dual-mode LaTeX compile (DATE CAM monitoring paper)
#
#  Produces TWO PDFs from one source tree:
#    1.  "DATE CAM Monitoring - No Comments.pdf"   clean submission copy
#    2.  "DATE CAM Monitoring - With Comments.pdf" annotated review copy
#
#  The showcomments toggle lives in comments.tex and DEFAULTS TO FALSE,
#  so Overleaf (and a plain pdflatex run) gives the clean copy. This
#  script flips it to true for the annotated build, then restores it.
#
#  Note: sed into a temp file, not perl -pi. A perl one-liner with \b
#  in it has silently written a backspace character into a source file
#  on this machine before.
#
#  USAGE:  bash compile.sh
# ============================================================

set -e

DRIVER="00 - DATE CAM Monitoring"      # main .tex file (no extension)
OUTBASE="DATE CAM Monitoring - Main"   # output PDF base name
APPDRIVER="0A - DATE CAM Monitoring Appendices"
APPOUTBASE="DATE CAM Monitoring - Appendices"
ENGINE="pdflatex"
BIB="bibtex"
TOGGLE_FILE="comments.tex"

flip () {   # $1 = false|true ; only the line marked "compile.sh targets"
    sed "/compile\.sh targets/s/{showcomments}{[a-z]*}/{showcomments}{$1}/" \
        "$TOGGLE_FILE" > "$TOGGLE_FILE.tmp"
    mv "$TOGGLE_FILE.tmp" "$TOGGLE_FILE"
}
comments_on ()  { flip true;  }
comments_off () { flip false; }

run_latex () {
    local outname="$1"
    local driver="${2:-$DRIVER}"
    $ENGINE -interaction=nonstopmode -jobname="$outname" "$driver".tex > /dev/null 2>&1 || true
    $BIB "$outname" > /dev/null 2>&1 || true
    $ENGINE -interaction=nonstopmode -jobname="$outname" "$driver".tex > /dev/null 2>&1 || true
    $ENGINE -interaction=nonstopmode -jobname="$outname" "$driver".tex > /dev/null 2>&1 || true
    if [ ! -f "$outname.pdf" ]; then
        echo "ERROR: $outname.pdf was not produced. Check $outname.log" >&2
        exit 1
    fi
}

trap comments_off EXIT      # always leave the source in the clean state

echo "Compiling: $OUTBASE - No Comments.pdf ..."
comments_off
run_latex "$OUTBASE - No Comments"
echo "  -> $OUTBASE - No Comments.pdf"

echo "Compiling: $OUTBASE - With Comments.pdf ..."
comments_on
run_latex "$OUTBASE - With Comments"
echo "  -> $OUTBASE - With Comments.pdf"

echo "Compiling: $APPOUTBASE - No Comments.pdf ..."
comments_off
run_latex "$APPOUTBASE - No Comments" "$APPDRIVER"
echo "  -> $APPOUTBASE - No Comments.pdf"

echo "Compiling: $APPOUTBASE - With Comments.pdf ..."
comments_on
run_latex "$APPOUTBASE - With Comments" "$APPDRIVER"
echo "  -> $APPOUTBASE - With Comments.pdf"

echo ""
echo "Done. Page counts:"
for f in "$OUTBASE - No Comments.pdf" "$OUTBASE - With Comments.pdf" "$APPOUTBASE - No Comments.pdf" "$APPOUTBASE - With Comments.pdf"; do
    if command -v pdfinfo > /dev/null 2>&1; then
        echo "  $f: $(pdfinfo "$f" | awk '/^Pages/{print $2}') pages"
    else
        echo "  $f"
    fi
done
echo "Source left with showcomments = false, ready to commit."
