import VuetifyLoaderPlugin from 'vuetify-loader/lib/plugin'
import pkg from './package'

export default {
  mode: 'spa',

  /*
  ** Headers of the page
  */
  head: {
    title: 'Cambridge Bitcoin Electricity Consumption Index (CBECI)',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description },
      { hid: 'keywords', name: 'keywords', content: 'Bitcoin, Cryptocurrency, Electricity, Energy, Mining, Efficiency, PoW, ASIC, Proof-of-work, Environmental, Blockchain, Index' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href:
          'https://fonts.googleapis.com/css?family=Exo+2:300,400,500,700|Material+Icons'
      }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [
    '~/assets/style/app.styl',
    '~/assets/style/main.css',
    'latex2js/lib/latex2js.css',
    'katex/dist/katex.min.css'
],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '@/plugins/vuetify',
    { src: '~plugins/ga.js', ssr: false },
    { src: '~plugins/latex2js.js', ssr: false },
    { src: '~plugins/katex2js.js', ssr: false },
  ],

  /*
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/axios',
  ],

  axios: {
    proxyHeaders: false,
    credentials: false,
    baseURL: 'https://cbeci.org'
  },
  /*
  ** Build configuration
  */
  build: {
    transpile: ['vuetify/lib'],
    plugins: [new VuetifyLoaderPlugin()],
    loaders: {
      stylus: {
        import: ['~assets/style/variables.styl']
      }
    },
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    }
  }
}
