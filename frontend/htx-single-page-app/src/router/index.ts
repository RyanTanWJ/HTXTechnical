import { createRouter, createWebHistory } from 'vue-router'
import TranscriptionsView from '@/views/TranscriptionsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: TranscriptionsView,
    },
    {
      path: '/upload',
      name: 'upload',
      component: () => import('../views/FileUploadView.vue'),
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('../views/SearchView.vue'),
    },
  ],
})

export default router
