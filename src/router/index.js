import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Layout from '../components/Layout.vue'
import AboutView from '../views/AboutView.vue'
import MemorialDetailView from '../views/MemorialDetailView.vue'
import SubmitMemorialView from '../views/SubmitMemorialView.vue'
import MemorialSaved from '../views/MemorialSaved.vue'
import MemorialSearch from '../views/MemorialSearch.vue'
import ModifyMemorialView from '../views/ModifyMemorialView'
import MemorialMap from "@/views/MemorialMap.vue";
import ContactUsView from '../views/ContactUsView'
import ReviewMemorialView from '../views/ReviewMemorialView'
import ContactUsSaved from '../views/ContactUsSaved.vue'
import FaqPage from "@/views/FaqPage.vue";
import SponsorsPage from "@/views/SponsorsPage.vue";


const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'home',
        component: HomeView
      },
      {
        path: '/about',
        name: 'about',
        component: AboutView
      },
      {
        path: '/faq',
        name: 'faq',
        component: FaqPage
      },
      {
        path: '/memorialdetail',
        name: 'memorialdetail',
        component: MemorialDetailView
      },
      {
        path: '/memorialdetail/:id',
        name: 'memorialdetail',
        component: MemorialDetailView
      },
      {
        path: '/submitmemorial',
        name: 'submitmemorial',
        component: SubmitMemorialView
      },
      {
        path: '/reviewmemorial',
        name: 'reviewmemorial',
        component: ReviewMemorialView
      },
      {
        path: '/memorialsaved',
        name: 'memorialsaved',
        component: MemorialSaved
      },
      {
        path: '/updatememorial',
        name: 'updatememorial',
        component: ModifyMemorialView
      },
      {
        path: '/memorialsearch',
        name: 'memorialsearch',
        component: MemorialSearch
      },
      {
        path: '/memorialmap',
        name: 'memorialmap',
        component: MemorialMap
      },
      {
        path: '/contactus',
        name: 'contactus',
        component: ContactUsView
      },
      {
        path: '/contactussaved',
        name: 'contactussaved',
        component: ContactUsSaved
      },
      {
        path: '/sponsors',
        name: 'sponsors',
        component: SponsorsPage
      },
    ],
  }
]

const router = createRouter({
  history: createWebHistory("/"),
  routes
})

export default router;