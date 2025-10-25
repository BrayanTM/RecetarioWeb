<script setup>
import FooterBase from '@/components/FooterBase.vue';
import HeaderBase from '@/components/HeaderBase.vue';

import { useRecipeDetail } from '@/composables/recipeDetailComposable.js';
import { watchEffect } from 'vue';

import { useRoute } from 'vue-router';

const route = useRoute();
const { dataRecipes: dataRecipes, error: error } = useRecipeDetail(route.params.slug);

watchEffect(() => {
  if (error.value) {
    window.location.href = '/error';
  }
});
</script>

<template>
  <HeaderBase />
  <div class="breadcumb-area bg-img bg-overlay" style="background-image: url(/img/bg-img/breadcumb4.jpg)">
    <div class="container h-100">
      <div class="row h-100 align-items-center">
        <div class="col-12">
          <div class="breadcumb-text text-center">
            <h2>{{ dataRecipes.recipe?.name }}</h2>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="receipe-post-area section-padding-80">


    <div class="container">
      <div class="row">
        <div class="col-12">
          <img :src="dataRecipes.recipe?.picture_url" :alt="dataRecipes.recipe?.name" style="height: 300px;" />
        </div>
      </div>
    </div>

    <div class="receipe-content-area">
      <div class="container">

        <div class="row">
          <div class="col-12 col-md-8">
            <div class="receipe-headline my-5">
              <span>{{ dataRecipes.recipe?.created_at }}</span>
              <h2>{{ dataRecipes.recipe?.name }}</h2>
              <div class="receipe-duration">
                <h6>Time : {{ dataRecipes.recipe?.time }}</h6>
                <h6>Category: {{ dataRecipes.recipe?.category_name }}</h6>
                <h6>Created by: {{ dataRecipes.recipe?.user_name }}</h6>
              </div>
            </div>
          </div>


        </div>

        <div class="row">
          <div class="col-12 col-lg-12">
            <div class="single-preparation-step d-flex">

              <p> {{ dataRecipes.recipe?.description }} </p>
            </div>

          </div>

        </div>


      </div>
    </div>
  </div>
  <FooterBase />
</template>
