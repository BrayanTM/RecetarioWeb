<script setup>
import FooterBase from '@/components/FooterBase.vue';
import HeaderBase from '@/components/HeaderBase.vue';
import { useRecipe } from '@/composables/recipeComposable.js';
import { watchEffect, ref } from 'vue';

import { Form, Field } from 'vee-validate';

const { dataRecipes: dataRecipes, categories: categories, error: error } = useRecipe();

watchEffect(() => {
  if (error.value) {
    window.location.href = '/error';
  }
});

let search = ref('');
let category_id = ref('0');

let send = () => {
  if (category_id.value != '0') {
    window.location.href = `/recipes/search?category_id=${category_id.value}&search=${search.value}`;
  }
};

</script>

<template>
  <HeaderBase />

  <div class="breadcumb-area bg-img bg-overlay" style="background-image: url(img/bg-img/breadcumb4.jpg)">
    <div class="container h-100">
      <div class="row h-100 align-items-center">
        <div class="col-12">
          <div class="breadcumb-text text-center">
            <h2>Recipes</h2>
          </div>
        </div>
      </div>
    </div>
  </div>

  <section class="top-catagory-area section-padding-80-0">
    <div class="container">

      <div class="receipe-post-search mb-80">
        <div class="container">
          <Form @submit="send()">
            <div class="row">

              <div class="col-12 col-lg-4">
                <Field as="select" v-model="category_id" class="form-control" name="category_id" id="category_id">
                  <option value="0">Selection.....</option>
                  <option v-for="(category, i) in categories.categories" :key="i" :value="category.id">{{ category.name
                    }}</option>
                </Field>
              </div>

              <div class="col-12 col-lg-4">
                <Field type="text" v-model="search" name="search" id="search" class="form-control"
                  placeholder="Search....." />
              </div>

              <div class="col-12 col-lg-3 text-right">
                <button type="submit" class="btn delicious-btn" title="Search">
                  <i class="fas fa-search"></i> Search
                </button>
              </div>

            </div>
          </Form>
        </div>
      </div>

    </div>
  </section>

  <section class="best-receipe-area">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="section-heading">
            <h3>All our recipes</h3>
          </div>
        </div>
      </div>

      <div class="row">
        <div v-for="(data, index) in dataRecipes.recipes" :key="index" class="col-12 col-sm-6 col-lg-4">
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
