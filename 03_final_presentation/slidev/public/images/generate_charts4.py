import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

out_dir = r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\public\images'

fig, ax = plt.subplots(1, 1, figsize=(9, 4.5))

criteria = ['Kidney\nDice', 'Tumor\nDice', 'Mean\nDice', 'HD95\nKidney', 'HD95\nTumor', 'Detection\nRate']
targets = [0.85, 0.50, 0.65, 30, 100, 0.90]
achieved = [0.9307, 0.6558, 0.7933, 19.98, 67.35, 1.0]

# Normalize for visualization (0-1 scale where 1 = target met or exceeded)
# For HD95, lower is better, so we invert
normalized = []
colors = []
for i, (t, a) in enumerate(zip(targets, achieved)):
    if i in [3, 4]:  # HD95 - lower is better
        norm = min(t / a, 1.2)  # cap at 1.2x
        color = '#2d6a4f' if a <= t else '#bc4b31'
    else:
        norm = min(a / t, 1.2)
        color = '#2d6a4f' if a >= t else '#bc4b31'
    normalized.append(norm)
    colors.append(color)

x = np.arange(len(criteria))
width = 0.35

# Target bars (outline only)
for i, (xi, t) in enumerate(zip(x, normalized)):
    ax.bar(xi - width/2, 1.0, width, fill=False, edgecolor='#8a8a8a', linewidth=1.5, linestyle='--', alpha=0.7)

# Achieved bars
bars = ax.bar(x + width/2, normalized, width, color=colors, alpha=0.8, edgecolor='white', linewidth=1)

# Add value labels
for i, (bar, a, t) in enumerate(zip(bars, achieved, targets)):
    height = bar.get_height()
    if i in [3, 4]:
        label = f'{a:.1f} mm'
        target_label = f'<{t} mm'
    elif i == 5:
        label = f'{a:.0%}'
        target_label = f'>{t:.0%}'
    else:
        label = f'{a:.3f}'
        target_label = f'>{t:.2f}'
    
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.03, label, 
            ha='center', va='bottom', fontsize=7, fontweight='bold', color=colors[i])

ax.set_xticks(x)
ax.set_xticklabels(criteria, fontsize=9)
ax.set_ylabel('Normalized to Target', fontsize=10, fontweight='bold')
ax.axhline(y=1.0, color='#8a8a8a', linestyle='--', linewidth=1, alpha=0.5)
ax.text(5.5, 1.03, 'Target', fontsize=8, color='#8a8a8a')
ax.set_ylim(0, 1.35)
ax.set_title('All Six Acceptance Criteria Met', fontsize=12, fontweight='bold', color='#1a1a1a')
ax.grid(True, alpha=0.3, axis='y')

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#2d6a4f', alpha=0.8, label='Target Met'),
    Patch(facecolor='none', edgecolor='#8a8a8a', linestyle='--', label='Target')
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'target_achieved.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("target_achieved.png generated successfully!")
