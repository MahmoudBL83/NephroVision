<script setup>
defineProps({
  number: { type: [String, Number], required: true },
  title: { type: String, required: true },
  description: { type: String, default: '' }
})
</script>

<template>
  <div class="pipeline-step">
    <div class="step-number">{{ number }}</div>
    <div class="step-body">
      <div class="step-title">{{ title }}</div>
      <div v-if="description" class="step-desc">{{ description }}</div>
    </div>
  </div>
</template>

<style scoped>
.pipeline-step {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  background: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 14px 18px;
  transition: border-color 0.2s ease;
}
.pipeline-step:hover {
  border-color: #c8c8c8;
}
.step-number {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #f0f4f8;
  border: 1px solid #1e3a5f;
  color: #1e3a5f;
  font-size: 0.7rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'SF Mono', monospace;
  margin-top: 1px;
}
.step-body {
  flex: 1;
  min-width: 0;
}
.step-title {
  font-size: 0.88rem;
  font-weight: 600;
  color: #1a1a1a;
  line-height: 1.3;
}
.step-desc {
  font-size: 0.75rem;
  color: #8a8a8a;
  margin-top: 3px;
  line-height: 1.4;
}
</style>
