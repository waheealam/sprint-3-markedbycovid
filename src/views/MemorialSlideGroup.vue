<template>
  <v-sheet :class="isUpcoming ? 'bg-grey-lighten-3' : ''">
    <v-slide-group
      v-model="activeMemorial"
      selectedClass="bg-grey-accent-1"
      center-active
      show-arrows
      :direction="$vuetify.display.xs ? 'vertical' : 'horizontal'"
    >
      <v-slide-group-item
        v-for="memorial in memorialSortedByDate"
        :key="memorial.id"
        v-slot="{ isSelected, toggle, selectedClass }"
      >
        <v-card
          :class="['ma-4', selectedClass]"
          elevation="5"
          height="520"
          width="330"
          @click="toggle"
        >
          <v-carousel
            height="220"
            show-arrows="hover"
            cycle
            cyle-interval="4000"
            hide-delimiter-background
            :hide-delimiters="false"
          >
            <v-carousel-item
              v-for="photoUrl in photoLinks.get(memorial.id)"
              :src="photoUrl"
            >
            </v-carousel-item>
          </v-carousel>

          <v-card-title
            class="text-orange-darken-4 text-capitalize font-weight-bold"
          >
            {{ memorial.name }}
          </v-card-title>
          <v-card-subtitle>
            <v-row class="text-green-darken-4 text-capitalize font-weight-bold">
              <v-col>{{ memorial.founder_name }}</v-col>
            </v-row>
            <v-row col="12" class="text-blue-darken-4 font-weight-bold">
              <v-col col="6" class="text-left">{{
                memorial.mem_location.time_active_start
              }}</v-col>
              <v-col
                col="6"
                class="text-right"
                v-if="
                  memorial.mem_location != null &&
                  memorial.mem_location.city != null
                "
                >{{ memorial.mem_location.city }},
                {{ memorial.mem_location.state }}</v-col
              >
            </v-row>
          </v-card-subtitle>
          <v-card-text class="text-justify">
            <div v-if="memorial.description.length < 220">
              {{ memorial.description }}
            </div>
            <div v-else>
              {{ memorial.description.substring(0, 220) + "..." }}
            </div>
          </v-card-text>
          <v-card-actions
            class="position-absolute justify-center"
            style="bottom: 0; left: 100px"
          >
            <v-btn
              :href="this.prepareUrl(memorial.website)"
              target="_blank"
              class="text-blue justify-center"
            >
              Learn More
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-slide-group-item>
    </v-slide-group>
  </v-sheet>
  <v-row v-if="memorialSortedByDate.length == 0">
    <v-col class="text-center font-weight-bold text-orange-darken-3">
      There are no
      <slot v-if="this.isUpcoming">upcoming events.</slot>
      <slot v-else>featured memorials.</slot>
    </v-col>
  </v-row>
</template>
<script>
import { APIService } from "@/http/APIService";
const apiService = new APIService();

export default {
  name: "Memorial Slide Group",
  props: ["isUpcoming"],
  data: () => ({
    model: null,
    memorials: [],
    photoLinks: new Map(),
    activeMemorial: "",
  }),
  mounted() {
    this.getMemorialsList();
  },
  computed: {
    memorialSortedByDate() {
      if (this.memorials.length == 0) return this.memorials;

      return this.memorials
        .slice()
        .sort(
          (a, b) =>
            new Date(a.mem_location.time_active_start).setHours(0, 0, 0, 0) -
            new Date(b.mem_location.time_active_start).setHours(0, 0, 0, 0)
        );
    },
    photoUrlsLength(photoUrls) {
      return photoUrls.length;
    },
  },
  methods: {
    getMemorialsList() {
      (this.isUpcoming
        ? apiService.getUpcomingEvents()
        : apiService.getFeaturedMemorials()
      )
        .then((getMemorialsResponse) => {
          this.memorials = getMemorialsResponse.data.data;
          return getMemorialsResponse.data.data;
        })
        .then((getMemorialsResponse) => {
          for (const i in this.memorials) {
            apiService
              .getMemorialProfilePhotoUrl(this.memorials[i].id)
              .then((memorialProfilePhotoLinkUrlResponse) => {
                let photoUrls = new Array();
                photoUrls = memorialProfilePhotoLinkUrlResponse.data.data;
                this.photoLinks.set(this.memorials[i].id, photoUrls);
              });
          }
        });
    },
    prepareUrl(url) {
      if (url != null && !url.startsWith("http")) {
        return "https://" + url;
      }
      return url;
    },
  },
};
</script>
