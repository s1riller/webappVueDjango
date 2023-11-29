import {createRouter, createWebHistory} from "vue-router";

import vHomeView from "@/views/v-home-view"
import HelloWorld from "@/components/HelloWorld.vue";
import VLoginView from "@/views/v-login-view.vue";
import VRegistrerView from "@/views/v-registrer-view.vue";
import VConfirmRegistrationView from "@/views/v-confirm-registration-view.vue";
const routes = [
    {path: "/", component: vHomeView, name: 'Home'},
    {path: "/hello", component: HelloWorld, name: 'hello'},
    {path: "/login", component: VLoginView, name: 'login'},
    {path: "/register", component: VRegistrerView, name: 'register'},
    {path: '/confirm-registration/:token', component: VConfirmRegistrationView, name: 'confirm-registration',},
];


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});


export default router
