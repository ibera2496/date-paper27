#!/usr/bin/env python3
"""gen_paper_figs.py -- figures for the DATE draft "Always-on LLM behavior
monitoring as an in-memory search problem" (v1, 2026-08-17).

Outputs, each placed at exactly the size given (IEEEtran two-column,
3.4 in single column / 7.0 in double column). No bbox_inches="tight" on
the placed panels -- figsize IS the placed size.

  figures/fig_kscaling_v1.{png,pdf}   7.0 x 2.9  (double column, Fig. 1)
  figures/fig_grids_v1.{png,pdf}      7.0 x 2.75 (double column, Fig. 4)
  figures/fig_shortlist_v1.{png,pdf}  7.0 x 2.5  (double column, Fig. 5)
  figures/fig_capacity_v1.{png,pdf}   3.4 x 2.6  (single column, Fig. 3)

DATA AND SOURCES
  Cross-domain AUROC grids (fig_grids, fig_shortlist): I. Bera, "CAM
  deception/safety detector -- methods and AUROC findings," 2026-08-14
  (CAM_Detector_Methods_Findings.docx in this folder). Llama-3.3-70B-Instruct,
  layer 33, 10-domain Truthfulness Spectrum grid, 70/30 bank/test split,
  row = training domain, column = test domain. Real cluster runs.
  Grids are read from that document verbatim (see GRIDS below).

  Bandwidth arithmetic (fig_kscaling, fig_capacity): arithmetic, not
  measurement. Bytes moved for monitoring per second = K * d * 2 bytes *
  tok/s at fp16. d = 8,192 (Llama-3.3-70B residual width); 1,000 tok/s
  assumed. CAM line is the query broadcast only, 16 KB/token at fp16.
  Vendor bandwidth figures: NVIDIA H100 SXM 3.35 TB/s, A100 80GB 2.0 TB/s,
  Jetson Thor 273 GB/s LPDDR5X, Jetson AGX Orin 204.8 GB/s. On-chip
  capacity markers: Jetson-class ~4 MB shared L2 (vendor spec),
  H100 50 MB L2 (vendor spec). These are ESTIMATES of monitoring traffic,
  not measured kernel throughput.

  Code widths (fig_capacity): 384 and 2,048 bits are the code widths
  measured in the detector study above; fp16 row = 8,192 x 2 B.

Style: house style, per house-graphs skill (Set1 series colors, Helvetica
with Liberation/DejaVu fallback on Linux, transparent background,
y-grid at 10% black, muted spines, direct labels rather than legends
where a panel is small).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.ticker import LogLocator

# ---- house palette -------------------------------------------------
RED = "#E41A1C"; BLUE = "#377EB8"; GREEN = "#4DAF4A"
PURPLE = "#984EA3"; ORANGE = "#FF7F00"
INK = "#1E293B"; MUTED = "#64748B"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "Liberation Sans", "DejaVu Sans"],
    "mathtext.fontset": "dejavusans",
    "axes.axisbelow": True,
})
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)


def finish(fig, name):
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=300, transparent=True)
    plt.close(fig)
    print("wrote", name)


def spines(ax, drop=("top", "right")):
    for s in drop:
        ax.spines[s].set_visible(False)
    for s in ax.spines.values():
        if s.get_visible():
            s.set_color(MUTED); s.set_linewidth(0.6)
    ax.tick_params(labelsize=6.4, colors=INK, length=2, pad=1.5)


# ====================================================================
# Fig. 1 -- monitoring traffic vs library size K
# ====================================================================
D, BY, TOK = 8192, 2, 1000
CAM = D * BY * TOK / 1e9                      # query broadcast only, GB/s
def traffic(K): return K * D * BY * TOK / 1e9  # GB/s

KMAX = 1e6
K = np.logspace(0, 6, 600)
fig, ax = plt.subplots(figsize=(7.0, 2.9))
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(1, KMAX); ax.set_ylim(CAM / 40, traffic(KMAX) * 4)

H100, A100, THOR = 3350.0, 2000.0, 273.0
ax.axhspan(H100, traffic(KMAX) * 4, color="#999999", alpha=0.14, zorder=0)
ax.text(1.4, traffic(KMAX) * 2.4, "more than an H100's entire HBM bandwidth",
        fontsize=6.6, style="italic", color=MUTED, va="top", zorder=3)

ax.plot(K, traffic(K), color=RED, lw=2.0, zorder=5)
ax.axhline(CAM, color=GREEN, lw=2.0, zorder=5)
ax.text(6.0, traffic(6.0) * 5.0,
        "GPU: the bank streams from HBM every token\n(linear in $K$)",
        color=RED, fontsize=7.0, fontweight="bold", rotation=27,
        rotation_mode="anchor", ha="left", va="bottom", linespacing=1.2, zorder=6)
ax.text(1.3e2, CAM * 1.5, "CAM: query broadcast only (flat in $K$)",
        color=GREEN, fontsize=7.0, fontweight="bold", va="bottom", zorder=6)

for y, lbl, col, va, fy in ((H100, "H100  3.35 TB/s", "#606060", "bottom", 1.15),
                            (A100, "A100  2.0 TB/s", "#606060", "top", 0.84),
                            (THOR, "Jetson Thor  273 GB/s", "#606060", "bottom", 1.15)):
    ax.axhline(y, color="#787878", ls=(0, (5, 3)), lw=1.0, zorder=4)
    ax.text(1.4, y * fy, lbl, color="#606060", fontsize=6.4, va=va, zorder=6)

for ceil, dx, dy, ha in ((H100, 0.80, 4.0, "right"), (THOR, 1.35, 1.9, "left")):
    kx = ceil / (D * BY * TOK / 1e9)
    ax.plot([kx], [ceil], marker="o", ms=5.5, mfc="white", mec=PURPLE, mew=1.6, zorder=7)
    ax.annotate(f"crossing at $K\\approx${kx/1e3:.0f}K", xy=(kx, ceil),
                xytext=(kx * dx, ceil * dy), color=PURPLE,
                fontsize=6.8, fontweight="bold", ha=ha, zorder=7)

pts = ((1, "deployed today:\n$K$ = 1", 0.42, "left", 1.4),
       (500, "4 observed behaviors $\\times$\ndomains $\\times$ layers", 0.10, "left", 1.35),
       (4096, "safety slice of an\nSAE dictionary", 0.42, "left", 1.35),
       (128256, "J-space: one row per\nvocabulary word", 0.10, "right", 0.80))
for kx, lbl, yf, ha, xf in pts:
    ax.axvline(kx, color=BLUE, ls=(0, (1, 2.2)), lw=0.9, zorder=2)
    ax.plot([kx], [traffic(kx)], marker="o", ms=4.5, mfc="white", mec=BLUE, mew=1.4, zorder=7)
    ax.text(kx * xf, CAM * yf, lbl, color=BLUE, fontsize=6.2, fontweight="bold",
            va="top", ha=ha, linespacing=1.2, zorder=6)

ax.set_xlabel("library size $K$   (stored signatures per monitored layer)",
              fontsize=7.4, color=INK)
ax.set_ylabel("monitoring traffic (GB/s)", fontsize=7.4, color=INK)
ax.xaxis.set_major_locator(LogLocator(base=10, numticks=8))
ax.yaxis.set_major_locator(LogLocator(base=10, numticks=8))
ax.grid(True, which="major", color="black", alpha=0.10, lw=0.5)
spines(ax)
fig.tight_layout(pad=0.3)
finish(fig, "fig_kscaling_v1")


# ====================================================================
# Fig. 3 -- what the bank costs to HOLD (capacity), vs. K
# ====================================================================
fig, ax = plt.subplots(figsize=(3.4, 2.6))
ax.set_xscale("log"); ax.set_yscale("log")
Kc = np.logspace(0, 6, 400)
rows = ((8192 * 16, "fp16, $d$ = 8,192", RED, "-"),
        (2048, "2,048-bit code", BLUE, "--"),
        (384, "384-bit code", GREEN, ":"))
for bits, lbl, col, ls in rows:
    ax.plot(Kc, Kc * bits / 8 / 1e6, color=col, lw=1.8, ls=ls, zorder=5)
    ax.text(9.0e5, 9.0e5 * bits / 8 / 1e6 * 2.4, lbl, color=col, fontsize=6.0,
            fontweight="bold", va="bottom", ha="right", zorder=6)
for cap, lbl in ((4.0, "Jetson-class shared L2  $\\sim$4 MB"),
                 (50.0, "H100 L2  50 MB")):
    ax.axhline(cap, color="#787878", ls=(0, (5, 3)), lw=1.0, zorder=3)
    ax.text(1.15, cap * 1.25, lbl, color="#606060", fontsize=6.0, va="bottom", zorder=6)
ax.axvline(128256, color=MUTED, ls=(0, (1, 2.2)), lw=0.9, zorder=2)
ax.text(128256 * 0.85, 3e-4, "J-space", color=MUTED, fontsize=6.0, rotation=90,
        ha="right", va="bottom", zorder=6)
ax.set_xlim(1, 1e6); ax.set_ylim(1e-4, 3e5)
ax.set_xlabel("library size $K$", fontsize=7.4, color=INK)
ax.set_ylabel("bank size per layer (MB)", fontsize=7.4, color=INK)
ax.grid(True, which="major", color="black", alpha=0.10, lw=0.5)
spines(ax)
fig.tight_layout(pad=0.3)
finish(fig, "fig_capacity_v1")


# ====================================================================
# Fig. 4 -- cross-domain AUROC grids
# ====================================================================
LBL = ["defn", "empir", "fict", "logic", "ethic", "syco", "repe", "role", "insid", "sandb"]  # evid -> empir per IB, Sep 17 (item 3)
HERE = os.path.dirname(os.path.abspath(__file__))
G = {n: np.load(os.path.join(HERE, f"{n}.npy"))
     for n in ("ternary384", "thermo384", "twostage_fp")}

cmap = LinearSegmentedColormap.from_list(
    "auroc", ["#F7F7F7", "#C6DBEF", "#6BAED6", "#2171B5", "#08306B"])

panels = ((G["ternary384"], "(a) sign-RP ternary, 384 b\nTCAM cell"),
          (G["thermo384"], "(b) thermometer, 384 b\nbinary CAM cell"),
          (G["twostage_fp"], "(c) Hamming shortlist +\nexact rerank (ceiling)"))
fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.75))
for ax, (M, title) in zip(axs, panels):
    im = ax.imshow(M, vmin=0.2, vmax=1.0, cmap=cmap)
    ax.set_title(title, fontsize=6.6, color=INK, pad=3, linespacing=1.25)
    ax.set_xticks(range(10)); ax.set_yticks(range(10))
    ax.set_xticklabels(LBL, fontsize=4.9, rotation=90, color=INK)
    ax.set_yticklabels(LBL, fontsize=4.9, color=INK)
    ax.tick_params(length=1.2, pad=1.0)
    for s in ax.spines.values():
        s.set_color(MUTED); s.set_linewidth(0.5)
    for i in range(10):
        for j in range(10):
            v = M[i, j]
            lab = "1.0" if v >= 0.995 else f"{v:.2f}"[1:]
            ax.text(j, i, lab, ha="center", va="center", fontsize=3.7,
                    color="white" if v > 0.72 else INK)
axs[0].set_ylabel("training domain", fontsize=6.8, color=INK)
for ax in axs:
    ax.set_xlabel("test domain", fontsize=6.8, color=INK, labelpad=1.5)
cb = fig.colorbar(im, ax=axs, fraction=0.020, pad=0.012)
cb.set_label("AUROC", fontsize=6.4, color=INK)
cb.ax.tick_params(labelsize=5.6, length=1.5, colors=INK)
cb.outline.set_edgecolor(MUTED); cb.outline.set_linewidth(0.5)
finish(fig, "fig_grids_v1")


# ====================================================================
# Fig. 5 -- the shortlist limitation
# ====================================================================
cov_lbl = ["defn", "empir", "fict", "logic", "ethic", "syco", "repe", "role", "insid", "sandb"]
cov_syco = [7.3, 8.6, 3.6, 34.5, 13.8, 100.0, 2.7, 8.1, 0.3, 3.6]
cov_defn = [100.0, 98.9, 98.3, 97.1, 95.2, 72.1, 99.5, 82.6, 14.0, 67.4]
floor_syco, floor_defn = 400 / 3201 * 100, 400 / 831 * 100

frac = [12.5, 25, 50, 75, 100]
rec_syco = [0.532, 0.562, 0.670, 0.738, 0.736]
rec_defn = [0.688, 0.726, 0.750, 0.755, 0.750]

fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.0, 2.5),
                             gridspec_kw={"width_ratios": [1.55, 1.0]})
x = np.arange(10); w = 0.38
a1.bar(x - w / 2, cov_syco, w, color=RED, zorder=3, label="sycophancy bank, $N$ = 3,201")
a1.bar(x + w / 2, cov_defn, w, color=BLUE, zorder=3, label="definitional bank, $N$ = 831")
a1.axhline(floor_syco, color=RED, ls=(0, (4, 2)), lw=1.0, zorder=4)
a1.axhline(floor_defn, color=BLUE, ls=(0, (4, 2)), lw=1.0, zorder=4)
bb = dict(facecolor="white", alpha=0.88, edgecolor="none", pad=0.8)
a1.text(-0.35, floor_syco + 1.5, f"$k/N$ = {floor_syco:.1f}%", color=RED,
        fontsize=5.6, ha="left", va="bottom", zorder=6, bbox=bb)
a1.text(-0.35, floor_defn + 1.5, f"$k/N$ = {floor_defn:.1f}%", color=BLUE,
        fontsize=5.6, ha="left", va="bottom", zorder=6, bbox=bb)
a1.set_xticks(x); a1.set_xticklabels(cov_lbl, fontsize=5.6, rotation=90, color=INK)
a1.set_ylabel("top-1 neighbor inside the\n$k$ = 400 shortlist (%)", fontsize=7.0,
              color=INK, linespacing=1.3)
a1.set_ylim(0, 128)
a1.legend(fontsize=5.8, loc="upper left", bbox_to_anchor=(0.015, 0.995), ncol=2,
          framealpha=0.9, edgecolor="#707070", borderpad=0.4, handlelength=1.2,
          columnspacing=0.9)
a1.set_title("(a) a fixed $k$ does not travel across bank sizes", fontsize=6.6,
             color=INK, pad=3)
a1.grid(True, axis="y", color="black", alpha=0.10, lw=0.5)
spines(a1)

a2.plot(frac, rec_syco, color=RED, lw=1.8, marker="o", ms=4, zorder=5)
a2.plot(frac, rec_defn, color=BLUE, lw=1.8, ls="--", marker="s", ms=4, zorder=5)
a2.text(52, 0.605, "sycophancy", color=RED, fontsize=6.4, fontweight="bold")
a2.text(52, 0.772, "definitional", color=BLUE, fontsize=6.4, fontweight="bold")
a2.set_xlabel("shortlist $k$, as % of that domain's own bank", fontsize=7.0, color=INK)
a2.set_ylabel("cross-domain AUROC (mean)", fontsize=7.0, color=INK)
a2.set_ylim(0.50, 0.80); a2.set_xlim(5, 105)
a2.set_title("(b) it recovers, at the cost of the shortlist", fontsize=6.6,
             color=INK, pad=3)
a2.grid(True, axis="y", color="black", alpha=0.10, lw=0.5)
spines(a2)
fig.tight_layout(pad=0.4)
finish(fig, "fig_shortlist_v1")

print("all figures written to", OUT)


# ====================================================================
#  ADDED 2026-08-21 for v02, per MN: frame K as growing, and bring the
#  J-space results in.
#
#  Fig. 2 -- fig_trajectory_v1: the published record of monitored library
#    size against time. Points are dated publications, listed below with
#    the arithmetic behind each K. NOT a forecast: the dotted guide is
#    drawn through the published points only.
#
#  Fig. 7 -- fig_jspace_v1: J-space (whole-vocabulary readout) fidelity.
#    Panels (a) and (b) are DIGITIZED from slides 20 and 21 of
#    "Most Recent Results.pptx.pdf" (J. Whalen, 2026-07-30); panel (c)
#    from slide 39 of the same deck. Point values were read off the
#    published charts at 200 dpi, then snapped to the powers-of-two the
#    sweep evidently used (D = 128 fixed, bits/dimension swept). They are
#    accurate to roughly +/-0.02 in fidelity. The underlying result files
#    were not available; if they surface, replace DIGITIZED_* below.
#
#    Panel (c) carries three limitations stated on slides 37 and 40 of
#    that deck: an epsilon-inside-sqrt bug zeroed the K = 32 and K = 320
#    points (dropped here), mean-token pooling was used by mistake, and
#    CAM top-k clipping is assumed away (firing is taken to imply
#    selection). Panels (a) and (b) carry no such flags.
# ====================================================================
from matplotlib.lines import Line2D
import matplotlib.dates as mdates
import datetime as _dt

# ---- Fig. 2: the trajectory -----------------------------------------
#  (date, K, label, arithmetic behind K)
TRAJ = [
    ("2025-01-01", 1,      "Constitutional\nclassifiers v1", "text classifiers; K=1 equivalent"),
    ("2025-07-01", 1,      "deployed\n“cheap monitors”", "~0.1% of serving, 1-2 things watched"),
    ("2026-01-15", 1,      "CC++ stage-1 probe\n(all traffic, every token)", "one linear probe over all layers"),
    ("2026-01-20", 1,      "Gemini deployed\nprobes", "one fixed middle layer"),
    ("2026-02-20", 325,    "per-behavior probes\n(Truthfulness Spectrum)", "5 behaviors x 5 domains x 13 layers"),
    ("2026-07-25", 520,    "one evaluation\ncampaign, observed", "4 behaviors x 10 domains x 13 layers"),
    ("2026-07-25", 1000,   None, "...x 25 layers"),
    ("2026-07-06", 128256, "J-space:\none row per vocabulary token", "|V| by construction, per layer"),
]
SAE_BAND = (1.6e7, 3.4e7, "feature dictionaries already published (16M--34M features)")

fig, ax = plt.subplots(figsize=(3.4, 2.8))
ax.set_yscale("log")
D0 = lambda d: mdates.date2num(_dt.date.fromisoformat(d))

for ylev, lbl in ((204000, "H100 HBM crossing"), (17000, "Jetson-class crossing")):
    ax.axhline(ylev, color="#787878", ls=(0, (5, 3)), lw=1.0, zorder=2)
    ax.text(D0("2024-12-20"), ylev * 1.4, lbl, fontsize=5.6, color="#606060",
            va="bottom", zorder=6)

ax.axhspan(SAE_BAND[0], SAE_BAND[1], color=PURPLE, alpha=0.13, zorder=0)
ax.text(D0("2024-12-20"), 2.3e7, "feature dictionaries, published 2024",
        fontsize=5.6, color=PURPLE, va="center", zorder=6)

# the published record, as an arrow between its endpoints. Not a fit.
ax.annotate("", xy=(D0("2026-07-06"), 1.0e5), xytext=(D0("2026-01-15"), 1.3),
            zorder=3,
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.6, alpha=0.55,
                            connectionstyle="arc3,rad=-0.12"))
PTS = (("2025-01-15", 1, "deployed activation\nmonitors: $K$ = 1", "left", 12, 7.0),
       ("2026-01-15", 1, None, None, 0, 1.0),
       ("2026-01-20", 1, None, None, 0, 1.0),
       ("2026-02-20", 325, "per-behavior\nprobes", "right", -12, 1.0),
       ("2026-07-25", 520, None, None, 0, 1.0),
       ("2026-07-25", 1000, "one evaluation campaign,\n4 behaviors observed", "left", 14, 0.55),
       ("2026-07-06", 128256, "J-space: one row per\nvocabulary token", "right", -10, 5.0))
ax.scatter([D0(d) for d, *_ in PTS], [k for _, k, *_ in PTS], s=24, color=BLUE,
           edgecolor="white", linewidth=0.8, zorder=6)
for d, k, lbl, ha, dx, yf in PTS:
    if lbl is None:
        continue
    ax.text(D0(d) + dx, k * yf, lbl, fontsize=5.8, color=BLUE, fontweight="bold",
            ha=ha, va="center", linespacing=1.2, zorder=7)

ax.set_xlim(D0("2024-12-01"), D0("2026-12-31"))
ax.set_ylim(0.45, 1.2e8)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=(4, 7, 10)))
ax.set_ylabel("monitored library size $K$ (rows per layer)", fontsize=7.0, color=INK)
ax.set_xlabel("date of the reported system or result", fontsize=7.0, color=INK)
ax.grid(True, which="major", color="black", alpha=0.10, lw=0.5)
spines(ax)
fig.tight_layout(pad=0.3)
finish(fig, "fig_trajectory_v1")


# ---- Fig. 7: J-space fidelity ---------------------------------------
# storage bits per CAM row -> fidelity. D = 128 held fixed throughout;
# the bits axis is bits/dimension for the quantized methods and the code
# width for the Hamming/sign methods. exact_cosine sits at 8,192 x 16 =
# 131,072 bits, i.e., an uncompressed fp16 row.
DIGITIZED_FIRING_F1 = {           # slide 20
    "lsq_euclidean": ([256, 384, 512, 768, 1024], [0.16, 0.34, 0.51, 0.73, 0.81]),
    "exact_l2_proj": ([1024, 2048, 4096], [0.61, 0.76, 0.84]),
    "hamming":       ([64, 128, 256, 512, 1024, 4096],
                      [0.17, 0.21, 0.30, 0.39, 0.49, 0.21]),
    "thermometer":   ([384, 896, 2048], [0.18, 0.25, 0.34]),
    "direct_sign":   ([4096], [0.21]),
}
DIGITIZED_TOP1 = {                # slide 21
    "lsq_euclidean": ([256, 384, 512, 768, 1024], [0.46, 0.54, 0.66, 0.88, 0.96]),
    "exact_l2_proj": ([2048, 4096], [1.00, 1.00]),
    "hamming":       ([64, 128, 256, 512, 1024, 4096],
                      [0.28, 0.41, 0.53, 0.66, 0.74, 0.16]),
    "thermometer":   ([384, 896, 2048], [0.29, 0.30, 0.40]),
    "direct_sign":   ([4096], [0.11]),
}
# slide 39; K = 32 and K = 320 dropped (epsilon-in-sqrt bug, slide 37/40)
DIGITIZED_SCALING = {
    "trained proj., full precision": ([100, 320, 1000, 3200, 10000],
                                      [0.69, 0.635, 0.527, 0.425, 0.30]),
    "trained proj., 3-bit":          ([100, 1000, 3200, 10000],
                                      [0.755, 0.60, 0.523, 0.43]),
    "fixed SVD proj., 3-bit":        ([100, 1000, 3200, 10000],
                                      [0.34, 0.29, 0.222, 0.15]),
}
STY = {"lsq_euclidean": (RED, "D", "-", "LSQ Euclidean"),
       "exact_l2_proj": (PURPLE, "P", "-", "exact $L_2$, fp16 rows"),
       "hamming":       (BLUE, "o", "--", "Hamming (sign code)"),
       "thermometer":   (GREEN, "s", ":", "thermometer"),
       "direct_sign":   (ORANGE, "X", "", "direct sign hash")}

fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.25))
for ax, (data, ylab, ttl) in zip(
        axs[:2],
        ((DIGITIZED_FIRING_F1, "per-row firing F1", "(a) threshold readout"),
         (DIGITIZED_TOP1, "top-1 agreement with exact J-lens", "(b) top-1 readout"))):
    ax.set_xscale("log")
    for key, (bx, by) in data.items():
        col, mk, ls, lbl = STY[key]
        if ls:
            ax.plot(bx, by, color=col, ls=ls, lw=1.3, marker=mk, ms=3.2, zorder=5)
        else:
            ax.plot(bx, by, color=col, ls="none", marker=mk, ms=4.0, zorder=5)
    ax.axhline(1.0, color=MUTED, ls=(0, (1, 2)), lw=0.9, zorder=3)
    ax.plot([131072], [1.0], marker="*", ms=7, color=INK, zorder=6)
    ax.text(131072, 0.93, "uncompressed\nfp16 row", fontsize=4.9, color=INK,
            ha="right", va="top", linespacing=1.15, zorder=6)
    ax.set_xlim(40, 4e5); ax.set_ylim(0, 1.12)
    ax.set_xlabel("storage bits per CAM row", fontsize=6.6, color=INK)
    ax.set_ylabel(ylab, fontsize=6.6, color=INK)
    ax.set_title(ttl, fontsize=6.6, color=INK, pad=3)
    ax.grid(True, color="black", alpha=0.10, lw=0.5)
    spines(ax)
axs[1].plot([], [])
h = [Line2D([], [], color=STY[k][0], ls=STY[k][2] or "none", marker=STY[k][1],
            ms=3.2, lw=1.3, label=STY[k][3]) for k in
     ("lsq_euclidean", "exact_l2_proj", "hamming", "thermometer", "direct_sign")]
axs[0].legend(handles=h, fontsize=4.8, loc="upper left", bbox_to_anchor=(0.02, 0.99),
              framealpha=0.9, edgecolor="#707070", borderpad=0.35,
              handlelength=1.5, labelspacing=0.28)

ax = axs[2]
ax.set_xscale("log")
SC = ((RED, "-", "o", "trained proj., 3-bit"),
      (BLUE, ":", "^", "trained proj., fp"),
      (GREEN, "--", "s", "fixed SVD proj., 3-bit"))
for (key, (kx, ky)), (col, ls, mk, lbl) in zip(
        (("trained proj., 3-bit", DIGITIZED_SCALING["trained proj., 3-bit"]),
         ("trained proj., full precision", DIGITIZED_SCALING["trained proj., full precision"]),
         ("fixed SVD proj., 3-bit", DIGITIZED_SCALING["fixed SVD proj., 3-bit"])), SC):
    ax.plot(kx, ky, color=col, ls=ls, lw=1.3, marker=mk, ms=3.2, zorder=5, label=lbl)
ax.set_xlim(70, 1.6e4); ax.set_ylim(0, 0.85)
ax.set_xlabel("library size $K$ (tracked vectors)", fontsize=6.6, color=INK)
ax.set_ylabel("per-row macro F1", fontsize=6.6, color=INK)
ax.set_title("(c) fidelity as the library grows", fontsize=6.6, color=INK, pad=3)
ax.legend(fontsize=4.8, loc="lower left", bbox_to_anchor=(0.02, 0.02),
          framealpha=0.9, edgecolor="#707070", borderpad=0.35,
          handlelength=1.5, labelspacing=0.28)
ax.grid(True, color="black", alpha=0.10, lw=0.5)
spines(ax)
fig.tight_layout(pad=0.4)
finish(fig, "fig_jspace_v1")


# ====================================================================
#  ADDED 2026-08-25 for v03, per MN: merge Fig. 1 (trajectory) and
#  Fig. 2 (traffic vs K) into ONE single-column intro figure.
#
#  fig_ladder_v1.{png,pdf}  3.4 x 3.0  (single column, intro Fig. 1)
#
#  Left axis: monitored library size K (published record vs date, same
#  points/sources as fig_trajectory_v1 above). Right axis: the SAME
#  positions read as GPU monitoring traffic in GB/s, via
#  traffic = K * d * 2 B * R  at d = 8,192 (fp16), R = 1,000 tok/s, one
#  monitored layer (Eq. 1 of the paper) -- i.e., 0.016384 GB/s per row.
#  Because traffic is proportional to K, one log axis carries both.
#  Dashed gray ceilings are vendor bandwidths (H100 3.35 TB/s SXM HBM3
#  datasheet; Jetson Thor 273 GB/s LPDDR5X vendor page), which map to
#  K ~= 204K and K ~= 17K at these settings. Green line: CAM query
#  broadcast (16 KB/token = 0.016 GB/s, flat in K; equals the GPU line
#  at exactly K = 1). ESTIMATES: traffic axis is arithmetic on vendor
#  figures, not measured kernel throughput. K points are published
#  values (see TRAJ block above for the arithmetic behind each).
#  Style: house style, per house-graphs skill.
# ====================================================================
GBPR = D * BY * TOK / 1e9         # GB/s per stored row = 0.016384

fig, ax = plt.subplots(figsize=(3.4, 3.0))
ax.set_yscale("log")

YLO, YHI = 0.16, 1.2e8
ax.set_ylim(YLO, YHI)
ax.set_xlim(D0("2024-12-01"), D0("2026-12-31"))

# right axis: GB/s = K * GBPR (proportional, so log decades line up)
sec = ax.secondary_yaxis("right", functions=(lambda k: k * GBPR,
                                             lambda t: t / GBPR))
sec.set_yscale("log")
TICKS = [1e-2, 1e-1, 1, 10, 100, 1000, 1e4, 1e5, 1e6]
TTXT = ["0.01", "0.1", "1", "10", "100", "1K", "10K", "100K", "1M"]
sec.set_yticks(TICKS); sec.set_yticklabels(TTXT)
sec.set_ylabel("GPU monitoring traffic (GB/s) at $10^{3}$ tok/s, one layer",
               fontsize=6.6, color=RED, labelpad=6)
sec.tick_params(labelsize=6.4, colors=RED, length=2, pad=1.5)
sec.spines["right"].set_color(RED); sec.spines["right"].set_linewidth(0.6)

# bandwidth ceilings: bandwidth / GBPR = the crossing K
for bw, lbl in ((3350.0, "H100 HBM  3.35 TB/s"),
                (273.0, "Jetson Thor  273 GB/s")):
    ax.axhline(bw / GBPR, color="#787878", ls=(0, (5, 3)), lw=1.0, zorder=2)
    ax.text(D0("2024-12-20"), bw / GBPR * 1.35, lbl, fontsize=5.6,
            color="#606060", va="bottom", zorder=6)

# CAM query broadcast: flat in K; equals the GPU line at K = 1
ax.axhline(1.0, color=GREEN, lw=1.6, zorder=3)
ax.text(D0("2026-12-10"), 0.72, "CAM: query broadcast only, flat in $K$ (0.016 GB/s)",
        fontsize=5.5, color=GREEN, fontweight="bold", ha="right", va="top",
        zorder=6)

# SAE band
ax.axhspan(SAE_BAND[0], SAE_BAND[1], color=PURPLE, alpha=0.13, zorder=0)
ax.text(D0("2024-12-20"), 2.3e7, "feature dictionaries: $K \\approx 10^{7}$ (2024;\nsafety-readable slice TBD)",
        fontsize=5.6, color=PURPLE, va="center", linespacing=1.2, zorder=6)

# the published record, arrow between endpoints (not a fit)
ax.annotate("", xy=(D0("2026-07-06"), 1.0e5), xytext=(D0("2026-01-15"), 1.3),
            zorder=3,
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.6, alpha=0.55,
                            connectionstyle="arc3,rad=-0.12"))
LPTS = (("2025-01-15", 1, "deployed monitors:\n$K$ = 1", "left", 12, 9.0),
        ("2026-01-15", 1, None, None, 0, 1.0),
        ("2026-01-20", 1, None, None, 0, 1.0),
        ("2026-02-20", 325, "per-behavior probes:\n$K \\approx 10^{2}$", "right", -12, 1.0),
        ("2026-07-25", 520, None, None, 0, 1.0),
        ("2026-07-25", 1000, "one evaluation\ncampaign: $K \\approx 10^{3}$", "right", -12, 1.9),
        ("2026-07-06", 128256, "whole-vocabulary readout:\n$K \\approx 1.3 \\times 10^{5}$", "right", -10, 6.5))
ax.scatter([D0(d) for d, *_ in LPTS], [k for _, k, *_ in LPTS], s=24,
           color=BLUE, edgecolor="white", linewidth=0.8, zorder=6)
for d, k, lbl, ha, dx, yf in LPTS:
    if lbl is None:
        continue
    ax.text(D0(d) + dx, k * yf, lbl, fontsize=5.8, color=BLUE,
            fontweight="bold", ha=ha, va="center", linespacing=1.2, zorder=7)

ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=(4, 7, 10)))
ax.set_ylabel("monitored library size $K$ (rows per layer)", fontsize=7.0,
              color=INK)
ax.set_xlabel("date of the reported system or result", fontsize=7.0, color=INK)
ax.grid(True, which="major", color="black", alpha=0.10, lw=0.5)
spines(ax, drop=("top",))
fig.tight_layout(pad=0.3)
finish(fig, "fig_ladder_v1")


# ====================================================================
#  ADDED 2026-08-28 per MN's hand markup on the v04 printout:
#
#  fig_ladder_v2.{png,pdf}  3.4 x 5.6  (single column, intro Fig. 1)
#
#  Two stacked panels. (a) is fig_ladder_v1 unchanged (see that block's
#  provenance notes). (b) is the new "how GPU bandwidth is consumed"
#  panel MN asked for in pink on Table II and in blue in the intro:
#  library size K vs aggregate token rate R, log-log, with straight
#  lines where monitoring traffic K*R*d*2B equals a stated share of a
#  part's memory bandwidth (K*R = share * BW / (2d bytes)). 100% lines
#  for H100 (3.35 TB/s), A100 (2.0 TB/s), Jetson Thor (273 GB/s), plus
#  10% and 1% of an H100 as gray guides. d = 8,192 (70B geometry),
#  fp16, one monitored layer; divide K by L_mon for the multi-layer
#  case. Marked point: whole-vocabulary K = 1.3e5 at 10^3 tok/s.
#  Token rate is the part's AGGREGATE rate, so batching moves a
#  deployment along the x-axis rather than adding one (per MN's margin
#  question). Arithmetic on vendor bandwidth figures, not measured
#  kernel throughput. Style: house style, per house-graphs skill.
# ====================================================================
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(3.4, 5.45))
gsp = gridspec.GridSpec(3, 1, height_ratios=[0.98, 0.82, 0.34], hspace=0.44)
axa = fig.add_subplot(gsp[0]); axb = fig.add_subplot(gsp[1])
axc = fig.add_subplot(gsp[2])

# ---------------- panel (a): the ladder (as fig_ladder_v1) ----------
ax = axa
ax.set_yscale("log")
YLO, YHI = 0.16, 1.2e8
ax.set_ylim(YLO, YHI)
ax.set_xlim(D0("2024-12-01"), D0("2026-12-31"))
sec = ax.secondary_yaxis("right", functions=(lambda k: k * GBPR,
                                             lambda t: t / GBPR))
sec.set_yscale("log")
TICKS = [1e-2, 1e-1, 1, 10, 100, 1000, 1e4, 1e5, 1e6]
TTXT = ["0.01", "0.1", "1", "10", "100", "1K", "10K", "100K", "1M"]
sec.set_yticks(TICKS); sec.set_yticklabels(TTXT)
sec.set_ylabel("GPU monitoring traffic (GB/s) at $10^{3}$ tok/s, one layer",
               fontsize=6.4, color=RED, labelpad=6)
sec.tick_params(labelsize=6.0, colors=RED, length=2, pad=1.5)
sec.spines["right"].set_color(RED); sec.spines["right"].set_linewidth(0.6)
for bw, lbl in ((3350.0, "H100 HBM  3.35 TB/s"),
                (273.0, "Jetson Thor  273 GB/s")):
    ax.axhline(bw / GBPR, color="#787878", ls=(0, (5, 3)), lw=1.0, zorder=2)
    ax.text(D0("2024-12-20"), bw / GBPR * 1.35, lbl, fontsize=5.4,
            color="#606060", va="bottom", zorder=6)
ax.axhline(1.0, color=GREEN, lw=1.6, zorder=3)
ax.text(D0("2026-12-10"), 0.72, "CAM: query broadcast only, flat in $K$ (0.016 GB/s)",
        fontsize=5.3, color=GREEN, fontweight="bold", ha="right", va="top",
        zorder=6)
ax.axhspan(SAE_BAND[0], SAE_BAND[1], color=PURPLE, alpha=0.13, zorder=0)
ax.text(D0("2024-12-20"), 2.3e7, "feature dictionaries: $K \\approx 10^{7}$ (2024;\nsafety-readable slice TBD)",
        fontsize=5.4, color=PURPLE, va="center", linespacing=1.2, zorder=6)
ax.annotate("", xy=(D0("2026-07-06"), 1.0e5), xytext=(D0("2026-01-15"), 1.3),
            zorder=3,
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.6, alpha=0.55,
                            connectionstyle="arc3,rad=-0.12"))
ax.scatter([D0(d) for d, *_ in LPTS], [k for _, k, *_ in LPTS], s=22,
           color=BLUE, edgecolor="white", linewidth=0.8, zorder=6)
for d, k, lbl, ha, dx, yf in LPTS:
    if lbl is None:
        continue
    ax.text(D0(d) + dx, k * yf, lbl, fontsize=5.6, color=BLUE,
            fontweight="bold", ha=ha, va="center", linespacing=1.2, zorder=7)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=(4, 7, 10)))
ax.set_ylabel("monitored library size $K$ (rows/layer)", fontsize=6.8, color=INK)
ax.set_xlabel("date of the reported system or result", fontsize=6.8,
              color=INK, labelpad=1.5)
ax.grid(True, which="major", color="black", alpha=0.10, lw=0.5)
spines(ax, drop=("top",))
ax.set_title("(a) the published record of $K$", fontsize=7.0, color=INK, pad=3)

# ---------------- panel (b): bandwidth ceilings vs (R, K) -----------
#  Restored Aug 28 pm per MN (preferred over the filled contour, which
#  is now its own figure, fig_contour_v1): straight lines where
#  monitoring consumes 100% of an H100 / A100 / Thor, plus 10% and 1%
#  H100 guides; share = K*R*16384 B / BW at d = 8,192, fp16, one layer.
ax = axb
ax.set_xscale("log"); ax.set_yscale("log")
BYTES_ROW = D * BY                      # 16,384 B per row per token
R = np.logspace(1, 4, 200)
def kline(bw_gbs, share):               # K at which share of bw is consumed
    return share * bw_gbs * 1e9 / (BYTES_ROW * R)
ax.fill_between(R, kline(3350.0, 1.0), 1e8, color="#999999", alpha=0.14,
                zorder=0)
def linelabel(x, bw, share, lbl, col, fs, above=True):
    y = share * bw * 1e9 / (BYTES_ROW * x) * (1.45 if above else 0.62)
    ax.text(x, y, lbl, fontsize=fs, fontweight="bold", color=col,
            rotation=-25, rotation_mode="anchor", ha="left", zorder=6)
for bw, col, ls in ((3350.0, RED, "-"), (2000.0, BLUE, "--"),
                    (273.0, GREEN, ":")):
    ax.plot(R, kline(bw, 1.0), color=col, lw=2.0, ls=ls, zorder=5)
linelabel(1.5e1, 3350.0, 1.0, "100% of H100", RED, 6.0, above=True)
linelabel(2.6e2, 2000.0, 1.0, "100% of A100", BLUE, 6.0, above=False)
linelabel(1.5e1, 273.0, 1.0, "100% of Thor", GREEN, 6.0, above=True)
for share, xl in ((0.10, 6.5e2), (0.01, 1.5e1)):
    ax.plot(R, kline(3350.0, share), color="#787878", lw=1.0,
            ls=(0, (5, 3)), zorder=3)
    y = share * 3350.0 * 1e9 / (BYTES_ROW * xl) * 0.60
    ax.text(xl, y, f"{int(share*100)}% of H100", fontsize=5.4,
            color="#606060", rotation=-25, rotation_mode="anchor",
            ha="left", zorder=6)
ax.plot([1e3], [128256], marker="o", ms=5.5, mfc="white", mec=BLUE,
        mew=1.6, zorder=7)
ax.annotate("whole-vocabulary readout\nat $10^{3}$ tok/s",
            xy=(1e3, 1.28e5), xytext=(1.1e2, 1.1e3), zorder=7,
            fontsize=5.6, color=BLUE, fontweight="bold", ha="left",
            va="top",
            arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8,
                            alpha=0.6))
ax.text(9e3, 4.5e7, "monitoring alone\nexceeds an H100", fontsize=5.6,
        style="italic", color=MUTED, ha="right", va="top", linespacing=1.2,
        zorder=6)
ax.set_xlim(10, 1e4); ax.set_ylim(1e2, 1e8)
ax.set_xticks([10, 100, 1000, 1e4])
ax.set_xticklabels(["10", "100", "1K", "10K"])
ax.set_xlabel("")
ax.set_ylabel("library size $K$ (rows/layer)", fontsize=6.8, color=INK)
ax.grid(True, which="major", color="black", alpha=0.10, lw=0.5)
spines(ax)
ax.set_title("(b) share of GPU memory bandwidth consumed", fontsize=7.0,
             color=INK, pad=3)

# -------- anchor strip: familiar workloads on the token-rate axis ---
#  Ranges are order-of-magnitude anchors (see Sec. III-B for the
#  conversions and citations): voice/chat/reasoning are per-stream
#  decode rates (they batch up to a node's aggregate); edge rows are
#  batch-1, so stream rate = part aggregate. VLA rows from VLA-Perf
#  (NVIDIA Research, arXiv 2602.18397): AR VLA ~3-6 Hz x ~7 action
#  tokens; pi0-class chunked at 19 Hz (Thor) x 50-action chunks.
#  Video: ~30 fps x 1e2-1e3 visual tokens/frame, clipped to the axis.
#  ESTIMATES, flagged as such in the text.
ANCH = [  # (label, lo, hi, row)
    ("voice user",            10,   25,  0),
    ("agentic run",           50,  300,  0),
    ("70B serving node",     1e3, 3e3,   0),
    ("chat user",             30,  100,  1),
    ("video backbone",       3e3, 1e4,   1),
    ("edge assistant",        15,   60,  2),
    ("reasoning stream",      70,  250,  2),
    ("VLA, chunked ($\\pi_0$)", 1e3, 8e3, 2),
    ("VLA, autoregressive",   20,   60,  3),
]
axc.set_xscale("log"); axc.set_xlim(10, 1e4); axc.set_ylim(-0.55, 3.95)
for lbl, lo, hi, row in ANCH:
    y = 3.15 - row
    axc.plot([lo, hi], [y, y], lw=3.2, color=BLUE, alpha=0.55,
             solid_capstyle="butt", zorder=4)
    axc.text((lo * hi) ** 0.5, y + 0.14, lbl, fontsize=4.7, color=INK,
             ha="center", va="bottom", zorder=5)
axc.set_xticks([10, 100, 1000, 1e4])
axc.set_xticklabels(["10", "100", "1K", "10K"])
axc.set_yticks([])
axc.set_xlabel("aggregate token rate (tokens/s)", fontsize=6.8, color=INK,
               labelpad=1.5)
axc.grid(True, axis="x", which="major", color="black", alpha=0.10, lw=0.5)
spines(axc, drop=("top", "right", "left"))
axc.set_title("workload anchors (order-of-magnitude; per-stream rates batch up)",
              fontsize=5.6, color=MUTED, pad=2)

axb.tick_params(labelbottom=True)

fig.tight_layout(pad=0.3)
fig.subplots_adjust(right=0.855)
finish(fig, "fig_ladder_v2")



# ====================================================================
#  ADDED 2026-08-28 pm: fig_contour_v1.{png,pdf}  3.4 x 2.7 (single
#  column, Sec. III; MN wants the filled contour as a SEPARATE figure
#  to look at, may cut later). Filled contours of the share of an
#  H100's HBM bandwidth consumed by monitoring, over (aggregate tok/s,
#  K = 10..1e6), share = K*R*16384 B / 3.35 TB/s (Eq. 2 at d = 8,192,
#  fp16, one monitored layer); decade levels 0.0001%..100%+; A100 and
#  Thor 100% lines overlaid (their fields = this one shifted by the
#  bandwidth ratio). Vendor figures, not measured kernel throughput.
#  Style: house style, per house-graphs skill.
# ====================================================================
fig, ax = plt.subplots(figsize=(3.4, 2.7))
ax.set_xscale("log"); ax.set_yscale("log")
Rv = np.logspace(1, 4, 240)
Kv = np.logspace(1, 6, 240)
RR, KK = np.meshgrid(Rv, Kv)
share_h100 = KK * RR * BYTES_ROW / (3350.0 * 1e9)
Z = np.log10(share_h100 * 100.0)
levels = [-4, -3, -2, -1, 0, 1, 2, 4]
fills = ["#FDEDEC", "#FADBD8", "#F5B7B1", "#F1948A",
         "#EC7063", "#E74C3C", "#C0392B"]
ax.contourf(RR, KK, Z, levels=levels, colors=fills, alpha=0.75, zorder=1)
cl = ax.contour(RR, KK, Z, levels=[-4, -3, -2, -1, 0, 1, 2],
                colors="#606060", linewidths=0.7, zorder=3)
fmt = {-4: "0.0001%", -3: "0.001%", -2: "0.01%", -1: "0.1%", 0: "1%",
       1: "10%", 2: "100% of H100"}
ax.clabel(cl, levels=[-4, -3, -2, -1, 0, 1, 2], fmt=fmt, fontsize=5.0,
          inline=True, inline_spacing=2)
for bw, col, ls, lbl, xl in ((2000.0, BLUE, "--", "100% of A100", 2.6e2),
                             (273.0, GREEN, ":", "100% of Thor", 3.4e1)):
    kk = bw * 1e9 / (BYTES_ROW * Rv)
    ax.plot(Rv, kk, color=col, lw=1.8, ls=ls, zorder=5)
    y = bw * 1e9 / (BYTES_ROW * xl) * 0.58
    ax.text(xl, y, lbl, fontsize=5.6, fontweight="bold", color=col,
            rotation=-25, rotation_mode="anchor", ha="left", zorder=6)
ax.plot([1e3], [128256], marker="o", ms=5.0, mfc="white", mec=BLUE,
        mew=1.5, zorder=7)
ax.annotate("whole-vocabulary readout\nat $10^{3}$ tok/s",
            xy=(1e3, 1.28e5), xytext=(1.15e2, 2.0e3), zorder=7,
            fontsize=5.2, color=BLUE, fontweight="bold", ha="left",
            va="top",
            arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8, alpha=0.7))
ax.text(9e3, 7.2e5, "exceeds an H100", fontsize=5.4, style="italic",
        color="white", ha="right", va="top", zorder=6)
ax.set_xlim(10, 1e4); ax.set_ylim(1e1, 1e6)
ax.set_xticks([10, 100, 1000, 1e4])
ax.set_xticklabels(["10", "100", "1K", "10K"])
ax.set_xlabel("aggregate token rate (tokens/s)", fontsize=6.8, color=INK)
ax.set_ylabel("library size $K$ (rows/layer)", fontsize=6.8, color=INK)
ax.grid(True, which="major", color="black", alpha=0.10, lw=0.5)
spines(ax)
fig.tight_layout(pad=0.3)
finish(fig, "fig_contour_v1")


# ====================================================================
# Fig. 4 v2 (fig_grids_v2) -- one figure, both protocols. Added
# 2026-08-28 per MN ("can we get all of this in 1 figure?").
#
# TOP ROW SOURCE: "CAM and Explainability: What Works and What Doesn't"
# (S. Gisiner, B. Haidinger, J. Whalen), slide 4 ("Signal Can Survive
# Compression"), embedded image transcribed cell-by-cell 2026-08-28.
#   (a) Baseline (Truthfulness Spectrum): the students' rendering of the
#       published four-domain grid (Llama-3.3-70B) -- rows are training
#       domains defn/empirical/fictional/logical plus a combined-training
#       row; columns are test domains.
#   (b) CAM Friendly Classifier: the first pipeline of Sec. IV-A
#       (128-d learned projection, 3-bit LSQ, Euclidean matchline),
#       scored per the deck's footnote "Comparison uses only datasets
#       shared with the Truthfulness Spectrum heatmap."
#   (c) delta = (b) - (a); recomputed here, matches the deck's printed
#       delta panel in all 20 cells.
# Every cell was present in the deck, so no placeholder (white) squares
# were needed. BOTTOM ROW: identical data/rendering to fig_grids_v1.
# ====================================================================
LBL4 = ["defn", "empir", "fict", "logic"]
LBL5 = LBL4 + ["comb"]
BASE = np.array([
    [1.00, 1.00, 0.99, 0.91],
    [0.99, 1.00, 1.00, 0.91],
    [0.99, 1.00, 1.00, 0.90],
    [0.99, 1.00, 0.98, 0.95],
    [1.00, 1.00, 0.99, 0.95],
])
CAMF = np.array([
    [1.00, 0.97, 1.00, 0.87],
    [0.94, 0.99, 0.99, 0.91],
    [0.98, 0.94, 1.00, 0.83],
    [0.96, 0.92, 0.92, 0.95],
    [0.99, 0.91, 0.99, 0.91],
])
DLT = CAMF - BASE

dcmap = LinearSegmentedColormap.from_list(
    "dlt", ["#B2182B", "#F7F7F7", "#2166AC"])


def annot_grid(ax, M, fs, delta=False):
    R, C = M.shape
    for i in range(R):
        for j in range(C):
            v = M[i, j]
            if delta:
                lab = "0" if abs(v) < 0.005 else \
                    f"{v:+.2f}".replace("0.", ".").replace("-", "−")
                col = INK
            else:
                lab = "1.0" if v >= 0.995 else f"{v:.2f}"[1:]
                col = "white" if v > 0.72 else INK
            ax.text(j, i, lab, ha="center", va="center", fontsize=fs,
                    color=col)


def grid_ticks(ax, xl, yl, fs):
    ax.set_xticks(range(len(xl))); ax.set_yticks(range(len(yl)))
    ax.set_xticklabels(xl, fontsize=fs, rotation=90, color=INK)
    ax.set_yticklabels(yl, fontsize=fs, color=INK)
    ax.tick_params(length=1.2, pad=1.0)
    for s in ax.spines.values():
        s.set_color(MUTED); s.set_linewidth(0.5)


fig = plt.figure(figsize=(7.0, 4.10))
gs = fig.add_gridspec(2, 3, height_ratios=[1.0, 1.90],
                      hspace=0.42, wspace=0.30,
                      left=0.065, right=0.895, top=0.945, bottom=0.085)

top = ((BASE, "(a) published baseline\n(Truthfulness Spectrum, 4-domain)",
        cmap, 0.2, 1.0, False),
       (CAMF, "(b) 3-bit LSQ Euclidean\n(first pipeline, shared datasets)",
        cmap, 0.2, 1.0, False),
       (DLT, "(c) fidelity change, (b) $-$ (a)\n(red = \\auroc lost)".replace("\\auroc", "AUROC"),
        dcmap, -0.12, 0.12, True))
ims = []
for k, (M, title, cm, lo, hi, isd) in enumerate(top):
    ax = fig.add_subplot(gs[0, k])
    im = ax.imshow(M, vmin=lo, vmax=hi, cmap=cm)
    if not isd:
        ims.append(im)
    ax.set_title(title, fontsize=6.6, color=INK, pad=3, linespacing=1.25)
    grid_ticks(ax, LBL4, LBL5, 5.4)
    annot_grid(ax, M, 5.0, delta=isd)
    if k == 0:
        ax.set_ylabel("training domain", fontsize=6.8, color=INK)

bottom = ((G["ternary384"], "(d) sign-RP ternary, 384 b\nTCAM cell"),
          (G["thermo384"], "(e) thermometer, 384 b\nbinary CAM cell"),
          (G["twostage_fp"], "(f) Hamming shortlist +\nexact rerank (ceiling)"))
baxs = []
for k, (M, title) in enumerate(bottom):
    ax = fig.add_subplot(gs[1, k])
    im = ax.imshow(M, vmin=0.2, vmax=1.0, cmap=cmap)
    ims.append(im)
    ax.set_title(title, fontsize=6.6, color=INK, pad=3, linespacing=1.25)
    grid_ticks(ax, LBL, LBL, 4.9)
    annot_grid(ax, M, 3.7)
    ax.set_xlabel("test domain", fontsize=6.8, color=INK, labelpad=1.5)
    if k == 0:
        ax.set_ylabel("training domain", fontsize=6.8, color=INK)
    baxs.append(ax)

cax = fig.add_axes([0.915, 0.085, 0.014, 0.860])
cb = fig.colorbar(ims[-1], cax=cax)
cb.set_label("AUROC", fontsize=6.4, color=INK)
cb.ax.tick_params(labelsize=5.6, length=1.5, colors=INK)
cb.outline.set_edgecolor(MUTED); cb.outline.set_linewidth(0.5)
finish(fig, "fig_grids_v2")


# ====================================================================
# Fig. (bit-width) -- fig_bitwidth_v1: cell-wise change in AUROC as the
# ternary code grows 384 -> 2,048 bits. Added Aug 28 night per MN's
# pick ("Small delta figure in Sec. V-B"). Data: student's grids --
# 384-bit from the Aug 14 methods doc (== ternary384.npy, verified
# 0 diffs), 2,048-bit from slide 2 of truthfulness_spectrum_grids.pptx
# (saved as ternary2048.npy). Cells losing more than 0.05 are outlined;
# the doc's aggregate says 23 such cells, this 3-decimal recount gives
# 24 (two cells at exactly -0.051).
# ====================================================================
from matplotlib.patches import Rectangle

D2048 = np.load(os.path.join(HERE, "ternary2048.npy")) - G["ternary384"]

fig, ax = plt.subplots(figsize=(3.4, 2.95))
fig.subplots_adjust(left=0.13, right=0.86, top=0.97, bottom=0.155)
im = ax.imshow(D2048, vmin=-0.32, vmax=0.32, cmap=dcmap)
grid_ticks(ax, LBL, LBL, 4.9)
for i in range(10):
    for j in range(10):
        v = D2048[i, j]
        lab = "0" if abs(v) < 0.005 else \
            f"{v:+.2f}".replace("0.", ".").replace("-", "−")
        ax.text(j, i, lab, ha="center", va="center", fontsize=3.6,
                color="white" if abs(v) > 0.21 else INK)
        if i != j and v < -0.05:
            ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False,
                                   edgecolor=INK, lw=0.7, zorder=5))
ax.set_xlabel("test domain", fontsize=6.8, color=INK, labelpad=1.5)
ax.set_ylabel("training domain", fontsize=6.8, color=INK)
cax2 = fig.add_axes([0.875, 0.155, 0.025, 0.815])
cb = fig.colorbar(im, cax=cax2)
cb.set_label("Δ AUROC, 2,048 b − 384 b", fontsize=6.0, color=INK)
cb.ax.tick_params(labelsize=5.4, length=1.5, colors=INK)
cb.outline.set_edgecolor(MUTED); cb.outline.set_linewidth(0.5)
finish(fig, "fig_bitwidth_v1")
