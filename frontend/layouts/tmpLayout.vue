<template>
  <v-app>
    <v-layout column class="menu hidden-sm-and-down">
      <v-list class="demo" expand>
        <v-list-tile>
          <nuxt-link :class="{'active': $route.path === '/'}" to="/?page=tmp1">
            Index
          </nuxt-link>
        </v-list-tile>
        <v-list-tile>
          <nuxt-link :class="{'active': $route.path.includes('/cbeci/comparisons/')}" to="/cbeci/comparisons/?page=tmp1">
            Comparisons
          </nuxt-link>
        </v-list-tile>
        <v-list-tile>
          <nuxt-link :class="{'active': $route.path === '/faq/'}" to="/faq/?page=tmp1">
            FAQ
          </nuxt-link>
        </v-list-tile>
        <v-list-tile>
          <nuxt-link :class="{'active': $route.path === '/cbeci/methodology/'}" to="/cbeci/methodology/?page=tmp1">
            Methodology
          </nuxt-link>
        </v-list-tile>
      </v-list>
    </v-layout>
    <v-content style="padding: 0 !important;">
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import Cookie from '@/components/Cookie.vue'
  export default {
    components: {
      Cookie
    },
    data() {
      return {
      }
    },
    computed: {
    },
    methods: {
    }
  }
</script>
