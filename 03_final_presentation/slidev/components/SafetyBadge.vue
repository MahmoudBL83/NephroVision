<script setup>
import { computed } from 'vue'

const props = defineProps({
  label: { type: String, required: true },
  status: { type: String, default: 'info' },
  description: { type: String, default: '' }
})

const config = computed(() => {
  const map = {
    info:    { color: '#1e3a5f', bg: '#f0f4f8', border: '#d0dce8' },
    success: { color: '#2d6a4f', bg: '#f0f7f4', border: '#c8e6d9' },
    warning: { color: '#bc4b31', bg: '#fdf5f2', border: '#f5d5cd' },
    danger:  { color: '#9b2c2c', bg: '#fdf2f2', border: '#f5d0d0' }
  }
  return map[props.status] || map.info
})
</script>

<template>
  <div class="safety-badge" :style="{ borderColor: config.border, background: config.bg }">
    <span class="badge-dot" :style="{ background: config.color }"></span>
    <div class="badge-content">
      <span class="badge-label" :style="{ color: config.color }">{{ label }}</span>
      <span v-if="description" class="badge-desc">{{ description }}</span>
    </div>
  </div>
</template>

<style scoped>
.safety-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 12px;
  border-radius: 999px;
  border: 1px solid;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  transition: all 0.2s ease;
}
.badge-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  flex-shrink: 0;
}
.badge-content {
  display: flex;
  flex-direction: column;
  line-height: 1.15;
}
.badge-label {
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.68rem;
}
.badge-desc {
  font-size: 0.62rem;
  color: #8a8a8a;
  font-weight: 400;
  margin-top: 1px;
}
</style>
