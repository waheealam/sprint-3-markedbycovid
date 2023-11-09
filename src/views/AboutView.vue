<template>
  <PageTitle pageTitle="About Us" />
  <v-container fluid px-20>
    <v-row justify="center" class="row bg-grey-lighten-3 text-md-justify mx-5">
      <br />
      <div
        class="about text-body-1 font-italic text-justify mx-5"
        style="height: auto"
        v-html="body.body"
      ></div>
      <br />
    </v-row>
  </v-container>
  <br />
  <div
    class="about text-h6 text-decoration-underline mx-5"
    style="height: auto"
    v-html="body.coreStaffTitle"
  ></div>
  <ul v-for="(coreStaff, index) in body.coreStaffs" :key="index">
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
            v-if="coreStaff.value.photoUrl"
            :src="coreStaff.value.photoUrl"
            alt=""
            class="ma-5 imgStyle"
          />
          <span v-else>No image available</span>
        </v-col>
        <v-col class="text-justify ma-3">
          <h3 class="ml-5 mt-5">{{ coreStaff.value.staffName }}</h3>
          <br />
          <div
            class="ml-5 mr-5"
            v-html="coreStaff.value.staffDescription"
          ></div>
          <br />
        </v-col>
      </v-row>
    </v-card>
  </ul>
</template>

<script>
import axios from "axios";
import { APIService } from "../http/APIService";
import PageTitle from "@/components/PageTitle.vue";
const apiService = new APIService();
export default {
  name: "AboutView",
  components: { PageTitle },
  data() {
    return {
      body: {},
    };
  },
  created() {
    this.getBody();
  },
  methods: {
    getBody() {
      apiService
        .getAboutPageContent()
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
