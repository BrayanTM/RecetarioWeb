import { useAuthStore } from '@/stores/authStore';
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
      path: '/verify-email/:token?',
      component: () => import('@/views/VerifyEmail.vue'),
      name: 'verifyEmail',
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
      path: '/contact',
      component: () => import('@/views/ContactPage.vue'),
      name: 'contact',
    },
    {
      path: '/register',
      component: () => import('@/views/RegisterPage.vue'),
      name: 'register',
      meta: { requiresAuth: false },
    },
    {
      path: '/login',
      component: () => import('@/views/LoginPage.vue'),
      name: 'login',
      meta: { requiresAuth: false },
    },
    {
      path: '/panel',
      component: () => import('@/views/PanelPage.vue'),
      name: 'panel',
      meta: { requiresAuth: true },
    },
    {
      path: '/:pathMatch(.*)*',
      component: () => import('@/views/ErrorPage404.vue'),
      name: 'error404',
    }
  ],
})

router.beforeEach((to) => {
  const authStore = useAuthStore();
  if (to.meta.requiresAuth) {
    authStore.isLogin();
  }
  if (to.meta.requiresAuth === false && authStore.authToken != null) {
    return { name: 'error404' };
  }
});

export default router
