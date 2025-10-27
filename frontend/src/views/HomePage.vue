<script setup>
import FooterBase from '@/components/FooterBase.vue';
import HeaderBase from '@/components/HeaderBase.vue';
import { getDataHome } from '@/services/homeServices.js';
import { onMounted, ref } from 'vue';

let dataHome = ref([]);

onMounted(async () => {
  dataHome.value = await getDataHome();
});
// console.log(dataHome);

</script>

<template>
  <HeaderBase />
  <div class="breadcumb-area bg-img bg-overlay" style="background-image: url(/img/bg-img/breadcumb3.jpg)">
    <div class="container h-100">
      <div class="row h-100 align-items-center">
        <div class="col-12">
          <div class="breadcumb-text text-center">
            <h2>Web Cookbook</h2>
          </div>
        </div>
      </div>
    </div>
  </div>

  <section class="top-catagory-area section-padding-80-0">
    <div class="container">

    </div>
  </section>
  <section class="best-receipe-area">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="section-heading">
            <h3>Latest published recipes</h3>
          </div>
        </div>
      </div>

      <div class="row">

        <div v-for="(data, index) in dataHome.recipes" :key="index" class="col-12 col-sm-6 col-lg-4">
          <div class="single-best-receipe-area mb-30">
            <img :src="data.picture_url" class="foto-mini" :alt="data.name" />
            <div class="receipe-content">
              <router-link :to="{ name: 'recipeDetail', params: { slug: data.slug } }">
                <h5>{{ data.name }}</h5>
              </router-link>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
  <FooterBase />
</template>

<style scoped></style>
