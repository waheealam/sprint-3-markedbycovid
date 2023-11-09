<template>
  <div class="faq-page">
    <PageTitle pageTitle="Frequently Asked Questions" />
    <v-container fluid>
      <v-row>
        <v-col v-for="(faq, index) in faqs" :key="index" cols="12">
          <v-card elevation="3" class="faq-card" outlined tile raised>
            <v-card-title
              class="faq-question"
              v-on:click="faq.expanded = !faq.expanded"
              style="white-space: pre-wrap"
            >
              {{ faq.value.question }}
              <v-icon v-if="!faq.expanded">mdi-chevron-down</v-icon>
              <v-icon v-if="faq.expanded">mdi-chevron-up</v-icon>
            </v-card-title>
            <v-expand-transition>
              <v-card-text
                class="faq-answer"
                v-if="faq.expanded"
                v-html="faq.value.answer"
              ></v-card-text>
            </v-expand-transition>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import { APIService } from "@/http/APIService";
import PageTitle from "@/components/PageTitle.vue";
const apiService = new APIService();
export default {
  name: "FaqPage",
  components: { PageTitle },
  data() {
    return {
      faqs: [],
    };
  },
  mounted() {
    this.getFaqs();
  },
  created() {
    this.getFaqs();
  },
  methods: {
    async getFaqs() {
      apiService
        .getFaqPageContent()
        .then((response) => {
          this.faqs = response.data.items[0].questions;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.faq-card {
  padding: 0px;
}

.faq-question {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 0px;
}

.faq-answer {
  font-size: 16px;
  line-height: 1.5;
}
</style>
