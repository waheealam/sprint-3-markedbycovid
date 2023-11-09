<template>
  <v-container fluid>
    <v-row justify="center" class="row">
      <v-col cols="12">
        <v-form ref="contactusForm" v-model="valid" lazy-validation>
          <v-row>
            <v-col cols="12" md="6">
              <v-text-field
                data-cy="first_name"
                v-model="firstname"
                :rules="firstNameRules"
                label="First Name*"
                prepend-inner-icon="mdi-account"
                counter="50"
                clearable
                required
              >
              </v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field
                data-cy="last_name"
                v-model="lastname"
                :rules="lastNameRules"
                label="Last Name*"
                prepend-inner-icon="mdi-account"
                counter="50"
                clearable
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
              <v-select
                data-cy="inquiry_type"
                v-model="inquirytype"
                label="Inquiry Type*"
                :items="inquiryItems"
                :rules="inquiryTypeRules"
              ></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
              <v-text-field
                data-cy="email_id"
                v-model="youremail"
                :rules="emailRules"
                label="Email*"
                prepend-inner-icon="mdi-email"
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
              <v-card outlined>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title
                      class="text-wrap"
                      style="text-align: left"
                      >Please enter your message here</v-list-item-title
                    >
                  </v-list-item-content>
                  <v-list-item-action>
                    <v-textarea
                      auto-grow
                      clearable
                      data-cy="message"
                      v-model="yourmessage"
                      :rules="messageRules"
                      counter=""
                      label="Message*"
                      required
                    ></v-textarea>
                  </v-list-item-action>
                </v-list-item>
              </v-card>
            </v-col>
          </v-row>
          <v-btn
            size="x-large"
            color="blue"
            class="mt-5"
            data-cy="Submit"
            @click="submitMesssage"
          >
            <h3 style="text-align: center; font-family: Verdana, sans-serif">
              Submit
            </h3>
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import { APIService } from "../http/APIService";
const apiService = new APIService();
export default {
  name: "ContactUs",
  data: (vm) => ({
    firstname: "",
    lastname: "",
    inquirytype: "General Inquiry",
    youremail: "",
    yourmessage: "",
    inquiryItems: ["General Inquiry", "Media Inquiry", "Research Inquiry"],
    firstNameRules: [
      (v) => !!v || "First name is required",
      (v) =>
        (v && v.length <= 50) || "First name must be less than 50 characters",
    ],

    lastNameRules: [
      (v) => !!v || "Last name is required",
      (v) =>
        (v && v.length <= 50) || "Last name must be less than 50 characters",
    ],

    inquiryTypeRules: [
      (v) => !!v || "Inquiry Type is required",
      (v) => v.length > 0 || "Select one Inquiry Type",
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

    messageRules: [
      (v) => !!v || "Message is required",
      (v) =>
        (v && v.length <= 4096) ||
        "Description must be less than 4096 characters",
    ],
  }),
  methods: {
    async submitMesssage() {
      if (this.$refs.contactusForm.validate()) {
        const API_URL = process.env.VUE_APP_API_ENDPOINT;
        let url = API_URL + "api/contactus/";
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.xsrfHeaderName = "X-CSRFToken";
        await axios
          .post(url, {
            first_name: this.firstname,
            last_name: this.lastname,
            inquiry: this.inquirytype,
            email: this.youremail,
            message: this.yourmessage,
          })
          .then((response) => {
            console.log(response);
            this.$refs.contactusForm.reset();
            this.$router.push({ name: "contactussaved" });
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style lang="css" scoped></style>
