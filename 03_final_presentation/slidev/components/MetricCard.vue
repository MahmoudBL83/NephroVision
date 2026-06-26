<script setup>
import { computed } from 'vue'

const props = defineProps({
  label: { type: String, required: true },
  value: { type: String, required: true },
  subvalue: { type: String, default: '' },
  status: { type: String, default: 'default' },
  color: { type: String, default: '' }
})

const resolvedColor = computed(() => {
  if (props.color) return props.color
  const map = { success: '#2d6a4f', warning: '#bc4b31', danger: '#9b2c2c', info: '#1e3a5f', default: '#1e3a5f' }
  return map[props.status] || map.default
})

const resolvedBg = computed(() => {
  const map = { success: '#f0f7f4', warning: '#fdf5f2', danger: '#fdf2f2', info: '#f0f4f8', default: '#f0f4f8' }
  return map[props.status] || map.default
})
</script>

<template>
  <div class="metric-card" :style="{ borderColor: resolvedColor + '40', background: resolvedBg }">
    <div class="metric-label">{{ label }}</div>
    <div class="metric-value" :style="{ color: resolvedColor }">{{ value }}</div>
    <div v-if="subvalue" class="metric-subvalue">{{ subvalue }}</div>
  </div>
</template>

<style scoped>
.metric-card {
  border-radius: 6px;
  border: 1px solid;
  padding: 20px 16px;
  text-align: center;
  min-width: 130px;
  transition: border-color 0.2s ease;
}
.metric-card:hover {
  border-color: #c0c0c0;
}
.metric-label {
  font-size: 0.6rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #a0a0a0;
  margin-bottom: 10px;
}
.metric-value {
  font-family: 'SF Mono', 'JetBrains Mono', Consolas, monospace;
  font-size: 1.7rem;
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.02em;
}
.metric-subvalue {
  font-size: 0.68rem;
  color: #a0a0a0;
  margin-top: 6px;
  font-weight: 500;
}
</style>
