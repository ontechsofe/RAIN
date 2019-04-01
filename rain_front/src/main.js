import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import './registerServiceWorker'
import VueChart from 'vue-chart-js'

Vue.config.productionTip = false

Vue.use(VueChart)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
