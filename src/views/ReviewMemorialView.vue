<template>
  <div class="text-center text-h5 font-weight-bold">Review Form</div>
  <div class="text-subtitle-2 font-weight-bold">
    Please review your entries before submitting the form:
  </div>

  <div v-for="(value, key) in formData" :key="key" class="text-body-2">
    <template v-if="key === 'mem_submitter'">
      <v-card class="mx-auto mb-4" max-width="100%" outlined>
        <v-row>
          <v-col cols="12" sm="12" md="6" lg="6">
            <v-list-item three-line>
              <v-list-item-content>
                <div class="mb-4 mt-2">
                  <strong>{{ changeTitle(key) }}</strong>
                </div>
                <div v-for="(val, key2) in value" class="ml-2">
                  <p>
                    <span class="text-capitalize">{{
                      key2.split("_").join(" ")
                    }}</span
                    >: {{ val }}
                  </p>
                </div>
              </v-list-item-content>
            </v-list-item>
          </v-col>
          <v-col
            cols="12"
            sm="12"
            md="6"
            lg="6"
            style="display: flex"
            class="text-body-2"
          >
            <div v-if="this.formData.profile_picture != null">
              <div v-if="this.formData.profile_picture">
                <v-banner>
                  <v-banner-text class="font-weight-bold"
                    >Profile picture</v-banner-text
                  >
                  <v-banner-text
                    v-if="this.formData.profile_picture"
                    class="font-weight-bold text-wrap"
                    style="color: blue"
                  >
                    If you do not see an image below, please go back and fix the
                    url.
                  </v-banner-text>
                </v-banner>
                <img
                  :src="this.formData.profile_picture"
                  alt=""
                  class="displayImage ma-5"
                />
              </div>
              <span v-else>
                <v-banner>
                  <v-banner-text class="font-weight-bold"
                    >Profile picture</v-banner-text
                  >
                </v-banner>
                <v-sheet
                  class="d-flex align-center justify-center flex-wrap text-center text-bold mx-auto"
                  color="grey-lighten-3"
                  width="150"
                  height="150"
                >
                  <sheet-footer class="text-subtitle-2 text-no-wrap">
                    Url not provided
                  </sheet-footer>
                </v-sheet>
              </span>
            </div>
          </v-col>
        </v-row>
      </v-card>
    </template>

    <template v-else-if="key === 'mem_location'">
      <v-card class="mx-auto mb-4" max-width="100%" outlined>
        <v-row>
          <v-col cols="12" sm="12" md="12" lg="12" class="text-body-2">
            <v-list-item three-line>
              <v-list-item-content>
                <div class="mb-4 mt-2">
                  <strong>{{ changeTitle(key) }}</strong>
                </div>
                <div v-for="(val, key2) in value" class="ml-2">
                  <p>
                    <span class="text-capitalize">{{
                      key2.split("_").join(" ")
                    }}</span
                    >: {{ val }}
                  </p>
                </div>
              </v-list-item-content>
            </v-list-item>
          </v-col>
        </v-row>
      </v-card>
      <v-card class="mx-auto mb-4" max-width="100%" outlined>
        <v-row>
          <v-col
            cols="12"
            sm="12"
            md="12"
            lg="12"
            v-if="displayCarousel(this.mediaData.photoLinks)"
            class="text-body-2"
          >
            <!-- Images display - START -->
            <v-banner>
              <v-banner-text class="font-weight-bold"
                >Media link pictures</v-banner-text
              >
              <v-banner-text
                class="font-weight-bold text-wrap"
                style="color: blue"
              >
                If you do not see a picture in any of the boxes below, please go
                back and fix the url.
              </v-banner-text>
            </v-banner>
            <br />
            <v-row>
              <v-col
                v-for="photoUrl in this.mediaData.photoLinks"
                :key="photoUrl"
                class="d-flex child-flex"
                cols="2"
              >
                <v-img
                  :src="photoUrl.purl"
                  aspect-ratio="1"
                  cover
                  class="bg-grey-lighten-2"
                >
                  <template v-slot:placeholder>
                    <v-row
                      class="fill-height ma-0"
                      align="center"
                      justify="center"
                    >
                      <v-progress-circular
                        indeterminate
                        color="grey-lighten-5"
                      ></v-progress-circular>
                    </v-row>
                  </template>
                </v-img>
              </v-col>
            </v-row>
            <br />
            <!-- Images display - END -->
          </v-col>
        </v-row>
      </v-card>
    </template>
  </div>
  <v-card
    v-if="Object.keys(memInfo).length > 0"
    class="mx-auto mb-1"
    max-width="100%"
    outlined
  >
    <v-list-item three-line>
      <v-list-item-content>
        <div class="mb-4 mt-2">
          <strong>Memorial Information</strong>
        </div>
        <div v-for="(val, key) in memInfo" class="ml-2">
          <p>
            <span class="text-capitalize">{{ key.split("_").join(" ") }}</span
            >: {{ val }}
          </p>
        </div>
      </v-list-item-content>
    </v-list-item>
  </v-card>
  <v-btn
    data-cy="edit"
    class="purple darken-2 white--text mt-5 me-4"
    color="blue"
    to="/submitmemorial"
    @click="editForm"
    v-if="formData"
  >
    <h3 style="text-align: center">Edit</h3>
  </v-btn>
  <v-btn
    data-cy="submit"
    class="purple darken-2 white--text mt-5"
    color="blue"
    @click="submitForm"
    v-if="formData"
  >
    <h3 style="text-align: center">Submit</h3>
  </v-btn>
</template>

<script>
import axios from "axios";
import { APIService } from "../http/APIService";
const apiService = new APIService();
export default {
  name: "ReviewMemorialView",
  data() {
    return {
      formData: null,
      mediaData: null,
      photoLinks: new Array(),
      defaultMemorialPhotoUrl: null,
    };
  },
  mounted() {
    this.formData = JSON.parse(window.localStorage.getItem("formData"));
    this.mediaData = JSON.parse(window.localStorage.getItem("mediaData"));
    window.localStorage.setItem("isRedirectedFromReview", JSON.stringify(true));
  },
  computed: {
    memInfo() {
      return this.flattenObject(this.formData);
    },
  },
  methods: {
    flattenObject(obj) {
      let result = {};

      for (let k in obj) {
        const value = obj[k];

        if (typeof value === "object" && value !== null) {
          const nestedObject = this.flattenObject(value);
        } else {
          result[k] = value;
        }
      }

      return result;
    },
    changeTitle(title) {
      return title === "mem_submitter"
        ? "Memorial Submitter"
        : title === "mem_location"
        ? "Memorial Location"
        : null;
    },
    async submitForm() {
      let memorial_id;
      const API_URL = process.env.VUE_APP_API_ENDPOINT;
      let url = API_URL + "api/create/";
      // apiService.submitMemorial().then(resp=>{
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.xsrfHeaderName = "X-CSRFToken";
      await axios
        .post(url, this.formData)
        .then((res) => {
          memorial_id = res.data.id;
          this.$store.commit("setSubmit", true);
        })
        .catch((error) => {
          console.log(error);
          // this.clearCheckAndForm();
        });
      let mediaurl = API_URL + "api/medialinkCreate/";
      let mem = { memorial: memorial_id };
      this.mediaData = { ...this.mediaData, ...mem };
      await axios
        .post(mediaurl, this.mediaData)
        .then((res) => {
          this.$store.commit("setSubmit", true);
          window.localStorage.removeItem("mediaData");
          window.localStorage.removeItem("formData");
          window.localStorage.removeItem("isRedirectedFromReview");
          this.$router.push({ name: "memorialsaved" });
        })
        .catch((error) => {
          console.log("media links save failed");
          // this.clearCheckAndForm();
        });
    },
    displayCarousel() {
      if (this.mediaData.photoLinks.length == 0) {
        return false;
      }
      if (this.mediaData.photoLinks.length == 1) {
        if (this.mediaData.photoLinks[0] == this.defaultMemorialPhotoUrl) {
          return false;
        }
      }
      return true;
    },
  },
};
</script>

<style>
.displayImage {
  width: 240px;
  height: 240px;
  object-fit: cover;
  object-position: 100% 20%;
}
</style>
