import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './rouer'
import { BootstrapVue, IconsPlugin  } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.config.productionTip = false

new Vue({
  store,
  router,
  BootstrapVue,
  IconsPlugin,
  render: h => h(App)
}).$mount('#app')
