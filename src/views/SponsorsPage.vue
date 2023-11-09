<template>
  <PageTitle pageTitle="Sponsors and Acknowledgements" />
  <ul v-for="(sponsor, index) in sponsors" :key="index">
    <br />
    <v-card style="height: auto" class="mx-10" outlined tile raised>
      <v-row class="text-center">
        <v-col
          cols="12"
          sm="12"
          md="2"
          lg="2"
          style="display: flex; justify-content: center"
        >
          <img
            v-if="sponsor.value.photoUrl"
            :src="sponsor.value.photoUrl"
            alt=""
            class="imgStyle ma-5"
          />
          <span v-else>No image available</span>
        </v-col>
        <v-col class="text-justify ma-3">
          <h3 class="ml-5 mt-5">{{ sponsor.value.sponsorName }}</h3>
          <br />
          <div
            class="ml-5 mr-5"
            v-html="sponsor.value.sponsorDescription"
          ></div>
          <br />
        </v-col>
      </v-row>
    </v-card>
  </ul>
  <br />
  <br />

  <h3>Memorial Matrix Advisors</h3>
  <ul v-for="(advisor, index) in advisors" :key="index">
    <br />
    <v-card style="height: auto" class="mx-10" outlined tile raised>
      <v-row class="text-center">
        <v-col
          cols="12"
          sm="12"
          md="2"
          lg="2"
          style="display: flex; justify-content: center"
        >
          <img
            v-if="advisor.value.advisorPhotoUrl"
            :src="advisor.value.advisorPhotoUrl"
            alt=""
            class="imgStyle ma-5"
          />
          <span v-else>No image available</span>
        </v-col>
        <v-col class="text-justify ma-3">
          <h3 class="ml-5 mt-5">{{ advisor.value.advisorName }}</h3>
          <br />
          <div
            class="ml-5 mr-5"
            v-html="advisor.value.advisorDescription"
          ></div>
          <br />
        </v-col>
      </v-row>
    </v-card>
  </ul>
  <br />
  <br />

  <h3>Memorial Matrix Volunteers</h3>
  <ul v-for="(volunteer, index) in volunteers" :key="index">
    <br />
    <v-card style="height: auto" class="mx-10" outlined tile raised>
      <v-row class="text-center">
        <v-col
          cols="12"
          sm="12"
          md="2"
          lg="2"
          style="display: flex; justify-content: center"
        >
          <img
            v-if="volunteer.value.volunteerPhotoUrl"
            :src="volunteer.value.volunteerPhotoUrl"
            alt=""
            class="imgStyle ma-5"
          />
          <span v-else>No image available</span>
        </v-col>
        <v-col class="text-justify ma-3">
          <h3 class="ml-5 mt-5">{{ volunteer.value.volunteerName }}</h3>
          <br />
          <div
            class="ml-5 mr-5"
            v-html="volunteer.value.volunteerDescription"
          ></div>
          <br />
        </v-col>
      </v-row>
    </v-card>
  </ul>
</template>

<script>
import axios from "axios";
import { APIService } from "@/http/APIService";
import PageTitle from "@/components/PageTitle.vue";
const apiService = new APIService();
export default {
  name: "SponsorsPage",
  components: { PageTitle },
  data() {
    return {
      sponsors: [],
      advisors: [],
      volunteers: [],
    };
  },
  mounted() {
    this.getPageContent();
  },
  created() {
    this.getPageContent();
  },
  methods: {
    async getPageContent() {
      apiService
        .getSponsorsPageContent()
        .then((response) => {
          this.sponsors = response.data.items[0].sponsors;
          this.advisors = response.data.items[0].advisors;
          this.volunteers = response.data.items[0].volunteers;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style>
.pre-formatted {
  white-space: pre;
}
.imgStyle {
  width: 200px;
  height: 200px;
  object-fit: cover;
  object-position: 100% 20%;
}
</style>
