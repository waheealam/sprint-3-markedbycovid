<template>
  <v-card height="60px" flat class="row-no-gutters">
    <v-card-title class="text-h5 font-weight-regular page-title">
      {{ pageTitle }}
    </v-card-title>
  </v-card>
</template>

<script>
export default {
  name: "PageTitle",
  props: ["pageTitle"],
  data: () => ({
    pageTitle: "",
  }),
};
</script>

<style>
.page-title {
  font-weight: 500;
  display: inline-block;
  padding-bottom: 10px;
  position: relative;
}
.page-title:before {
  content: "";
  position: absolute;
  width: 80px;
  height: 5px;
  bottom: 0px;
  left: 16px;
  border-bottom: 3px solid orange;
}
</style>
