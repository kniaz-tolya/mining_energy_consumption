<template>
  <v-layout column justify-center align-center id="wrap-container">
    <v-snackbar
            v-model="error.status"
            top
            :timeout="0"
    >
      {{ error.message }}
      <v-btn
              color="pink"
              flat
              @click="error = false"
      >
        Close
      </v-btn>
    </v-snackbar>
    <v-layout row align-center>
      <v-flex>
        <img src="~static/live.png" height="40">
      </v-flex>
      <v-flex pa-3>
        <v-layout column>
          <span class="index-text">&nbsp;Bitcoin network power</span>
          <v-layout row>
            <v-icon class="icon-custom">
              updated
            </v-icon>
            <span style="margin-left: 4px" class="index-subtext">updated every 24 hours</span>
          </v-layout>
        </v-layout>
      </v-flex>
    </v-layout>
    <client-only>
      <cards />
    </client-only>
    <template v-if="!error.blocks.includes('chart')">
      <chart />
    </template>
    <template v-else>
      <v-progress-circular indeterminate :size="50" :width="5" />
    </template>
    <!--<chartLoading v-if="progress"/>-->
    <v-layout row align-center my-4>
      <a href="https://cbeci.org/api/csv" target="_blank">Download data in CSV format</a>
    </v-layout>
    <v-layout row align-center my-4>
      <span style="text-align: center">You can adjust the electricity cost parameter below to explore how the model reacts.</span>
    </v-layout>
    <client-only>
      <controllers />
    </client-only>
  </v-layout>
</template>

<script>
import Controllers from '~/components/index/Controllers'
import myMiddleware from '@/middleware/myMiddleware'
// import Cards from '~/components/index/Cards'
import ChartLoading from '~/components/index/ChartLoading'
import Chart from '~/components/index/Chart'

export default {
  name: 'index',
  layout: myMiddleware || 'default',
  components: {
    controllers: Controllers,
    cards: () => import('~/components/index/Cards'),
    chartLoading: ChartLoading,
    chart: Chart
  },
  async fetch ({ store }) {
    await store.dispatch('INITIALIZATION')
  },
  mounted() {
    if (typeof window === 'object') {
      window.addEventListener('resize', this.resize());
    }
  },
  data() {
    return {
      containerWidth: 0
    }
  },
  computed: {
      progress() {
          return this.$store.state.progress2
      },
    error: {
      get () {
        return this.$store.state.error
      },
      set () {
        this.$store.commit('SET_ERROR', {status: false, message: ''})
      }
    }
  },
  methods: {
    resize () {
      const body = document.body
      const html = document.documentElement
      document.iframeHeight = Math.max( body.scrollHeight, body.clientHeight, body.offsetHeight,
              html.clientHeight, html.scrollHeight, html.offsetHeight )
    }
  }
}
</script>
