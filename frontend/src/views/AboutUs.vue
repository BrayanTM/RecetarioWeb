<script setup>
import HeaderBase from '@/components/HeaderBase.vue';
import FooterBase from '@/components/FooterBase.vue';

</script>

<template>
<HeaderBase />
<div class="breadcumb-area bg-img bg-overlay" style="background-image: url(/img/bg-img/breadcumb1.jpg)">
  <div class="container h-100">
      <div class="row h-100 align-items-center">
          <div class="col-12">
              <div class="breadcumb-text text-center">
                  <h2>About Us</h2>
              </div>
          </div>
      </div>
  </div>
</div>
<section class="about-area section-padding-80">
  <div class="container">
      <div class="row">
          <div class="col-12">
              <div class="section-heading">
                  <h3>Who We Are and What We Do</h3>
              </div>
          </div>
      </div>

      <div class="row">
          <div class="col-12">
              <h6 class="sub-heading pb-5">We are a team of passionate food lovers dedicated to sharing our favorite recipes and culinary tips with the world.</h6>

              <p class="text-center">Our mission is to inspire home cooks of all skill levels to create delicious meals and enjoy the process of cooking.</p>
          </div>
      </div>


      <div class="row">
          <div class="col-12">
              <img class="mb-70" src="/img/bg-img/about.png" alt="" />

          </div>
      </div>
  </div>
</section>
<FooterBase />

</template>
