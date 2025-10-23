import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('@/views/HomePage.vue'),
      name: 'home',
    },
    {
      path: '/about-us',
      component: () => import('@/views/AboutUs.vue'),
      name: 'aboutUs',
    },
    {
      path: '/recipes',
      component: () => import('@/views/RecipeList.vue'),
      name: 'recipeList',
    },
    {
      path: '/recipe/:slug',
      component: () => import('@/views/RecipeDetail.vue'),
      name: 'recipeDetail',
    },
    {
      path: '/recipes/search',
      component: () => import('@/views/RecipeSearch.vue'),
      name: 'recipeSearch',
    },
    {
      path: '/:pathMatch(.*)*',
      component: () => import('@/views/ErrorPage404.vue'),
      name: 'error404',
    }
  ],
})

export default router
