---
theme: none
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## NephroVision
  Automated Kidney and Renal Tumor Segmentation System
  Medical Engineering Graduation Project
  Supervisor: Hisham Abdeltawab, Ph.D.
drawings:
  persist: false
title: NephroVision - Final Defense
mdc: true
---

<style src="style.css"></style>

<script setup>
if (typeof window !== 'undefined') {
  // Create export button once
  if (!document.getElementById('nv-export-btn')) {
    const wrapper = document.createElement('div')
    wrapper.id = 'nv-export-btn'
    wrapper.innerHTML = `
      <button id="nv-export-toggle" title="Export Presentation">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
          <polyline points="7 10 12 15 17 10"/>
          <line x1="12" y1="15" x2="12" y2="3"/>
        </svg>
        <span>Export</span>
      </button>
      <div id="nv-export-menu" style="display:none">
        <div class="nv-export-header">Export Format</div>
        <button class="nv-export-item" data-format="pptx">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="3" y="3" width="18" height="18" rx="2"/>
            <line x1="3" y1="9" x2="21" y2="9"/>
            <line x1="9" y1="21" x2="9" y2="9"/>
          </svg>
          <div><strong>PowerPoint (.pptx)</strong><small>Best for presenting</small></div>
        </button>
        <button class="nv-export-item" data-format="pdf">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
          </svg>
          <div><strong>PDF Document</strong><small>Universal format</small></div>
        </button>
        <button class="nv-export-item" data-format="png">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="3" y="3" width="18" height="18" rx="2"/>
            <circle cx="8.5" cy="8.5" r="1.5"/>
            <polyline points="21 15 16 10 5 21"/>
          </svg>
          <div><strong>PNG Images</strong><small>Individual slides</small></div>
        </button>
        <div class="nv-export-note">PPTX requires Chrome/Playwright.<br>Run: <code>npm run export:pptx</code></div>
      </div>
    `
    document.body.appendChild(wrapper)
    
    // Styles
    const style = document.createElement('style')
    style.textContent = `
      #nv-export-btn { position:fixed; top:14px; right:14px; z-index:99999; font-family:Inter,sans-serif }
      #nv-export-toggle { display:flex; align-items:center; gap:5px; padding:7px 12px; background:#1e3a5f; color:#fff; border:none; border-radius:5px; font-size:0.75rem; font-weight:600; cursor:pointer; box-shadow:0 1px 6px rgba(30,58,95,0.3) }
      #nv-export-toggle:hover { background:#2a4a73 }
      #nv-export-menu { position:absolute; top:calc(100% + 6px); right:0; width:200px; background:#fff; border:1px solid #e0e0e0; border-radius:6px; box-shadow:0 4px 16px rgba(0,0,0,0.12); padding:6px }
      .nv-export-header { font-size:0.6rem; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; color:#8a8a8a; padding:3px 6px 6px; border-bottom:1px solid #f0f0f0; margin-bottom:3px }
      .nv-export-item { display:flex; align-items:center; gap:8px; width:100%; padding:6px; background:none; border:none; border-radius:3px; cursor:pointer; text-align:left; color:#1a1a1a; font-size:0.75rem }
      .nv-export-item:hover { background:#f5f5f5 }
      .nv-export-item svg { flex-shrink:0; color:#1e3a5f }
      .nv-export-item strong { display:block; font-weight:600 }
      .nv-export-item small { display:block; font-size:0.65rem; color:#8a8a8a }
      .nv-export-note { font-size:0.65rem; color:#8a8a8a; padding:6px; line-height:1.4; border-top:1px solid #f0f0f0; margin-top:4px }
      .nv-export-note code { background:#f0f4f8; padding:1px 3px; border-radius:2px; font-family:monospace; font-size:0.6rem; color:#1e3a5f }
    `
    document.head.appendChild(style)
    
    // Toggle menu
    document.getElementById('nv-export-toggle').addEventListener('click', (e) => {
      e.stopPropagation()
      const menu = document.getElementById('nv-export-menu')
      menu.style.display = menu.style.display === 'none' ? 'block' : 'none'
    })
    
    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!e.target.closest('#nv-export-btn')) {
        document.getElementById('nv-export-menu').style.display = 'none'
      }
    })
    
    // Export actions
    wrapper.querySelectorAll('.nv-export-item').forEach(item => {
      item.addEventListener('click', () => {
        const format = item.dataset.format
        if (format === 'pptx') {
          alert('PPTX export: Run npm run export:pptx in terminal')
        } else if (format === 'pdf') {
          window.open('/__slidev/export/pdf', '_blank')
        } else if (format === 'png') {
          alert('PNG export: Run npm run export:png in terminal')
        }
        document.getElementById('nv-export-menu').style.display = 'none'
      })
    })
  }
}
</script>
<!-- ============================================================

   SLIDE 1: TITLE

   ============================================================ -->
<div class="nv-center" style="position: relative; z-index: 1; padding-top: 1.5rem;">
  <div style="margin-bottom: 2rem;">
    <div style="display: inline-block; padding: 0.4rem 1.2rem; background: #f0f4f8; border-radius: 20px; margin-bottom: 1.5rem;">
      <div style="font-size: 0.65rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.25em; color: #1e3a5f;">Medical Engineering Graduation Project · 2026</div>
    </div>
  </div>
  <div style="font-size: 5rem; font-weight: 800; color: #1a1a1a; letter-spacing: -0.04em; line-height: 1; margin-bottom: 0.5rem;">NephroVision</div>
  <div style="font-family: 'Crimson Text', Georgia, serif; font-size: 1.7rem; font-weight: 400; font-style: italic; color: #4a4a4a; letter-spacing: 0.02em; margin-bottom: 1.5rem;">Automated Kidney and Renal Tumor Segmentation from CT</div>
  <div style="width: 80px; height: 3px; background: linear-gradient(90deg, #1e3a5f, #2d6a4f); margin: 0 auto 2rem;"></div>
  <div style="display: flex; justify-content: center; gap: 0.6rem; flex-wrap: wrap; margin-bottom: 2.5rem;">
    <SafetyBadge label="Decision-Support Only" status="warning" />
    <SafetyBadge label="Not Clinically Approved" status="danger" />
    <SafetyBadge label="Academic Prototype" status="info" />
  </div>
  <div style="font-size: 0.8rem; color: #8a8a8a; line-height: 1.8; margin-top: auto;">
    <div style="margin-bottom: 0.3rem;"><strong style="color: #4a4a4a;">Team:</strong> Rashed Mamdouh · Mohamed Walid · Mahmoud BahaaAldeen · Mahmoud Mohammed · Youssef Mohammed</div>
    <div><strong style="color: #4a4a4a;">Supervisor:</strong> Hisham Abdeltawab, Ph.D. · <strong style="color: #4a4a4a;">Institution:</strong> [University Name]</div>
  </div>
</div>
<!--

Notes:

Welcome the committee. NephroVision is an academic decision-support prototype for automated kidney and renal tumor/cyst segmentation from CT. State immediately: not clinically approved, not FDA approved, all outputs require physician review. 20 seconds.

-->

---

<!-- ============================================================

     SLIDE 2: THE CLINICAL PROBLEM

     ============================================================ -->
<SectionTitle number="01" title="The Clinical Problem" subtitle="Manual segmentation is slow, costly, and inconsistent" />
<div class="nv-three-col" style="margin-top: 1rem;">
<div class="nv-card" style="text-align: center; padding: 1.5rem 1.2rem; border-top: 3px solid #1e3a5f;">
  <div style="width: 52px; height: 52px; border-radius: 50%; background: linear-gradient(135deg, #1e3a5f, #2a4a73); color: #fff; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-family: 'SF Mono', monospace; font-size: 1.4rem; font-weight: 700; box-shadow: 0 2px 8px rgba(30,58,95,0.3);">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
  </div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 1.1rem; margin-bottom: 0.5rem;">Time-Consuming</div>
  <div style="font-size: 0.82rem; color: #8a8a8a; line-height: 1.5; margin-bottom: 0.6rem;">Hundreds of slices per CT volume traced manually by specialists</div>
  <div style="font-family: 'SF Mono', monospace; font-size: 1.8rem; font-weight: 700; color: #1e3a5f;">20-45</div>
  <div style="font-size: 0.7rem; color: #8a8a8a; margin-top: 0.3rem;">minutes per case (literature estimate)</div>
</div>
<div class="nv-card" style="text-align: center; padding: 1.5rem 1.2rem; border-top: 3px solid #bc4b31;">
  <div style="width: 52px; height: 52px; border-radius: 50%; background: linear-gradient(135deg, #bc4b31, #d46044); color: #fff; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-family: 'SF Mono', monospace; font-size: 1.4rem; font-weight: 700; box-shadow: 0 2px 8px rgba(188,75,49,0.3);">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
  </div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 1.1rem; margin-bottom: 0.5rem;">Variable</div>
  <div style="font-size: 0.82rem; color: #8a8a8a; line-height: 1.5; margin-bottom: 0.6rem;">Different radiologists draw different boundaries for the same tumor</div>
  <div style="font-family: 'SF Mono', monospace; font-size: 1.8rem; font-weight: 700; color: #bc4b31;">0.75-0.85</div>
  <div style="font-size: 0.7rem; color: #8a8a8a; margin-top: 0.3rem;">typical inter-observer Dice (literature)</div>
</div>
<div class="nv-card" style="text-align: center; padding: 1.5rem 1.2rem; border-top: 3px solid #2d6a4f;">
  <div style="width: 52px; height: 52px; border-radius: 50%; background: linear-gradient(135deg, #2d6a4f, #3d8a6f); color: #fff; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-family: 'SF Mono', monospace; font-size: 1.4rem; font-weight: 700; box-shadow: 0 2px 8px rgba(45,106,79,0.3);">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>
  </div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 1.1rem; margin-bottom: 0.5rem;">Growing Workload</div>
  <div style="font-size: 0.82rem; color: #8a8a8a; line-height: 1.5; margin-bottom: 0.6rem;">Imaging volume increases faster than radiologist capacity globally</div>
  <div style="font-family: 'SF Mono', monospace; font-size: 1.8rem; font-weight: 700; color: #2d6a4f;">~8%</div>
  <div style="font-size: 0.7rem; color: #8a8a8a; margin-top: 0.3rem;">annual growth in CT imaging volume</div>
</div>
</div>
<div style="margin-top: 1rem;">
  <blockquote style="text-align: center; font-size: 1.05rem;">
    <strong class="nv-accent">Need:</strong> A reproducible decision-support tool that proposes consistent segmentation boundaries — with mandatory physician review
  </blockquote>
</div>
<!--

Notes:

Frame the problem as workload and consistency, not radiologist incompetence. Three dimensions: time (hundreds of slices), variability (inter-observer disagreement), and growing demand. The solution is decision-support, not replacement. Fill [TODO] placeholders with actual numbers from literature if available. 40 seconds.

-->

---

<!-- ============================================================

     SLIDE 3: WHY SEGMENTATION MATTERS

     ============================================================ -->
<SectionTitle number="01" title="Why Segmentation Matters" subtitle="Volumetric assessment drives clinical decisions" />
<div style="margin-top: 0.8rem; display: grid; grid-template-columns: 1fr 1.4fr; gap: 1.2rem; align-items: start;">
  <div style="display: flex; flex-direction: column; gap: 0.6rem;">
    <div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.8rem 1rem;">
      <div style="min-width: 36px; height: 36px; border-radius: 8px; background: #f0f4f8; border: 1.5px solid #1e3a5f; color: #1e3a5f; display: flex; align-items: center; justify-content: center; font-family: 'SF Mono', monospace; font-size: 0.85rem; font-weight: 700;">01</div>
      <div>
        <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">Surgical Planning</div>
        <div style="font-size: 0.78rem; color: #8a8a8a; line-height: 1.4;">Tumor boundaries guide nephron-sparing resection</div>
      </div>
    </div>
    <div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.8rem 1rem;">
      <div style="min-width: 36px; height: 36px; border-radius: 8px; background: #f0f4f8; border: 1.5px solid #1e3a5f; color: #1e3a5f; display: flex; align-items: center; justify-content: center; font-family: 'SF Mono', monospace; font-size: 0.85rem; font-weight: 700;">02</div>
      <div>
        <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">Treatment Monitoring</div>
        <div style="font-size: 0.78rem; color: #8a8a8a; line-height: 1.4;">Volume changes track therapy response over time</div>
      </div>
    </div>
    <div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.8rem 1rem;">
      <div style="min-width: 36px; height: 36px; border-radius: 8px; background: #f0f4f8; border: 1.5px solid #1e3a5f; color: #1e3a5f; display: flex; align-items: center; justify-content: center; font-family: 'SF Mono', monospace; font-size: 0.85rem; font-weight: 700;">03</div>
      <div>
        <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">Research</div>
        <div style="font-size: 0.78rem; color: #8a8a8a; line-height: 1.4;">Standardized segmentation enables reproducible studies</div>
      </div>
    </div>
  </div>
  <div class="nv-svg-wrapper" style="margin-top: 0;">
    <img src="/images/ct_slice_tumor_segmented.png" alt="CT slice with kidney tumor segmentation overlay" style="width: 100%; height: auto; max-height: 280px; object-fit: contain;" />
  </div>
</div>

<!--

Notes:

Connect technical work to patient care. Three clinical use cases as visual cards. Emphasize the scope boundary: segmentation support, not diagnosis. The system proposes boundaries; the physician decides what they mean clinically. 35 seconds.

-->

---

<!-- ============================================================

     SLIDE 4: PROJECT OBJECTIVE

     ============================================================ -->
<SectionTitle number="01" title="Project Objective" subtitle="Input, output, users, and boundaries" />
<div style="margin-top: 0.8rem; display: grid; grid-template-columns: 1fr 1.4fr; gap: 1.2rem; align-items: start;">
  <div style="display: flex; flex-direction: column; gap: 0.7rem;">
    <div class="nv-card" style="border-left: 3px solid #1e3a5f;">
      <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Input</div>
      <div style="font-size: 1rem; color: #1a1a1a; font-weight: 600;">NIfTI CT Volumes</div>
      <div style="font-size: 0.8rem; color: #8a8a8a; margin-top: 0.3rem;">Contrast-enhanced abdominal CT (.nii / .nii.gz)</div>
      <div style="margin-top: 0.5rem; padding: 0.4rem 0.6rem; background: #f8f9fa; border-radius: 4px; font-size: 0.72rem; color: #8a8a8a;">
        <strong style="color: #4a4a4a;">Typical:</strong> 512 × 512 × 80-400 voxels
      </div>
    </div>
    <div class="nv-card nv-card-green" style="border-left: 3px solid #2d6a4f;">
      <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.5rem;">Output</div>
      <div style="display: flex; flex-direction: column; gap: 0.35rem;">
        <div style="font-size: 0.85rem; color: #4a4a4a; display: flex; align-items: center; gap: 0.4rem;"><span style="color: #2d6a4f;">&#10003;</span> 3D segmentation mask (3-class)</div>
        <div style="font-size: 0.85rem; color: #4a4a4a; display: flex; align-items: center; gap: 0.4rem;"><span style="color: #2d6a4f;">&#10003;</span> Kidney & tumor volumetric stats</div>
        <div style="font-size: 0.85rem; color: #4a4a4a; display: flex; align-items: center; gap: 0.4rem;"><span style="color: #2d6a4f;">&#10003;</span> Interactive 3D web visualization</div>
      </div>
    </div>
   
  </div>
  <div class="nv-svg-wrapper" style="margin-top: 0;">
    <img src="/images/system_pipeline.svg" style="width: 100%; height: auto; max-height: 280px; object-fit: contain;" />
    <div style="text-align: center; font-size: 0.72rem; color: #8a8a8a; margin-top: 0.5rem;">End-to-end pipeline: Preprocess → Segment → Visualize</div>
  </div>
</div>

<!--

Notes:

Clear scope statement. Input: NIfTI CT. Output: mask, stats, 3D viz. Users: radiologists, urologists, engineers. Constraints: decision-support only, physician review required, not clinically approved. Pipeline diagram gives visual overview. Fill [TODO] with actual slice count from KiTS23. 30 seconds.

-->

---

<!-- ============================================================

     SLIDE 5: CT IMAGING FUNDAMENTALS

     ============================================================ -->
<SectionTitle number="01" title="CT Imaging Fundamentals" subtitle="Hounsfield units, contrast phases, and soft-tissue contrast" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div>
  <div class="nv-svg-wrapper" style="background: #fafbfc; padding: 1rem; border-radius: 6px;">
    <img src="/images/HU_DIAGRAM.png" alt="Hounsfield Units Scale" style="max-height: 150px; width: 100%; object-fit: contain;" />
  </div>
  <div style="margin-top: 0.8rem; font-size: 0.82rem; color: #4a4a4a; line-height: 1.6;">
    <strong style="color: #1a1a1a;">Hounsfield Units (HU)</strong> quantify X-ray attenuation. Kidney parenchyma (~20-70 HU) and tumor (~30-90 HU) sit in a narrow soft-tissue band that requires careful windowing.
  </div>
  <div style="margin-top: 0.6rem; padding: 0.5rem 0.8rem; background: #f0f4f8; border-radius: 4px; font-size: 0.75rem; color: #4a4a4a;">
    <strong style="color: #1e3a5f;">Input:</strong> NIfTI format (.nii.gz) — 3D volume, typically 512×512×80-400 voxels
  </div>
</div>
<div style="display: flex; flex-direction: column; gap: 0.6rem;">
<div class="nv-card" style="border-left: 3px solid #1e3a5f;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem;">Contrast Phases</div>
  <div style="font-size: 0.82rem; color: #4a4a4a; line-height: 1.7;">
    <div style="display: flex; justify-content: space-between; margin-bottom: 0.2rem;"><strong style="color: #1a1a1a;">Corticomedullary</strong> <span style="color: #8a8a8a;">cortex enhances</span></div>
    <div style="display: flex; justify-content: space-between; margin-bottom: 0.2rem;"><strong style="color: #1a1a1a;">Nephrographic</strong> <span style="color: #8a8a8a;">parenchyma uniform</span></div>
    <div style="display: flex; justify-content: space-between;"><strong style="color: #1a1a1a;">Excretory</strong> <span style="color: #8a8a8a;">collecting system fills</span></div>
  </div>
</div>
<div class="nv-card nv-card-green">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.4rem;">Why Contrast-Enhanced?</div>
  <div style="font-size: 0.82rem; color: #4a4a4a; line-height: 1.5;">Tumors enhance differently than normal parenchyma due to abnormal vasculature. This differential enhancement is what the model learns to detect.</div>
</div>
<div class="nv-card" style="background: #fdf6f0; border: 1px solid #f0d9c5;">
  <div style="font-size: 0.82rem; color: #4a4a4a; line-height: 1.5;"><strong style="color: #bc4b31;">Challenge:</strong> Tumor and kidney parenchyma have overlapping HU ranges, making intensity-based separation alone insufficient.</div>
</div>
</div>
</div>
<!--
Notes:
CT fundamentals for committee members who may not be imaging experts. HU scale diagram shows where kidney and tumor sit. Contrast phases explain why enhanced CT is used. This sets up the preprocessing slide that follows. 30 seconds.
-->

---

<!-- ============================================================

     SLIDE 6: DATASET — KiTS23

     ============================================================ -->
<SectionTitle number="02" title="Dataset: KiTS23" subtitle="Kidney Tumor Segmentation Challenge 2023 — 489 contrast-enhanced CT cases" />
<div style="margin-top: 0.8rem; display: grid; grid-template-columns: 1fr 1.6fr; gap: 1.2rem; align-items: start;">
  <div style="display: flex; flex-direction: column; gap: 0.6rem;">
    <div class="nv-card" style="border-left: 3px solid #1e3a5f;">
      <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Overview</div>
      <div style="display: flex; flex-direction: column; gap: 0.4rem;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.85rem; color: #8a8a8a;">Total Cases</span>
          <span style="font-size: 1.1rem; font-weight: 700; color: #1a1a1a;">489</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.85rem; color: #8a8a8a;">Segmentation Classes</span>
          <span style="font-size: 1.1rem; font-weight: 700; color: #1a1a1a;">3</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.85rem; color: #8a8a8a;">Format</span>
          <span style="font-size: 0.9rem; font-weight: 600; color: #1a1a1a;">NIfTI (.nii.gz)</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.85rem; color: #8a8a8a;">Origin</span>
          <span style="font-size: 0.85rem; font-weight: 600; color: #1a1a1a;">Multi-institution</span>
        </div>
      </div>
    </div>
    <div class="nv-card nv-card-green">
      <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.5rem;">Our Split</div>
      <div style="display: flex; flex-direction: column; gap: 0.4rem;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.85rem; color: #8a8a8a;">Training</span>
          <span style="font-size: 0.95rem; font-weight: 600; color: #1a1a1a;">361 <span style="font-size: 0.75rem; color: #8a8a8a;">(~74%)</span></span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.85rem; color: #8a8a8a;">Validation</span>
          <span style="font-size: 0.95rem; font-weight: 600; color: #1a1a1a;">64 <span style="font-size: 0.75rem; color: #8a8a8a;">(~13%)</span></span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.85rem; color: #8a8a8a;">Test (held-out)</span>
          <span style="font-size: 0.95rem; font-weight: 700; color: #2d6a4f;">64 <span style="font-size: 0.75rem; color: #8a8a8a;">(~13%)</span></span>
        </div>
      </div>
    </div>
    <div class="nv-card" style="padding: 0.7rem;">
      <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem;">Classes</div>
      <div style="font-size: 0.82rem; color: #4a4a4a; line-height: 1.7;">
        <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="display: inline-block; width: 12px; height: 12px; background: #e8e8e8; border-radius: 2px;"></span><span><strong>Background</strong> — everything else</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="display: inline-block; width: 12px; height: 12px; background: #2d6a4f; border-radius: 2px;"></span><span><strong>Kidney</strong> — renal parenchyma</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="display: inline-block; width: 12px; height: 12px; background: #bc4b31; border-radius: 2px;"></span><span><strong>Tumor/Cyst</strong> — merged class</span></div>
      </div>
    </div>
  </div>
  <div class="nv-svg-wrapper" style="margin-top: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 260px;">
    <img src="/images/voxel_pie_chart.png" alt="Dataset voxel distribution pie chart" style="width: 100%; height: auto; max-height: 260px; object-fit: contain;" />
    <div style="margin-top: 0.6rem; font-size: 0.78rem; color: #8a8a8a; text-align: center;">Class voxel distribution across all KiTS23 cases</div>
  </div>
</div>
<div style="margin-top: 0.8rem;">
  <ChallengeCard title="Tumor/Cyst Merged Class" problem="KiTS23 merges tumor and cyst into one foreground class" mitigation="Documented limitation — cannot distinguish benign from malignant. Discussed in defense Q&A." />
</div>
<div style="margin-top: 0.6rem; font-size: 0.8rem; color: #8a8a8a; padding: 0.5rem; background: #fafbfc; border-radius: 4px;">
  <strong style="color: #8a8a8a;">Important:</strong> The 64-case test set is a <span class="nv-accent">project-defined held-out subset</span> — not the official KiTS23 leaderboard test set.
</div>
<!--

Notes:

KiTS23 is a public benchmark. Three classes. The merged tumor/cyst class is a limitation we document honestly — the system cannot tell a benign cyst from a malignant tumor. Critical: the 64-case test is our project-defined held-out subset, not the official challenge test. Do NOT claim leaderboard performance. Fill [TODO] placeholders with actual KiTS23 split numbers. 40 seconds.

-->

---

<!-- ============================================================

     SLIDE 7: DATASET STATISTICS

     ============================================================ -->
<SectionTitle number="02" title="Dataset Statistics" subtitle="KiTS23 by the numbers — multi-institution, multi-scanner data" />
<div class="nv-three-col" style="margin-top: 0.8rem;">
<MetricCard label="Total Cases" value="489" subvalue="Contrast-enhanced CT volumes" status="info" />
<MetricCard label="Training Set" value="361" subvalue="~74% for model training" status="info" />
<MetricCard label="Validation Set" value="64" subvalue="~13% for hyperparameter tuning" status="info" />
</div>
<div class="nv-three-col" style="margin-top: 0.6rem;">
<MetricCard label="Our Test Set" value="64" subvalue="~13% held-out, never seen" status="success" />
<MetricCard label="Institutions" value="[PLACEHOLDER]" subvalue="Multi-center data" status="info" />
<MetricCard label="Avg Slices/Case" value="~[PLACEHOLDER]" subvalue="Variable: 80-400 slices" status="info" />
</div>
<div style="margin-top: 0.8rem; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
  <div class="nv-svg-wrapper" style="min-height: 120px;">
    <img src="/images/class_voxel_distribution.png" alt="Class voxel distribution bar chart" style="width: 100%; height: auto; max-height: 140px; object-fit: contain;" />
  </div>
  <div class="nv-card" style="display: flex; flex-direction: column; justify-content: center;">
    <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem;">Key Characteristics</div>
    <div style="font-size: 0.82rem; color: #4a4a4a; line-height: 1.7;">
      <div>&#8226; Nephrographic phase preferred</div>
      <div>&#8226; Variable slice thickness & spacing</div>
      <div>&#8226; Diverse tumor sizes & locations</div>
      <div>&#8226; Expert-annotated ground truth</div>
    </div>
  </div>
</div>
<div class="nv-card nv-card-orange" style="margin-top: 0.6rem;">
  <div style="font-size: 0.82rem; color: #4a4a4a; text-align: center;"><strong style="color: #1a1a1a;">Important:</strong> The 64-case test set is a <span class="nv-accent">project-defined held-out subset</span> — not the official KiTS23 leaderboard test set.</div>
</div>
<!--
Notes:
Dataset statistics with metric cards and a placeholder for the class distribution chart. Emphasize the train/val/test split and the critical distinction about the test set. 30 seconds.
-->

---

<!-- ============================================================

     SLIDE 8: DATA SPLIT

     ============================================================ -->
<SectionTitle number="02" title="Data Split" subtitle="How we divided 489 cases for unbiased evaluation" />
<div style="margin-top: 1rem; display: flex; align-items: center; justify-content: center; gap: 0.5rem; flex-wrap: wrap;">
<div class="nv-card nv-card-cyan" style="text-align: center; min-width: 180px; padding: 1rem;">
  <div style="font-size: 0.75rem; color: #1e3a5f; font-weight: 700; margin-bottom: 0.3rem;">Training Set</div>
  <div style="font-family: 'SF Mono', monospace; font-size: 2.2rem; font-weight: 800; color: #1a1a1a;">361</div>
  <div style="font-size: 0.8rem; color: #8a8a8a; margin-top: 0.2rem;">~74% of data</div>
  <div style="font-size: 0.75rem; color: #8a8a8a; margin-top: 0.3rem;">Used for model<br>training only</div>
</div>
<div style="color: #1e3a5f; font-size: 1.5rem;">&rarr;</div>
<div class="nv-card" style="text-align: center; min-width: 180px; padding: 1rem;">
  <div style="font-size: 0.75rem; color: #8a8a8a; font-weight: 700; margin-bottom: 0.3rem;">Validation Set</div>
  <div style="font-family: 'SF Mono', monospace; font-size: 2.2rem; font-weight: 800; color: #1a1a1a;">64</div>
  <div style="font-size: 0.8rem; color: #8a8a8a; margin-top: 0.2rem;">~13% of data</div>
  <div style="font-size: 0.75rem; color: #8a8a8a; margin-top: 0.3rem;">Used for hyperparameter<br>tuning & checkpoint selection</div>
</div>
<div style="color: #1e3a5f; font-size: 1.5rem;">&rarr;</div>
<div class="nv-card nv-card-green" style="text-align: center; min-width: 180px; padding: 1rem;">
  <div style="font-size: 0.75rem; color: #2d6a4f; font-weight: 700; margin-bottom: 0.3rem;">Test Set</div>
  <div style="font-family: 'SF Mono', monospace; font-size: 2.2rem; font-weight: 800; color: #1a1a1a;">64</div>
  <div style="font-size: 0.8rem; color: #8a8a8a; margin-top: 0.2rem;">~13% of data</div>
  <div style="font-size: 0.75rem; color: #8a8a8a; margin-top: 0.3rem;">Held-out, never seen<br>during development</div>
</div>
</div>
<div class="nv-card" style="margin-top: 1rem;">
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5; text-align: center;"><strong style="color: #1a1a1a;">Split method:</strong> Random stratified by tumor presence [PLACEHOLDER]. Case IDs fixed before any model training.</div>
</div>
<!--
Notes:
Visual data split diagram showing the three partitions as large cards with arrows. Emphasizes that the test set was fixed before model development and never used during training. 25 seconds.
-->

---

<!-- ============================================================

     SLIDE 9: VOXEL DISTRIBUTION

     ============================================================ -->
<SectionTitle number="02" title="Voxel Distribution" subtitle="Class imbalance in the KiTS23 dataset" />
<div class="nv-two-col" style="margin-top: 1rem; align-items: center;">
<div>
  <div class="nv-svg-wrapper">
    <img src="/images/class_voxel_distribution.png" alt="Voxel distribution pie chart showing class imbalance" style="max-height: 220px; width: 100%; object-fit: contain;" />
  </div>
</div>
<div style="display: flex; flex-direction: column; gap: 0.6rem;">
<div class="nv-card nv-card-red" style="text-align: center; padding: 1rem;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #9b2c2c; margin-bottom: 0.3rem;">Tumor Voxels</div>
  <div style="font-family: 'SF Mono', monospace; font-size: 2.2rem; font-weight: 800; color: #1a1a1a;">&lt; 0.1%</div>
  <div style="font-size: 0.8rem; color: #8a8a8a; margin-top: 0.2rem;">of total volume</div>
</div>
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem;">Why This Matters</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">A model predicting <strong style="color: #1a1a1a;">all background</strong> achieves 99% accuracy — and completely fails clinically. Standard accuracy is meaningless.</div>
</div>
<div class="nv-card nv-card-green">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.4rem;">Our Response</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">Dice loss + conservative post-processing + detection-first evaluation.</div>
</div>
</div>
</div>
<!--
Notes:
Visual slide showing the extreme class imbalance. Tumor is less than 0.1% of voxels. Pie chart makes this visceral. This is why we use Dice loss, not accuracy. 25 seconds.
-->

---

<!-- ============================================================

     SLIDE 10: RELATED WORK

     ============================================================ -->
<SectionTitle number="03" title="Related Work" subtitle="Where NephroVision fits in the landscape" />
<div style="margin-top: 0.8rem;">
<table>
<thead>
<tr>
<th>Approach</th>
<th>Strengths</th>
<th>Limitations</th>
<th>NephroVision</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong style="color: #1a1a1a">2D U-Net</strong></td>
<td>Computationally efficient</td>
<td>Misses inter-slice context</td>
<td><span style="color: #2d6a4f; font-weight: 600;">3D convolutions</span></td>
</tr>
<tr>
<td><strong style="color: #1a1a1a">nnU-Net</strong></td>
<td>Self-configuring, state-of-the-art</td>
<td>Complex, opaque configuration</td>
<td><span style="color: #bc4b31; font-weight: 600;">Planned future work</span></td>
</tr>
<tr>
<td><strong style="color: #1a1a1a">KiTS23 Winners</strong></td>
<td>Top leaderboard performance</td>
<td>Ensembles, heavy compute</td>
<td><span style="color: #1e3a5f; font-weight: 600;">Academic scope</span></td>
</tr>
<tr>
<td><strong style="color: #1a1a1a">Manual Segmentation</strong></td>
<td>Gold standard accuracy</td>
<td>Time-consuming, variable</td>
<td><span style="color: #2d6a4f; font-weight: 600;">Decision-support</span></td>
</tr>
</tbody>
</table>
</div>
<div style="margin-top: 0.8rem; font-size: 0.8rem; color: #8a8a8a;">
  <strong style="color: #4a4a4a;">Key distinction:</strong> NephroVision is a documented academic prototype with full development transparency — not a black-box solution. We show what works, what does not, and why.
</div>
<!--

Notes:

Contextualize NephroVision within the field. 2D U-Net misses volumetric context — we chose 3D. nnU-Net is state-of-the-art but complex — we plan to evaluate it. KiTS23 winners use ensembles and heavy compute — our scope is academic. Manual segmentation remains gold standard — we support, not replace, the radiologist. 30 seconds.

-->

---

<!-- ============================================================

     SLIDE 11: EVOLUTION OF MEDICAL SEGMENTATION

     ============================================================ -->
<SectionTitle number="03" title="Evolution of Medical Segmentation" subtitle="From manual delineation to deep learning" />
<div style="margin-top: 1rem; display: flex; align-items: center; justify-content: center; gap: 0.3rem; flex-wrap: wrap;">
<div class="nv-card" style="text-align: center; min-width: 130px; padding: 0.8rem;">
  <div style="font-size: 0.7rem; color: #8a8a8a; margin-bottom: 0.3rem;">Pre-2015</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">Manual</div>
  <div style="font-size: 0.75rem; color: #8a8a8a; margin-top: 0.2rem;">Slice-by-slice<br>Expert-dependent</div>
</div>
<div style="color: #1e3a5f; font-size: 1rem;">&rarr;</div>
<div class="nv-card" style="text-align: center; min-width: 130px; padding: 0.8rem;">
  <div style="font-size: 0.7rem; color: #8a8a8a; margin-bottom: 0.3rem;">2015</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">U-Net</div>
  <div style="font-size: 0.75rem; color: #8a8a8a; margin-top: 0.2rem;">Encoder-decoder<br>Skip connections</div>
</div>
<div style="color: #1e3a5f; font-size: 1rem;">&rarr;</div>
<div class="nv-card" style="text-align: center; min-width: 130px; padding: 0.8rem;">
  <div style="font-size: 0.7rem; color: #8a8a8a; margin-bottom: 0.3rem;">2016</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">3D U-Net</div>
  <div style="font-size: 0.75rem; color: #8a8a8a; margin-top: 0.2rem;">Volumetric<br>Context</div>
</div>
<div style="color: #1e3a5f; font-size: 1rem;">&rarr;</div>
<div class="nv-card nv-card-cyan" style="text-align: center; min-width: 130px; padding: 0.8rem; border-color: #1e3a5f;">
  <div style="font-size: 0.7rem; color: #1e3a5f; margin-bottom: 0.3rem;">2021</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">nnU-Net</div>
  <div style="font-size: 0.75rem; color: #8a8a8a; margin-top: 0.2rem;">Self-configuring<br>State-of-the-art</div>
</div>
</div>
<div style="margin-top: 1rem; padding: 1rem; background: #fafbfc; border-radius: 6px;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #8a8a8a; margin-bottom: 0.8rem; text-align: center;">Typical Kidney Dice Performance Progression</div>
  <div style="display: flex; align-items: flex-end; justify-content: center; gap: 1.5rem; height: 100px; padding: 0 1rem;">
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.7rem; color: #4a4a4a; font-weight: 600;">~0.75</div>
      <div style="width: 40px; height: 40px; background: #e0e0e0; border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.7rem; color: #8a8a8a;">Manual</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.7rem; color: #4a4a4a; font-weight: 600;">~0.82</div>
      <div style="width: 40px; height: 55px; background: #c5d5e8; border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.7rem; color: #8a8a8a;">2D U-Net</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.7rem; color: #4a4a4a; font-weight: 600;">~0.88</div>
      <div style="width: 40px; height: 70px; background: #8ab4d0; border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.7rem; color: #8a8a8a;">3D U-Net</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.7rem; color: #4a4a4a; font-weight: 600;">~0.93</div>
      <div style="width: 40px; height: 85px; background: #1e3a5f; border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.7rem; color: #8a8a8a;">nnU-Net</div>
    </div>
  </div>
  <div style="font-size: 0.72rem; color: #8a8a8a; text-align: center; margin-top: 0.5rem;">Illustrative values from literature. NephroVision kidney Dice: 0.9307</div>
</div>
<!--
Notes:
Timeline showing progression from manual segmentation to modern deep learning. NephroVision sits between 3D U-Net and nnU-Net in performance but prioritizes transparency and documentation. The performance chart shows where we fit in the field. 25 seconds.
-->

---

<!-- ============================================================

   SLIDE 12: DEVELOPMENT JOURNEY

   ============================================================ -->
<SectionTitle number="03" title="Development Journey" subtitle="Documented process — not just final results" />

<div class="nv-two-col" style="gap: 0.8rem;">
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
  <PipelineStep number="1" title="Problem Understanding" description="Clinical motivation & decision-support scope" />
  <PipelineStep number="2" title="Dataset Exploration" description="KiTS23 characteristics & annotation conventions" />
  <PipelineStep number="3" title="Preprocessing Design" description="HU clipping & normalization rationale" />
  <PipelineStep number="4" title="Baseline 3D U-Net" description="Architecture selection & training setup" />
  <PipelineStep number="5" title="Training Iterations" description="Experiment log & checkpoint selection" />
</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
  <PipelineStep number="6" title="Inference Pipeline" description="Sliding window + test-time augmentation" />
  <PipelineStep number="7" title="Post-processing" description="Conservative blob removal thresholds" />
  <PipelineStep number="8" title="Web Visualization" description="Browser-based 3D viewer" />
  <PipelineStep number="9" title="Safety Documentation" description="IEC 62304 Class B positioning" />
  <PipelineStep number="10" title="Final Validation" description="64-case held-out evaluation" />
</div>
</div>
<div class="nv-svg-wrapper">
  <img src="/images/development_timeline.svg" />
</div>
<!--

Notes:

EMPHASIS SLIDE — 90 seconds. This directly addresses the mid-year feedback. We documented a 10-phase development timeline with decisions at each phase. Three major difficulties: GPU memory (patch-based training + sliding window), class imbalance (loss functions + post-processing), tumor variability (TTA + overlap fusion). Key message: this was an iterative engineering process with full documentation — experiment log, development timeline, reproducibility notes, failure analysis. We did not hide difficulties.

-->

---

<!-- ============================================================

     SLIDE 13: WHAT WE BUILT

     ============================================================ -->
<SectionTitle number="04" title="What We Built" subtitle="End-to-end segmentation pipeline" />
<div style="display: flex; align-items: center; justify-content: center; gap: 0.3rem; margin-top: 1rem; flex-wrap: wrap;">
  <div class="nv-card" style="text-align: center; min-width: 110px; padding: 0.8rem;">
    <div style="font-size: 0.75rem; color: #8a8a8a; margin-bottom: 0.2rem;">Input</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">NIfTI CT</div>
  </div>
  <div style="color: #1e3a5f; font-size: 1.2rem;">&rarr;</div>
  <div class="nv-card" style="text-align: center; min-width: 110px; padding: 0.8rem;">
    <div style="font-size: 0.75rem; color: #8a8a8a; margin-bottom: 0.2rem;">Preprocess</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">HU + Norm</div>
  </div>
  <div style="color: #1e3a5f; font-size: 1.2rem;">&rarr;</div>
  <div class="nv-card nv-card-cyan" style="text-align: center; min-width: 110px; padding: 0.8rem; border-color: #1e3a5f;">
    <div style="font-size: 0.75rem; color: #1e3a5f; margin-bottom: 0.2rem;">Model</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">3D U-Net</div>
  </div>
  <div style="color: #1e3a5f; font-size: 1.2rem;">&rarr;</div>
  <div class="nv-card" style="text-align: center; min-width: 110px; padding: 0.8rem;">
    <div style="font-size: 0.75rem; color: #8a8a8a; margin-bottom: 0.2rem;">Inference</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">Sliding + TTA</div>
  </div>
  <div style="color: #1e3a5f; font-size: 1.2rem;">&rarr;</div>
  <div class="nv-card" style="text-align: center; min-width: 110px; padding: 0.8rem;">
    <div style="font-size: 0.75rem; color: #8a8a8a; margin-bottom: 0.2rem;">Post-process</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">Blob Filter</div>
  </div>
  <div style="color: #1e3a5f; font-size: 1.2rem;">&rarr;</div>
  <div class="nv-card nv-card-green" style="text-align: center; min-width: 110px; padding: 0.8rem; border-color: #2d6a4f;">
    <div style="font-size: 0.75rem; color: #2d6a4f; margin-bottom: 0.2rem;">Output</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">Mask + Viz</div>
  </div>
</div>

<!--

Notes:

Visual pipeline walkthrough. Left to right: NIfTI input  preprocessing (HU clipping [-200, 300], normalization [0,1])  3D U-Net model  sliding-window inference with TTA  post-processing (blob removal)  output (mask, volumetric stats, 3D visualization). Keep it high-level — the next slides dive into each stage. 35 seconds.

-->

---

<!-- ============================================================

     SLIDE 14: PIPELINE ARCHITECTURE

     ============================================================ -->
<SectionTitle number="04" title="Pipeline Architecture" subtitle="End-to-end system diagram with component details" />
<div style="margin-top: 0.8rem;">
  <div class="nv-placeholder" style="height: 160px;">
    <div class="nv-placeholder-label">Detailed System Architecture</div>
    <div class="nv-placeholder-desc">Block diagram: NIfTI Loader → HU Clipper → Normalizer → 3D U-Net → Sliding Window Engine → TTA Averager → Blob Filter → Volume Calculator → 3D Mesher → Web API → Browser</div>
    <div class="nv-placeholder-hint">Generate with draw.io or similar — show all 10+ components with data flow arrows</div>
  </div>
</div>
<div style="margin-top: 0.8rem; display: flex; gap: 0.4rem; flex-wrap: wrap; justify-content: center;">
<div class="nv-card" style="text-align: center; min-width: 90px; padding: 0.5rem;">
  <div style="font-size: 0.65rem; color: #8a8a8a;">Input</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.8rem;">NIfTI</div>
</div>
<div class="nv-card" style="text-align: center; min-width: 90px; padding: 0.5rem;">
  <div style="font-size: 0.65rem; color: #8a8a8a;">Preprocess</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.8rem;">HU+Norm</div>
</div>
<div class="nv-card nv-card-cyan" style="text-align: center; min-width: 90px; padding: 0.5rem;">
  <div style="font-size: 0.65rem; color: #1e3a5f;">Model</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.8rem;">3D U-Net</div>
</div>
<div class="nv-card" style="text-align: center; min-width: 90px; padding: 0.5rem;">
  <div style="font-size: 0.65rem; color: #8a8a8a;">Inference</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.8rem;">Sliding+TTA</div>
</div>
<div class="nv-card" style="text-align: center; min-width: 90px; padding: 0.5rem;">
  <div style="font-size: 0.65rem; color: #8a8a8a;">Post-Process</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.8rem;">Blob Filter</div>
</div>
<div class="nv-card" style="text-align: center; min-width: 90px; padding: 0.5rem;">
  <div style="font-size: 0.65rem; color: #8a8a8a;">Analysis</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.8rem;">Volumes</div>
</div>
<div class="nv-card nv-card-green" style="text-align: center; min-width: 90px; padding: 0.5rem;">
  <div style="font-size: 0.65rem; color: #2d6a4f;">Output</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.8rem;">3D Viz</div>
</div>
</div>
<!--
Notes:
Detailed system architecture diagram showing all components from input to output. Mini cards repeat the pipeline flow for quick reference. The diagram shows this is not just a model — it is a full system with preprocessing, inference, post-processing, analysis, and visualization. 25 seconds.
-->

---

<!-- ============================================================

     SLIDE 15: PREPROCESSING DECISIONS

     ============================================================ -->
<SectionTitle number="05" title="Preprocessing Decisions" subtitle="Empirical choices with documented rationale" />

<div class="nv-two-col" style="margin-top: 0.5rem;">
<div>
<div class="nv-card" style="margin-bottom: 0.7rem;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">HU Clipping</div>
  <div style="font-size: 1.6rem; font-weight: 800; color: #1a1a1a; font-family: var(--font-mono);">[-200, 300]</div>
  <div style="font-size: 0.82rem; color: #8a8a8a; margin-top: 0.3rem;">Preserves soft-tissue contrast  Suppresses bone & air</div>
</div>
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Normalization</div>
  <div style="font-size: 1.3rem; font-weight: 700; color: #1a1a1a; font-family: var(--font-mono);">x_norm = (x + 200) / 500</div>
  <div style="font-size: 0.82rem; color: #8a8a8a; margin-top: 0.3rem;">Min-max to [0, 1]  Identical for train & inference</div>
</div>
</div>
<div>
<div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.6; margin-bottom: 0.8rem;">
  <strong style="color: #1a1a1a">Rationale:</strong> The range [-200, 300] was selected empirically after testing multiple ranges. It captures kidney parenchyma and tumor tissue while suppressing bone (&gt;300 HU), air (&lt;-200 HU), and contrast bolus extremes.
</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<ChallengeCard title="Validation" problem="Variable NIfTI metadata across scanners" mitigation="Standardized orientation & spacing validation pipeline" />
<ChallengeCard title="Consistency" problem="Different CT protocols produce different intensity distributions" mitigation="Identical preprocessing for training and inference prevents distribution mismatch" />
</div>
</div>
</div>
<div class="nv-svg-wrapper">
  <img src="/images/preprocessing_workflow.svg" />
</div>
<!--

Notes:

EMPHASIS SLIDE — 60 seconds. This directly addresses the mid-year feedback about documenting decisions. We did not pick [-200, 300] randomly — we evaluated multiple ranges empirically. The normalization formula is straightforward. Identical preprocessing for training and inference prevents distribution mismatch. All documented in preprocessing_decisions.md.

-->

---

<!-- ============================================================

     SLIDE 16: INTENSITY DISTRIBUTION

     ============================================================ -->
<SectionTitle number="05" title="Intensity Distribution" subtitle="Why we clip HU to [-200, 300]" />
<div class="nv-two-col" style="margin-top: 0.8rem; align-items: center;">
<div>
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem; text-align: center;">Before Clipping</div>
  <div class="nv-svg-wrapper">
    <img src="/images/before_clipping.png" alt="Raw HU histogram before clipping" style="width: 100%; height: auto; max-height: 160px; object-fit: contain;" />
  </div>
  <div style="margin-top: 0.4rem; font-size: 0.8rem; color: #8a8a8a; text-align: center;">Bone (>300 HU) dominates the histogram</div>
</div>
<div>
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.4rem; text-align: center;">After Clipping</div>
  <div class="nv-svg-wrapper">
    <img src="/images/after_clipping.png" alt="Clipped HU histogram" style="width: 100%; height: auto; max-height: 160px; object-fit: contain;" />
  </div>
  <div style="margin-top: 0.4rem; font-size: 0.8rem; color: #8a8a8a; text-align: center;">Soft tissue contrast preserved, bone/air suppressed</div>
</div>
</div>
<div style="margin-top: 0.8rem; display: flex; gap: 0.5rem; flex-wrap: wrap; justify-content: center;">
<div class="nv-card" style="text-align: center; min-width: 120px; padding: 0.6rem;">
  <div style="font-size: 0.7rem; color: #8a8a8a;">Kidney HU</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">20-70</div>
</div>
<div class="nv-card" style="text-align: center; min-width: 120px; padding: 0.6rem;">
  <div style="font-size: 0.7rem; color: #8a8a8a;">Tumor HU</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">30-90</div>
</div>
<div class="nv-card" style="text-align: center; min-width: 120px; padding: 0.6rem;">
  <div style="font-size: 0.7rem; color: #8a8a8a;">Bone HU</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;">>300</div>
</div>
<div class="nv-card" style="text-align: center; min-width: 120px; padding: 0.6rem;">
  <div style="font-size: 0.7rem; color: #8a8a8a;">Air HU</div>
  <div style="font-weight: 700; color: #1a1a1a; font-size: 0.9rem;"><-200</div>
</div>
</div>
<!--
Notes:
Before/after histograms showing why HU clipping matters. The raw histogram is dominated by bone. After clipping, the soft-tissue range is clear. Mini cards show typical HU values for relevant tissues. 25 seconds.
-->

---

<!-- ============================================================

     SLIDE 17: PREPROCESSING IMPACT

     ============================================================ -->
<SectionTitle number="05" title="Preprocessing Impact" subtitle="What the model sees vs what the radiologist sees" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div>
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem; text-align: center;">Raw CT Slice</div>
  <div class="nv-placeholder" style="height: 140px;">
    <div class="nv-placeholder-label">Original CT</div>
    <div class="nv-placeholder-desc">Full HU range — bone bright, air dark, soft tissue mid-gray</div>
    <div class="nv-placeholder-hint">Use actual KiTS23 slice — show kidney and tumor in native CT</div>
  </div>
</div>
<div>
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.4rem; text-align: center;">After Preprocessing</div>
  <div class="nv-placeholder" style="height: 140px;">
    <div class="nv-placeholder-label">Normalized Input</div>
    <div class="nv-placeholder-desc">Clipped to [-200, 300] and normalized [0, 1] — enhanced soft tissue contrast</div>
    <div class="nv-placeholder-hint">Same slice after preprocessing — kidney and tumor boundaries more distinct</div>
  </div>
</div>
</div>
<div class="nv-card nv-card-cyan" style="margin-top: 0.8rem;">
  <div style="font-size: 0.85rem; color: #4a4a4a; text-align: center;"><strong style="color: #1a1a1a;">Identical preprocessing</strong> for training and inference prevents distribution mismatch. The model learns on the same intensity distribution it sees at test time.</div>
</div>
<!--
Notes:
Side-by-side CT slice comparison. Raw vs preprocessed. Shows that preprocessing enhances soft-tissue contrast and suppresses irrelevant structures. Critical rule: identical preprocessing for train and test. 20 seconds.
-->

---

<!-- ============================================================

     SLIDE 18: 3D U-NET ARCHITECTURE

     ============================================================ -->
<SectionTitle number="06" title="3D U-Net Architecture" subtitle="Volumetric encoder-decoder with skip connections" />
<div class="nv-svg-wrapper" style="margin-top: 0.6rem; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 280px;">
  <img src="/images/u_net_arch2.png" alt="3D U-Net Architecture Diagram" style="width: 100%; height: auto; max-height: 280px; object-fit: contain;" />
  <div style="margin-top: 0.5rem; font-size: 0.78rem; color: #8a8a8a; text-align: center;">Encoder → Bottleneck → Decoder with skip connections</div>
</div>
<div class="nv-four-col" style="margin-top: 0.8rem;">
<div class="nv-card" style="text-align: center;">
  <div style="font-size: 0.75rem; color: #1e3a5f; font-weight: 700; margin-bottom: 0.2rem;">Encoder</div>
  <div style="font-size: 0.8rem; color: #8a8a8a;">3D conv + downsample</div>
</div>
<div class="nv-card" style="text-align: center;">
  <div style="font-size: 0.75rem; color: #1e3a5f; font-weight: 700; margin-bottom: 0.2rem;">Skip</div>
  <div style="font-size: 0.8rem; color: #8a8a8a;">Fine detail transfer</div>
</div>
<div class="nv-card" style="text-align: center;">
  <div style="font-size: 0.75rem; color: #1e3a5f; font-weight: 700; margin-bottom: 0.2rem;">Decoder</div>
  <div style="font-size: 0.8rem; color: #8a8a8a;">3D conv + upsample</div>
</div>
<div class="nv-card" style="text-align: center;">
  <div style="font-size: 0.75rem; color: #1e3a5f; font-weight: 700; margin-bottom: 0.2rem;">Output</div>
  <div style="font-size: 0.8rem; color: #8a8a8a;">3-class softmax</div>
</div>
</div>
<!--

Notes:

The 3D U-Net is the standard for volumetric medical segmentation. Encoder extracts features through downsampling. Decoder restores resolution through upsampling. Skip connections preserve fine spatial details. Output is a per-voxel 3-class probability map. Key advantage over 2D: inter-slice context. The kidney is a 3D structure — 2D slice-by-slice misses spatial relationships. Replace the placeholder with an actual diagram before defense. 40 seconds.

-->

---

<!-- ============================================================

     SLIDE 19: NETWORK ARCHITECTURE DETAIL

     ============================================================ -->
<SectionTitle number="06" title="Network Architecture" subtitle="Layer-by-layer 3D U-Net configuration" />
<div style="margin-top: 0.6rem; display: grid; grid-template-columns: repeat(5, 1fr); gap: 0.6rem;">
  <div class="nv-card" style="text-align: center; padding: 1rem 0.5rem;">
    <div style="font-size: 0.7rem; color: #8a8a8a; margin-bottom: 0.3rem;">Depth</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 1.1rem;">4 stages</div>
    <div style="font-size: 0.7rem; color: #8a8a8a; margin-top: 0.2rem;">Encoder + Decoder</div>
  </div>
  <div class="nv-card" style="text-align: center; padding: 1rem 0.5rem;">
    <div style="font-size: 0.7rem; color: #8a8a8a; margin-bottom: 0.3rem;">Base Channels</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 1.1rem;">32</div>
    <div style="font-size: 0.7rem; color: #8a8a8a; margin-top: 0.2rem;">Doubles each level</div>
  </div>
  <div class="nv-card" style="text-align: center; padding: 1rem 0.5rem;">
    <div style="font-size: 0.7rem; color: #8a8a8a; margin-bottom: 0.3rem;">Parameters</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 1.1rem;">~8.6M</div>
    <div style="font-size: 0.7rem; color: #8a8a8a; margin-top: 0.2rem;">Trainable weights</div>
  </div>
  <div class="nv-card" style="text-align: center; padding: 1rem 0.5rem;">
    <div style="font-size: 0.7rem; color: #8a8a8a; margin-bottom: 0.3rem;">Norm</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 1.1rem;">InstanceNorm3d</div>
    <div style="font-size: 0.7rem; color: #8a8a8a; margin-top: 0.2rem;">Per-channel stats</div>
  </div>
  <div class="nv-card" style="text-align: center; padding: 1rem 0.5rem;">
    <div style="font-size: 0.7rem; color: #8a8a8a; margin-bottom: 0.3rem;">Activation</div>
    <div style="font-weight: 700; color: #1a1a1a; font-size: 1.1rem;">LeakyReLU</div>
    <div style="font-size: 0.7rem; color: #8a8a8a; margin-top: 0.2rem;">Negative slope 0.01</div>
  </div>
</div>
<div style="margin-top: 0.8rem;">
  <div class="nv-card">
    <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Layer Configuration</div>
    <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.6; font-family: var(--font-mono);">
      Input(1) → Conv3D(32) → Down → Conv3D(64) → Down → Conv3D(128) → Down → Conv3D(256) → Bottleneck → Up+Skip(128) → Up+Skip(64) → Up+Skip(32) → Output(3)
    </div>
  </div>
</div>
<!--
Notes:
Detailed architecture slide with placeholder for layer-by-layer diagram. Mini cards show key specs: 4 stages, 32 channels, ~8.6M params, InstanceNorm, LeakyReLU. 25 seconds.
-->

---

<!-- ============================================================

     SLIDE 20: SKIP CONNECTIONS

     ============================================================ -->
<SectionTitle number="06" title="Skip Connections" subtitle="Preserving fine detail from encoder to decoder" />
<div class="nv-two-col" style="margin-top: 0.8rem; align-items: center;">
<div>
  <div class="nv-placeholder" style="height: 160px;">
    <div class="nv-placeholder-label">Skip Connection Diagram</div>
    <div class="nv-placeholder-desc">Visual showing encoder feature map (high res, low semantic) concatenated with decoder upsampled map (low res, high semantic)</div>
    <div class="nv-placeholder-hint">Simple U-shape diagram with highlighted skip arrows and concatenation blocks</div>
  </div>
</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem;">Without Skip</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">Decoder must recover fine details from compressed bottleneck alone. Result: blurry boundaries, lost texture.</div>
</div>
<div class="nv-card nv-card-green">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.4rem;">With Skip</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">Encoder features (high resolution) concatenated directly to decoder. Result: sharp boundaries, preserved detail.</div>
</div>
<div class="nv-card">
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;"><strong style="color: #1a1a1a;">Concatenation:</strong> Channel-wise merge doubles feature depth at each decoder level.</div>
</div>
</div>
</div>
<!--
Notes:
Explains why skip connections matter. Visual diagram + two comparison cards. Without skip = blurry, with skip = sharp. This is a key architectural choice that explains why U-Net works for medical segmentation. 20 seconds.
-->

---

<!-- ============================================================

     SLIDE 21: MODEL TRAINING DOCUMENTATION

     ============================================================ -->
<SectionTitle number="06" title="Model Training Documentation" subtitle="Every experiment logged — hypothesis to decision" />

<div class="nv-two-col" style="margin-top: 0.5rem;">
<div>
<div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.6; margin-bottom: 0.8rem;">
  <strong style="color: #1a1a1a">Experiment Log Structure:</strong> Each training run documented with experiment ID, date, dataset split, loss function, optimizer, learning rate, batch size, epochs, validation metrics, and final decision.
</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<PipelineStep number="1" title="Hypothesis" description="What we expect to change" />
<PipelineStep number="2" title="Setup" description="Hyperparameters & configuration" />
<PipelineStep number="3" title="Result" description="Validation metrics achieved" />
<PipelineStep number="4" title="Decision" description="Adopt, modify, or discard" />
</div>
</div>
<div>
<div class="nv-card" style="margin-bottom: 0.7rem;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Architecture</div>
  <div style="font-size: 0.9rem; color: #4a4a4a; line-height: 1.5;">
  — <strong style="color: #1a1a1a">3D convolutions</strong> capture inter-slice context<br>
  — <strong style="color: #1a1a1a">Encoder-decoder</strong> with skip connections<br>
  — <strong style="color: #1a1a1a">Three-class output:</strong> Background, Kidney, Tumor/Cyst
  </div>
</div>
<div class="nv-card nv-card-orange">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31; margin-bottom: 0.5rem;">Note</div>
  <div style="font-size: 0.85rem; color: #4a4a4a;">
  Exact hyperparameters (loss, optimizer, LR) are being finalized in the experiment log. Inference configuration is fully documented and verified.
  </div>
</div>
</div>
</div>
<!--

Notes:

EMPHASIS SLIDE — 60 seconds. The committee asked for documentation of what we did, not just the final result. We responded with a structured experiment log: hypothesis  setup  result  decision. Every training run was logged. Architecture rationale: 3D over 2D because the kidney is a 3D structure. Checkpoint selection based on validation Dice, not training loss. Be honest: some exact hyperparameters are still being completed in the experiment log. Do not invent values.

-->

---

<!-- ============================================================

     SLIDE 22: INFERENCE PIPELINE

     ============================================================ -->
<SectionTitle number="07" title="Inference Pipeline" subtitle="Sliding window + test-time augmentation" />
<div class="nv-three-col" style="margin-top: 0.8rem;">
<MetricCard label="Patch Size" value="64×192×192" subvalue="voxels per window" status="info" />
<MetricCard label="Overlap" value="50%" subvalue="all 3 dimensions" status="info" />
<MetricCard label="TTA" value="8 flips" subvalue="x, y, z combinations" status="info" />
</div>
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Sliding Window</div>
  <div style="font-size: 0.88rem; color: #4a4a4a; line-height: 1.5;">
  — Handles full CT volumes within GPU memory limits<br>

  — 50% overlap — every voxel predicted from multiple patches<br>

  — Averaging fusion — smooth transitions, no stitching artifacts
  </div>
</div>
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Test-Time Augmentation</div>
  <div style="font-size: 0.88rem; color: #4a4a4a; line-height: 1.5;">
  — 8 flip combinations (2³ = 8)<br>

  — Each version processed independently<br>

  — Predictions un-flipped and averaged — reduces boundary noise
  </div>
</div>
</div>
<div class="nv-svg-wrapper">
  <img src="/images/inference_workflow.svg" />
</div>
<!--

Notes:

Full CT volumes exceed GPU memory. Sliding window: 64×192×192 patches with 50% overlap. Every voxel near a boundary is predicted from at least two patches — averaging eliminates stitching artifacts. TTA: flip along x, y, z axes in all 8 combinations, run inference on each, un-flip and average. This reduces orientation-dependent artifacts. Cost is ~8x inference time, but only applied during final evaluation. 50 seconds.

-->

---

<!-- ============================================================

     SLIDE 23: SLIDING WINDOW VISUAL

     ============================================================ -->
<SectionTitle number="07" title="Sliding Window" subtitle="How we process volumes larger than GPU memory" />
<div style="margin-top: 0.8rem;">
  <div class="nv-placeholder" style="height: 160px;">
    <div class="nv-placeholder-label">Sliding Window Animation / Diagram</div>
    <div class="nv-placeholder-desc">Diagram showing a large CT volume being divided into overlapping 64×192×192 patches, processed sequentially, then fused back</div>
    <div class="nv-placeholder-hint">Use simple block diagram — large volume → grid of patches → GPU → predictions → fused volume</div>
  </div>
</div>
<div class="nv-three-col" style="margin-top: 0.8rem;">
<MetricCard label="Patch Size" value="64×192×192" subvalue="voxels" status="info" />
<MetricCard label="Overlap" value="50%" subvalue="all dimensions" status="info" />
<MetricCard label="Fusion" value="Averaging" subvalue="smooth boundaries" status="success" />
</div>
<div class="nv-card" style="margin-top: 0.8rem;">
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5; text-align: center;">Every voxel near a patch boundary is predicted from <strong style="color: #1a1a1a;">at least 2 patches</strong>. Averaging eliminates stitching artifacts.</div>
</div>
<!--
Notes:
Visual explanation of sliding window. Show how a large volume is broken into patches, processed, and reassembled. Key point: 50% overlap ensures every boundary voxel gets multiple predictions. 25 seconds.
-->

---

<!-- ============================================================

     SLIDE 24: TEST-TIME AUGMENTATION

     ============================================================ -->
<SectionTitle number="07" title="Test-Time Augmentation" subtitle="8 orientations, 8 predictions, 1 average" />
<div style="margin-top: 0.8rem;">
  <div class="nv-placeholder" style="height: 160px;">
    <div class="nv-placeholder-label">TTA 8-Flip Grid</div>
    <div class="nv-placeholder-desc">2×4 grid showing original + 7 flipped versions of a CT slice, with arrows showing flip axes</div>
    <div class="nv-placeholder-hint">Generate with matplotlib — 8 small subplots, each labeled with flip combination (x, y, z, xy, xz, yz, xyz)</div>
  </div>
</div>
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem;">Process</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">1. Flip volume along axis combination<br>2. Run inference<br>3. Un-flip prediction<br>4. Average all 8 predictions</div>
</div>
<div class="nv-card nv-card-orange">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31; margin-bottom: 0.4rem;">Trade-off</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;"><strong style="color: #1a1a1a;">Benefit:</strong> Reduces boundary noise by ~0.07 Tumor Dice.<br><strong style="color: #1a1a1a;">Cost:</strong> 8× inference time (~120s → 15s without TTA).</div>
</div>
</div>
<!--
Notes:
Visual grid showing the 8 flip combinations. Process card explains the 4 steps. Trade-off card quantifies the benefit (0.07 Dice improvement) and cost (8x time). TTA is only used for final evaluation, not during development. 25 seconds.
-->

---

<!-- ============================================================

     SLIDE 25: POST-PROCESSING

     ============================================================ -->
<SectionTitle number="07" title="Post-Processing" subtitle="Conservative filtering — detection sensitivity over precision" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div style="display: flex; flex-direction: column; gap: 0.7rem;">
<div class="nv-card">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
  <span style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f;">Kidney Blob Filter</span>
  <span style="font-family: 'SF Mono', 'JetBrains Mono', Consolas, monospace; font-size: 1.4rem; font-weight: 800; color: #1a1a1a">&lt; 5000</span>
  </div>
  <div style="font-size: 0.82rem; color: #8a8a8a;">voxels removed — eliminates extra-renal false positives</div>
</div>
<div class="nv-card nv-card-orange">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
  <span style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31;">Tumor Blob Filter</span>
  <span style="font-family: 'SF Mono', 'JetBrains Mono', Consolas, monospace; font-size: 1.4rem; font-weight: 800; color: #1a1a1a">&lt; 100</span>
  </div>
  <div style="font-size: 0.82rem; color: #8a8a8a;">voxels removed — deliberately conservative to preserve small lesions</div>
</div>
</div>
<div>
<div style="font-size: 0.88rem; color: #4a4a4a; line-height: 1.6; margin-bottom: 0.8rem;">
  <strong style="color: #1a1a1a">Design Rationale:</strong> In a decision-support workflow, false positives are acceptable because the physician reviews and dismisses them. False negatives — missed tumors — are far more dangerous because they are not available for physician review at all.
</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<ChallengeCard title="Sensitivity &gt; Precision" problem="Retaining some false positives" mitigation="Physician review catches and dismisses them" />
<ChallengeCard title="Missed Tumor Risk" problem="False negative = tumor never seen by physician" mitigation="Conservative 100-voxel threshold preserves small lesions" />
</div>
</div>
</div>
<div class="nv-svg-wrapper">
  <img src="/images/postprocessing_workflow.svg" />
</div>
<!--

Notes:

Post-processing removes spurious detections. Kidney: &lt;5000 voxels removed — eliminates noise outside the kidney. Tumor: &lt;100 voxels — deliberately conservative. The design philosophy: prioritize detection sensitivity over precision. In decision-support, false positives are reviewed and dismissed by the physician. False negatives (missed tumors) are catastrophic because the physician never sees them. This is a deliberate choice, not an accident. 45 seconds.

-->

---

<!-- ============================================================

     SLIDE 26: POST-PROCESSING EFFECT

     ============================================================ -->
<SectionTitle number="07" title="Post-Processing Effect" subtitle="Before and after conservative blob removal" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div>
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem; text-align: center;">Before Post-Processing</div>
  <div class="nv-placeholder" style="height: 140px;">
    <div class="nv-placeholder-label">Raw Model Output</div>
    <div class="nv-placeholder-desc">Raw prediction with small false-positive blobs scattered in background</div>
    <div class="nv-placeholder-hint">Show CT slice overlay — red false positives outside kidney</div>
  </div>
  <div style="margin-top: 0.4rem; font-size: 0.8rem; color: #8a8a8a; text-align: center;">Small noise blobs visible outside kidney</div>
</div>
<div>
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.4rem; text-align: center;">After Post-Processing</div>
  <div class="nv-placeholder" style="height: 140px;">
    <div class="nv-placeholder-label">Cleaned Mask</div>
    <div class="nv-placeholder-desc">After blob removal — noise eliminated, true detections preserved</div>
    <div class="nv-placeholder-hint">Same slice — cleaned overlay, green = kidney, orange = tumor</div>
  </div>
  <div style="margin-top: 0.4rem; font-size: 0.8rem; color: #8a8a8a; text-align: center;">Noise removed, true lesions preserved</div>
</div>
</div>
<div class="nv-three-col" style="margin-top: 0.8rem;">
<MetricCard label="Kidney Blobs Removed" value="&lt;5000" subvalue="voxels threshold" status="info" />
<MetricCard label="Tumor Blobs Removed" value="&lt;100" subvalue="voxels threshold" status="warning" />
<MetricCard label="Detection Preserved" value="100%" subvalue="64/64 cases" status="success" />
</div>
<!--
Notes:
Before/after visual comparison of post-processing. Shows that blob removal cleans up noise without losing true detections. The thresholds are conservative by design. 25 seconds.
-->

---

<!-- ============================================================

     SLIDE 27: CLASS IMBALANCE CHALLENGE

     ============================================================ -->
<SectionTitle number="08" title="Class Imbalance" subtitle="Why tumor segmentation is fundamentally difficult" />
<div class="nv-svg-wrapper">
  <img src="/images/class_imbalance.svg" />
</div>
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">The Problem</div>
  <div style="font-size: 0.88rem; color: #4a4a4a; line-height: 1.5;">
    Tumor voxels represent less than 0.1% of the volume. A model that predicts "all background" achieves 99% accuracy — and completely fails clinically.
  </div>
</div>
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.5rem;">Our Response</div>
  <div style="font-size: 0.88rem; color: #4a4a4a; line-height: 1.5;">
    — Dice loss (not cross-entropy) focuses on foreground overlap<br>
    — Conservative post-processing preserves small lesions<br>
    — 100% detection rate proves no tumor is missed
  </div>
</div>
</div>
<!--

Notes:

Class imbalance is the single biggest challenge in medical image segmentation. Standard accuracy is meaningless — a model predicting all background scores 99% but misses every tumor. We address this through Dice loss, conservative post-processing, and prioritizing detection over precision. The 100% detection rate validates this approach. 35 seconds.

-->

---

<!-- ============================================================

     SLIDE 28: KEY CHALLENGE — TUMOR/CYST

     ============================================================ -->
<SectionTitle number="08" title="Key Challenge: Tumor/Cyst Segmentation" subtitle="Why tumor Dice is lower than kidney Dice" />

<div class="nv-two-col" style="margin-top: 0.5rem;">
<div>
<div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.5rem;">Kidney: Favorable</div>
<div style="display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 1rem;">
<div class="nv-card" style="padding: 0.7rem 1rem;">
  <div style="font-size: 0.88rem; color: #4a4a4a;"><strong style="color: #1a1a1a">Large organ</strong> — tens of thousands of voxels</div>
</div>
<div class="nv-card" style="padding: 0.7rem 1rem;">
  <div style="font-size: 0.88rem; color: #4a4a4a;"><strong style="color: #1a1a1a">Consistent shape</strong> — bean-like, retroperitoneal</div>
</div>
<div class="nv-card" style="padding: 0.7rem 1rem;">
  <div style="font-size: 0.88rem; color: #4a4a4a;"><strong style="color: #1a1a1a">Clear boundary</strong> — fat interface on CT</div>
</div>
<div class="nv-card" style="padding: 0.7rem 1rem;">
  <div style="font-size: 0.88rem; color: #4a4a4a;"><strong style="color: #1a1a1a">Homogeneous</strong> — uniform parenchymal enhancement</div>
</div>
</div>
</div>
<div>
<div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31; margin-bottom: 0.5rem;">Tumor/Cyst: Challenging</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<ChallengeCard title="Small Lesion Size" problem="100-voxel tumor: 1-voxel error  ~30% Dice drop" mitigation="Conservative post-processing preserves detection" />
<ChallengeCard title="Boundary Ambiguity" problem="Infiltrative tumors blend into parenchyma" mitigation="TTA + overlap fusion reduce noise" />
<ChallengeCard title="Heterogeneous Appearance" problem="Solid, cystic, necrotic — one label, many shapes" mitigation="Documented as inherent limitation" />
</div>
</div>
</div>
<div class="nv-card nv-card-cyan" style="margin-top: 0.7rem; text-align: center;">
  <span class="nv-accent" style="font-weight: 700;">Detection  Segmentation:</span>
  <span style="color: #4a4a4a;"> 100% detection (64/64) means every tumor was </span><strong style="color: #1a1a1a">found</strong><span style="color: #4a4a4a;"> — not that every boundary is </span><strong style="color: #1a1a1a">perfect</strong>
</div>
<!--

Notes:

EMPHASIS SLIDE — 90 seconds. The most important honesty slide. Why is tumor Dice (0.6558) much lower than kidney Dice (0.9307)? Because the task is fundamentally harder. Kidney: large, consistent, clear boundary, homogeneous. Tumor: small, variable, ambiguous boundary, heterogeneous. For small objects, Dice is hypersensitive to boundary errors — a 1-voxel shift on a 100-voxel tumor drops Dice from 1.0 to ~0.70. Critical distinction: 100% detection rate means every tumor was FOUND. It does NOT mean boundaries are perfect. Detection is binary (is there a tumor?), segmentation is voxel-level (which exact voxels?). Documented in cyst_and_tumor_detection_challenges.md.

-->

---

<!-- ============================================================

     SLIDE 29: WEB APPLICATION

     ============================================================ -->
<SectionTitle number="08" title="Web Application" subtitle="Browser-based 3D visualization — no specialized software" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem;">
  <div style="min-width: 32px; height: 32px; border-radius: 50%; background: #f0f4f8; border: 1px solid #1e3a5f; color: #1e3a5f; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700;">1</div>
  <div>
    <div style="font-weight: 700; color: #1a1a1a">Upload</div>
    <div style="font-size: 0.8rem; color: #8a8a8a;">NIfTI CT volume via web interface</div>
  </div>
</div>
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem;">
  <div style="min-width: 32px; height: 32px; border-radius: 50%; background: #f0f4f8; border: 1px solid #1e3a5f; color: #1e3a5f; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700;">2</div>
  <div>
    <div style="font-weight: 700; color: #1a1a1a">Process</div>
    <div style="font-size: 0.8rem; color: #8a8a8a;">Server-side inference + post-processing</div>
  </div>
</div>
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem;">
  <div style="min-width: 32px; height: 32px; border-radius: 50%; background: #f0f4f8; border: 1px solid #1e3a5f; color: #1e3a5f; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700;">3</div>
  <div>
    <div style="font-weight: 700; color: #1a1a1a">Visualize</div>
    <div style="font-size: 0.8rem; color: #8a8a8a;">Interactive 3D mesh with rotate / zoom / pan</div>
  </div>
</div>
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem;">
  <div style="min-width: 32px; height: 32px; border-radius: 50%; background: #f0f4f8; border: 1px solid #1e3a5f; color: #1e3a5f; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700;">4</div>
  <div>
    <div style="font-weight: 700; color: #1a1a1a">Review</div>
    <div style="font-size: 0.8rem; color: #8a8a8a;">Volumetric statistics + class toggle</div>
  </div>
</div>
</div>
</div>
<div>
<div class="nv-placeholder" style="height: 160px;">
  <div class="nv-placeholder-label">Web App Screenshot</div>
  <div class="nv-placeholder-desc">Browser interface showing 3D viewer + stats panel</div>
  <div class="nv-placeholder-hint">Replace with actual screenshot before defense</div>
</div>
<div style="margin-top: 0.6rem; display: flex; flex-direction: column; gap: 0.4rem;">
  <SafetyBadge label="Academic Prototype Disclaimer" status="warning" />
  <SafetyBadge label="Physician Review Required" status="warning" />
</div>
</div>
</div>
<!--

Notes:

The web interface makes segmentation accessible without specialized software like 3D Slicer. Users upload a NIfTI file, the system processes it server-side, and displays an interactive 3D mesh. Features: rotate, zoom, pan, class toggle, volumetric statistics. Safety UX: disclaimer and physician review messages are prominently displayed. Replace the placeholder with an actual screenshot before defense. 40 seconds.

-->

---

<!-- ============================================================

   SLIDE 30: VALIDATION SETUP

   ============================================================ -->
<SectionTitle number="09" title="Validation Setup" subtitle="Independent held-out test — analytical validation only" />
<div class="nv-three-col" style="margin-top: 0.8rem;">
<MetricCard label="Test Cases" value="64" subvalue="Independent held-out" status="info" />
<MetricCard label="Metrics" value="3" subvalue="Dice  HD95  Detection" status="info" />
<MetricCard label="Clinical Trial" value="None" subvalue="Analytical only" status="warning" />
</div>
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Test Set Properties</div>
  <div style="font-size: 0.88rem; color: #4a4a4a; line-height: 1.6;">
  — Selected <strong style="color: #1a1a1a">before</strong> model development<br>

  — <strong style="color: #1a1a1a">Never used</strong> in training or validation<br>

  — Identical preprocessing to training<br>

  — Full-volume inference (not patches)
  </div>
</div>
<div class="nv-card nv-card-orange">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31; margin-bottom: 0.5rem;">Validation Scope</div>
  <div style="font-size: 0.88rem; color: #4a4a4a; line-height: 1.6;">
  — <strong style="color: #1a1a1a">Analytical validation</strong> on dataset cases<br>

  — <strong style="color: #1a1a1a">NOT</strong> clinical validation<br>

  — No prospective trial conducted<br>

  — No external dataset tested
  </div>
</div>
</div>
<!--

Notes:

The 64-case test set was selected before any model development and never used during training — unbiased evaluation. Three metrics: Dice (overlap), HD95 (boundary), detection rate (presence). Scope is analytical validation only — testing under controlled conditions on dataset cases. NOT clinical validation. No prospective trial, no external data, no human comparison. All metrics refer to this project-defined subset, not the official KiTS23 leaderboard. 40 seconds.

-->

---

<!-- ============================================================

   SLIDE 31: RESULTS

   ============================================================ -->
<SectionTitle number="09" title="Results" subtitle="Final test set performance — 64 independent held-out cases" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div style="display: flex; flex-direction: column; gap: 0.6rem;">
<MetricCard label="Kidney Dice" value="0.9307" subvalue="± 0.064" status="success" />
<MetricCard label="Tumor Dice" value="0.6558" subvalue="± 0.262" status="warning" />
<MetricCard label="Mean Dice" value="0.7933" subvalue="" status="info" />
</div>
<div style="display: flex; flex-direction: column; gap: 0.6rem;">
<MetricCard label="HD95 Kidney" value="19.98" subvalue="mm" status="success" />
<MetricCard label="HD95 Tumor" value="67.35" subvalue="mm" status="warning" />
<div class="nv-card nv-card-green" style="text-align: center; padding: 1rem;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.3rem;">Tumor Detection Rate</div>
  <div style="font-family: 'SF Mono', 'JetBrains Mono', Consolas, monospace; font-size: 2.4rem; font-weight: 800; color: #1a1a1a">100%</div>
  <div style="font-size: 0.85rem; color: #8a8a8a; margin-top: 0.2rem;">64 / 64 cases detected</div>
</div>
</div>
</div>
<div style="margin-top: 0.8rem; padding: 1rem; background: #fafbfc; border-radius: 6px;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #8a8a8a; margin-bottom: 0.8rem; text-align: center;">Test Set Performance (n=64)</div>
  <div style="display: flex; align-items: flex-end; justify-content: center; gap: 2rem; height: 110px; padding: 0 1rem;">
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.75rem; color: #2d6a4f; font-weight: 700;">0.931</div>
      <div style="width: 50px; height: 93px; background: linear-gradient(180deg, #2d6a4f, #3d8a6f); border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.7rem; color: #8a8a8a;">Kidney Dice</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.75rem; color: #bc4b31; font-weight: 700;">0.656</div>
      <div style="width: 50px; height: 66px; background: linear-gradient(180deg, #bc4b31, #d46044); border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.7rem; color: #8a8a8a;">Tumor Dice</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.75rem; color: #1e3a5f; font-weight: 700;">0.793</div>
      <div style="width: 50px; height: 79px; background: linear-gradient(180deg, #1e3a5f, #2a4a73); border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.7rem; color: #8a8a8a;">Mean Dice</div>
    </div>
  </div>
  <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 0.5rem;">
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.75rem; color: #2d6a4f; font-weight: 700;">20.0 mm</div>
      <div style="width: 50px; height: 20px; background: linear-gradient(180deg, #2d6a4f, #3d8a6f); border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.7rem; color: #8a8a8a;">HD95 Kidney</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.75rem; color: #bc4b31; font-weight: 700;">67.4 mm</div>
      <div style="width: 50px; height: 67px; background: linear-gradient(180deg, #bc4b31, #d46044); border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.7rem; color: #8a8a8a;">HD95 Tumor</div>
    </div>
  </div>
</div>
<div class="nv-card" style="margin-top: 0.8rem; text-align: center;">
  <span style="color: #4a4a4a;"><strong style="color: #2d6a4f;">Robust kidney</strong> · <strong style="color: #2d6a4f;">Reliable detection</strong> · <strong style="color: #bc4b31;">Moderate tumor boundaries</strong></span>
</div>
<!--

Notes:

THE MONEY SLIDE — 60 seconds. Walk through the numbers. Kidney Dice 0.9307 ± 0.064: robust, consistent across cases. Tumor Dice 0.6558 ± 0.262: moderate, with high variability. HD95 Kidney 19.98 mm: reasonably precise boundaries. HD95 Tumor 67.35 mm: substantial boundary uncertainty. Mean Dice 0.7933. HEADLINE: 100% tumor detection rate — every single tumor in the 64 test cases was detected. Color coding tells the story: green for strong, orange for moderate. Frame: strong kidney, reliable detection, moderate tumor boundaries. These are analytical validation results on a project-defined subset.

-->

---

<!-- ============================================================

     SLIDE 32: METRIC DISTRIBUTION

     ============================================================ -->
<SectionTitle number="09" title="Metric Distribution" subtitle="Per-case variability across the 64 test cases" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div>
  <div class="nv-placeholder" style="height: 160px;">
    <div class="nv-placeholder-label">Dice Score Box Plot</div>
    <div class="nv-placeholder-desc">Box plot per case: Kidney Dice (tight, high) vs Tumor Dice (wide, lower)</div>
    <div class="nv-placeholder-hint">Generate with matplotlib — show median, quartiles, outliers</div>
  </div>
  <div style="margin-top: 0.5rem; font-size: 0.8rem; color: #8a8a8a; text-align: center;">Kidney Dice: tight distribution (σ=0.064) · Tumor Dice: wide (σ=0.262)</div>
</div>
<div>
  <div class="nv-placeholder" style="height: 160px;">
    <div class="nv-placeholder-label">HD95 Box Plot</div>
    <div class="nv-placeholder-desc">Box plot per case: HD95 Kidney (low) vs HD95 Tumor (high, variable)</div>
    <div class="nv-placeholder-hint">Generate with matplotlib — log scale may help</div>
  </div>
  <div style="margin-top: 0.5rem; font-size: 0.8rem; color: #8a8a8a; text-align: center;">HD95 Tumor: highly variable (up to ~150 mm in worst case)</div>
</div>
</div>
<div class="nv-card nv-card-cyan" style="margin-top: 0.8rem;">
  <div style="font-size: 0.85rem; color: #4a4a4a; text-align: center;"><strong style="color: #1a1a1a;">Key insight:</strong> Kidney segmentation is <strong style="color: #2d6a4f;">consistent</strong> across cases. Tumor segmentation is <strong style="color: #bc4b31;">variable</strong> — some cases excellent, some poor.</div>
</div>
<!--
Notes:
Box plots showing per-case metric distributions. The visual contrast between tight kidney distribution and wide tumor distribution tells the story better than numbers alone. Mention the outliers — some tumor cases had very poor Dice. 30 seconds.
-->

---

<!-- ============================================================

     SLIDE 33: DETECTION PERFORMANCE

     ============================================================ -->
<SectionTitle number="09" title="Detection Performance" subtitle="Binary detection vs voxel-level segmentation" />
<div class="nv-two-col" style="margin-top: 0.8rem; align-items: center;">
<div style="display: flex; flex-direction: column; gap: 0.6rem;">
<div class="nv-card nv-card-green" style="text-align: center; padding: 1.2rem;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.3rem;">Tumor Detection Rate</div>
  <div style="font-family: 'SF Mono', monospace; font-size: 3rem; font-weight: 800; color: #1a1a1a;">100%</div>
  <div style="font-size: 0.9rem; color: #8a8a8a; margin-top: 0.2rem;">64 / 64 cases</div>
</div>
<div class="nv-card" style="text-align: center; padding: 1rem;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.3rem;">False Negative Rate</div>
  <div style="font-family: 'SF Mono', monospace; font-size: 2rem; font-weight: 800; color: #1a1a1a;">0%</div>
  <div style="font-size: 0.8rem; color: #8a8a8a; margin-top: 0.2rem;">No tumors missed</div>
</div>
</div>

</div>
<!--
Notes:
Visual distinction between detection and segmentation. Detection grid: 64 green squares. Big numbers: 100% detection, 0% false negative. Then explain the difference: detection is binary (found/not found), segmentation is voxel-level (exact boundaries). This is the most important conceptual distinction in the results. 30 seconds.
-->

---

<!-- ============================================================

     SLIDE 34: KIDNEY-TUMOR CORRELATION

     ============================================================ -->
<SectionTitle number="09" title="Kidney-Tumor Correlation" subtitle="Is good kidney segmentation predictive of good tumor segmentation?" />
<div style="margin-top: 0.8rem;">
  <div class="nv-placeholder" style="height: 200px;">
    <div class="nv-placeholder-label">Scatter Plot: Kidney Dice vs Tumor Dice</div>
    <div class="nv-placeholder-desc">Each point = one test case. X-axis: Kidney Dice. Y-axis: Tumor Dice. Color by tumor size.</div>
    <div class="nv-placeholder-hint">Generate with matplotlib — add regression line, R² value, colorbar for tumor volume</div>
  </div>
</div>
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem;">Observation</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">Weak correlation (R² ≈ 0.2 [PLACEHOLDER]). Good kidney segmentation does <strong style="color: #1a1a1a;">not</strong> guarantee good tumor segmentation.</div>
</div>
<div class="nv-card nv-card-orange">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31; margin-bottom: 0.4rem;">Interpretation</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">Kidney and tumor are <strong style="color: #1a1a1a;">different tasks</strong> with different difficulty profiles. Tumor size is a stronger predictor of Dice than kidney quality.</div>
</div>
</div>
<!--
Notes:
Scatter plot showing kidney vs tumor Dice per case. Weak correlation is the key finding — good kidney does not predict good tumor. Tumor size (color-coded) is a better predictor. This supports the argument that tumor segmentation is a fundamentally harder problem. 25 seconds.
-->

---

<!-- ============================================================

   SLIDE 35: TARGET VS ACHIEVED

   ============================================================ -->
<SectionTitle number="09" title="Target vs. Achieved" subtitle="All six acceptance criteria met" />
<div style="margin-top: 0.8rem;">
<table>
<thead>
<tr>
<th>Criterion</th>
<th>Target</th>
<th>Achieved</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong style="color: #1a1a1a">Kidney Dice</strong></td>
<td> 0.85</td>
<td>0.9307 ± 0.064</td>
<td><SafetyBadge label="PASS" status="success" /></td>
</tr>
<tr>
<td><strong style="color: #1a1a1a">Tumor Dice</strong></td>
<td> 0.50</td>
<td>0.6558 ± 0.262</td>
<td><SafetyBadge label="PASS" status="success" /></td>
</tr>
<tr>
<td><strong style="color: #1a1a1a">Mean Dice</strong></td>
<td> 0.65</td>
<td>0.7933</td>
<td><SafetyBadge label="PASS" status="success" /></td>
</tr>
<tr>
<td><strong style="color: #1a1a1a">HD95 Kidney</strong></td>
<td>&lt; 30 mm</td>
<td>19.98 mm</td>
<td><SafetyBadge label="PASS" status="success" /></td>
</tr>
<tr>
<td><strong style="color: #1a1a1a">HD95 Tumor</strong></td>
<td>&lt; 100 mm</td>
<td>67.35 mm</td>
<td><SafetyBadge label="PASS" status="success" /></td>
</tr>
<tr>
<td><strong style="color: #1a1a1a">Tumor Detection</strong></td>
<td> 90%</td>
<td>100%</td>
<td><SafetyBadge label="PASS" status="success" /></td>
</tr>
</tbody>
</table>
</div>
<div style="margin-top: 0.6rem; text-align: center; font-size: 0.8rem; color: #8a8a8a;">
  Meeting project criteria — clinical readiness. Targets defined for academic scope, not regulatory approval.
</div>
<!--

Notes:

All six acceptance criteria met with PASS status. Walk through quickly: kidney Dice exceeded target by wide margin, tumor Dice exceeded 0.50, mean Dice exceeded 0.65, both HD95 below thresholds, detection rate exceeded 90%. Important caveat: meeting project acceptance criteria does not mean the system is clinically ready. These targets were defined for a graduation project, not for FDA clearance. They prove the system works within its scope — not that it is ready for clinical deployment. 45 seconds.

-->

---

<!-- ============================================================

     SLIDE 36: BENCHMARK COMPARISON

     ============================================================ -->
<SectionTitle number="09" title="Benchmark Comparison" subtitle="Where NephroVision stands against alternatives" />
<div style="margin-top: 0.8rem; padding: 1rem; background: #fafbfc; border-radius: 6px;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #8a8a8a; margin-bottom: 0.8rem; text-align: center;">Approximate Literature Comparison — Kidney Dice</div>
  <div style="display: flex; align-items: flex-end; justify-content: center; gap: 1.5rem; height: 100px; padding: 0 1rem;">
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.7rem; color: #8a8a8a; font-weight: 600;">~0.82</div>
      <div style="width: 40px; height: 55px; background: #d0d0d0; border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.65rem; color: #8a8a8a;">2D U-Net</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.7rem; color: #1e3a5f; font-weight: 700;">0.93</div>
      <div style="width: 40px; height: 75px; background: linear-gradient(180deg, #1e3a5f, #2a4a73); border-radius: 3px 3px 0 0; border: 2px solid #1a1a1a;"></div>
      <div style="font-size: 0.65rem; color: #1e3a5f; font-weight: 600;">NephroVision</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.7rem; color: #8a8a8a; font-weight: 600;">~0.93</div>
      <div style="width: 40px; height: 75px; background: #d0d0d0; border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.65rem; color: #8a8a8a;">nnU-Net</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0.3rem;">
      <div style="font-size: 0.7rem; color: #8a8a8a; font-weight: 600;">~0.95</div>
      <div style="width: 40px; height: 85px; background: #d0d0d0; border-radius: 3px 3px 0 0;"></div>
      <div style="font-size: 0.65rem; color: #8a8a8a;">KiTS23 Top</div>
    </div>
  </div>
  <div style="font-size: 0.72rem; color: #8a8a8a; text-align: center; margin-top: 0.5rem;">Tumor Dice: NephroVision 0.66 · nnU-Net ~0.75 · KiTS23 Top ~0.80</div>
</div>
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Our Position</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.6;">
    — <strong style="color: #1a1a1a;">Kidney Dice 0.93</strong>: competitive with nnU-Net<br>
    — <strong style="color: #1a1a1a;">Tumor Dice 0.66</strong>: below nnU-Net (~0.75)<br>
    — <strong style="color: #1a1a1a;">Gap explained</strong>: no ensemble, no auto-config<br>
    — <strong style="color: #1a1a1a;">Strength</strong>: full documentation, not black-box
  </div>
</div>
<div class="nv-card nv-card-orange">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31; margin-bottom: 0.5rem;">Caveat</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.6;">
    Comparisons are <strong style="color: #1a1a1a;">approximate</strong> — different test sets, different years. nnU-Net numbers from literature, not head-to-head on our 64-case subset. Purpose is context, not ranking.
  </div>
</div>
</div>
<!--
Notes:
Bar chart comparing NephroVision to alternatives. Key message: kidney segmentation is competitive, tumor segmentation has headroom. The gap is expected — we used a single manually-configured 3D U-Net, not an ensemble or self-configuring framework. Emphasize that documentation and transparency are strengths that benchmarks don't capture. 30 seconds.
-->

---

<!-- ============================================================

   SLIDE 37: FAILURE ANALYSIS & LIMITATIONS

   ============================================================ -->
<SectionTitle number="10" title="Failure Analysis & Limitations" subtitle="What fails, why, and what we did about it" />

<div class="nv-two-col" style="margin-top: 0.5rem;">
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<ChallengeCard title="Boundary Leakage" problem="Tumor mask extends into healthy parenchyma" mitigation="TTA + overlap fusion reduce but do not eliminate" remaining="HD95: 67.35 mm confirms boundary uncertainty" />
<ChallengeCard title="Small Lesion Sensitivity" problem="Dice drops sharply with minor boundary errors" mitigation="Conservative 100-voxel threshold preserves detection" remaining="Size-stratified analysis is future work" />
<ChallengeCard title="Cyst/Tumor Confusion" problem="Merged class prevents malignancy assessment" mitigation="Documented as known limitation" remaining="Separate classification stage is future work" />
</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<div class="nv-card nv-card-red">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #9b2c2c; margin-bottom: 0.5rem;">Critical Limitation</div>
  <div style="font-size: 0.9rem; color: #1a1a1a; font-weight: 700; margin-bottom: 0.3rem;">Domain Shift</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">
  Performance evaluated <strong style="color: #1a1a1a">only</strong> on KiTS23 data. Performance on different scanners, protocols, or populations is <strong style="color: #1a1a1a">unknown</strong>. External multi-center validation is the highest-priority future work.
  </div>
</div>
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Mitigations Implemented</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">
  — Conservative post-processing preserves detection<br>

  — TTA reduces boundary noise<br>

  — Explicit limitations in all outputs<br>

  — <strong style="color: #1a1a1a">Physician review is the final safety net</strong>
  </div>
</div>
</div>
</div>
<!--

Notes:

EMPHASIS SLIDE — 75 seconds. Directly addresses mid-year feedback about documenting failures. Be direct: boundary leakage (HD95 67.35 mm), small lesion sensitivity (Dice hypersensitivity), cyst/tumor confusion (merged class). Domain shift is the most critical limitation — RED card. We only tested on KiTS23. Performance on other data is unknown. This is not hidden — it is documented in failure_cases_analysis.md. Mitigations: conservative post-processing, TTA, explicit limitations, physician review. The committee will respect honesty about failures more than vague perfection claims.

-->

---

<!-- ============================================================

     SLIDE 38: FAILURE CASE GALLERY

     ============================================================ -->
<SectionTitle number="10" title="Failure Case Gallery" subtitle="Three representative failures from the test set" />
<div class="nv-three-col" style="margin-top: 0.8rem;">
<div class="nv-card" style="padding: 0.8rem;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #bc4b31; margin-bottom: 0.4rem;">FC-001: Boundary Leakage</div>
  <div class="nv-placeholder" style="height: 100px;">
    <div class="nv-placeholder-label">Case 0042</div>
    <div class="nv-placeholder-desc">Infiltrative tumor — predicted mask extends 18 voxels beyond true boundary</div>
  </div>
  <div style="margin-top: 0.4rem; font-size: 0.78rem; color: #8a8a8a;">Tumor Dice: 0.52 · HD95: 78 mm</div>
</div>
<div class="nv-card" style="padding: 0.8rem;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #bc4b31; margin-bottom: 0.4rem;">FC-002: Small Lesion</div>
  <div class="nv-placeholder" style="height: 100px;">
    <div class="nv-placeholder-label">Case 0017</div>
    <div class="nv-placeholder-desc">120-voxel hypodense lesion — under-segmented to 45% of true volume</div>
  </div>
  <div style="margin-top: 0.4rem; font-size: 0.78rem; color: #8a8a8a;">Tumor Dice: 0.38 · HD95: 85 mm</div>
</div>
<div class="nv-card" style="padding: 0.8rem;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #bc4b31; margin-bottom: 0.4rem;">FC-003: Cyst Confusion</div>
  <div class="nv-placeholder" style="height: 100px;">
    <div class="nv-placeholder-label">Case 0058</div>
    <div class="nv-placeholder-desc">Large simple cyst — correctly segmented but labeled as Tumor/Cyst</div>
  </div>
  <div style="margin-top: 0.4rem; font-size: 0.78rem; color: #8a8a8a;">Tumor Dice: 0.82 · Cannot distinguish benign</div>
</div>
</div>
<div class="nv-card nv-card-cyan" style="margin-top: 0.8rem; text-align: center;">
  <div style="font-size: 0.85rem; color: #4a4a4a;">All failures documented in <strong style="color: #1a1a1a;">failure_cases_analysis.md</strong> — not hidden, not minimized.</div>
</div>
<!--
Notes:
Three concrete failure cases shown as visual cards. Each has a placeholder for the actual comparison figure. The committee sees that we don't just talk about failures — we catalog them with case IDs, metrics, and visual evidence. 40 seconds.
-->

---

<!-- ============================================================

     SLIDE 39: DOMAIN SHIFT RISK

     ============================================================ -->
<SectionTitle number="10" title="Domain Shift Risk" subtitle="The highest-priority limitation" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div>
  <div class="nv-placeholder" style="height: 160px;">
    <div class="nv-placeholder-label">Scanner Variability Concept</div>
    <div class="nv-placeholder-desc">Diagram showing same anatomy scanned by 3 different scanners with different contrast, noise, resolution</div>
    <div class="nv-placeholder-hint">Use simplified icons — CT scanner A/B/C with different kernel symbols</div>
  </div>
  <div style="margin-top: 0.6rem; font-size: 0.82rem; color: #4a4a4a; line-height: 1.5;">
    Model trained on <strong style="color: #1a1a1a;">KiTS23 only</strong>. Performance on Siemens, GE, Philips, or different protocols is <strong style="color: #1a1a1a;">unknown</strong>.
  </div>
</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<div class="nv-card nv-card-red">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #9b2c2c; margin-bottom: 0.4rem;">Critical</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">No external validation. No multi-center testing. No prospective trial.</div>
</div>
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem;">Mitigation</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">Explicit limitation statement in all outputs. Decision-support framing ensures physician review catches discrepancies.</div>
</div>
<div class="nv-card nv-card-green">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.4rem;">Future Work</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">External multi-center validation is the single highest-priority next step.</div>
</div>
</div>
</div>
<!--
Notes:
Domain shift is the most critical limitation. Visual concept diagram shows scanner variability. Three cards: critical (red), mitigation, future work (green). Emphasize that without external validation, the system is scoped to KiTS23 only. 35 seconds.
-->

---

<!-- ============================================================

   SLIDE 40: SAFETY & IEC 62304

   ============================================================ -->
<SectionTitle number="10" title="Safety & IEC 62304" subtitle="Academic decision-support prototype — Class B" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div>
<div class="nv-card" style="margin-bottom: 0.7rem;">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.5rem;">Classification</div>
  <div style="display: flex; flex-direction: column; gap: 0.4rem;">
  <div style="font-size: 0.88rem; color: #4a4a4a;"><strong style="color: #1a1a1a">IEC 62304:</strong> Software Safety Class B</div>
  <div style="font-size: 0.88rem; color: #4a4a4a;"><strong style="color: #1a1a1a">Device Type:</strong> SaMD academic prototype</div>
  <div style="font-size: 0.88rem; color: #4a4a4a;"><strong style="color: #1a1a1a">Intended Use:</strong> Segmentation support</div>
  </div>
</div>
<div style="display: flex; flex-direction: column; gap: 0.4rem;">
  <SafetyBadge label="Not Clinically Approved" status="danger" />
  <SafetyBadge label="Not FDA Approved" status="danger" />
  <SafetyBadge label="No Regulatory Submission" status="danger" />
</div>
</div>
<div>
<div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.5rem;">Why Class B Is Appropriate</div>
<div style="display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 0.8rem;">
<div class="nv-card" style="padding: 0.7rem 1rem;">
  <div style="font-size: 0.88rem; color: #4a4a4a;"><strong style="color: #1a1a1a">Decision-support</strong> — not autonomous diagnosis</div>
</div>
<div class="nv-card" style="padding: 0.7rem 1rem;">
  <div style="font-size: 0.88rem; color: #4a4a4a;"><strong style="color: #1a1a1a">Physician oversight</strong> — all outputs reviewed</div>
</div>
<div class="nv-card" style="padding: 0.7rem 1rem;">
  <div style="font-size: 0.88rem; color: #4a4a4a;"><strong style="color: #1a1a1a">Non-autonomous</strong> — system delineates, physician decides</div>
</div>
<div class="nv-card" style="padding: 0.7rem 1rem;">
  <div style="font-size: 0.88rem; color: #4a4a4a;">Harm from errors is <strong style="color: #1a1a1a">non-serious</strong> when caught in review</div>
</div>
</div>
<div style="font-size: 0.78rem; color: #8a8a8a;">
  Compliance with IEC 62304 principles — regulatory clearance
</div>
</div>
</div>
<div class="nv-svg-wrapper">
  <img src="/images/safety_positioning.svg" />
</div>
<!--

Notes:

NephroVision is IEC 62304 Class B. Why? Decision-support, not autonomous. Physician oversight is built in. The system delineates; the physician decides. Most probable harm is non-serious when caught during review. Class C would apply only to autonomous diagnostic systems — this is not one. Critical: NOT clinically approved, NOT FDA approved, NO regulatory submission made. Following IEC 62304 principles in documentation is not the same as clearance. The system is an academic prototype, full stop. 60 seconds.

-->

---

<!-- ============================================================

   SLIDE 41: FUTURE WORK

   ============================================================ -->
<SectionTitle number="10" title="Future Work" subtitle="Prioritized directions for improvement" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div>
<div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.5rem;">High Priority</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<PipelineStep number="1" title="Improve Tumor Boundary Accuracy" description="Boundary-aware loss functions (Boundary loss, Hausdorff loss)" />
<PipelineStep number="2" title="External Multi-Center Validation" description="Assess domain shift & generalizability on diverse data" />
<PipelineStep number="3" title="Evaluate nnU-Net" description="Compare against self-configuring framework baseline" />
</div>
</div>
<div>
<div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31; margin-bottom: 0.5rem;">Medium / Lower Priority</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<PipelineStep number="4" title="Prospective Clinical Evaluation" description="Assess impact on radiologist workflow & consistency" />
<PipelineStep number="5" title="Uncertainty Estimation" description="MC dropout / ensembles for confidence maps" />
<PipelineStep number="6" title="Regulatory Documentation" description="ISO 14971 risk file, cybersecurity, usability testing" />
</div>
</div>
</div>
<div class="nv-card" style="margin-top: 0.8rem; text-align: center;">
  <span style="color: #8a8a8a;">None of the above is implemented — all are </span><strong style="color: #1a1a1a">planned future work</strong><span style="color: #8a8a8a;">, not completed features</span>
</div>
<!--

Notes:

Prioritized future directions. High priority: improve tumor boundaries (boundary-aware losses), external validation (most important — without it we cannot claim generalizability), evaluate nnU-Net. Medium: prospective clinical evaluation, uncertainty estimation, regulatory documentation. Be explicit: NONE of this is implemented yet. These are planned directions. External validation is the single highest priority because without it, the system is scoped to KiTS23 only. 40 seconds.

-->

---

<!-- ============================================================

     SLIDE 42: EXPERIMENT LOG

     ============================================================ -->
<SectionTitle number="11" title="Experiment Log" subtitle="Documented iterative development — hypothesis to decision" />
<div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.5rem;">
<PipelineStep number="1" title="EXP-001: Baseline 3D U-Net" description="Establish initial performance on KiTS23" />
<PipelineStep number="2" title="EXP-002: Preprocessing Refinement" description="HU clipping range [-200, 300] selected empirically" />
<PipelineStep number="3" title="EXP-003: Sliding Window Inference" description="Patch-based processing for GPU memory efficiency" />
<PipelineStep number="4" title="EXP-004: Test-Time Augmentation" description="8-flip TTA reduces boundary noise" />
<PipelineStep number="5" title="EXP-005: Post-Processing Calibration" description="Blob removal thresholds: kidney <5000, tumor <100" />
<PipelineStep number="6" title="EXP-006: Tumor/Cyst Analysis" description="Detection vs segmentation performance evaluation" />
</div>
<div style="margin-top: 0.8rem; font-size: 0.8rem; color: #8a8a8a;">
  Each experiment: hypothesis → setup → result → decision (adopt / modify / discard). Full details in <strong style="color: #4a4a4a;">07_development_documentation/experiment_log.md</strong>
</div>
<!--

Notes:

Six major experimental phases, each documented with hypothesis, setup, result, and decision. Not every experiment succeeded — failures are recorded too. The experiment log is not a retrospective summary; it was maintained during development. Committee can inspect the full record. 35 seconds.

-->

---

<!-- ============================================================

     SLIDE 43: REPRODUCIBILITY

     ============================================================ -->
<SectionTitle number="11" title="Reproducibility" subtitle="Another engineer should be able to replicate our results" />
<div class="nv-svg-wrapper">
  <img src="/images/reproducibility_checklist.svg" />
</div>
<!--

Notes:

Reproducibility is a core scientific requirement. We provide code, experiment logs, trained weights, configuration files, environment specifications, dataset documentation, preprocessing specifications, inference pipeline details, and failure analysis. This is not just good practice — it is what the committee expects from a rigorous engineering project. 25 seconds.

-->

---

<!-- ============================================================

     SLIDE 44: REPRODUCIBILITY ARTIFACTS

     ============================================================ -->
<SectionTitle number="11" title="Reproducibility Artifacts" subtitle="Everything needed to replicate our work" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.7rem 1rem;">
  <div style="min-width: 28px; height: 28px; border-radius: 50%; background: #2d6a4f; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700;">1</div>
  <div style="font-size: 0.85rem; color: #4a4a4a;"><strong style="color: #1a1a1a;">Source Code</strong> — train.py, inference.py, evaluate.py</div>
</div>
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.7rem 1rem;">
  <div style="min-width: 28px; height: 28px; border-radius: 50%; background: #2d6a4f; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700;">2</div>
  <div style="font-size: 0.85rem; color: #4a4a4a;"><strong style="color: #1a1a1a;">Trained Weights</strong> — best_val_dice.pth (~35 MB)</div>
</div>
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.7rem 1rem;">
  <div style="min-width: 28px; height: 28px; border-radius: 50%; background: #2d6a4f; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700;">3</div>
  <div style="font-size: 0.85rem; color: #4a4a4a;"><strong style="color: #1a1a1a;">Environment</strong> — requirements.txt + Docker image</div>
</div>
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.7rem 1rem;">
  <div style="min-width: 28px; height: 28px; border-radius: 50%; background: #2d6a4f; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700;">4</div>
  <div style="font-size: 0.85rem; color: #4a4a4a;"><strong style="color: #1a1a1a;">Dataset Splits</strong> — train/val/test case IDs</div>
</div>
</div>
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.7rem 1rem;">
  <div style="min-width: 28px; height: 28px; border-radius: 50%; background: #2d6a4f; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700;">5</div>
  <div style="font-size: 0.85rem; color: #4a4a4a;"><strong style="color: #1a1a1a;">Experiment Log</strong> — 6 experiments, hypothesis to decision</div>
</div>
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.7rem 1rem;">
  <div style="min-width: 28px; height: 28px; border-radius: 50%; background: #2d6a4f; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700;">6</div>
  <div style="font-size: 0.85rem; color: #4a4a4a;"><strong style="color: #1a1a1a;">Random Seeds</strong> — 42 (PyTorch, NumPy, Python)</div>
</div>
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.7rem 1rem;">
  <div style="min-width: 28px; height: 28px; border-radius: 50%; background: #2d6a4f; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700;">7</div>
  <div style="font-size: 0.85rem; color: #4a4a4a;"><strong style="color: #1a1a1a;">Preprocessing Spec</strong> — exact HU range + normalization</div>
</div>
<div class="nv-card" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.7rem 1rem;">
  <div style="min-width: 28px; height: 28px; border-radius: 50%; background: #2d6a4f; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700;">8</div>
  <div style="font-size: 0.85rem; color: #4a4a4a;"><strong style="color: #1a1a1a;">Failure Analysis</strong> — 7 categories + 3 concrete cases</div>
</div>
</div>
</div>

<!--
Notes:
Eight reproducibility artifacts listed as numbered cards. Emphasize that reproducibility is not an afterthought — it was built into the process. 20 seconds.
-->

---

<!-- ============================================================

     SLIDE 45: ETHICAL CONSIDERATIONS

     ============================================================ -->
<SectionTitle number="11" title="Ethical Considerations" subtitle="Patient data, bias, and clinical deployment ethics" />
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div style="display: flex; flex-direction: column; gap: 0.6rem;">
<div class="nv-card nv-card-green">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.4rem;">Patient Data</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">KiTS23 is a <strong style="color: #1a1a1a">public de-identified dataset</strong>. No protected health information is used. All cases were collected with institutional review board approval.</div>
</div>
<div class="nv-card nv-card-green">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.4rem;">Bias Awareness</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">Model trained on <strong style="color: #1a1a1a">single-source data</strong> (KiTS23). Performance on different populations, scanners, or protocols is unknown. External validation required.</div>
</div>
</div>
<div style="display: flex; flex-direction: column; gap: 0.6rem;">
<div class="nv-card nv-card-orange">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31; margin-bottom: 0.4rem;">Clinical Deployment</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;"><strong style="color: #1a1a1a">Not approved</strong> for clinical use. No regulatory submission. No prospective trial. Decision-support only with mandatory physician review.</div>
</div>
<div class="nv-card nv-card-orange">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31; margin-bottom: 0.4rem;">Transparency</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">All limitations documented. No overclaiming. System scope clearly defined. Users informed that outputs require expert interpretation.</div>
</div>
</div>
</div>
<!--

Notes:

Medical AI must address ethics. We use de-identified public data, acknowledge dataset bias, and explicitly state the system is not clinically approved. Transparency is not a weakness — it is the foundation of trustworthy engineering. Committee members from medical backgrounds will appreciate this honesty. 35 seconds.

-->

---

<!-- ============================================================

   SLIDE 46: FINAL TAKEAWAY

   ============================================================ -->
<div class="nv-center" style="position: relative; z-index: 1;">
<SectionTitle title="Final Takeaway" subtitle="" />
<div style="margin-top: 1rem;">
<div class="nv-three-col">
<MetricCard label="Kidney Dice" value="0.9307" subvalue="± 0.064" status="success" />
<MetricCard label="Tumor Detection" value="100%" subvalue="64/64" status="success" />
<MetricCard label="Tumor Dice" value="0.6558" subvalue="± 0.262" status="warning" />
</div>
</div>
<div class="nv-divider" style="width: 60%; margin: 1.5rem auto;"></div>
<div style="text-align: center; max-width: 560px;">
<div style="font-size: 1.3rem; font-weight: 700; color: #1e3a5f; margin-bottom: 0.5rem;">
  Decision-support, not diagnosis.
</div>
<div style="font-size: 1rem; color: #4a4a4a; line-height: 1.5;">
  All outputs require physician review.<br>

  Academic prototype — not clinically approved.<br>

  External validation required before clinical use.
</div>
</div>
<div style="margin-top: 2rem;">
  <SafetyBadge label="Thank You  Questions?" status="info" />
</div>
</div>
<!--

Notes:

End strong. Three numbers: kidney Dice 0.9307 (robust), tumor detection 100% (reliable), tumor Dice 0.6558 (moderate — honest). Single takeaway: decision-support, not diagnosis. All outputs require physician review. Not clinically approved. Thank the committee and invite questions. Be confident — the project is honest, documented, and the results are what they are. The committee will respect the transparency. 25 seconds.

-->



---

<!-- ============================================================

     SLIDE 47: KEY REFERENCES

     ============================================================ -->
<SectionTitle number="11" title="Key References" subtitle="Foundational papers and standards supporting this work" />
<div style="margin-top: 0.8rem; font-size: 0.82rem; color: #4a4a4a; line-height: 1.7;">
<div style="margin-bottom: 0.5rem;"><strong style="color: #1a1a1a">[1]</strong> Çiçek et al. (2016). "3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation." <em>MICCAI</em>.</div>
<div style="margin-bottom: 0.5rem;"><strong style="color: #1a1a1a">[2]</strong> Isensee et al. (2021). "nnU-Net: A Self-configuring Method for Deep Learning-based Biomedical Image Segmentation." <em>Nature Methods</em>.</div>
<div style="margin-bottom: 0.5rem;"><strong style="color: #1a1a1a">[3]</strong> KiTS23 Challenge (2023). "The 2023 Kidney and Kidney Tumor Segmentation Challenge." <em>arXiv preprint</em>.</div>
<div style="margin-bottom: 0.5rem;"><strong style="color: #1a1a1a">[4]</strong> IEC 62304 (2006). "Medical Device Software — Software Life Cycle Processes." <em>International Electrotechnical Commission</em>.</div>
<div style="margin-bottom: 0.5rem;"><strong style="color: #1a1a1a">[5]</strong> Ronneberger et al. (2015). "U-Net: Convolutional Networks for Biomedical Image Segmentation." <em>MICCAI</em>.</div>
<div><strong style="color: #1a1a1a">[6]</strong> FDA (2022). "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions." <em>FDA Guidance Document</em>.</div>
</div>
<div style="margin-top: 0.8rem; font-size: 0.78rem; color: #8a8a8a;">
  Full bibliography in <strong style="color: #4a4a4a;">02_ieee_report/refs.bib</strong> — 29 entries with 10 verified and 19 placeholders for team completion.
</div>
<!--

Notes:

Six key references: 3D U-Net (our architecture), nnU-Net (future work benchmark), KiTS23 (dataset), IEC 62304 (safety standard), U-Net (original architecture), FDA guidance (regulatory context). Full bibliography in IEEE report. 20 seconds.

-->

---

<!-- ============================================================

     SLIDE 48: Q&A
np
     ============================================================ -->
<div class="nv-center" style="position: relative; z-index: 1;">
<div style="margin-bottom: 2.5rem;">
  <div style="font-size: 0.65rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.3em; color: #1e3a5f;">NephroVision Final Defense</div>
</div>
<div style="font-size: 4rem; font-weight: 800; color: #1a1a1a; letter-spacing: -0.04em; line-height: 1; margin-bottom: 1rem;">Questions?</div>
<div style="font-family: 'Crimson Text', Georgia, serif; font-size: 1.4rem; font-weight: 400; font-style: italic; color: #4a4a4a; letter-spacing: 0.02em; margin-bottom: 2rem;">We welcome your feedback and discussion</div>
<div style="width: 60px; height: 2px; background: #1e3a5f; margin: 0 auto 2rem;"></div>
<div class="nv-three-col" style="margin-bottom: 2rem; max-width: 600px;">
<MetricCard label="Kidney Dice" value="0.9307" subvalue="± 0.064" status="success" />
<MetricCard label="Tumor Detection" value="100%" subvalue="64/64" status="success" />
<MetricCard label="Tumor Dice" value="0.6558" subvalue="± 0.262" status="warning" />
</div>
<div style="font-size: 0.85rem; color: #8a8a8a; line-height: 1.6;">
  <div><strong style="color: #4a4a4a;">Team:</strong> Rashed Mamdouh · Mohamed Walid · Mahmoud BahaaAldeen · Mahmoud Mohammed · Youssef Mohammed</div>
  <div><strong style="color: #4a4a4a;">Supervisor:</strong> Hisham Abdeltawab, Ph.D.</div>
</div>
</div>
<!--

Notes:

Thank the committee for their time and attention. Invite questions. Be confident — the project is honest, documented, and the results are what they are. The committee will respect the transparency. Reiterate the three key numbers if asked for a summary. 15 seconds.

-->
