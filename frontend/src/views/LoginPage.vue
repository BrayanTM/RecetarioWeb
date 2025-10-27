<script setup>
import FooterBase from '@/components/FooterBase.vue';
import HeaderBase from '@/components/HeaderBase.vue';
import { loginValidationSchema } from '@/schemas/validationScheme';
import { useLoginComposable } from '@/composables/useSecurityComposable.js';

import { Form, Field, ErrorMessage } from 'vee-validate';
import { ref } from 'vue';

let email = ref('');
let password = ref('');

let button = ref('block');
let preloader = ref('none');
let errorMessage = ref('');
let successMessage = ref('');

const { login } = useLoginComposable();

let send = async () => {
  button.value = 'none';
  preloader.value = 'block';
  errorMessage.value = '';
  successMessage.value = '';

  const result = await login({
    email: email.value,
    password: password.value
  });

  button.value = 'block';
  preloader.value = 'none';

  if (result.success) {
    successMessage.value = result.message;
    // Clear form
    email.value = '';
    password.value = '';

    // Redirect after 2 seconds
    setTimeout(() => {
      window.location.href = '/panel';
    }, 2000);
  } else {
    errorMessage.value = result.message;
  }
};

</script>

<template>
  <HeaderBase />
  <div className="breadcumb-area bg-img bg-overlay mb-5" style="background-image: url(/img/bg-img/breadcumb5.jpg)">
    <div className="container h-100">
      <div className="row h-100 align-items-center">
        <div className="col-12">
          <div className="breadcumb-text text-center">
            <h2>Login</h2>
          </div>
        </div>
      </div>
    </div>
  </div>


  <div className="contact-area section-padding-0-80 mt-5">
    <div className="container">
      <div className="row">
        <div className="col-12">
          <div className="section-heading">
            <h3>Insert your credentials</h3>
          </div>
        </div>
      </div>

      <div className="row">
        <div className="col-8 mx-auto">
          <div className="contact-form-area">

            <!-- Success Message -->
            <div v-if="successMessage" class="alert alert-success alert-dismissible fade show" role="alert">
              <strong>Success!</strong> {{ successMessage }}
              <button type="button" class="close" @click="successMessage = ''" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>

            <!-- Error Message -->
            <div v-if="errorMessage" class="alert alert-danger alert-dismissible fade show" role="alert">
              <strong>Error!</strong> {{ errorMessage }}
              <button type="button" class="close" @click="errorMessage = ''" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>

            <Form :validation-schema="loginValidationSchema" @submit="send()">

              <div class="row">

                <div class="col-12 col-lg-12">
                  <ErrorMessage name="email" class="text text-danger" />
                  <Field type="text" name="email" v-model="email" class="form-control" placeholder="E-Mail:" />
                </div>

                <div class="col-12 col-lg-12">
                  <ErrorMessage name="password" class="text text-danger" />
                  <Field type="password" v-model="password" name="password" class="form-control"
                    placeholder="Password:" />
                </div>

                <div class="col-12 text-center" :style="'display:' + button">
                  <button class="btn delicious-btn mt-30" type="submit" title="Send">
                    Send
                  </button>
                </div>
                <div class="col-12 text-center" :style="'display:' + preloader">
                  <img src="/img/img/load.gif" />
                </div>

              </div>
            </Form>
          </div>
        </div>
      </div>
    </div>
  </div>

  <FooterBase />
</template>
