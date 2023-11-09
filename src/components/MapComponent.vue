<template>
  <div>
    <GMapMap
      :center="{ lat: 41.25716, lng: -95.995102 }"
      :zoom="4"
      map-type-id="terrain"
      style="width: auto; height: 660px"
    >
      <GMapCluster>
        <GMapMarker
          :key="index"
          v-for="(m, index) in filteredData"
          :position="m.position"
          :clickable="true"
          :draggable="true"
          @click="toggleInfoWindow(m, index)"
        >
          <GMapInfoWindow
            :options="infoOptions"
            :position="infoWindowPos"
            :opened="infoWinOpen === index"
            @closeclick="infoWinOpen = false"
          />
        </GMapMarker>
      </GMapCluster>
    </GMapMap>
  </div>
</template>

<script>
import { computed } from "@vue/runtime-core";
import { APIService } from "../http/APIService";
const apiService = new APIService();

export default {
  name: "MapComponent",
  props: ["min", "max"],

  data() {
    return {
      center: { lat: 37.25716, lng: -95.995102 },
      API_KEY: process.env.VUE_APP_GOOGLE_API_KEY || "",
      markers: [],
      infoWindowPos: null,
      infoWinOpen: null,
      currentMidx: null,
      infoOptions: {
        content: "",
        //optional: offset infowindow so it visually sits nicely on top of our marker
        pixelOffset: {
          width: 0,
          height: -35,
        },
      },
    };
  },

  mounted() {
    this.loadMarkers();
  },

  computed: {
    filteredData() {
      const minDate = new Date(this.min);
      const maxDate = new Date(this.max);
      return this.markers.filter((marker) => {
        const userDate =
          marker.mem_location.time_active_start == null
            ? minDate
            : new Date(marker.mem_location.time_active_start);
        return userDate >= minDate && userDate < maxDate;
      });
    },
  },
  methods: {
    loadMarkers() {
      apiService
        .getMemorials()
        .then((response) => {
          var result = response.data.data;
          if (result.length > 0) {
            for (let i = 0; i < result.length; i++) {
              let memorial = {};
              memorial.id = result[i].id;
              memorial.mem_start_time =
                result[i].mem_location.time_active_start;
              memorial.mem_end_time = result[i].mem_location.time_active_end;
              memorial.mem_location = result[i].mem_location;

              let position = {};
              position.lat = parseFloat(result[i].mem_location.lat_coord);
              position.lng = parseFloat(result[i].mem_location.long_coord);
              memorial.position = position;

              this.markers.push(memorial);
            }
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    async toggleInfoWindow(marker, index) {
      this.infoWindowPos = marker.position;
      let photoUrls = new Array();
      await apiService
        .getMemorialProfilePhotoUrl(marker.id)
        .then((memorialProfilePhotoLinkUrlResponse) => {
          photoUrls = memorialProfilePhotoLinkUrlResponse.data.data;
        })
        .then(async (memorialProfilePhotoLinkUrlResponse) => {
          await apiService
            .getMemorialView(marker.id)
            .then((memorialViewResponse) => {
              let memorialView = memorialViewResponse.data;
              marker.infoText =
                "<table>" +
                "<tr>" +
                "<td colSpan='2'>" +
                "<img src= " +
                photoUrls[0] +
                " height=200 width=400>" +
                "</td>" +
                "</tr>" +
                "<tr>" +
                "<td>" +
                "<strong> Memorial Name: </strong>" +
                "</td>" +
                "<td>" +
                '<a href="/memorialdetail/' +
                memorialView.id +
                '" id="' +
                memorialView.id +
                '" target\="blank">' +
                memorialView.name +
                "</a>" +
                "</td>" +
                "</tr>" +
                "<tr>" +
                "<td>" +
                "<strong> Founder Name: </strong>" +
                "</td>" +
                "<td>" +
                memorialView.founder_name +
                "</td>" +
                (memorialView.mem_location.time_active_start != null
                  ? "<tr>" +
                    "<td>" +
                    "<strong> Memorial Start Date: </strong>" +
                    "</td>" +
                    "<td>" +
                    memorialView.mem_location.time_active_start +
                    "</td>" +
                    "</tr>"
                  : "") +
                (memorialView.mem_location.time_active_end != null
                  ? "<tr>" +
                    "<td>" +
                    "<strong> Memorial End Date: </strong>" +
                    "</td>" +
                    "<td>" +
                    memorialView.mem_location.time_active_end +
                    "</td>" +
                    "</tr>"
                  : "") +
                (memorialView.type != null
                  ? "<tr>" +
                    "<td>" +
                    "<strong> Memorial Type: </strong>" +
                    "</td>" +
                    "<td>" +
                    memorialView.type +
                    "</td>" +
                    "</tr>"
                  : "");
            });
          this.infoOptions.content = marker.infoText;
          //check if its the same marker that was selected if yes toggle
          this.infoWinOpen = this.infoWinOpen === index ? null : index;
        });
    },
  },
};
</script>
<style scoped>
a,
a:visited,
a:hover,
a:active {
  color: inherit;
}
</style>
