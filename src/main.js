import 'vuetify/styles'
import '@fortawesome/fontawesome-free/css/all.css'
import { createApp } from 'vue'
// import VueGoogleMaps from '@fawmi/vue-google-maps'
import VueGoogleMaps from 'vue-google-maps-community-fork'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/lib/components'
import * as directives from 'vuetify/lib/directives'
//import { aliases, fa } from 'vuetify/iconsets/fa4'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

const vuetify = createVuetify({
    components,
    directives,
    icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
          mdi,
        },
      },
  })
//createApp(App).use(store, axios).use(router).mount('#app')
createApp(App).use(store, axios).use(router)
.use(vuetify)
.use(VueGoogleMaps, {
  load: {
      key: process.env.VUE_APP_GOOGLE_API_KEY || '',
      libraries: 'places',
      // language: 'de',
  },
}).mount('#memorialApp')