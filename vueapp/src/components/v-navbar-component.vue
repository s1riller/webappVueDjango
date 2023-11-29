<script>
export default {
  name: 'vNavbarComponent',
  props: {
    msg: String
  }
}
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light" id="ftco-navbar">
    <div class="container">
      <a class="navbar-brand" @click="this.$router.push({name:'Home'})">nebu</a>
      <div class="social-media order-lg-last">
        <button @click="this.$router.push({ name: 'register' })" type="button"
                class="btn mb-2 mb-md-0 py-3 px-4 custom-btn-color">Регистрация
        </button>
        <button @click="this.$router.push({ name: 'login' })" type="button"
                class="btn mb-2 mb-md-0 py-3 px-4 custom-btn-color mx-2">
          Войти
        </button>
      </div>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#ftco-nav"
              aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="ftco-nav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active"><a href="#" class="nav-link">Home</a></li>
          <li class="nav-item"><a href="#" class="nav-link">About</a></li>
          <li class="nav-item"><a href="#" class="nav-link">Work</a></li>
          <li class="nav-item"><a href="#" class="nav-link">Blog</a></li>
          <li class="nav-item"><a href="#" class="nav-link">Contact</a></li>
          <li class="nav-item">
            <input type="text" class="form-control" placeholder="Search on the site">
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.custom-btn-color {
  background-color: #302A7E;
  color: #ffffff; /* Цвет текста */
  border-color: #302A7E; /* Цвет границы */
}


</style>