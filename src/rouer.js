import Vue from 'vue'
import VueRouter from 'vue-router'
import Catalog_page from './views/Catalog_page'
import card_detail_page from "@/components/card_detail_page";
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Catalog_page
  },
  {
    path: '/:en_name',
    name: 'detail_card_page',
    component: card_detail_page,
    props: true
  }


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
