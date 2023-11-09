<template>
  <v-parallax
    height="800"
    :src="
      homePagePhotoUrl != null
        ? homePagePhotoUrl
        : require('@/assets/memorial.jpg')
    "
    style="position: relative; top: -16px"
  >
    <!--    src="https://imageio.forbes.com/specials-images/imageserve/623255af50c4f4882a8ca298/WASHINGTON-RENDER/0x0.jpg"> -->

    <div
      class="d-flex flex-column fill-height justify-center align-center text-white"
    >
      <p class="text-h4">Crowd-sourced online library of</p>
      <p class="text-h4">Covid memorials and remembrances.</p>
      <p class="text-subtitle-1 font-weight-thin">
        This includes tangible memorial sites and structures, temporary sites
        and
      </p>
      <p class="text-subtitle-1 font-weight-thin">
        installations, vigils, performances, and virtual memorials.
      </p>
      <br />

      <div>
        <v-btn
          flat
          variant="outlined"
          v-if="watchVideoEmbedUrl"
          size="large"
          prepend-icon="mdi-play"
          class="text-capitalize"
          @click="homeVideDialog = true"
        >
          Watch Video
          <v-dialog v-model="homeVideDialog" width="auto">
            <v-card width="640" height="440" class="bg-grey-lighten-2">
              <v-card-item v-html="watchVideoEmbedUrl" />
              <!---
              <iframe width="600" height="400"
                      src="https://www.youtube.com/embed/K2kVdKb8gco?start=35"
                      title="YouTube video player"
                      frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                      allowfullscreen>
              </iframe>
              --->
            </v-card>
          </v-dialog>
        </v-btn>
      </div>
    </div>
  </v-parallax>

  <v-item-group
    selected-class="bg-primary"
    style="position: relative; top: -85px"
  >
    <v-container>
      <v-row>
        <v-col cols="12" md="4">
          <v-item v-slot="{ isSelected, selectedClass, toggle }">
            <v-card height="200" class="bg-yellow-darken-4">
              <div
                class="d-flex flex-column fill-height justify-center align-center " >
                <p class="text-h4 font-weight-thin text-black">
                  Featuring <b>{{ memorialCount }}</b>
                </p>
                <br />
                <p class="text-h4 font-weight-thin text-black" style=" padding-bottom: 11px">
                  Memorials
                </p>

                <br />
                <v-btn
                  data-cy="memorials"
                  flat
                  size="large"
                  color="white"
                  class="text-capitalize"
                  href="/memorialmap"

                >
                  View Map
                </v-btn>
              </div>
            </v-card>
          </v-item>
        </v-col>
        <v-col cols="12" md="4">
          <v-item v-slot="{ isSelected, selectedClass, toggle }">
            <v-card height="200" class="bg-yellow-darken-3">
              <div
                class="d-flex flex-column fill-height justify-center align-center"
              >
                <p class="text-h4 font-weight-thin text-black">
                  Submit Memorial
                </p>
                <br />
                <p class="text-subtitle-1 font-weight-light text-black">
                  Have a story to share ?
                </p>
                <br />
                <br />
                <v-btn
                  data-cy="submit_memorial"
                  flat
                  size="large"
                  color="white"
                  class="text-capitalize"
                  href="/submitmemorial"
                >
                  Submit Memorial
                </v-btn>
              </div>
            </v-card>
          </v-item>
        </v-col>
        <v-col cols="12" md="4">
          <v-item v-slot="{ isSelected, selectedClass, toggle }">
            <v-card height="200" class="bg-yellow-darken-1" style=" padding-bottom: 6px">
              <div
                class="d-flex flex-column fill-height justify-center align-center"
              >
                <p class="text-h4 font-weight-thin text-black">Donate</p>
                <br />
                <p class="text-subtitle-1 font-weight-light text-black">
                  Donate to support the
                </p>
                <p class="text-subtitle-1 font-weight-light text-black">
                  Marked By Covid Memorial Matrix
                </p>
                <br />
                <v-btn
                  data-cy="donate"
                  flat
                  size="large"
                  color="white"
                  class="text-capitalize"
                  href="https://secure.actblue.com/donate/memorialmatrix"
                  target="_blank"
                >
                  Donate Now
                </v-btn>
              </div>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>

  <v-sheet
    class="bg-grey-lighten-3"
    fluid
    style="position: relative; top: -45px"
  >
    <MemorialMapView />
  </v-sheet>

  <br />

  <v-sheet fluid style="position: relative; top: -45px">
    <div class="d-flex flex-column fill-height justify-center align-center">
      <PageTitle pageTitle="Featured Memorials" />
    </div>
  </v-sheet>

  <div style="position: relative; top: -45px">
    <MemorialSlideGroup :is-upcoming="false" />
  </div>

  <br />

  <v-sheet
    class="bg-grey-lighten-3"
    fluid
    style="position: relative; top: -45px"
  >
    <div class="d-flex flex-column fill-height justify-center align-center">
      <PageTitle pageTitle="Upcoming Events" class="bg-grey-lighten-3" />
    </div>
  </v-sheet>

  <div style="position: relative; top: -45px">
    <MemorialSlideGroup :is-upcoming="true" class="bg-grey-lighten-3" />
  </div>
</template>

<script>
// @ is an alias to /src
import MapComponent from "@/components/MapComponent.vue";
import Slider from "@vueform/slider";
import MemorialSlideGroup from "@/views/MemorialSlideGroup.vue";
import MemorialMapView from "@/views/MemorialMap.vue";
import { APIService } from "@/http/APIService";
import PageTitle from "@/components/PageTitle.vue";

const apiService = new APIService();
export default {
  name: "HomeView",
  components: {
    MapComponent,
    PageTitle,
    MemorialMapView,
    MemorialSlideGroup,
    Slider,
  },
  data() {
    return {
      homeVideDialog: false,
      memorialCount: "",
      watchVideoEmbedUrl: "",
      homePagePhotoUrl: null,
    };
  },
  mounted() {
    this.getMemorialCount(),
      this.getWatchVideoEmbedUrl(),
      this.getHomePagePhotoUrl();
  },
  methods: {
    getMemorialCount() {
      apiService.getMemorialCount().then((res) => {
        this.memorialCount = res.data.data;
      });
    },
    getWatchVideoEmbedUrl() {
      apiService
        .getWebsiteConfigurationParameter("HOME_PAGE_WATCH_VIDEO_EMBED_URL")
        .then((res) => {
          this.watchVideoEmbedUrl = res.data.data;
        });
    },
    getHomePagePhotoUrl() {
      apiService
        .getWebsiteConfigurationParameter("HOME_PAGE_PHOTO_URL")
        .then((res) => {
          this.homePagePhotoUrl = res.data.data;
        });
    },
  },
};
</script>

<style src="@vueform/slider/themes/default.css"></style>
