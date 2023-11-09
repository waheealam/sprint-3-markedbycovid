<template>
  <v-footer bottom fixed padless class="ma-0 pa-0" width="auto">
    <v-container elevation="2" fluid>
      <v-row class="bg-grey-darken-2 text-center">
        <v-col cols="12" sm="12" md="3" lg="3">
          <v-btn
            data-cy="contact_us_footer"
            href="/contactus"
            x-large
            class="mx-0"
            icon="mdi-email"
            variant="plain"
          ></v-btn>
          <v-btn
            data-cy="facebook_footer"
            :href="this.body.facebookLink"
            x-large
            class="mx-0"
            icon="mdi-facebook"
            variant="plain"
            target="_blank"
          ></v-btn>
          <v-btn
            data-cy="instagram_footer"
            :href="this.body.instagramLink"
            x-large
            class="mx-0"
            icon="mdi-instagram"
            variant="plain"
            target="_blank"
          ></v-btn>
          <v-btn
            data-cy="twitter_footer"
            :href="this.body.twitterLink"
            x-large
            class="mx-0"
            icon="mdi-twitter"
            variant="plain"
            target="_blank"
          ></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="6" lg="6">
          <v-btn data-cy="home" href="/" x-large class="mx-0" variant="plain"
            >Home</v-btn
          >
          <v-btn
            data-cy="about"
            href="/about"
            x-large
            class="mx-0"
            variant="plain"
            >About</v-btn
          >
          <v-btn
            data-cy="contact_us_footer_2"
            href="/contactus"
            x-large
            class="mx-0"
            variant="plain"
            >Contact Us</v-btn
          >
          <v-btn data-cy="faq" href="/faq" x-large class="mx-0" variant="plain"
            >FAQ</v-btn
          >
        </v-col>
        <v-col cols="12" sm="12" md="3" lg="3">
          <v-btn
            data-cy="share"
            :href="this.body.shareStoryLink"
            x-large
            class="mx-0"
            variant="plain"
            target="_blank"
            >Share</v-btn
          >
          <v-btn
            data-cy="donate_footer"
            :href="this.body.donate"
            x-large
            class="mx-0"
            variant="plain"
            target="_blank"
            >Donate</v-btn
          >
        </v-col>
      </v-row>
      <!-- LOGOs -->
      <v-row v-bind:class="'bg-' + colorTheme + '-lighten-4  text-center'">
        <v-col cols="12" sm="12" md="4" lg="3">
          <!-- Marked by Covid's Memorial Matrix logo -->
          <a href="/">
            <img
              src="@/assets/logo_footer.png"
              style="
                max-width: 250px;
                max-height: 300px;
                vertical-align: middle;
                padding-bottom: 10px;
                padding-top: 10px;
              "
              alt=""
            />
          </a>
        </v-col>
        <v-col
          cols="12"
          sm="12"
          md="4"
          lg="6"
          class="text-subtitle-2 font-weight-thin text-justify"
        >
          The Memorial Matrix web application and ecosystem is the product of a
          partnership between Marked By Covid (MBC) a Non-Profit organization
          and the University of Nebraska Omaha, College of Information Science
          and Technology (UNO IS&T). This collaborative effort between the MIS
          Capstone Students and Faculty of UNO IS&T and the Marked By Covid team
          and activists, is an effort to support the global community affected
          by Covid
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="3">
          <a href="https://www.unomaha.edu/">
            <img
              src="https://www.unomaha.edu/university-communications/downloadables/lock-up/uno-lock-up-color-black.png"
              style="
                max-width: 200px;
                max-height: 500px;
                vertical-align: middle;
                padding-bottom: 10px;
                padding-top: 10px;
              "
              alt=""
            />
          </a>
        </v-col>
      </v-row>
      <v-row class="bg-grey-darken-2 text-center">
        <v-col>
          <!--          <v-btn-->
          <!--            x-large-->
          <!--            class="mx-0 text-right"-->
          <!--            variant="plain"> &copy; {{ new Date().getFullYear() }} </v-btn>-->
          <v-btn
            href="https://www.markedbycovid.com/"
            x-large
            class="mx-0"
            variant="plain"
            target="_blank"
          >
            &copy; Marked By Covid
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
import { APIService } from "../http/APIService";
const apiService = new APIService();
export default {
  name: "FooterComponent",
  props: ["colorTheme"],
  data: () => ({
    icons: ["mdi-facebook", "mdi-twitter", "mdi-instagram"],
    body: {},
  }),
  created() {
    this.getBody();
  },
  methods: {
    getBody() {
      apiService
        .getFooterContent()
        .then((response) => {
          this.body = response.data.items[0];
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
