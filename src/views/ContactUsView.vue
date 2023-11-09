<template>
  <PageTitle pageTitle="Contact Us"> </PageTitle>
  <v-container fluid>
    <v-hover>
      <template v-slot:default="{ isHovering, props }">
        <v-card variant="outlined">
          <v-card-text class="text-h6"
            >Thank you for visiting Memorial Matrix website</v-card-text
          >
          <v-card-text>
            Any Questions? Please leave us your thoughts. We are happy to hear
            from you!!
          </v-card-text>
        </v-card>
      </template>
    </v-hover>
    <v-row class="fill-height ma-0" align="center" justify="center">
      <v-col
        cols="12"
        sm="12"
        md="6"
        lg="6"
        mt-2
        class="order-last order-md-first"
      >
        <div>
          <ContactUs />
        </div>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6">
        <div>
          <v-img
            max-height="550"
            :src="contactUsImageUrl"
            :lazy-src="contactUsImageUrl"
            aspect-ratio="1"
            cover
            alt="contactus"
          ></v-img>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ContactUs from "@/components/ContactUs.vue";
import PageTitle from "@/components/PageTitle.vue";
import { APIService } from "@/http/APIService";
const apiService = new APIService();
export default {
  components: {
    ContactUs,
    PageTitle,
  },
  data: () => ({
    contactUsImageUrl: "",
  }),
  mounted() {
    this.getContactUsImageUrl();
  },
  methods: {
    getContactUsImageUrl() {
      apiService
        .getWebsiteConfigurationParameter("CONTACT_US_IMAGE_URL")
        .then((res) => {
          this.contactUsImageUrl = res.data.data;
          if (this.contactUsImageUrl == null)
            this.contactUsImageUrl =
              "https://images.squarespace-cdn.com/content/v1/61ea0471aaadbc3bce33ad60/1646701015481-RCXL8FUYBHTQ9BTV95VP/Screen+Shot+1.jpeg?format=1000w";
        });
    },
  },
};
</script>

<style lang="css" scoped>
h1 {
  text-decoration: underline;
  margin-bottom: 5%;
}
</style>
