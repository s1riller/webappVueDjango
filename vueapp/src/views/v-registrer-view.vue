<template>
  <div class="v-register-view">
    <!-- Section: Design Block -->
    <section class="text-center">
      <div class="card mx-4 mx-md-5">
        <div class="card-body py-5 px-md-5">
          <div class="row d-flex justify-content-center">
            <div class="col-lg-8">
              <h2 class="fw-bold mb-5">Зарегистрироваться</h2>
              <form @submit.prevent="register">

                <!-- Email input -->
                <div class="form-outline mb-4">
                  <input v-model="email" type="email" id="form3Example3" class="form-control"
                         autocomplete="current-email"/>
                  <label class="form-label" for="form3Example3">Почта</label>
                </div>

                <!-- Password input -->
                <div class="form-outline mb-4">
                  <input v-model="password" type="password" id="form3Example4" class="form-control"
                         autocomplete="current-password"/>
                  <label class="form-label" for="form3Example4">Пароль</label>
                </div>


                <!-- Submit button -->
                <button type="submit" class="btn btn-primary btn-block mb-4">
                  Зарегистрироваться
                </button>

                <!-- Error messages -->
                <div v-if="errorMessage" class="alert alert-danger" role="alert">
                  {{ errorMessage }}
                </div>
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

                <!-- Register buttons -->
                <div class="text-center">
                  <!-- Social media buttons... -->
                </div>

              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'; // Import Axios for making HTTP requests
import {APP_BACKEND_DOMAIN} from '@/main';

export default {
  name: 'v-register-view',
  data() {
    return {
      email: '',
      password: '',
      errorMessage: '', // Added for displaying general error messages
      errorMessages: {
        email: '',
        password: '',
      }, // Added for displaying specific error messages
      successMessage: '', // Added for displaying success message
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post(`${APP_BACKEND_DOMAIN}/api/auth/users/`, {
          email: this.email,
          password: this.password,
        });

        console.log('Registration successful:', response.data);

        // Set success message
        this.successMessage = `Успешная регистрация, добро пожаловать ${response.data.email}!`;
        this.email = '';
        this.password = '';
        // Optionally, you can redirect the user to a new page or perform other actions after successful registration.
      } catch (error) {
        // Handle registration error
        console.error('Registration failed:', error.response.data);

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
          }
        }
      }
    },
  },
  mounted() {
    console.log('Backend Domain:', APP_BACKEND_DOMAIN);
  },
};
</script>

<style scoped>
/* Your styles go here */
</style>
