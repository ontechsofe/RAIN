<template>
  <v-app dark>
    <v-toolbar app color="primary">
      <img height="45px" src="@/assets/logo_white.png">
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
    return { }
  }
}
</script>
