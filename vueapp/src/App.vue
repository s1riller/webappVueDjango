<template>
  <div id="app">
    <v-navbar-component/>

    <router-view/>
  </div>
</template>

<script>
import vNavbarComponent from "@/components/v-navbar-component.vue"
import 'bootstrap/dist/css/bootstrap.css';


export default {
  name: 'App',
  components: {
    vNavbarComponent
  }
}
</script>

<style>
</style>
