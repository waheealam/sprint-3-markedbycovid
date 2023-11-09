<template>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Archivo+Narrow&display=swap"
    rel="stylesheet"
  />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo+Narrow&display=swap"
    rel="stylesheet"
  />

  <PageTitle pageTitle="Submit Memorial" page />

  <div id="SubmitMemorial">
    <v-container fluid>
      <v-row justify="center" class="row bg-grey-lighten-3 text-md-center">
        <v-col cols="auto">
          <v-card elevation="5">
            <v-card-title class="text-wrap sub_memorial_css2">
              Please provide your information:
            </v-card-title>
          </v-card>
          <br />
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="first_name"
                  v-model="firstname"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="nameRules"
                  label="First Name*"
                  counter="50"
                  clearable
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="last_name"
                  v-model="lastname"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="nameRules"
                  label="Last Name*"
                  :counter="50"
                  clearable
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="youremail"
                  v-model="youremail"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="emailRules"
                  label="Email*"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="yzip"
                  v-model="yzip"
                  label="Zip*"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="zipRules"
                  counter="5"
                  clearable
                  required
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-card>
                  <v-list-item>
                    <!--                    <v-list-item-content>-->
                    <!--                      <v-list-item-title class="text-wrap, sub_memorial_css" style="text-align:left" >Did you lose anyone close to you due to Covid-19?</v-list-item-title>-->
                    <!--                    </v-list-item-content>-->
                    <v-list-item-action>
                      <v-checkbox
                        data-cy="covid_checkbox"
                        v-model="loss"
                        color="green"
                        label="Did you lose anyone close to you due to Covid-19?"
                      ></v-checkbox>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>
              <v-col cols="12" md="6">
                <v-card>
                  <v-list-item>
                    <!--                    <v-list-item-content>-->
                    <!--                      <v-list-item-title class="text-wrap, sub_memorial_css" style="text-align:left" >Are you affiliated with Marked By Covid?</v-list-item-title>-->
                    <!--                    </v-list-item-content>-->
                    <v-list-item-action>
                      <v-checkbox
                        data-cy="covid_aff_checkbox"
                        v-model="affiliated"
                        color="green"
                        label="Are you affiliated with Marked By Covid?"
                      ></v-checkbox>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-card elevation="5">
                  <v-card-title class="text-wrap sub_memorial_css2"
                    >Memorial Details:</v-card-title
                  >
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="4">
                <v-card>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap sub_memorial_css"
                        style="text-align: left"
                        >If you do not know the official name of the memorial,
                        please put a brief description (eg. “I-95 Roadside
                        Memorial”)*</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-textarea
                        data-cy="memorial_name"
                        auto-grow
                        clearable
                        v-model="memorialname"
                        variant="solo"
                        bg-color="grey-lighten-4"
                        class="sub_memorial_css"
                        :rules="memorialnameRules"
                        counter="256"
                        label="Memorial Name*"
                        required
                      ></v-textarea>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>

              <v-col cols="12" md="4">
                <v-card>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap sub_memorial_css"
                        style="text-align: left"
                        >Please provide a description of the memorial. (This may
                        include an artist’s statement or
                        rationale.)*</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-textarea
                        data-cy="memorial_description"
                        auto-grow
                        clearable
                        v-model="description"
                        variant="solo"
                        bg-color="grey-lighten-4"
                        class="sub_memorial_css"
                        type="description"
                        :rules="descriptionRules"
                        counter="4096"
                        label="Memorial Description*"
                        required
                      ></v-textarea>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>

              <v-col cols="12" md="4">
                <v-textarea
                  data-cy="founder_name"
                  v-model="foundername"
                  variant="solo"
                  class="sub_memorial_css"
                  bg-color="grey-lighten-4"
                  :rules="founderRulesNot"
                  counter="75"
                  label="Contact/Founder"
                  clearable
                ></v-textarea>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="12" md="12" lg="12">
                <v-card>
                  <v-list-item>
                    <!--                    <v-list-item-content>-->
                    <!--                      <v-list-item-title class="text-wrap, sub_memorial_css" style="text-align:left" >Is this memorial part of a Covid Memorial Day observance?</v-list-item-title>-->
                    <!--                    </v-list-item-content>-->
                    <v-list-item-action>
                      <v-checkbox
                        data-cy="covid_obs_checkbox"
                        v-model="observance"
                        color="green"
                        label="Is this memorial part of a Covid Memorial Day observance?"
                      ></v-checkbox>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-card>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap sub_memorial_css"
                        style="text-align: left"
                        >Please use the auto complete address field below or use
                        open map to enter the address</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <GMapAutocomplete
                        data-cy="mem_location"
                        @place_changed="setPlace"
                      >
                        <!-- <template v-slot:input="slotProps">
                    <v-text-field
                      ref="input"
                      v-bind="slotProps"
                      prepend-inner-icon="mdi-map-marker"
                      hide-details
                      clearable
                      @click:clear="clearAddress()"
                    />
                  </template> -->
                      </GMapAutocomplete>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="street"
                  v-model="street"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  label="Street Address"
                  clearable
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="4">
                <v-text-field
                  data-cy="city"
                  v-model="city"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  label="City"
                  clearable
                >
                </v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field
                  data-cy="state"
                  v-model="state"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  label="State"
                  clearable
                  persistent-hint
                  hint="Two Letter Code"
                >
                </v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field
                  data-cy="zip"
                  v-model="zip"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  label="Zip"
                  clearable
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md>
                <v-card class="overflow-y-auto">
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap sub_memorial_css"
                        style="text-align: left"
                        >If you do not know the street address, use this link to
                        drop a pin.</v-list-item-title
                      >
                    </v-list-item-content>
                    <br />
                    <v-list-item-action>
                      <v-btn
                        flat
                        @click="dialog = true"
                        color="green"
                        variant="outlined"
                        append-icon="mdi-google-maps"
                        >Open Map
                      </v-btn>
                      <v-dialog v-model="dialog" width="unset">
                        <v-card>
                          <v-card-text>
                            <LatLongPicker
                              @markerLat="getLatitude"
                              @markerLong="getLongitude"
                            />
                          </v-card-text>
                          <v-card-actions>
                            <v-btn color="primary" block @click="dialog = false"
                              >Please Pin & Click on Marker and Close
                              Dialog</v-btn
                            >
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12">
                <v-text-field
                  data-cy="mem_type"
                  v-model="mem_type"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  label="Type"
                  hint="Example: website, monument, plaque"
                  persistent-hint
                  clearable
                ></v-text-field>
              </v-col>
              <v-col cols="6" md="6">
                <v-checkbox
                  data-cy="vcheckbox"
                  v-model="vcheckbox"
                  class="sub_memorial_css"
                  color="green"
                  label="Virtual"
                ></v-checkbox>
              </v-col>
              <v-col cols="6" md="6">
                <v-checkbox
                  data-cy="temp_checkbox"
                  v-model="tempcheckbox"
                  class="sub_memorial_css"
                  color="green"
                  label="Temporary"
                ></v-checkbox>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="date"
                  v-model="date"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="dateRulesNot"
                  label="Memorial Start Date"
                  hint="MM/DD/YYYY"
                  persistent-hint
                >
                </v-text-field>

                <p style="font-family: 'Archivo Narrow', sans-serif">
                  Leave blank if unknown
                </p>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="end_date"
                  v-model="enddate"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="dateRulesNot"
                  label="Memorial End Date"
                  hint="MM/DD/YYYY"
                  persistent-hint
                ></v-text-field>
                <p style="font-family: 'Archivo Narrow', sans-serif">
                  Leave blank if not applicable
                </p>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="memorial_website"
                  v-model="memorialwebsite"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="[
                    (v) =>
                      !v || !v.trim() || this.isURL(v) || 'URL is not valid',
                  ]"
                  label="Website Link"
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="memorial_email"
                  v-model="memorialemail"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="emailRulesNot"
                  label="Email"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="memorial_profile_link"
                  v-model="memorialphoto"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="[
                    (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                  ]"
                  label="Profile Photo Link"
                  persistent-hint
                  hint="Add a profile photo link here"
                ></v-text-field>
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="virtual_tour"
                  v-model="virtualtour"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="[
                    (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                  ]"
                  label="Virtual Tour Link"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" md="4">
                <div
                  v-for="(item, index) in photoLinks"
                  :key="index"
                  class="d-flex"
                >
                  <v-text-field
                    data-cy="photo_links"
                    v-model="item.purl"
                    variant="solo"
                    bg-color="grey-lighten-4"
                    class="sub_memorial_css"
                    persistent-hint
                    hint="Add a photo link here"
                    label="Photo Link"
                    :rules="[
                      (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                    ]"
                  >
                  </v-text-field>
                  <v-icon
                    icon="mdi-close"
                    color="red"
                    @click="removePhotoLink(index)"
                    v-show="index != 0"
                  ></v-icon>
                </div>
                <v-btn
                  flat
                  border
                  elevation="0"
                  variant="outlined"
                  color="green"
                  prepend-icon="mdi-plus"
                  @click="addRow"
                  >Add Photo Link</v-btn
                >
              </v-col>

              <v-col cols="12" md="4">
                <div
                  v-for="(item, index) in videoLinks"
                  :key="index"
                  class="d-flex"
                >
                  <v-text-field
                    data-cy="video_links"
                    v-model="item.vurl"
                    variant="solo"
                    bg-color="grey-lighten-4"
                    class="sub_memorial_css"
                    persistent-hint
                    hint="Add a video link here"
                    label="Video Link"
                    :rules="[
                      (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                    ]"
                  >
                  </v-text-field>
                  <v-icon
                    icon="mdi-close"
                    color="red"
                    @click="removeVideoLink(index)"
                    v-show="index != 0"
                  ></v-icon>
                </div>
                <v-btn
                  flat
                  border
                  elevation="0"
                  variant="outlined"
                  color="green"
                  prepend-icon="mdi-plus"
                  @click="addvLink"
                  >Add Video Link</v-btn
                >
              </v-col>

              <v-col cols="12" md="4">
                <div
                  v-for="(item, index) in pressLinks"
                  :key="index"
                  class="d-flex"
                >
                  <v-text-field
                    data-cy="press_links"
                    v-model="item.pcurl"
                    variant="solo"
                    bg-color="grey-lighten-4"
                    class="sub_memorial_css"
                    persistent-hint
                    hint="Add a press coverage link here"
                    label="Press Coverage Link"
                    :rules="[
                      (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                    ]"
                  >
                  </v-text-field>
                  <v-icon
                    icon="mdi-close"
                    color="red"
                    @click="removePCLink(index)"
                    v-show="index != 0"
                  ></v-icon>
                </div>
                <v-btn
                  flat
                  border
                  elevation="0"
                  color="green"
                  variant="outlined"
                  prepend-icon="mdi-plus"
                  @click="addPCLink"
                  >Add Press Link</v-btn
                >
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="4">
                <v-text-field
                  data-cy="twitter"
                  v-model="twitter"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="[
                    (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                  ]"
                  label="Twitter"
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field
                  data-cy="instagram"
                  v-model="instagram"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="[
                    (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                  ]"
                  label="Instagram"
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field
                  data-cy="facebook"
                  v-model="facebook"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="sub_memorial_css"
                  :rules="[
                    (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                  ]"
                  label="Facebook"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row dense>
              <v-col cols="12" md="6">
                <v-card class="overflow-y-auto">
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap sub_memorial_css"
                        style="text-align: left"
                      >
                        I confirm that the information that I am submitting is
                        correct to the best of my knowledge*</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-checkbox
                        data-cy="first_checkbox"
                        v-model="firstcheckbox"
                        color="green"
                        class="sub_memorial_css"
                        :rules="[(v) => !!v || 'You must agree to continue!']"
                        label="Yes, I agree"
                        required
                      >
                      </v-checkbox>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>
              <v-col cols="12" md="6">
                <v-card class="overflow-y-auto">
                  <v-list-item>
                    <!--                    <v-list-item-content>-->
                    <!--                    <v-list-item-content>-->
                    <!--                    <v-checkbox data-cy="sec_checkbox" v-model="seccheckbox" color="green" class="text-wrap sub_memorial_css" label="I would like to receive email updates about the Memorial Matrix"></v-checkbox>-->
                    <!--                    </v-list-item-content>-->
                    <!--                      <v-list-item-title class="text-wrap sub_memorial_css" style="text-align:left" >I would like to receive email updates about the Memorial Matrix</v-list-item-title>-->
                    <!--                    </v-list-item-content>-->
                    <v-list-item-action>
                      <v-checkbox
                        data-cy="sec_checkbox"
                        v-model="seccheckbox"
                        color="green"
                        class="sub_memorial_css"
                        label="I would like to receive email updates about the Memorial Matrix"
                      ></v-checkbox>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>
            </v-row>

            <v-btn
              data-cy="review"
              class="purple darken-2 white--text mt-5"
              color="green"
              @click="submitForm"
            >
              <h3
                style="
                  text-align: center;
                  font-family: 'Archivo Narrow', sans-serif;
                "
              >
                Review
              </h3>
            </v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import { APIService } from "../http/APIService";
import LatLongPicker from "@/components/LatLongPicker.vue";
import PageTitle from "@/components/PageTitle.vue";
const apiService = new APIService();
export default {
  name: "SubmitMemorialView",
  components: {
    PageTitle,
    LatLongPicker,
  },
  data: (vm) => ({
    firstname: "",
    lastname: "",
    youremail: "",
    yzip: "",
    loss: false,
    observance: false,
    affiliated: false,
    counter: 0,
    memorialname: "",
    foundername: "",
    street: "",
    city: "",
    state: "",
    zip: "",
    description: "",
    mem_type: "",
    memorialphoto: "",
    urlstring: "",
    memorialwebsite: "",
    memorialemail: "",
    virtualtour: "",
    photolinks: "",
    video: "",
    press: "",
    twitter: "",
    instagram: "",
    facebook: "",
    firstcheckbox: false,
    seccheckbox: false,
    vcheckbox: false,
    tempcheckbox: false,
    dialog: false,
    latitude: "",
    longitude: "",
    date: null,
    photoLinks: [{ purl: "" }],
    videoLinks: [{ vurl: "" }],
    pressLinks: [{ pcurl: "" }],

    enddate: null,
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length <= 50) || "Name must be less than 50 characters",
    ],
    zipRules: [
      (v) => !!v || "Zip is required",
      (v) => /^\d{5}$/.test(v) || "Zip must be 5 digits",
    ],
    memorialnameRules: [
      (v) => !!v || "Memorial name is required",
      (v) => (v && v.length <= 256) || "Name must be less than 256 characters",
    ],
    founderRulesNot: [
      (v) =>
        !v.trim() ||
        (v && v.length <= 75) ||
        "Name must be less than 75 characters",
    ],
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) =>
        /^(([^<>()[\]\\.,;:\s@']+(\.[^<>()\\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          v
        ) || "E-mail must be valid",
    ],
    emailRulesNot: [
      (v) =>
        !v ||
        !v.trim() ||
        /^(([^<>()[\]\\.,;:\s@']+(\.[^<>()\\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          v
        ) ||
        "E-mail must be valid",
    ],
    dateRulesNot: [
      // (0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2}$  --the strict regexp for mm/dd/yyyy date
      // (v) => ( /^\d{1,2}\/\d{1,2}\/\d{4}$ --just digit,digit/digit,digit/digit,digit,digit,digit
      (v) =>
        !v ||
        !v.trim() ||
        /^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2}$/.test(v) ||
        "MM/DD/YYYY format required",
    ],
    descriptionRules: [
      (v) => !!v || "Description is required",
      (v) =>
        (v && v.length <= 4096) ||
        "Description must be less than 4096 characters",
    ],

    //
    //Need to get this fixed--using inline rule for now: tried identical format as inline
    //urlRulesNot: [
    //    (v) => (!v.trim()) ||
    //    this.isURL(v)) || "URL is not valid",
    //],

    urlRules: [
      (v) => !!v || "Required.",
      (v) => this.isURL(v) || "URL is not valid",
    ],

    id: 1,
    id1: 1,
    id2: 1,
  }),
  mounted() {
    const formData = JSON.parse(window.localStorage.getItem("formData"));
    const mediaData = JSON.parse(window.localStorage.getItem("mediaData"));
    const isRedirectedFromReview = JSON.parse(
      window.localStorage.getItem("isRedirectedFromReview")
    );
    if (isRedirectedFromReview) {
      if (formData) {
        this.firstname = formData.mem_submitter.first_name;
        this.lastname = formData.mem_submitter.last_name;
        this.youremail = formData.mem_submitter.email;
        this.yzip = formData.mem_submitter.zipcode;
        this.loss = formData.mem_submitter.web_user_loss;
        this.affiliated = formData.mem_submitter.web_user_affiliated;
        this.seccheckbox = formData.mem_submitter.email_updates;
        this.memorialname = formData.name;
        this.description = formData.description;
        this.foundername = formData.founder_name;
        this.memorialwebsite = formData.website;
        this.memorialphoto = formData.profile_picture;
        this.virtualtour = formData.google_virtual_tour;
        this.memorialemail = formData.email;
        this.observance = formData.memorial_day_observance;
        this.mem_type = formData.memorial_type_desc;
        this.facebook = formData.social_media_facebook;
        this.instagram = formData.social_media_instagram;
        this.twitter = formData.social_media_twitter;
        this.firstcheckbox = formData.confirm_data_accuracy;
        this.vcheckbox = formData.type == "virtual" ? true : false;
        this.tempcheckbox =
          formData.mem_location.permanent == "temporary" ? true : false;
        let month,
          day,
          year = "";
        formData.mem_location.time_active_start !== null
          ? ([year, month, day] =
              formData.mem_location.time_active_start.split("-"))
          : console.log("start date empty");
        if (
          formData.mem_location.time_active_start !== null &&
          formData.mem_location.time_active_start !== ""
        ) {
          this.date = `${month.padStart(2, "0")}/${day.padStart(
            2,
            "0"
          )}/${year}`;
          console.log(`Reformatted start date is ${this.date}`);
        } else {
          console.log("start date still empty :-/");
        }
        formData.mem_location.time_active_end !== null
          ? ([year, month, day] =
              formData.mem_location.time_active_end.split("-"))
          : console.log("end date empty");
        if (
          formData.mem_location.time_active_end !== null &&
          formData.mem_location.time_active_end !== ""
        ) {
          this.enddate = `${month.padStart(2, "0")}/${day.padStart(
            2,
            "0"
          )}/${year}`;
          console.log(`Reformatted end date is ${this.enddate}`);
        } else {
          console.log("end date still empty :-/");
        }
        this.street = formData.mem_location.address;
        this.state = formData.mem_location.state;
        this.city = formData.mem_location.city;
        this.zip = formData.mem_location.zipcode;
        this.latitude = formData.mem_location.lat_coord;
        this.longitude = formData.mem_location.long_coord;
      }
      if (mediaData) {
        this.photoLinks = mediaData.photoLinks;
        this.videoLinks = mediaData.videoLinks;
        this.pressLinks = mediaData.pressLinks;
      }
      window.localStorage.removeItem("isRedirectedFromReview");
    }
  },
  methods: {
    setPlace(e) {
      console.log(e);
      this.latitude = e.geometry.location.lat();
      this.longitude = e.geometry.location.lng();
      for (const component of e.address_components) {
        const componentType = component.types[0];
        switch (componentType) {
          case "street_number": {
            this.street = `${component.long_name}`;
            break;
          }

          case "route": {
            this.street += " " + component.short_name;
            break;
          }
          case "postal_code": {
            this.zip = `${component.long_name}`;
            break;
          }
          case "locality":
            this.city = component.long_name;
            break;
          case "administrative_area_level_1": {
            this.state = component.short_name;
            break;
          }
          case "country":
            this.country = component.long_name;
            break;
        }
      }
    },
    clearAddress() {
      this.street = "";
      this.city = "";
      this.state = "";
      this.zip = "";
      this.latitude = "";
      this.longitude = "";
    },
    clearCheckAndForm() {
      this.loss = false;
      this.observance = false;
      this.affiliated = false;
      this.firstcheckbox = false;
      this.seccheckbox = false;
      this.vcheckbox = false;
      this.tempcheckbox = false;
      this.date = "";
      this.enddate = "";
    },

    getLatitude(value) {
      this.latitude = value;
    },
    getLongitude(value) {
      this.longitude = value;
    },

    removePhotoLink(index) {
      this.photoLinks.splice(index, 1);
    },

    removeVideoLink(index) {
      this.videoLinks.splice(index, 1);
    },

    removePCLink(index) {
      this.pressLinks.splice(index, 1);
    },

    addRow() {
      this.photoLinks.push({
        purl: "",
      });
    },

    addvLink() {
      this.videoLinks.push({
        vurl: "",
      });
    },

    addPCLink() {
      this.pressLinks.push({
        pcurl: "",
      });
    },
    isURL(str) {
      let url;

      try {
        url = new URL(str);
      } catch (_) {
        return false;
      }

      return url.protocol === "http:" || url.protocol === "https:";
    },

    async submitForm() {
      this.$refs.form.validate();
      // There has to be a check about null on save
      // Null error being returned when these are clearable
      // in the form fields and left null
      if (this.street === null) {
        this.street = "";
      }
      if (this.city === null) {
        this.city = "";
      }
      if (this.state === null) {
        this.state = "";
      }
      if (this.zip === null) {
        this.zip = "";
      }
      let month,
        day,
        year = "";
      let formStartStrDate = null;
      let formEndStrDate = null;
      this.date !== null
        ? ([month, day, year] = this.date.split("/"))
        : console.log("start date empty");
      if (this.date !== null && this.date !== "") {
        formStartStrDate = `${year}-${month.padStart(2, "0")}-${day.padStart(
          2,
          "0"
        )}`;
        // this.date = formStrDate;
      } else {
        console.log("start date still empty :-/");
      }
      this.enddate !== null
        ? ([month, day, year] = this.enddate.split("/"))
        : console.log("end date empty");
      if (this.enddate !== null && this.enddate !== "") {
        // let month, day, year = "";
        // [month, day, year] = this.enddate.split("/")
        formEndStrDate = `${year}-${month.padStart(2, "0")}-${day.padStart(
          2,
          "0"
        )}`;
        // this.enddate = formStrDate;
      } else {
        console.log("end date still empty :-/");
      }

      let vtype = !this.vcheckbox ? "physical" : "virtual";

      let locationPerm = !this.tempcheckbox ? "permanent" : "temporary";
      window.localStorage.setItem(
        "formData",
        JSON.stringify({
          mem_submitter: {
            first_name: this.firstname,
            last_name: this.lastname,
            email: this.youremail,
            zipcode: this.yzip,
            web_user_loss: this.loss,
            web_user_affiliated: this.affiliated,
            email_updates: this.seccheckbox,
          },
          name: this.memorialname,
          memorial_day_observance: this.observance,
          description: this.description,
          founder_name: this.foundername,
          website: this.memorialwebsite,
          profile_picture: this.memorialphoto,
          google_virtual_tour: this.virtualtour,
          email: this.memorialemail,
          type: vtype,
          memorial_type_desc: this.mem_type,
          social_media_facebook: this.facebook,
          social_media_instagram: this.instagram,
          social_media_twitter: this.twitter,
          confirm_data_accuracy: this.firstcheckbox,

          mem_location: {
            address: this.street,
            city: this.city,
            state: this.state,
            zipcode: this.zip,
            permanent: locationPerm,
            time_active_start: formStartStrDate,
            time_active_end: formEndStrDate,
            lat_coord: this.latitude,
            long_coord: this.longitude,
          },
        })
      );

      window.localStorage.setItem(
        "mediaData",
        JSON.stringify({
          photoLinks: this.photoLinks,
          videoLinks: this.videoLinks,
          pressLinks: this.pressLinks,
        })
      );
      this.$refs.form.validate().then((result) => {
        if (result.valid) {
          this.$router.push({ name: "reviewmemorial" });
        }
      });
    },
  },
};
</script>
<style>
#app {
  /*font-family: "Avenir", Helvetica, Arial, sans-serif;*/
  font-family: "Archivo Narrow", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.sub_memorial_css {
  font-family: "Archivo Narrow", sans-serif;
}
.sub_memorial_css2 {
  font-family: "Archivo Black", sans-serif;
}
</style>
