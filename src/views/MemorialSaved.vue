<template>
  <div id="MemorialSaved">
    <v-container style="padding-top: 8%; padding-bottom: 12%" fluid>
      <v-row justify="center" class="row">
        <v-col style="max-width: 70%; max-height: 40%">
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
              Thank you for submitting a memorial to Marked by Covid's Memorial
              Matrix. A volunteer will review your submission before publishing.
              We may reach out to you by email if we have any questions.
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "MemorialSaved",
};
</script>

<style scoped></style>
