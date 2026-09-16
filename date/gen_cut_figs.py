#!/usr/bin/env python3
"""gen_cut_figs.py -- figures regenerated for the DATE 2027 length cut
(date/main.tex). Style and data follow ../gen_paper_figs.py (house
palette, Helvetica/DejaVu, transparent background, figsize IS the
placed size, no bbox_inches="tight").

  figures/fig_grids_v3.{png,pdf}   7.0 x 2.3   (double column, Fig. 2)
      The bottom row of fig_grids_v2 alone, relettered (a)-(c); the
      four-domain top row was cut on 2026-09-16 (IB's call; MN had
      flagged it). Domain label "evid" -> "empir" per IB (same dataset
      the source paper calls empirical); the other abbreviations
      already match the source paper's names.
      DATA: ternary384.npy, thermo384.npy, twostage_fp.npy (copied from
      the parent folder; I. Bera's ten-domain cluster runs,
      Llama-3.3-70B-Instruct layer 33, 70/30 split, seed 0).
      Row = training (bank) domain, column = test domain.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

INK = "#1E293B"; MUTED = "#64748B"
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "Liberation Sans", "DejaVu Sans"],
    "mathtext.fontset": "dejavusans",
    "axes.axisbelow": True,
})
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)


def finish(fig, name):
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=300, transparent=True)
    plt.close(fig)
    print("wrote", name)


cmap = LinearSegmentedColormap.from_list(
    "auroc", ["#F7F7F7", "#C6DBEF", "#6BAED6", "#2171B5", "#08306B"])
LBL = ["defn", "empir", "fict", "logic", "ethic", "syco", "repe", "role", "insid", "sandb"]
G = {n: np.load(os.path.join(HERE, f"{n}.npy"))
     for n in ("ternary384", "thermo384", "twostage_fp")}


def annot_grid(ax, M, fs):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            v = M[i, j]
            lab = "1.0" if v >= 0.995 else f"{v:.2f}"[1:]
            ax.text(j, i, lab, ha="center", va="center", fontsize=fs,
                    color="white" if v > 0.72 else INK)


def grid_ticks(ax, xl, yl, fs):
    ax.set_xticks(range(len(xl))); ax.set_yticks(range(len(yl)))
    ax.set_xticklabels(xl, fontsize=fs, rotation=90, color=INK)
    ax.set_yticklabels(yl, fontsize=fs, color=INK)
    ax.tick_params(length=1.2, pad=1.0)
    for s in ax.spines.values():
        s.set_color(MUTED); s.set_linewidth(0.5)


# ---- fig_grids_v3: the ten-domain grids, one row ----------------------
fig = plt.figure(figsize=(7.0, 2.3))
gs = fig.add_gridspec(1, 3, wspace=0.30,
                      left=0.065, right=0.895, top=0.875, bottom=0.18)
panels = ((G["ternary384"], "(a) sign-RP ternary, 384 b -- TCAM cell"),
          (G["thermo384"], "(b) thermometer, 384 b -- binary CAM cell"),
          (G["twostage_fp"], "(c) Hamming shortlist + exact rerank (ceiling)"))
ims = []
for k, (M, title) in enumerate(panels):
    ax = fig.add_subplot(gs[0, k])
    im = ax.imshow(M, vmin=0.2, vmax=1.0, cmap=cmap); ims.append(im)
    ax.set_title(title.replace(" -- ", " – "), fontsize=6.6, color=INK, pad=3)
    grid_ticks(ax, LBL, LBL, 4.9)
    annot_grid(ax, M, 3.7)
    ax.set_xlabel("test domain", fontsize=6.8, color=INK, labelpad=1.5)
    if k == 0:
        ax.set_ylabel("training domain", fontsize=6.8, color=INK)
cax = fig.add_axes([0.915, 0.18, 0.014, 0.695])
cb = fig.colorbar(ims[-1], cax=cax)
cb.set_label("AUROC", fontsize=6.4, color=INK)
cb.ax.tick_params(labelsize=5.6, length=1.5, colors=INK)
cb.outline.set_edgecolor(MUTED); cb.outline.set_linewidth(0.5)
finish(fig, "fig_grids_v3")


# ======================================================================
#  fig_ladder_v3.{png,pdf}  3.4 x 2.2   (single column, intro Fig. 1)
#  Panel (b) of fig_ladder_v2 alone: library size K vs aggregate token
#  rate R, log-log, with straight lines where monitoring traffic
#  K*R*d*2B equals a stated share of a part's memory bandwidth
#  (K*R = share*BW/(2d B)). 100% lines for H100 (3.35 TB/s), A100
#  (2.0 TB/s), Jetson Thor (273 GB/s); 10% and 1% of an H100 as gray
#  guides. d = 8,192, fp16, one monitored layer. Marked point: the
#  whole-vocabulary K = 1.3e5 at 1e3 tok/s. Panel (a) (the K-vs-date
#  record) and the workload anchor strip were cut 2026-09-16 for
#  length; the anchor paragraph in the text went with the strip.
#  Arithmetic on vendor bandwidth figures, not measured throughput.
# ======================================================================
RED = "#E41A1C"; BLUE = "#377EB8"; GREEN = "#4DAF4A"
PURPLE = "#984EA3"; ORANGE = "#FF7F00"
from matplotlib.lines import Line2D


def spines(ax, drop=("top", "right")):
    for s in drop:
        ax.spines[s].set_visible(False)
    for s in ax.spines.values():
        if s.get_visible():
            s.set_color(MUTED); s.set_linewidth(0.6)
    ax.tick_params(labelsize=6.4, colors=INK, length=2, pad=1.5)


D, BY = 8192, 2
BYTES_ROW = D * BY
fig, ax = plt.subplots(figsize=(3.4, 2.2))
ax.set_xscale("log"); ax.set_yscale("log")
R = np.logspace(1, 4, 200)
def kline(bw_gbs, share):
    return share * bw_gbs * 1e9 / (BYTES_ROW * R)
ax.fill_between(R, kline(3350.0, 1.0), 1e8, color="#999999", alpha=0.14, zorder=0)
def linelabel(x, bw, share, lbl, col, fs, above=True):
    y = share * bw * 1e9 / (BYTES_ROW * x) * (1.45 if above else 0.62)
    ax.text(x, y, lbl, fontsize=fs, fontweight="bold", color=col,
            rotation=-25, rotation_mode="anchor", ha="left", zorder=6)
for bw, col, ls in ((3350.0, RED, "-"), (2000.0, BLUE, "--"), (273.0, GREEN, ":")):
    ax.plot(R, kline(bw, 1.0), color=col, lw=2.0, ls=ls, zorder=5)
linelabel(1.5e1, 3350.0, 1.0, "100% of H100", RED, 6.0, above=True)
linelabel(2.6e2, 2000.0, 1.0, "100% of A100", BLUE, 6.0, above=False)
linelabel(1.5e1, 273.0, 1.0, "100% of Thor", GREEN, 6.0, above=True)
for share, xl in ((0.10, 6.5e2), (0.01, 1.5e1)):
    ax.plot(R, kline(3350.0, share), color="#787878", lw=1.0, ls=(0, (5, 3)), zorder=3)
    y = share * 3350.0 * 1e9 / (BYTES_ROW * xl) * 0.60
    ax.text(xl, y, f"{int(share*100)}% of H100", fontsize=5.4, color="#606060",
            rotation=-25, rotation_mode="anchor", ha="left", zorder=6)
ax.plot([1e3], [128256], marker="o", ms=5.5, mfc="white", mec=BLUE, mew=1.6, zorder=7)
ax.annotate("whole-vocabulary readout\nat $10^{3}$ tok/s", xy=(1e3, 1.28e5),
            xytext=(1.1e2, 1.1e3), zorder=7, fontsize=5.6, color=BLUE,
            fontweight="bold", ha="left", va="top",
            arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8, alpha=0.6))
ax.text(9e3, 4.5e7, "monitoring alone\nexceeds an H100", fontsize=5.6, style="italic",
        color=MUTED, ha="right", va="top", linespacing=1.2, zorder=6)
ax.set_xlim(10, 1e4); ax.set_ylim(1e2, 1e8)
ax.set_xticks([10, 100, 1000, 1e4]); ax.set_xticklabels(["10", "100", "1K", "10K"])
ax.set_xlabel("aggregate token rate (tokens/s)", fontsize=6.8, color=INK, labelpad=1.5)
ax.set_ylabel("library size $K$ (rows/layer)", fontsize=6.8, color=INK)
ax.grid(True, which="major", color="black", alpha=0.10, lw=0.5)
spines(ax)
fig.tight_layout(pad=0.3)
finish(fig, "fig_ladder_v3")


# ======================================================================
#  fig_jspace_v2.{png,pdf}  3.4 x 1.8   (single column, Sec. V Fig.)
#  Panels (a) and (b) of fig_jspace_v1 at single-column width; panel
#  (c) (fidelity vs library size) was cut 2026-09-16 with the
#  subsection that discussed it. DATA: DIGITIZED from slides 20 and 21
#  of "Most Recent Results.pptx.pdf" (J. Whalen, 2026-07-30), as in
#  gen_paper_figs.py; +/-0.02. Replace from result files when they
#  surface (orange flag in main.tex).
# ======================================================================
DIGITIZED_FIRING_F1 = {
    "lsq_euclidean": ([256, 384, 512, 768, 1024], [0.16, 0.34, 0.51, 0.73, 0.81]),
    "exact_l2_proj": ([1024, 2048, 4096], [0.61, 0.76, 0.84]),
    "hamming":       ([64, 128, 256, 512, 1024, 4096], [0.17, 0.21, 0.30, 0.39, 0.49, 0.21]),
    "thermometer":   ([384, 896, 2048], [0.18, 0.25, 0.34]),
    "direct_sign":   ([4096], [0.21]),
}
DIGITIZED_TOP1 = {
    "lsq_euclidean": ([256, 384, 512, 768, 1024], [0.46, 0.54, 0.66, 0.88, 0.96]),
    "exact_l2_proj": ([2048, 4096], [1.00, 1.00]),
    "hamming":       ([64, 128, 256, 512, 1024, 4096], [0.28, 0.41, 0.53, 0.66, 0.74, 0.16]),
    "thermometer":   ([384, 896, 2048], [0.29, 0.30, 0.40]),
    "direct_sign":   ([4096], [0.11]),
}
STY = {"lsq_euclidean": (RED, "D", "-", "LSQ Euclidean"),
       "exact_l2_proj": (PURPLE, "P", "-", "exact $L_2$ (fp16)"),
       "hamming":       (BLUE, "o", "--", "Hamming (sign)"),
       "thermometer":   (GREEN, "s", ":", "thermometer"),
       "direct_sign":   (ORANGE, "X", "", "direct sign hash")}
fig, axs = plt.subplots(1, 2, figsize=(3.4, 1.8))
for ax, (data, ylab, ttl) in zip(axs, (
        (DIGITIZED_FIRING_F1, "per-row firing F1", "(a) threshold readout"),
        (DIGITIZED_TOP1, "top-1 agreement", "(b) top-1 readout"))):
    ax.set_xscale("log")
    for key, (bx, by) in data.items():
        col, mk, ls, lbl = STY[key]
        if ls:
            ax.plot(bx, by, color=col, ls=ls, lw=1.1, marker=mk, ms=2.6, zorder=5)
        else:
            ax.plot(bx, by, color=col, ls="none", marker=mk, ms=3.4, zorder=5)
    ax.axhline(1.0, color=MUTED, ls=(0, (1, 2)), lw=0.8, zorder=3)
    ax.plot([131072], [1.0], marker="*", ms=6, color=INK, zorder=6)
    ax.text(131072, 0.93, "fp16 row", fontsize=4.6, color=INK, ha="right", va="top", zorder=6)
    ax.set_xlim(40, 4e5); ax.set_ylim(0, 1.12)
    ax.set_xticks([1e2, 1e3, 1e4, 1e5]); ax.set_xticklabels(["100", "1K", "10K", "100K"])
    ax.set_xlabel("storage bits per CAM row", fontsize=6.0, color=INK, labelpad=1.5)
    ax.set_ylabel(ylab, fontsize=6.0, color=INK, labelpad=1.5)
    ax.set_title(ttl, fontsize=6.4, color=INK, pad=2.5)
    ax.grid(True, color="black", alpha=0.10, lw=0.5)
    spines(ax); ax.tick_params(labelsize=5.6)
h = [Line2D([], [], color=STY[k][0], ls=STY[k][2] or "none", marker=STY[k][1],
            ms=2.6, lw=1.1, label=STY[k][3]) for k in
     ("lsq_euclidean", "exact_l2_proj", "hamming", "thermometer", "direct_sign")]
axs[0].legend(handles=h, fontsize=4.3, loc="upper left", bbox_to_anchor=(0.0, 1.0),
              framealpha=0.9, edgecolor="#707070", borderpad=0.3,
              handlelength=1.2, labelspacing=0.2, handletextpad=0.5)
fig.tight_layout(pad=0.3, w_pad=0.6)
finish(fig, "fig_jspace_v2")
