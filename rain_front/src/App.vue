<template>
  <v-app dark>
    <v-toolbar app color="primary">
      <v-toolbar-title class="headline">
        <span class="font-weight-light">r</span>
        <span>AI</span>
        <span class="font-weight-light">n</span>
      </v-toolbar-title>
    </v-toolbar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      //
    }
  }
}
</script>
