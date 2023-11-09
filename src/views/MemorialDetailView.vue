<template>
  <PageTitle pageTitle="Memorial Details"> </PageTitle>

  <v-card elevation="5" @click="toggle">
    <v-card-title
      class="text-orange-darken-4 text-capitalize font-weight-bold text-center text-h6"
    >
      {{ memorialView.name }}
    </v-card-title>

    <v-card-subtitle>
      <v-row
        class="text-green-darken-4 text-capitalize font-weight-bold text-center text-subtitle-1"
      >
        <v-col>{{ memorialView.founder_name }}</v-col>
      </v-row>
    </v-card-subtitle>

    <v-divider />
    <br />

    <v-row>
      <v-col
        cols="12"
        sm="12"
        :md="displayCarousel(photoLinks) ? 6 : 12"
        :lg="displayCarousel(photoLinks) ? 6 : 12"
      >
        <v-card-text class="text-justify text-body-1">
          <div>{{ memorialView.description }}</div>
        </v-card-text>
        <v-card-text class="text-body-1">
          <div v-if="memorialView.memorial_type_desc">
            <strong>Type:</strong>
            <span>{{ memorialView.memorial_type_desc }}</span>
          </div>
          <div v-if="memorialView.type">
            <strong>Memorial Type:</strong>
            <span class="text-capitalize">{{ memorialView.type }}</span>
          </div>
          <div v-if="this.mem_location_type">
            <strong>Memorial Location Type:</strong>
            <span>{{ memorialView.mem_location.type }}</span>
          </div>
          <div v-if="this.mem_location_permanent">
            <strong>Permanent or Temporary:</strong>
            <span class="text-capitalize">{{
              memorialView.mem_location.permanent
            }}</span>
          </div>
          <div v-if="memorialView.founder_name">
            <strong> Founder Name: </strong>
            <span>{{ memorialView.founder_name }}</span>
          </div>
          <div v-if="memorialView.email">
            <strong> Email: </strong> <span>{{ memorialView.email }}</span>
          </div>
          <div v-if="memorialView.website">
            <strong> Website: </strong>
            <a v-bind:href="memorialView.website" target="_blank">{{
              memorialView.website < 20
                ? memorialView.website
                : memorialView.website.substring(0, 40) + "..."
            }}</a>
          </div>
          <div v-if="this.startdate">
            <strong> Start Date: </strong> <span>{{ this.startdate }}</span>
          </div>
          <div v-if="this.enddate">
            <strong> End Date: </strong> <span>{{ this.enddate }}</span>
          </div>
          <br />
          <div v-if="memorialView.profile_picture">
            <strong> Memorial Profile Pic: </strong>
            <a v-bind:href="memorialView.profile_picture" target="_blank">{{
              memorialView.profile_picture < 40
                ? memorialView.profile_picture
                : memorialView.profile_picture.substring(0, 40) + "..."
            }}</a>
          </div>
          <div v-if="memorialView.google_virtual_tour">
            Virtual Tour:
            <a v-bind:href="memorialView.google_virtual_tour" target="_blank">{{
              memorialView.google_virtual_tour < 40
                ? memorialView.google_virtual_tour
                : memorialView.google_virtual_tour.substring(0, 40) + "..."
            }}</a>
          </div>
          <div v-if="memorialView.social_media_facebook">
            <strong> Facebook: </strong>
            <a
              v-bind:href="memorialView.social_media_facebook"
              target="_blank"
              >{{
                memorialView.social_media_facebook < 40
                  ? memorialView.social_media_facebook
                  : memorialView.social_media_facebook.substring(0, 40) + "..."
              }}</a
            >
          </div>
          <div v-if="memorialView.social_media_twitter">
            <strong> Twitter: </strong>
            <a
              v-bind:href="memorialView.social_media_twitter"
              target="_blank"
              >{{
                memorialView.social_media_twitter < 40
                  ? memorialView.social_media_twitter
                  : memorialView.social_media_twitter.substring(0, 40) + "..."
              }}</a
            >
          </div>
          <div v-if="memorialView.social_media_instagram">
            <strong> Instagram: </strong>
            <a
              v-bind:href="memorialView.social_media_instagram"
              target="_blank"
              >{{
                memorialView.social_media_instagram < 20
                  ? memorialView.social_media_instagram
                  : memorialView.social_media_instagram.substring(0, 40) + "..."
              }}</a
            >
          </div>
        </v-card-text>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" v-if="displayCarousel(photoLinks)">
        <v-carousel
          height="300"
          width="550"
          :show-arrows="photoLinks.length > 1 ? 'hover' : false"
          cycle
          cyle-interval="4000"
          hide-delimiter-background
          :hide-delimiters="photoLinks.length < 2"
          cover
        >
          <v-carousel-item v-for="photoUrl in photoLinks" :src="photoUrl">
          </v-carousel-item>
        </v-carousel>
      </v-col>
    </v-row>

    <!--    <v-divider/>-->

    <v-row>
      <v-col cols="12" sm="12" md="6" lg="6">
        <v-card-text class="text-body-1">
          <div
            v-if="medialLinks.length > 0"
            class="text-blue-darken-4 font-weight-bold"
          >
            Associated Media Links
          </div>
          <br />
          <div v-for="medialink in medialLinks" v-bind:key="medialink">
            <div v-if="medialink.type !== 'photo'">
              <p>
                <strong>{{ medialink.type }}: </strong>
                <a v-bind:href="medialink.url" target="_blank">{{
                  medialink.url.length < 40
                    ? medialink.url
                    : medialink.url.substring(0, 40) + "..."
                }}</a>
              </p>
            </div>
          </div>
        </v-card-text>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" align="center">
        <div class="text-blue-darken-4 font-weight-bold">Memorial Location</div>
        <div class="text-orange-darken-4 font-weight-bold">
          <strong>{{ address }}</strong>
        </div>
        <div
          id="location_m"
          v-if="this.pos.lng !== '' && this.pos.lat !== ''"
          class="align-center"
        >
          <GMapMap
            :center="this.pos"
            :zoom="4"
            map-type-id="terrain"
            style="width: 550px; height: 300px"
          >
            <GMapMarker
              :position="this.pos"
              :clickable="true"
              :draggable="true"
            >
            </GMapMarker>
          </GMapMap>
        </div>
        <div
          id="location_m"
          v-if="this.pos.lng === '' && this.pos.lat === ''"
          class="align-center"
        >
          <GMapMap
            :center="{ lat: 41.25716, lng: -95.995102 }"
            :zoom="4"
            map-type-id="terrain"
            style="width: 550px; height: 300px"
          >
          </GMapMap>
        </div>
      </v-col>
    </v-row>

    <br />
    <v-divider />

    <v-card-actions>
      <v-row>
        <v-col cols="12" sm="12" md="6" lg="6" align="center">
          <!--          <v-btn-->
          <!--            size="large"-->
          <!--            :href="this.prepareUrl(memorialView.website)"-->
          <!--            target="_blank"-->
          <!--            class="text-blue" >-->
          <!--            Learn More-->
          <!--          </v-btn>-->
          <router-link :to="{ name: 'updatememorial' }">
            <v-btn
              data-cy="edit_memorial"
              size="large"
              elevation="2"
              @click="setpk(memorialView.id)"
              class="text-blue"
            >
              Edit Memorial
            </v-btn>
          </router-link>
        </v-col>
        <v-col cols="12" sm="12" md="6" lg="6" align="center">
          <v-btn
            @click="share('facebook')"
            target="_blank"
            prepend-icon="mdi-facebook"
            class="text-blue justify-center"
          >
            Share via Facebook
          </v-btn>
          <v-btn
            @click="share('instagram')"
            target="_blank"
            prepend-icon="mdi-instagram"
            class="text-blue justify-center"
          >
            Share via Instagram
          </v-btn>
          <v-btn
            @click="share('email')"
            target="_blank"
            prepend-icon="mdi-email"
            class="text-blue justify-center"
          >
            Share via Email
          </v-btn>
        </v-col>
      </v-row>
    </v-card-actions>
  </v-card>
</template>

<style></style>

<script>
import PageTitle from "@/components/PageTitle.vue";
import { APIService } from "@/http/APIService";

const apiService = new APIService();
export default {
  components: {
    PageTitle,
  },
  name: "MemorialDetailView",
  data: () => ({
    memorialView: {},
    pos: { lat: "", lng: "" },
    startdate: "",
    enddate: "",
    address: "",
    medialLinks: {},
    valid: true,
    mem_location_type: "",
    mem_location_permanent: "",
    photoLinks: new Array(),
    defaultMemorialPhotoUrl: null,
  }),
  mounted() {
    this.getMemorialView();
    this.getMediaLinks();
    this.getPhotoLinks();
    this.getMemorialDefaultPhotoUrl();
  },
  methods: {
    getMemorialView() {
      this.memorialid = this.$route.params.id;
      apiService.getMemorialView(this.memorialid).then((res) => {
        this.memorialView = res.data;
        if (
          this.memorialView.mem_location.lat_coord !== null &&
          this.memorialView.mem_location.long_coord !== null
        ) {
          this.pos.lat = parseFloat(this.memorialView.mem_location.lat_coord);
          this.pos.lng = parseFloat(this.memorialView.mem_location.long_coord);
        }
        if (this.memorialView.mem_location !== null) {
          this.mem_location_type = this.memorialView.mem_location.type;
          this.mem_location_permanent =
            this.memorialView.mem_location.permanent;
          let street_addr =
            this.memorialView.mem_location.address !== null
              ? this.memorialView.mem_location.address + ", "
              : "";
          let city =
            this.memorialView.mem_location.city !== null
              ? this.memorialView.mem_location.city + ", "
              : "";
          let state =
            this.memorialView.mem_location.state !== null
              ? this.memorialView.mem_location.state
              : "";
          this.address = street_addr + city + state;
        }
        this.startdate = this.memorialView.mem_location.time_active_start;
        let month,
          day,
          year = "";
        let formStrDate,
          ddmmyyyyStrDate = "";
        this.startdate !== null
          ? ([year, month, day] = this.startdate.split("-"))
          : console.log("start date empty");
        if (this.startdate !== null) {
          formStrDate = `${year}-${month.padStart(2, "0")}-${day.padStart(
            2,
            "0"
          )}`;
          ddmmyyyyStrDate = `${month.padStart(2, "0")}/${day.padStart(
            2,
            "0"
          )}/${year}`;
          this.startdate = ddmmyyyyStrDate;
        } else {
          console.log("start date still empty :-/");
        }

        this.enddate = this.memorialView.mem_location.time_active_end;
        let formEndDate,
          ddmmyyyyEndDate = "";
        this.enddate !== null || this.enddate === ""
          ? ([year, month, day] = this.enddate.split("-"))
          : console.log("end date empty");
        if (this.enddate !== null || this.enddate === "") {
          formEndDate = `${year}-${month.padStart(2, "0")}-${day.padStart(
            2,
            "0"
          )}`;
          ddmmyyyyEndDate = `${month.padStart(2, "0")}/${day.padStart(
            2,
            "0"
          )}/${year}`;
          this.enddate = ddmmyyyyEndDate;
        } else {
          console.log("end date still empty :-/");
        }
      });
    },
    share(provider) {
      let url = window.location.href;
      switch (provider) {
        case "facebook":
          window.open(
            "https://www.facebook.com/sharer/sharer.php?u=" +
              encodeURIComponent(url)
          );
          break;
        case "email":
          window.open(
            "mailto:?subject=Check out this link&body=" +
              encodeURIComponent(url)
          );
          break;
        case "instagram":
          window.open(
            "https://www.instagram.com/?url=" + encodeURIComponent(url)
          );
        default:
          console.log("Invalid provider.");
      }
    },
    getMediaLinks() {
      this.memorialid = this.$route.params.id;
      apiService.getMediaLinksView(this.memorialid).then((res) => {
        this.medialLinks = res.data;
      });
    },
    getPhotoLinks() {
      this.memorialid = this.$route.params.id;
      apiService
        .getMemorialProfilePhotoUrl(this.memorialid)
        .then((memorialProfilePhotoLinkUrlResponse) => {
          this.photoLinks = memorialProfilePhotoLinkUrlResponse.data.data;
        });
    },
    getMemorialDefaultPhotoUrl() {
      apiService
        .getWebsiteConfigurationParameter("MEMORIAL_DEFAULT_PICTURE_URL")
        .then((res) => {
          this.defaultMemorialPhotoUrl = res.data.data;
        });
    },
    setpk(id) {
      localStorage.setItem("id", id);
    },
    prepareUrl(url) {
      if (url != null && !url.startsWith("http")) {
        return "https://" + url;
      }
      return url;
    },
    displayCarousel(photoLinks) {
      if (photoLinks.length == 0) {
        return false;
      }
      if (photoLinks.length == 1) {
        if (photoLinks[0] == this.defaultMemorialPhotoUrl) {
          return false;
        }
      }
      return true;
    },
  },
};
</script>
