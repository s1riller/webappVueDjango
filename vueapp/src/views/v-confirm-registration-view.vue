<template>
  <div class="v-confirm-view">
    <section class="text-center">
      <div class="card mx-4 mx-md-5">
        <div class="card-body py-5 px-md-5">
          <div class="row d-flex justify-content-center">
            <div class="col-lg-8">
              <h2 class="fw-bold mb-5">Подтверждение регистрации</h2>
              <div v-if="confirmationDetail">
                <h5>{{ confirmationDetail }}</h5>
              </div>
              <div v-if="confirmationDetail==='Ваша регистрация успешно подтверждена!'">
                <button @click="this.$router.push({ name: 'login' })" type="button"
                        class="btn btn-primary">Вход
                </button>
              </div>
              <div v-if="confirmationDetail!=='Ваша регистрация успешно подтверждена!'">
                <button @click="this.$router.push({ name: 'register' })" type="button"
                        class="btn btn-primary">Регистрация
                </button>
              </div>

            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import {APP_BACKEND_DOMAIN} from '@/main';

export default {
  data() {
    return {
      confirmationDetail: null,
    }
  },
  mounted() {
    // Извлекаем токен из URL
    const token = this.$route.params.token;

    // Отправляем GET-запрос для подтверждения регистрации
    axios
        .get(`${APP_BACKEND_DOMAIN}/api/confirm-registration/${token}/`)
        .then((response) => {
          // Обработка успешного подтверждения
          this.confirmationDetail = response.data.detail;
        })
        .catch((error) => {
          // Обработка ошибки подтверждения
          // console.error('Ошибка подтверждения регистрации:', error.response.data.detail);
          this.confirmationDetail = error.response.data.detail;
        });
  },
};
</script>

<style scoped>
/* Ваши стили */
</style>
