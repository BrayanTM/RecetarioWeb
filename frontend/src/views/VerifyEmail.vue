<script setup>
import HeaderBase from '@/components/HeaderBase.vue';
import FooterBase from '@/components/FooterBase.vue';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useVerifyEmailComposable } from '@/composables/useSecurityComposable.js';

const route = useRoute();
const router = useRouter();
const uid = ref('');

// Get reactive variables from composable
const { verify, loading, error, success, message } = useVerifyEmailComposable();

// Extract token from query parameters and verify
onMounted(async () => {
  uid.value = route.query.token || '';
  if (uid.value) {
    await verify({ uid: uid.value });
  }
});

function goToLogin() {
  router.push('/login');
}
</script>

<template>
  <HeaderBase />

  <div className="breadcumb-area bg-img bg-overlay mb-5" style="background-image: url(/img/bg-img/breadcumb6.jpg)">
    <div className="container h-100">
      <div className="row h-100 align-items-center">
        <div className="col-12">
          <div className="breadcumb-text text-center">
            <h2>Email Verification</h2>
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
            <h3>Please wait while we verify your email</h3>
          </div>
        </div>
      </div>

      <div className="row">
        <div className="col-8 mx-auto">
          <div className="contact-form-area text-center">

            <div v-if="!uid" class="alert alert-warning" role="alert">
              Missing token in the URL. Please use the link sent to your email.
            </div>

            <div v-else>
              <div v-if="loading" class="my-4">
                <img src="/img/img/load.gif" alt="Loading" />
              </div>

              <div v-if="success && message" class="alert alert-success" role="alert">
                <strong>Success!</strong> {{ message }}
              </div>

              <div v-if="error" class="alert alert-danger" role="alert">
                <strong>Error!</strong> {{ error }}
              </div>

              <div class="mt-4">
                <button class="btn delicious-btn" @click="goToLogin">Go to Login</button>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>

  <FooterBase />
</template>

