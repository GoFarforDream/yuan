<script setup>
import { computed, reactive, ref } from 'vue'

const API_URL = import.meta.env.VITE_API_URL || 'http://yuan.voyagers.work/api'

const form = reactive({
  name1: '',
  name2: '',
})

const result = ref(null)
const loading = ref(false)
const error = ref('')
const requestHint = ref('准备就绪')

const canSubmit = computed(() => form.name1.trim() && form.name2.trim() && !loading.value)

const scoreStyle = computed(() => {
  const score = result.value?.score ?? 0
  return {
    background: `conic-gradient(#d81b60 ${score * 3.6}deg, #f9d7e3 0deg)`,
  }
})

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

async function calculate() {
  if (!canSubmit.value) return

  loading.value = true
  error.value = ''
  requestHint.value = '正在整理信息'

  try {
    await sleep(450)
    requestHint.value = '正在计算契合指数'

    const response = await fetch(`${API_URL}/compatibility`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name1: form.name1,
        name2: form.name2,
      }),
    })

    const data = await response.json()
    if (!response.ok) {
      throw new Error(data.detail || '测算失败，请稍后重试')
    }

    await sleep(250)
    result.value = data
    requestHint.value = '测算完成'
  } catch (err) {
    error.value = err.message || '测算失败，请稍后重试'
    requestHint.value = '请求失败'
  } finally {
    loading.value = false
  }
}

function resetForm() {
  form.name1 = ''
  form.name2 = ''
  result.value = null
  error.value = ''
  requestHint.value = '准备就绪'
}
</script>

<template>
  <main class="page-shell">
    <section class="calculator-panel">
      <div class="topbar">
        <div class="brand-row">
          <span class="brand-mark">Y</span>
          <span>缘分测算</span>
        </div>
        <span class="status-pill" :class="{ active: loading }">{{ requestHint }}</span>
      </div>

      <header class="headline">
        <p class="eyebrow">姓名 · 契合指数</p>
        <h1>一份正式的缘分测算报告</h1>
        <p class="subtitle">输入两个人的姓名，得到分数、文案和三个参考维度。</p>
      </header>

      <form class="match-form" @submit.prevent="calculate">
        <div class="person-card">
          <span class="person-label">第一位</span>
          <label>
            <span>姓名</span>
            <input v-model="form.name1" type="text" autocomplete="name" placeholder="例如：林小鹿" />
          </label>
        </div>

        <div class="link-badge">MATCH</div>

        <div class="person-card">
          <span class="person-label">第二位</span>
          <label>
            <span>姓名</span>
            <input v-model="form.name2" type="text" autocomplete="name" placeholder="例如：许星河" />
          </label>
        </div>

        <div class="actions">
          <button class="primary-button" type="submit" :disabled="!canSubmit">
            {{ loading ? '测算中' : '开始测算' }}
          </button>
          <button class="ghost-button" type="button" @click="resetForm">重置</button>
        </div>
      </form>

      <p v-if="error" class="error-text">{{ error }}</p>
    </section>

    <section class="result-panel" :class="{ 'empty-result': !result, loading }">
      <template v-if="loading && !result">
        <div class="loading-frame">
          <div class="pulse-line wide"></div>
          <div class="pulse-line medium"></div>
          <div class="pulse-line short"></div>
          <p>正在生成报告，请稍候。</p>
        </div>
      </template>

      <template v-else-if="result">
        <div class="result-topline">
          <span>{{ result.name1 }}</span>
          <span class="small-heart">♥</span>
          <span>{{ result.name2 }}</span>
        </div>

        <div class="score-ring" :style="scoreStyle">
          <div>
            <strong>{{ result.score }}</strong>
            <span>分</span>
          </div>
        </div>

        <h2>{{ result.message }}</h2>

        <div class="metric-list">
          <div class="metric-item">
            <div>
              <span>心动火花</span>
              <strong>{{ result.chemistry }}</strong>
            </div>
            <meter min="0" max="100" :value="result.chemistry"></meter>
          </div>
          <div class="metric-item">
            <div>
              <span>相处节奏</span>
              <strong>{{ result.rhythm }}</strong>
            </div>
            <meter min="0" max="100" :value="result.rhythm"></meter>
          </div>
          <div class="metric-item">
            <div>
              <span>缘分浓度</span>
              <strong>{{ result.destiny }}</strong>
            </div>
            <meter min="0" max="100" :value="result.destiny"></meter>
          </div>
        </div>
      </template>

      <template v-else>
        <div class="empty-orbit">
          <span>♥</span>
        </div>
        <h2>等待一份正式的测算结果</h2>
        <p>填写信息后，报告会在这里展示。</p>
      </template>
    </section>
  </main>
</template>
