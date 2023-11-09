<template>
  <div>
    <GMapMap
      :center="{ lat: 41.25716, lng: -95.995102 }"
      :zoom="4"
      map-type-id="terrain"
      style="width: 1150px; height: 550px"
      ref="mapRef"
      @click="handleMapClick"
    >
      <GMapMarker
        :position="marker.position"
        :clickable="true"
        :draggable="true"
        @drag="handleMarkerDrag"
        @click="panToMarker"
      />
    </GMapMap>
  </div>
</template>
<script>
export default {
  name: "LatLongPicker",
  data() {
    return {
      marker: { position: { lat: 41.25716, lng: -95.995102 } },
      coordinates: null,
    };
  },
  methods: {
    //sets the position of marker when dragged
    handleMarkerDrag(e) {
      this.marker.position = { lat: e.latLng.lat(), lng: e.latLng.lng() };
    },

    //Moves the map view port to marker
    panToMarker() {
      this.$refs.mapRef.panTo(this.marker.position);
      this.$emit("markerLat", this.marker.position.lat);
      this.$emit("markerLong", this.marker.position.lng);
    },
    //Moves the marker to click position on the map
    handleMapClick(e) {
      this.marker.position = { lat: e.latLng.lat(), lng: e.latLng.lng() };
    },
  },
};
</script>
