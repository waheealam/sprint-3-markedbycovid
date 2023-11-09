<template>
  <v-app>
    <v-toolbar app>
      <v-app-bar app v-bind:class="'bg-' + colorTheme + '-lighten-1'">
        <v-app-bar-nav-icon
          v-if="$vuetify.display.smAndDown"
          @click.stop="drawer = !drawer"
        />

        <v-app-bar-title>
          <a href="/">
            <img
              :src="require('@/assets/logo_header.png')"
              alt="logo"
              class="header-img"
            />
          </a>
        </v-app-bar-title>

        <v-btn
          v-if="$vuetify.display.mdAndUp"
          class="text-capitalize"
          v-for="item in menuItemsList.filter((m) => m.mainMenu)"
          :prepend-icon="item.icon"
          :to="item.urlTo"
          :href="item.urlHref"
          :data-cy="item.CypressID"
          v-bind:target="item.openInNewWindow ? '_blank' : null"
          exact
        >
          {{ item.name }}
        </v-btn>

        <v-menu v-if="$vuetify.display.mdAndUp">
          <template v-slot:activator="{ props }">
            <v-btn data-cy="resources" class="text-capitalize" v-bind="props">
              Resources <v-icon>mdi-menu-down</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="(item, index) in menuItemsList.filter((m) => !m.mainMenu)"
              :key="index"
              :value="index"
              :prepend-icon="item.icon"
              :to="item.urlTo"
              :href="item.urlHref"
              :data-cy="item.CypressID"
              v-bind:target="item.openInNewWindow ? '_blank' : null"
              exact
            >
              {{ item.name }}
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>
    </v-toolbar>

    <v-navigation-drawer
      app
      temporary
      v-model="drawer"
      floating
      class="bg-grey-lighten-2"
    >
      <v-list nav density="compact">
        <v-list-item-group>
          <v-list-item
            v-for="item in menuItemsList"
            :color="item.color"
            :prepend-icon="item.icon"
            :to="item.urlTo"
            :href="item.urlHref"
            :data-cy="item.CypressID"
            v-bind:target="item.openInNewWindow ? '_blank' : null"
            >{{ item.name }}
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-content app>
      <v-container app fluid>
        <router-view />
      </v-container>
    </v-content>

    <FooterComponent :colorTheme="colorTheme" />
  </v-app>
</template>
<script>
import "@mdi/font/css/materialdesignicons.css";
import FooterComponent from "./FooterComponent.vue";
import { APIService } from "@/http/APIService";
const apiService = new APIService();
export default {
  name: "Layout",
  components: { FooterComponent },
  data: () => ({
    drawer: null,
    icons: ["mdi-facebook", "mdi-twitter", "mdi-instagram"],
    colorTheme: null,
    menuItemsList: [
      {
        name: "Submit",
        urlTo: "/submitmemorial",
        icon: "mdi-pencil",
        CypressID: "submit_mem",
        mainMenu: true,
      },
      {
        name: "Search",
        urlTo: "/memorialsearch",
        icon: "mdi-magnify",
        CypressID: "search_memorial",
        mainMenu: true,
      },
      {
        name: "Memorial Map",
        urlTo: "/memorialmap",
        icon: "mdi-map",
        CypressID: "memorial_map",
        mainMenu: true,
      },
      {
        name: "Donate",
        urlHref: "https://secure.actblue.com/donate/memorialmatrix",
        icon: "mdi-cash",
        color: "blue-darken-4",
        openInNewWindow: true,
        CypressID: "mbc_donate",
        mainMenu: true,
      },
      {
        name: "Contact Us",
        urlTo: "/contactus",
        icon: "mdi-email",
        CypressID: "mbc_contact_us",
        mainMenu: false,
      },
      {
        name: "About",
        urlTo: "/about",
        icon: "mdi-account",
        CypressID: "about_us",
        mainMenu: false,
      },
      {
        name: "FAQ",
        urlTo: "/faq",
        icon: "mdi-comment-question-outline",
        CypressID: "faq_page",
        mainMenu: false,
      },
      {
        name: "Sponsors",
        urlTo: "/sponsors",
        icon: "mdi-handshake-outline",
        CypressID: "sponsors",
        mainMenu: false,
      },
    ],
  }),
  mounted() {
    this.getColorTheme();
  },
  methods: {
    getColorTheme() {
      apiService
        .getWebsiteConfigurationParameter("HOME_PAGE_THEME_COLOR")
        .then((res) => {
          this.colorTheme = res.data.data;
          if (this.colorTheme == null) this.colorTheme = "blue-grey";
        });
    },
  },
};
</script>

<style>
.header-img {
  height: 90px;
  max-height: 200px;
  vertical-align: middle;
  padding-bottom: 3px;
  padding-top: 12px;
}
</style>
