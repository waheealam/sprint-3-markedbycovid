<template>
  <v-sheet class="bg-grey-lighten-3" fluid>
    <div class="d-flex flex-column fill-height justify-center align-center">
      <PageTitle pageTitle="Memorial Map" class="bg-grey-lighten-3" />
    </div>
    <MapComponent :min="value[0]" :max="value[1]" />
    <br />
    <br />
    <div class="d-flex flex-column fill-height justify-center align-center">
      <Slider
        v-model="value"
        :min="minimum"
        :max="maximum"
        :format="format"
        :step="step"
        style="width: 95%; justify-items: center"
      />
    </div>
    <br />
  </v-sheet>
</template>

<script>
// @ is an alias to /src
import MapComponent from "@/components/MapComponent.vue";
import Slider from "@vueform/slider";
import PageTitle from "@/components/PageTitle.vue";

export default {
  name: "MemorialMapView",
  components: {
    PageTitle,
    props: ["showPageTitle"],
    MapComponent,
    Slider,
  },
  data() {
    return {
      value: [1583042400000, 1709708400000],
      minimum: 1583042400000,
      maximum: 1709708400000,
      step: 7945200000,
      format: function (value) {
        return new Date(value).toDateString().split(" ").slice(1).join(" ");
      },
      showPageTitle: "",
    };
  },
};
</script>

<style src="@vueform/slider/themes/default.css"></style>
