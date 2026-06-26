<script setup>
defineProps({
  title: { type: String, required: true },
  subtitle: { type: String, default: '' },
  number: { type: String, default: '' }
})
</script>

<template>
  <div class="section-title-wrapper">
    <div class="section-title-row">
      <div v-if="number" class="section-number">{{ number }}</div>
      <h1 class="section-title">{{ title }}</h1>
    </div>
    <p v-if="subtitle" class="section-subtitle">{{ subtitle }}</p>
    <div class="section-line"></div>
  </div>
</template>

<style scoped>
.section-title-wrapper {
  margin-bottom: 12px;
}
.section-title-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 4px;
}
.section-number {
  font-family: 'Crimson Text', Georgia, serif;
  font-size: 1.4rem;
  font-weight: 700;
  color: #1e3a5f;
  line-height: 1;
  letter-spacing: -0.02em;
  opacity: 0.5;
  flex-shrink: 0;
}
.section-title {
  font-size: 1.6rem !important;
  font-weight: 700 !important;
  color: #1a1a1a !important;
  letter-spacing: -0.02em;
  line-height: 1.2;
  margin: 0 !important;
}
.section-subtitle {
  font-size: 0.85rem;
  color: #8a8a8a;
  margin: 0 0 6px 0;
  font-weight: 400;
  font-family: 'Crimson Text', Georgia, serif;
  font-style: italic;
  line-height: 1.3;
}
.section-line {
  height: 1.5px;
  width: 40px;
  background: #1e3a5f;
  border-radius: 1px;
}
</style>
