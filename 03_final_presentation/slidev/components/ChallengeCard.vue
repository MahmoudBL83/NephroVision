<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: { type: String, required: true },
  problem: { type: String, default: '' },
  mitigation: { type: String, default: '' },
  remaining: { type: String, default: '' }
})

const hasBody = computed(() => props.problem || props.mitigation || props.remaining)
</script>

<template>
  <div class="challenge-card">
    <div class="challenge-header">
      <div class="challenge-dot"></div>
      <div class="challenge-title">{{ title }}</div>
    </div>
    <div v-if="hasBody" class="challenge-body">
      <div v-if="problem" class="challenge-row">
        <span class="challenge-key">Problem:</span>
        <span class="challenge-val">{{ problem }}</span>
      </div>
      <div v-if="mitigation" class="challenge-row">
        <span class="challenge-key">Mitigation:</span>
        <span class="challenge-val">{{ mitigation }}</span>
      </div>
      <div v-if="remaining" class="challenge-row">
        <span class="challenge-key">Remaining:</span>
        <span class="challenge-val">{{ remaining }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.challenge-card {
  background: #fdf5f2;
  border: 1px solid #f5d5cd;
  border-radius: 6px;
  padding: 12px 16px;
  transition: all 0.2s ease;
}
.challenge-card:hover {
  border-color: #e8c4bb;
}
.challenge-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}
.challenge-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #bc4b31;
  flex-shrink: 0;
}
.challenge-title {
  font-size: 0.88rem;
  font-weight: 600;
  color: #1a1a1a;
}
.challenge-body {
  display: flex;
  flex-direction: column;
  gap: 3px;
}
.challenge-row {
  display: flex;
  gap: 6px;
  font-size: 0.78rem;
  line-height: 1.35;
}
.challenge-key {
  font-weight: 600;
  color: #bc4b31;
  flex-shrink: 0;
  min-width: 64px;
}
.challenge-val {
  color: #4a4a4a;
}
</style>
