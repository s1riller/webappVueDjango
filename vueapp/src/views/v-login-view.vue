<script>
import axios from 'axios'; // Import Axios for making HTTP requests
import {APP_BACKEND_DOMAIN} from '@/main';

export default {
  name: 'v-login-view',
  data() {
    return {
      email: '',
      password: '',
      successMessage: '',
      errorMessages: {
        email: '',
        password: '',
      },
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post(`${APP_BACKEND_DOMAIN}/api/auth/token/login`, {
          email: this.email,
          password: this.password,
        });

        // Assuming your backend returns a token in the response
        const token = response.data.auth_token;

        // Store the token in localStorage or Vuex store for future requests
        localStorage.setItem('authToken', token);
        this.email = '';
        this.password = '';
        // Set success message
        this.successMessage = 'Добро пожаловать!';


        // Redirect or perform any other action upon successful login
        console.log('Login successful!', token);
      } catch (error) {

        // Reset success and error messages
        this.successMessage = '';
        this.errorMessage = '';
        this.errorMessages.email = '';
        this.errorMessages.password = '';

        // Check specific error types and set corresponding error messages
        if (error.response.data.email) {
          if (error.response.data.email[0] === "This field may not be blank.") {
            this.errorMessages.email = 'Введите почту';
          } else if (error.response.data.email[0] === "Пользователь with this email already exists.") {
            this.errorMessages.email = 'Пользователь уже существует';
          }
        }

        if (error.response.data.password) {
          if (error.response.data.password[0] === "This field may not be blank.") {
            this.errorMessages.password = 'Введите пароль';
          } else if (error.response.data.password[0] === "This password is too short. It must contain at least 8 characters.") {
            this.errorMessages.password = 'Придумайте другой пароль, этот коротки пароль';
          } else if (error.response.data.password[0] === "The password is too similar to the email.") {
            this.errorMessages.password = 'Придумайте другой пароль, этот пароль похож на почту';
          } else {
            this.errorMessages.password = 'Неверные данные';
          }

        }
        this.errorMessages.password = 'Неверные данные';

        console.error('Login failed:', error.response.data);
      }
    },
  },
  mounted() {
    console.log('Backend Domain:', APP_BACKEND_DOMAIN);
  },
};
</script>

<template>
  <div class="v-login-view">
    <!-- Section: Design Block -->
    <section class="text-center">

      <div class="card mx-4 mx-md-5 ">
        <div class="card-body py-5 px-md-5">

          <div class="row d-flex justify-content-center">
            <div class="col-lg-8">
              <h2 class="fw-bold mb-5">Войти</h2>
              <form>

                <div class="form-outline mb-4">
                  <input v-model="email" type="email" id="form3Example3" class="form-control"
                         autocomplete="current-email"/>
                  <label class="form-label" for="form3Example3">Почта</label>
                </div>

                <div class="form-outline mb-4">
                  <input v-model="password" type="password" id="form3Example4" class="form-control"
                         autocomplete="current-password"/>
                  <label class="form-label" for="form3Example4">Пароль</label>
                </div>
                <!-- Error messages -->
                <div v-if="errorMessages.email" class="alert alert-danger" role="alert">
                  {{ errorMessages.email }}
                </div>
                <div v-if="errorMessages.password" class="alert alert-danger" role="alert">
                  {{ errorMessages.password }}
                </div>

                <!-- Success message -->
                <div v-if="successMessage" class="alert alert-success" role="alert">
                  {{ successMessage }}
                </div>

                <button @click.prevent="login" type="submit" class="btn btn-primary btn-block mb-4">
                  Войти
                </button>

                <div class="text-center">
                  <p>Войти с</p>
                  <button type="button" class="btn btn-link btn-floating mx-1">
                    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="50" height="50" viewBox="0 0 48 48">
                      <path fill="#4caf50" d="M45,16.2l-5,2.75l-5,4.75L35,40h7c1.657,0,3-1.343,3-3V16.2z"></path>
                      <path fill="#1e88e5" d="M3,16.2l3.614,1.71L13,23.7V40H6c-1.657,0-3-1.343-3-3V16.2z"></path>
                      <polygon fill="#e53935"
                               points="35,11.2 24,19.45 13,11.2 12,17 13,23.7 24,31.95 35,23.7 36,17"></polygon>
                      <path fill="#c62828"
                            d="M3,12.298V16.2l10,7.5V11.2L9.876,8.859C9.132,8.301,8.228,8,7.298,8h0C4.924,8,3,9.924,3,12.298z"></path>
                      <path fill="#fbc02d"
                            d="M45,12.298V16.2l-10,7.5V11.2l3.124-2.341C38.868,8.301,39.772,8,40.702,8h0 C43.076,8,45,9.924,45,12.298z"></path>
                    </svg>
                  </button>

                  <button type="button" class="btn btn-link btn-floating mx-1">
                    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="50" height="50" viewBox="0 0 48 48">
                      <path fill="#3F51B5"
                            d="M42,37c0,2.762-2.238,5-5,5H11c-2.761,0-5-2.238-5-5V11c0-2.762,2.239-5,5-5h26c2.762,0,5,2.238,5,5V37z"></path>
                      <path fill="#FFF"
                            d="M34.368,25H31v13h-5V25h-3v-4h3v-2.41c0.002-3.508,1.459-5.59,5.592-5.59H35v4h-2.287C31.104,17,31,17.6,31,18.723V21h4L34.368,25z"></path>
                    </svg>
                  </button>

                  <button type="button" class="btn btn-link btn-floating mx-1">
                    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="50" height="50" viewBox="0 0 50 50">
                      <path
                          d="M 11 4 C 7.1456661 4 4 7.1456661 4 11 L 4 39 C 4 42.854334 7.1456661 46 11 46 L 39 46 C 42.854334 46 46 42.854334 46 39 L 46 11 C 46 7.1456661 42.854334 4 39 4 L 11 4 z M 11 6 L 39 6 C 41.773666 6 44 8.2263339 44 11 L 44 39 C 44 41.773666 41.773666 44 39 44 L 11 44 C 8.2263339 44 6 41.773666 6 39 L 6 11 C 6 8.2263339 8.2263339 6 11 6 z M 13.085938 13 L 22.308594 26.103516 L 13 37 L 15.5 37 L 23.4375 27.707031 L 29.976562 37 L 37.914062 37 L 27.789062 22.613281 L 36 13 L 33.5 13 L 26.660156 21.009766 L 21.023438 13 L 13.085938 13 z M 16.914062 15 L 19.978516 15 L 34.085938 35 L 31.021484 35 L 16.914062 15 z"></path>
                    </svg>
                  </button>

                  <button type="button" class="btn btn-link btn-floating mx-1">
                    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="50" height="50" viewBox="0 0 48 48">
                      <path fill="#1976d2"
                            d="M42,37c0,2.762-2.238,5-5,5H11c-2.761,0-5-2.238-5-5V11c0-2.762,2.239-5,5-5h26c2.762,0,5,2.238,5,5 V37z"></path>
                      <path fill="#fff"
                            d="M35.937,18.041c0.046-0.151,0.068-0.291,0.062-0.416C35.984,17.263,35.735,17,35.149,17h-2.618 c-0.661,0-0.966,0.4-1.144,0.801c0,0-1.632,3.359-3.513,5.574c-0.61,0.641-0.92,0.625-1.25,0.625C26.447,24,26,23.786,26,23.199 v-5.185C26,17.32,25.827,17,25.268,17h-4.649C20.212,17,20,17.32,20,17.641c0,0.667,0.898,0.827,1,2.696v3.623 C21,24.84,20.847,25,20.517,25c-0.89,0-2.642-3-3.815-6.932C16.448,17.294,16.194,17,15.533,17h-2.643 C12.127,17,12,17.374,12,17.774c0,0.721,0.6,4.619,3.875,9.101C18.25,30.125,21.379,32,24.149,32c1.678,0,1.85-0.427,1.85-1.094 v-2.972C26,27.133,26.183,27,26.717,27c0.381,0,1.158,0.25,2.658,2c1.73,2.018,2.044,3,3.036,3h2.618 c0.608,0,0.957-0.255,0.971-0.75c0.003-0.126-0.015-0.267-0.056-0.424c-0.194-0.576-1.084-1.984-2.194-3.326 c-0.615-0.743-1.222-1.479-1.501-1.879C32.062,25.36,31.991,25.176,32,25c0.009-0.185,0.105-0.361,0.249-0.607 C32.223,24.393,35.607,19.642,35.937,18.041z"></path>
                    </svg>
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>

</style>