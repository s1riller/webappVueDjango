import {createApp} from 'vue'
import App from './App.vue'
import routes from '@/router'

createApp(App)
    .use(router)
    .mount('#app')
