import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router'
import './assets/css/global.css'
import axios from 'axios'
import qs from 'qs'

Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.prototype.$qs = qs

// axios.defaults.baseURL = 'http://localhost:5000'
axios.interceptors.request.use(
  config => {
    const tokenStr = window.sessionStorage.getItem('token')
    if(tokenStr){
      config.headers.token = tokenStr
    }
    return config
  }
)

// 设置一个响应拦截器
axios.interceptors.response.use(
  response => {
    if(response.data.status === 10016 || response.data.status === 10017){
      window.sessionStorage.removeItem('token')
      router.replace(
        {
          path: '/login'
        }
      )
    }
    return response
  }
)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
