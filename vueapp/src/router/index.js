import { createRouter, createWebHistory } from "vue-router";

import vHomeView from "@/views/v-home-view"
import HelloWorld from "@/components/HelloWorld.vue";

const routes = [
    { path: "/", component: vHomeView, name:'Home' },
    { path: "/hello", component: HelloWorld, name:'hello' },
];


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});


export default router;
