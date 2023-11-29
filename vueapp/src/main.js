import {createApp} from 'vue'
import App from './App.vue'
import router from '@/router'


createApp(App)
    .use(router)
    .mount('#app')



export const APP_BACKEND_DOMAIN = 'http://127.0.0.1:8000/';