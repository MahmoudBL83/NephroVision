import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

out_dir = r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\public\images'

# ============================================
# 1. SKIP CONNECTION DIAGRAM (PNG)
# ============================================
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.set_xlim(0, 8)
ax.set_ylim(0, 4)
ax.axis('off')

# Encoder (left side)
enc_boxes = [(0.5, 3.2, 1.2, 0.5), (0.5, 2.4, 1.0, 0.5), (0.5, 1.6, 0.8, 0.5), (0.5, 0.8, 0.6, 0.5)]
enc_labels = ['256x256\n64 ch', '128x128\n128 ch', '64x64\n256 ch', '32x32\n512 ch']
enc_colors = ['#c5d5e8', '#a0c0e0', '#7aaad8', '#5595d0']

for i, (x, y, w, h) in enumerate(enc_boxes):
    rect = plt.Rectangle((x, y), w, h, fill=True, facecolor=enc_colors[i], edgecolor='#1e3a5f', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, enc_labels[i], ha='center', va='center', fontsize=6, color='#1a1a1a')

# Bottleneck
rect = plt.Rectangle((2.5, 1.2), 0.8, 0.8, fill=True, facecolor='#1e3a5f', edgecolor='#1a1a1a', linewidth=2)
ax.add_patch(rect)
ax.text(2.9, 1.6, 'Bottleneck\n32x32', ha='center', va='center', fontsize=6, color='white', fontweight='bold')

# Decoder (right side)
dec_boxes = [(4.0, 0.8, 0.6, 0.5), (4.0, 1.6, 0.8, 0.5), (4.0, 2.4, 1.0, 0.5), (4.0, 3.2, 1.2, 0.5)]
dec_labels = ['32x32\n512 ch', '64x64\n256 ch', '128x128\n128 ch', '256x256\n64 ch']
dec_colors = ['#5595d0', '#7aaad8', '#a0c0e0', '#c5d5e8']

for i, (x, y, w, h) in enumerate(dec_boxes):
    rect = plt.Rectangle((x, y), w, h, fill=True, facecolor=dec_colors[i], edgecolor='#1e3a5f', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, dec_labels[i], ha='center', va='center', fontsize=6, color='#1a1a1a')

# Skip connection arrows
skip_colors = ['#2d6a4f', '#3d8a6f', '#4daa8f', '#5dcaaf']
for i in range(4):
    y_enc = enc_boxes[i][1] + enc_boxes[i][3]/2
    y_dec = dec_boxes[3-i][1] + dec_boxes[3-i][3]/2
    ax.annotate('', xy=(4.0, y_dec), xytext=(1.7, y_enc),
               arrowprops=dict(arrowstyle='->', color=skip_colors[i], lw=2, 
                              connectionstyle='arc3,rad=0.3'))
    ax.text(2.85, (y_enc + y_dec)/2, 'skip', fontsize=5, color=skip_colors[i], ha='center', fontweight='bold')

# Output
rect = plt.Rectangle((5.8, 3.2), 1.2, 0.5, fill=True, facecolor='#e8f5e9', edgecolor='#2d6a4f', linewidth=2)
ax.add_patch(rect)
ax.text(6.4, 3.45, 'Output Mask', ha='center', va='center', fontsize=8, color='#2d6a4f', fontweight='bold')

ax.annotate('', xy=(5.8, 3.45), xytext=(5.2, 3.45),
           arrowprops=dict(arrowstyle='->', color='#1a1a1a', lw=1.5))

# Encoder/Decoder labels
ax.text(1.1, 3.9, 'Encoder', ha='center', fontsize=9, fontweight='bold', color='#1e3a5f')
ax.text(4.6, 3.9, 'Decoder', ha='center', fontsize=9, fontweight='bold', color='#1e3a5f')

plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'skip_connections.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# ============================================
# 2. WEB APP MOCKUP (PNG)
# ============================================
fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# Browser chrome
browser_rect = plt.Rectangle((0.2, 0.2), 9.6, 4.6, fill=True, facecolor='#f5f5f5', edgecolor='#cccccc', linewidth=1)
ax.add_patch(browser_rect)

# Title bar
title_rect = plt.Rectangle((0.2, 4.4), 9.6, 0.4, fill=True, facecolor='#e8e8e8', edgecolor='#cccccc', linewidth=1)
ax.add_patch(title_rect)
ax.text(5, 4.6, 'NephroVision — Decision-Support Segmentation', ha='center', va='center', fontsize=10, color='#1a1a1a', fontweight='bold')

# Sidebar (stats)
sidebar_rect = plt.Rectangle((0.3, 0.3), 2.5, 4.0, fill=True, facecolor='white', edgecolor='#e0e0e0', linewidth=1)
ax.add_patch(sidebar_rect)
ax.text(1.55, 4.1, 'Statistics', ha='center', fontsize=9, fontweight='bold', color='#1e3a5f')
ax.text(0.5, 3.7, 'Kidney Volume:', fontsize=7, color='#4a4a4a')
ax.text(2.5, 3.7, '245.3 ml', fontsize=7, color='#2d6a4f', fontweight='bold', ha='right')
ax.text(0.5, 3.4, 'Tumor Volume:', fontsize=7, color='#4a4a4a')
ax.text(2.5, 3.4, '12.7 ml', fontsize=7, color='#bc4b31', fontweight='bold', ha='right')
ax.text(0.5, 3.1, 'Detection:', fontsize=7, color='#4a4a4a')
ax.text(2.5, 3.1, 'Yes', fontsize=7, color='#2d6a4f', fontweight='bold', ha='right')

# Class toggle
ax.text(1.55, 2.5, 'Toggle Classes', ha='center', fontsize=8, fontweight='bold', color='#1e3a5f')
toggle_bg = plt.Rectangle((0.5, 2.0), 2.1, 0.3, fill=True, facecolor='#2d6a4f', edgecolor='#2d6a4f', linewidth=1, alpha=0.3)
ax.add_patch(toggle_bg)
ax.text(1.55, 2.15, 'Kidney', ha='center', fontsize=7, color='#2d6a4f')
toggle_bg2 = plt.Rectangle((0.5, 1.6), 2.1, 0.3, fill=True, facecolor='#bc4b31', edgecolor='#bc4b31', linewidth=1, alpha=0.3)
ax.add_patch(toggle_bg2)
ax.text(1.55, 1.75, 'Tumor', ha='center', fontsize=7, color='#bc4b31')

# Disclaimer
warn_rect = plt.Rectangle((0.4, 0.5), 2.3, 0.7, fill=True, facecolor='#fff8e1', edgecolor='#f0c040', linewidth=1)
ax.add_patch(warn_rect)
ax.text(1.55, 0.95, 'Decision-Support Only', ha='center', fontsize=6, color='#8a6d3b', fontweight='bold')
ax.text(1.55, 0.7, 'Not for clinical use', ha='center', fontsize=6, color='#8a6d3b')

# Main 3D viewer area
viewer_rect = plt.Rectangle((3.0, 0.3), 6.7, 4.0, fill=True, facecolor='#fafbfc', edgecolor='#e0e0e0', linewidth=1)
ax.add_patch(viewer_rect)

# Simulate 3D mesh (wireframe-like)
from mpl_toolkits.mplot3d import proj3d
theta = np.linspace(0, 2*np.pi, 30)
phi = np.linspace(0, np.pi, 20)
THETA, PHI = np.meshgrid(theta, phi)

# Kidney ellipsoid
R = 1.0
X = R * np.sin(PHI) * np.cos(THETA) * 0.8 + 6.5
Y = R * np.sin(PHI) * np.sin(THETA) * 0.5 + 2.5
Z = R * np.cos(PHI) * 1.2

# Draw as contour-like lines on 2D
for i in range(0, len(theta), 3):
    ax.plot(X[:, i], Z[:, i], color='#2d6a4f', linewidth=0.8, alpha=0.6)
for i in range(0, len(phi), 3):
    ax.plot(X[i, :], Z[i, :], color='#2d6a4f', linewidth=0.8, alpha=0.6)

# Tumor sphere
R_t = 0.25
X_t = R_t * np.sin(PHI) * np.cos(THETA) * 0.8 + 6.2
Y_t = R_t * np.sin(PHI) * np.sin(THETA) * 0.5 + 2.8
Z_t = R_t * np.cos(PHI) * 1.2 + 0.3
for i in range(0, len(theta), 4):
    ax.plot(X_t[:, i], Z_t[:, i], color='#bc4b31', linewidth=0.8, alpha=0.7)
for i in range(0, len(phi), 4):
    ax.plot(X_t[i, :], Z_t[i, :], color='#bc4b31', linewidth=0.8, alpha=0.7)

# Controls
ax.text(6.35, 3.9, '3D Interactive Viewer', ha='center', fontsize=9, fontweight='bold', color='#1a1a1a')
ax.text(6.35, 0.5, '[Rotate]  [Zoom]  [Pan]  [Reset]', ha='center', fontsize=7, color='#8a8a8a')

plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'webapp_mockup.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# ============================================
# 3. FAILURE CASES (3 images)
# ============================================
np.random.seed(50)

for case_idx, (case_name, case_desc, save_name) in enumerate([
    ('FC-001: Boundary Leakage', 'Tumor mask extends into healthy parenchyma', 'failure_case_001.png'),
    ('FC-002: Small Lesion', '120-voxel lesion under-segmented', 'failure_case_002.png'),
    ('FC-003: Cyst Confusion', 'Large cyst correctly segmented but labeled Tumor/Cyst', 'failure_case_003.png'),
]):
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.axis('off')
    
    # CT slice background
    x = np.linspace(-2, 2, 64)
    y = np.linspace(-2, 2, 64)
    X, Y = np.meshgrid(x, y)
    
    # Kidney
    kidney_mask = ((X-0.3)**2/1.5 + (Y+0.2)**2/1.2) < 1.0
    # Tumor (different shapes per case)
    if case_idx == 0:
        # Leaky boundary - tumor extends too far
        true_tumor = ((X-0.1)**2 + (Y-0.1)**2) < 0.25
        pred_tumor = ((X-0.1)**2 + (Y-0.1)**2) < 0.42  # larger
    elif case_idx == 1:
        # Small lesion - under-segmented
        true_tumor = ((X+0.3)**2 + (Y-0.3)**2) < 0.18
        pred_tumor = ((X+0.3)**2 + (Y-0.3)**2) < 0.10  # smaller
    else:
        # Cyst - round, well-defined
        true_tumor = ((X-0.2)**2 + (Y+0.4)**2) < 0.35
        pred_tumor = true_tumor.copy()
    
    ct = np.zeros_like(X)
    ct[kidney_mask] = 0.55
    ct[true_tumor] = 0.72
    ct += np.random.normal(0, 0.02, ct.shape)
    
    ax.imshow(ct, extent=[0, 4, 0, 4], cmap='gray', aspect='auto')
    ax.contour(kidney_mask, extent=[0, 4, 0, 4], colors='#2d6a4f', linewidths=2, alpha=0.8)
    ax.contour(true_tumor, extent=[0, 4, 0, 4], colors='#bc4b31', linewidths=2, alpha=0.8, linestyles='--')
    ax.contour(pred_tumor, extent=[0, 4, 0, 4], colors='#1e3a5f', linewidths=1.5, alpha=0.7)
    
    # Title
    ax.text(2, 3.7, case_name, ha='center', fontsize=9, fontweight='bold', color='#1a1a1a')
    ax.text(2, 3.4, case_desc, ha='center', fontsize=7, color='#8a8a8a')
    
    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='#bc4b31', lw=2, linestyle='--', label='Ground Truth'),
        Line2D([0], [0], color='#1e3a5f', lw=1.5, label='Prediction')
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=6)
    
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, save_name), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ============================================
# 4. SCANNER VARIABILITY DIAGRAM (PNG)
# ============================================
fig, ax = plt.subplots(1, 1, figsize=(8, 3))
ax.set_xlim(0, 8)
ax.set_ylim(0, 3)
ax.axis('off')

scanners = [
    ('Scanner A\n(Siemens)', '#e8f4fd', 'Sharp kernel\n120 kVp'),
    ('Scanner B\n(GE)', '#fdf2e8', 'Soft kernel\n100 kVp'),
    ('Scanner C\n(Philips)', '#f0f8e8', 'Standard kernel\n120 kVp'),
]

for i, (name, color, params) in enumerate(scanners):
    x = 0.8 + i * 2.5
    # Scanner icon (simplified)
    rect = plt.Rectangle((x, 1.0), 1.8, 1.6, fill=True, facecolor=color, edgecolor='#1a1a1a', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x + 0.9, 2.2, name, ha='center', fontsize=8, fontweight='bold', color='#1a1a1a')
    ax.text(x + 0.9, 1.6, params, ha='center', fontsize=6, color='#8a8a8a', linespacing=0.9)
    
    # Gantry circle
    circle = plt.Circle((x + 0.9, 0.5), 0.3, fill=False, edgecolor='#1a1a1a', linewidth=2)
    ax.add_patch(circle)
    ax.text(x + 0.9, 0.5, 'CT', ha='center', va='center', fontsize=6, color='#1a1a1a')

# Warning
warn_rect = plt.Rectangle((0.5, 2.8), 7.0, 0.15, fill=True, facecolor='#fff8e1', edgecolor='#f0c040', linewidth=1)
ax.add_patch(warn_rect)
ax.text(4, 2.875, 'Same anatomy → different intensity distributions → model may behave differently', 
        ha='center', va='center', fontsize=8, color='#8a6d3b', fontweight='bold')

ax.text(4, 0.15, 'Domain Shift Risk: Performance on non-KiTS23 scanners is unknown', 
        ha='center', fontsize=9, color='#bc4b31', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'scanner_variability.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("All additional charts generated successfully!")
