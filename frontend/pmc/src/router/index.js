import { createRouter, createWebHistory } from 'vue-router'
import search from "@/components/search.vue";
// import telegram_message from "@/components/telegram_message.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: search
  },
  {
    path: '/:catchAll(.*)',
    name: 'all',
    component: search
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
