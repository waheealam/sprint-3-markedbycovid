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

  <div id="ModifyMemorial">
    <v-container fluid>
      <v-row justify="center" class="row">
        <v-col cols="auto">
          <v-card elevation="5">
            <v-card-title class="text-wrap mod_memorial_css2">
              Please provide your information:
            </v-card-title>
          </v-card>
          <br />
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-row>
              <v-col cols="2" md="6">
                <v-text-field
                  data-cy="mod_first_name"
                  v-model="firstname"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
                  :rules="nameRules"
                  label="First Name*"
                  counter="50"
                  clearable
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="mod_last_name"
                  v-model="lastname"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
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
                  data-cy="mod_youremail"
                  v-model="youremail"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
                  :rules="emailRules"
                  label="Email*"
                  clearable
                  required
                >
                </v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="mod_yzip"
                  v-model="yzip"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
                  label="Zip*"
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
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap, sub_memorial_css"
                        style="text-align: left"
                        >Did you lose anyone close to you due to
                        Covid-19?</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-checkbox
                        data-cy="covid_checkbox"
                        v-model="loss"
                        color="green"
                        label="Yes"
                      ></v-checkbox>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>
              <v-col cols="12" md="6">
                <v-card>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap, sub_memorial_css"
                        style="text-align: left"
                        >Are you affiliated with Marked By
                        Covid?</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-checkbox
                        data-cy="covid_aff_checkbox"
                        v-model="affiliated"
                        color="green"
                        label="Yes"
                      ></v-checkbox>
                      <v-checkbox
                        data-cy="mod_covid_checkbox"
                        v-model="loss"
                        color="green"
                        label="Yes"
                      ></v-checkbox>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-card elevation="5">
                  <v-card-title class="text-wrap mod_memorial_css2"
                    >Information about the Memorial:</v-card-title
                  >
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="4">
                <v-card outlined>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap mod_memorial_css"
                        style="text-align: left"
                        >If you do not know the official name of the memorial,
                        please put a brief description (eg. “I-95 Roadside
                        Memorial”)*</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-textarea
                        data-cy="mod_memorial_name"
                        auto-grow
                        clearable
                        v-model="memorialname"
                        variant="solo"
                        bg-color="grey-lighten-4"
                        class="mod_memorial_css"
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
                <v-card outlined>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap mod_memorial_css"
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
                        class="mod_memorial_css"
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
                  data-cy="mod_founder_name"
                  v-model="foundername"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
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
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap, sub_memorial_css"
                        style="text-align: left"
                        >Is this memorial part of a Covid Memorial Day
                        observance?</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-checkbox
                        data-cy="covid_obs_checkbox"
                        v-model="observance"
                        color="green"
                        label="Yes"
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
                        class="text-wrap mod_memorial_css"
                        style="text-align: left"
                        >Please use the auto complete address field below or use
                        open map to the enter address</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <GMapAutocomplete
                        data-cy="mod_mem_location"
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
                  class="mod_memorial_css"
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
                  class="mod_memorial_css"
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
                  class="mod_memorial_css"
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
                  class="mod_memorial_css"
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
                        class="text-wrap mod_memorial_css"
                        style="text-align: left"
                        >If you do not know the street address, use this link to
                        drop a pin.</v-list-item-title
                      >
                    </v-list-item-content>
                    <br />
                    <v-list-item-action>
                      <v-btn
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
                  data-cy="mod_mem_type"
                  v-model="mem_type"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
                  label="Type"
                  hint="Example: web site, monument, plaque"
                  persistent-hint
                ></v-text-field>
              </v-col>
              <v-col cols="6" md="6">
                <v-checkbox
                  data-cy="mod_vcheckbox"
                  v-model="vcheckbox"
                  color="green"
                  label="Virtual"
                ></v-checkbox>
              </v-col>
              <v-col cols="6" md="6">
                <v-checkbox
                  data-cy="mod_temp_checkbox"
                  v-model="tempcheckbox"
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
                  class="mod_memorial_css"
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
                  class="mod_memorial_css"
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
                  data-cy="mod_memorial_website"
                  v-model="memorialwebsite"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
                  :rules="[
                    (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                  ]"
                  label="Website Link"
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="mod_memorial_email"
                  v-model="memorialemail"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
                  :rules="emailRulesNot"
                  label="Email"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  data-cy="mod_memorial_profile_link"
                  v-model="memorialphoto"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
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
                  data-cy="mod_virtual_tour"
                  v-model="virtualtour"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
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
                    data-cy="mod_photo_links"
                    v-model="item.purl"
                    label="Photo Link"
                    persistent-hint
                    hint="Add a photo link here"
                    variant="solo"
                    bg-color="grey-lighten-4"
                    class="mod_memorial_css"
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
                  border
                  elevation="0"
                  color="green"
                  variant="outlined"
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
                    data-cy="mod_video_links"
                    v-model="item.vurl"
                    label="Video Link"
                    persistent-hint
                    hint="Add a video link here"
                    variant="solo"
                    bg-color="grey-lighten-4"
                    class="mod_memorial_css"
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
                  border
                  elevation="0"
                  color="green"
                  variant="outlined"
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
                    data-cy="mod_press_links"
                    v-model="item.pcurl"
                    label="Press Coverage Link"
                    persistent-hint
                    hint="Add a press coverage link here"
                    variant="solo"
                    bg-color="grey-lighten-4"
                    class="mod_memorial_css"
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
                  data-cy="mod_twitter"
                  v-model="twitter"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
                  :rules="[
                    (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                  ]"
                  label="Twitter"
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field
                  data-cy="mod_instagram"
                  v-model="instagram"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
                  :rules="[
                    (v) => !v.trim() || this.isURL(v) || 'URL is not valid',
                  ]"
                  label="Instagram"
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field
                  data-cy="mod_facebook"
                  v-model="facebook"
                  variant="solo"
                  bg-color="grey-lighten-4"
                  class="mod_memorial_css"
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
                        class="text-wrap mod_memorial_css"
                        style="text-align: left"
                      >
                        I confirm that the information that I am submitting is
                        correct to the best of my knowledge*</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-checkbox
                        data-cy="mod_first_checkbox"
                        v-model="firstcheckbox"
                        color="green"
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
                    <v-list-item-content>
                      <v-list-item-title
                        class="text-wrap mod_memorial_css"
                        style="text-align: left"
                        >I would like to receive email updates about the
                        Memorial Matrix</v-list-item-title
                      >
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-checkbox
                        data-cy="mod_sec_checkbox"
                        v-model="seccheckbox"
                        color="green"
                        label="Yes, I agree"
                      ></v-checkbox>
                    </v-list-item-action>
                  </v-list-item>
                </v-card>
              </v-col>
            </v-row>

            <v-btn
              data-cy="update"
              class="purple darken-2 white--text mt-5"
              color="blue"
              @click="modifyForm"
            >
              <h3
                style="
                  text-align: center;
                  font-family: 'Archivo Narrow', sans-serif;
                "
              >
                Update
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
const apiService = new APIService();
export default {
  name: "ModifyMemorialView",
  components: {
    LatLongPicker,
  },
  data: (vm) => ({
    mem_submitter_id: "",
    mem_location_id: "",
    firstname: "",
    lastname: "",
    youremail: "",
    yzip: "",
    loss: false,
    affiliated: false,
    observance: false,
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
    pFlag: true,
    vFlag: true,
    pcFlag: true,
  }),

  created() {
    this.getData(this.$route.params.id);
    this.getMedia();
  },
  methods: {
    setPlace(e) {
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
      this.affiliated = false;
      this.observance = false;
      this.firstcheckbox = false;
      this.seccheckbox = false;
      this.vcheckbox = false;
      this.tempcheckbox = false;
      this.dialog = false;
      this.date = "";
      this.enddate = "";
      this.menu1 = false;
      this.menu2 = false;
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
    async getData(id) {
      let id2 = localStorage.getItem("id");
      apiService.getMemorialView(id2).then((resp) => {
        this.mem_location_id = resp.data.mem_location.id;
        this.memorialname = resp.data.name;
        this.observance = resp.data.memorial_day_observance;
        this.foundername = resp.data.founder_name;
        this.description = resp.data.description;
        this.street = resp.data.mem_location.address;
        this.city = resp.data.mem_location.city;
        this.state = resp.data.mem_location.state;
        this.zip = resp.data.mem_location.zipcode;
        this.latitude = resp.data.mem_location.lat_coord;
        this.longitude = resp.data.mem_location.long_coord;
        this.mem_type = resp.data.memorial_type_desc;
        this.vcheckbox = resp.data.type === "virtual";
        this.tempcheckbox = resp.data.mem_location.permanent === "temporary";
        this.date = resp.data.mem_location.time_active_start;
        //Remember, date comes back in YYYY-MM_DD format
        let month,
          day,
          year = "";
        let formStrDate,
          ddmmyyyyStrDate = "";
        this.date !== null
          ? ([year, month, day] = this.date.split("-"))
          : console.log("start date empty");
        if (this.date !== null) {
          formStrDate = `${year}-${month.padStart(2, "0")}-${day.padStart(
            2,
            "0"
          )}`;
          console.log(
            `the date back from db ${this.date} and parsed date ${formStrDate}`
          );
          ddmmyyyyStrDate = `${month.padStart(2, "0")}/${day.padStart(
            2,
            "0"
          )}/${year}`;
          this.date = ddmmyyyyStrDate;
        } else {
          console.log("start date still empty :-/");
        }
        this.enddate = resp.data.mem_location.time_active_end;
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
        resp.data.website
          ? (this.memorialwebsite = resp.data.website)
          : (this.memorialwebsite = "");
        this.memorialemail = resp.data.email;
        this.memorialphoto = resp.data.profile_picture;
        this.virtualtour = resp.data.google_virtual_tour;
        this.twitter = resp.data.social_media_twitter;
        this.facebook = resp.data.social_media_facebook;
        this.instagram = resp.data.social_media_instagram;
      });
      //fix date
      //Remember, date comes back in YYYY-MM-DD format
      let month,
        day,
        year = "";
      let formStrDate,
        ddmmyyyyStrDate = "";
      this.date !== null
        ? ([year, month, day] = this.date.split("-"))
        : console.log("start date empty");
      if (this.date !== null) {
        formStrDate = `${year}-${month.padStart(2, "0")}-${day.padStart(
          2,
          "0"
        )}`;
        ddmmyyyyStrDate = `${month.padStart(2, "0")}/${day.padStart(
          2,
          "0"
        )}/${year}`;
        this.date = ddmmyyyyStrDate;
      } else {
        console.log("start date still empty :-/");
      }
      this.enddate = this.parseSlashDate;
    },
    async getMedia() {
      let id = localStorage.getItem("id");
      apiService.getMediaLinksView(id).then((resp) => {
        //this.memorialphoto = resp.data.data[0].url
        for (let i = 0; i < resp.data.length; i++) {
          if (resp.data[i].type == "photo") {
            if (this.pFlag) {
              this.photoLinks[0].purl = resp.data[i].url;
              this.pFlag = false;
              continue;
            }
            this.photoLinks.push({
              purl: resp.data[i].url,
            });
          }
          if (resp.data[i].type == "video") {
            if (this.vFlag) {
              this.videoLinks[0].vurl = resp.data[i].url;
              this.vFlag = false;
              continue;
            }
            this.videoLinks.push({
              vurl: resp.data[i].url,
            });
          }
          if (resp.data[i].type == "press coverage") {
            if (this.pcFlag) {
              this.pressLinks[0].pcurl = resp.data[i].url;
              this.pcFlag = false;
              continue;
            }
            this.pressLinks.push({
              pcurl: resp.data[i].url,
            });
          }
        }
      });
    },

    async modifyForm() {
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
      let id2 = localStorage.getItem("id");
      let month,
        day,
        year = "";
      let formStrDate = "";
      this.date !== null
        ? ([month, day, year] = this.date.split("/"))
        : console.log("start date empty");
      if (this.date !== null) {
        formStrDate = `${year}-${month.padStart(2, "0")}-${day.padStart(
          2,
          "0"
        )}`;
        this.date = formStrDate;
      } else {
        console.log("start date still empty :-/");
      }

      this.enddate !== null
        ? ([month, day, year] = this.enddate.split("/"))
        : console.log("end date empty");
      if (this.enddate !== null) {
        // let month, day, year = "";
        // [month, day, year] = this.enddate.split("/")
        formStrDate = `${year}-${month.padStart(2, "0")}-${day.padStart(
          2,
          "0"
        )}`;
        this.enddate = formStrDate;
      } else {
        console.log("end date still empty :-/");
      }
      let vtype = !this.vcheckbox ? "physical" : "virtual";
      let locationPerm = !this.tempcheckbox ? "permanent" : "temporary";
      let memorial_id;
      const API_URL = process.env.VUE_APP_API_ENDPOINT;
      let url = API_URL + "api/update/" + id2 + "/";
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.xsrfHeaderName = "X-CSRFToken";
      await axios
        .put(url, {
          mem_submitter: {
            first_name: this.firstname,
            last_name: this.lastname,
            email: this.youremail,
            zipcode: this.yzip,
            web_user_loss: this.loss,
            web_user_affiliated: this.affiliated,
            email_updates: this.seccheckbox,
          },
          id: id2,
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
            time_active_start: this.date,
            time_active_end: this.enddate,
            lat_coord: this.latitude,
            long_coord: this.longitude,
          },
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          this.clearCheckAndForm();
        });
      let mediaurl = API_URL + "api/medialinkUpdate/";
      await axios
        .put(mediaurl, {
          photoLinks: this.photoLinks,
          videoLinks: this.videoLinks,
          pressLinks: this.pressLinks,
          memorial: id2,
        })
        .then((response) => {
          this.$refs.form.reset();
          this.$router.push({ name: "memorialsaved" });
        })
        .catch((error) => {
          this.clearCheckAndForm();
        });
    },
    parseDashDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${month}/${day}/${year}`;
    },
    parseSlashDate(date) {
      if (!date) return null;
      const [month, day, year] = date.split("/");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    },
  },
};
</script>

<style>
.mod_memorial_css {
  font-family: "Archivo Narrow", sans-serif;
}
.mod_memorial_css2 {
  font-family: "Archivo Black", sans-serif;
}
</style>
