<template>

  <div id="ContactUsSaved">
    <v-container style="padding-top: 8%; padding-bottom: 12%" fluid>
      <v-row justify="center" class="row">
        <v-col style="max-width: 65%; max-height: 40%">
          <v-card elevation="5">
            <v-card-actions class="justify-center">
              <v-img
                :src="require('@/assets/checked.png')"
                padding-top="10px"
                max-height="20%"
                max-width="20%"
              />
            </v-card-actions>
            <v-card-title class="text-wrap">
              Thank you for submitting your inquiries to Marked by Covid's
              Memorial Matrix. We will get back to you as soon as possible.
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "ContactUsSaved",
};
</script>

<style scoped></style>
