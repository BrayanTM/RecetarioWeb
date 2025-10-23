<script setup>
import FooterBase from '@/components/FooterBase.vue';
import HeaderBase from '@/components/HeaderBase.vue';
import { contactValidationSchema } from '@/schemas/validationScheme';
import { useContactComposable } from '@/composables/useContactComposable.js';

import { Form, Field, ErrorMessage } from 'vee-validate';
import { ref } from 'vue';

let name = ref('');
let email = ref('');
let phone = ref('');
let message = ref('');

let button = ref('block');
let preloader = ref('none');

const { sendData } = useContactComposable();

let send = () => {
  button.value = 'none';
  preloader.value = 'block';
  sendData({ name: name.value, email: email.value, phone: phone.value, message: message.value });
};

</script>

<template>
  <HeaderBase />
  <div class="breadcumb-area bg-img bg-overlay" style="background-image: url(img/bg-img/breadcumb4.jpg)">
    <div class="container h-100">
      <div class="row h-100 align-items-center">
        <div class="col-12">
          <div class="breadcumb-text text-center">
            <h2>Contact Us</h2>
          </div>
        </div>
      </div>
    </div>
  </div>


  <div class="contact-information-area section-padding-80">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="logo mb-80">
            <img src="/img/core-img/logo2.png" alt="" style="width: 144px;height:65px" />
          </div>
        </div>
      </div>

      <div class="row">


        <div class="col-12 col-lg-12">
          <div class="row">
            <div class="col-4">
              <div class="single-contact-information mb-30">
                <h6>Address:</h6>
                <p>481 Creekside Lane Avila <br />Beach, CA 93424</p>
              </div>
            </div>
            <div class="col-4">
              <div class="single-contact-information mb-30">
                <h6>Phones:</h6>
                <p>+53 345 7953 32453 <br />+53 345 7557 822112</p>
              </div>
            </div>
            <div class="col-4">
              <div class="single-contact-information mb-30">
                <h6>E-Mail:</h6>
                <p>{{ 'yourmail@gmail.com' }}</p>
              </div>
            </div>
          </div>


        </div>


      </div>
    </div>
  </div>
  <div class="contact-area section-padding-0-80">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="section-heading">
            <h3>Tell us how we can help you!!</h3>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-12">
          <div class="contact-form-area">
            <Form :validation-schema="contactValidationSchema" @submit="send()">

              <div class="row">

                <div class="col-12 col-lg-6">
                  <ErrorMessage name="name" class="text text-danger" />
                  <Field type="text" name="name" class="form-control" v-model="name" placeholder="Name" />
                </div>

                <div class="col-12 col-lg-6">
                  <ErrorMessage name="email" class="text text-danger" />
                  <Field type="text" name="email" class="form-control" v-model="email" placeholder="E-Mail" />
                </div>


                <div class="col-12">
                  <ErrorMessage name="phone" class="text text-danger" />
                  <Field type="text" name="phone" class="form-control" v-model="phone" placeholder="Phone" />
                </div>

                <div class="col-12">
                  <ErrorMessage name="message" class="text text-danger" />
                  <Field as="textarea" name="message" class="form-control" v-model="message" placeholder="Message"
                    cols="30" row="10" />
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
