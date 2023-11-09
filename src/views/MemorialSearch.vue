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

  <PageTitle pageTitle="Search Memorials" />
  <v-form @submit.prevent="memorialSearch">
    <v-row>
      <v-col cols="12" md="2">
        <v-text-field
          data-cy="searchName"
          class="text-h3"
          label="Name"
          v-model="searchName"
          hide-details
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2">
        <v-text-field
          data-cy="searchFounderName"
          label="Founder Name"
          v-model="searchFounderName"
          hide-details
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2">
        <v-text-field
          data-cy="searchCity"
          label="City"
          v-model="searchCity"
          hide-details
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2">
        <v-text-field
          data-cy="searchState"
          label="State"
          v-model="searchState"
          hide-details
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2">
        <v-text-field
          data-cy="searchZip"
          label="Zipcode"
          v-model="searchZip"
          hide-details
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2">
        <v-text-field
          data-cy="searchType"
          label="Memorial Type"
          v-model="searchType"
          hide-details
          clearable
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" md="2">
        <v-text-field
          data-cy="searchStartDate"
          label="Start Date"
          v-model="searchStartDate"
          hide-details
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2">
        <v-text-field
          data-cy="searchEndDate"
          label="End Date"
          v-model="searchEndDate"
          hide-details
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2" align-self="center">
        <v-btn data-cy="searchButton" color="blue" type="submit">Search</v-btn>
      </v-col>
      <v-col
        cols="12"
        md="6"
        align="right"
        align-self="end"
        class="text-subtitle-2 font-weight-medium"
      >
        {{ pagingMessage }}
      </v-col>
    </v-row>
  </v-form>

  <br />
  <v-divider />

  <v-table class="mem_search_css">
    <thead class="bg-grey-lighten-2">
      <tr>
        <th class="text-left mem_search_css">Name</th>
        <th class="text-left mem_search_css">Founder Name</th>
        <th class="text-left mem_search_css">City</th>
        <th class="text-left mem_search_css">State</th>
        <th class="text-left mem_search_css">Zipcode</th>
        <th class="text-left mem_search_css">Memorial Type</th>
        <th class="text-left mem_search_css" @click="sortByStartDate">
          Start Date
          <span v-if="sortBy !== 'start_date'">&#8693;</span>
          <span v-if="sortOrder === 'asc' && sortBy === 'start_date'"
            >&uarr;</span
          >
          <span v-if="sortOrder === 'desc' && sortBy === 'start_date'"
            >&darr;</span
          >
        </th>
        <th class="text-left mem_search_css" @click="sortByEndDate">
          End Date
          <span v-if="sortBy !== 'end_date'">&#8693;</span>
          <span v-if="sortOrder === 'asc' && sortBy === 'end_date'"
            >&uarr;</span
          >
          <span v-if="sortOrder === 'desc' && sortBy === 'end_date'"
            >&darr;</span
          >
        </th>
        <th class="text-left mem_search_css">Options</th>
      </tr>
    </thead>
    <tbody v-if="filteredData.length > 0">
      <tr v-for="memorialLists in filteredData" :key="memorialLists.id">
        <td class="mem_search_css2">
          <router-link
            :to="{ name: 'memorialdetail', params: { id: memorialLists.id } }"
          >
            {{ memorialLists.name }}
          </router-link>
        </td>
        <td class="mem_search_css2">{{ memorialLists.founder_name }}</td>
        <td class="mem_search_css2">
          {{ memorialLists.mem_location && memorialLists.mem_location.city }}
        </td>
        <td class="mem_search_css2">
          {{ memorialLists.mem_location && memorialLists.mem_location.state }}
        </td>
        <td class="mem_search_css2">
          {{ memorialLists.mem_location && memorialLists.mem_location.zipcode }}
        </td>
        <td class="mem_search_css2">{{ memorialLists.type }}</td>
        <td class="mem_search_css2">
          {{
            memorialLists.mem_location &&
            memorialLists.mem_location.time_active_start
          }}
        </td>
        <td class="mem_search_css2">
          {{
            memorialLists.mem_location &&
            memorialLists.mem_location.time_active_end
          }}
        </td>
        <td>
          <div>
            <router-link
              :to="{ name: 'memorialdetail', params: { id: memorialLists.id } }"
            >
              <v-btn
                data-cy="view"
                size="small"
                variant="elevated"
                color="green"
                class="mem_search_css2"
                @click="setpk(memorialLists.id)"
                >View</v-btn
              >
            </router-link>
            <router-link :to="{ name: 'updatememorial' }">
              <v-btn
                data-cy="edit"
                size="small"
                variant="elevated"
                color="green"
                class="mem_search_css2"
                @click="setpk(memorialLists.id)"
                >Edit</v-btn
              >
            </router-link>
          </div>
        </td>
      </tr>
    </tbody>
  </v-table>

  <v-divider />
  <br />

  <div>
    <v-row>
      <v-col cols="2">
        <v-select
          class="select"
          v-model="pageSize"
          :items="computePageSizes"
          label="Items Per Page"
          @update:modelValue="handlePageSizeChange"
        ></v-select>
      </v-col>
      <v-col>
        <v-pagination
          class="pagination pl-2"
          v-model="page"
          :length="totalPages"
          total-visible="7"
          next-icon="mdi-menu-right"
          prev-icon="mdi-menu-left"
          @update:modelValue="handlePageChange"
        ></v-pagination>
      </v-col>
    </v-row>
  </div>
  <div v-if="filteredData.length < 1" class="text-center mt-2">
    There is no data found!
  </div>
</template>
<script>
import { computed } from "@vue/runtime-core";
import { APIService } from "@/http/APIService";
import PageTitle from "@/components/PageTitle.vue";
const apiService = new APIService();
export default {
  name: "MemorialSearch",
  components: { PageTitle },
  data: () => ({
    memorialList: [],
    searchName: "",
    searchFounderName: "",
    searchCity: "",
    searchState: "",
    searchZip: "",
    searchType: "",
    searchStartDate: "",
    searchEndDate: "",
    valid: true,
    sortBy: "",
    sortOrder: "",
    showNextButton: false,
    showPreviousButton: false,
    page: 1,
    next: "",
    previous: "",
    pageSize: 25,
    pageSizes: [25, 50, 75, 100],
    totalPages: 0,
    total: 0,
    // return {
    //   loading: false,
    //   item: [],
    //   search: null,
    //   select: null,
    // }
  }),
  mounted() {
    this.getMemorialList();
  },

  computed: {
    filteredData() {
      return this.memorialList;
    },
    pagingMessage() {
      let start = (parseInt(this.page) - 1) * parseInt(this.pageSize) + 1;
      let end = parseInt(this.page) * parseInt(this.pageSize);
      let pageend = end;
      if (pageend > this.total) pageend = this.total;
      let msg = "Showing " + start + " to " + pageend + " of " + this.total;
      return msg;
    },
    computePageSizes() {
      return this.pageSizes.filter((n) => n <= this.total);
    },
  },
  methods: {
    // Reference: https://www.bezkoder.com/vuetify-pagination-server-side/
    getRequestParams() {
      let params = {};
      if (this.searchName) {
        params["searchName"] = this.searchName;
      }
      if (this.searchFounderName) {
        params["searchFounderName"] = this.searchFounderName;
      }
      if (this.searchCity) {
        params["searchCity"] = this.searchCity;
      }
      if (this.searchState) {
        params["searchState"] = this.searchState;
      }
      if (this.searchZip) {
        params["searchZip"] = this.searchZip;
      }
      if (this.searchType) {
        params["searchType"] = this.searchType;
      }
      if (this.searchStartDate) {
        params["searchStartDate"] = this.searchStartDate;
      }
      if (this.searchEndDate) {
        params["searchEndDate"] = this.searchEndDate;
      }
      if (this.page) {
        params["page"] = this.page;
      }
      if (this.pageSize) {
        params["page_size"] = this.pageSize;
      }
      return params;
    },
    handlePageChange(value) {
      this.page = value;
      this.getMemorialList();
    },
    handlePageSizeChange(size) {
      this.pageSize = size;
      this.page = 1;
      this.getMemorialList();
    },
    memorialSearch(value) {
      this.getMemorialList();
      // if (this.searchMemorials.length > 1 || this.searchMemorials.length === 0) {
      //   this.getMemorialList();
      // }
    },
    getMemorialList() {
      const params = this.getRequestParams();
      apiService.getMemorialList(params).then((res) => {
        this.memorialList = res.data.results;
        this.next = res.data.next;
        this.previous = res.data.previous;
        this.total = res.data.count;
        this.totalPages = Math.ceil(res.data.count / this.pageSize);
      });
    },
    setpk(id) {
      localStorage.setItem("id", id);
    },
    sortByStartDate() {
      if (this.sortOrder === "asc" && this.sortBy === "start_date") {
        this.memorialList.sort(
          (a, b) =>
            new Date(b.mem_location.time_active_start) -
            new Date(a.mem_location.time_active_start)
        );
        this.sortOrder = "desc";
      } else {
        this.memorialList.sort(
          (a, b) =>
            new Date(a.mem_location.time_active_start) -
            new Date(b.mem_location.time_active_start)
        );
        this.sortOrder = "asc";
        this.sortBy = "start_date";
      }
    },
    sortByEndDate() {
      if (this.sortOrder === "asc" && this.sortBy === "end_date") {
        this.memorialList.sort(
          (a, b) =>
            new Date(b.mem_location.time_active_end) -
            new Date(a.mem_location.time_active_end)
        );
        this.sortOrder = "desc";
      } else {
        this.memorialList.sort(
          (a, b) =>
            new Date(a.mem_location.time_active_end) -
            new Date(b.mem_location.time_active_end)
        );
        this.sortOrder = "asc";
        this.sortBy = "end_date";
      }
    },
  },
};
</script>

<style>
.mem_search_css {
  font-weight: bold;
  /*font-family: Verdana,sans-serif;*/
  font-family: "Archivo Black", sans-serif;
  font-size: large;
}
.mem_search_css2 {
  font-weight: normal;
  font-family: "Archivo Narrow", sans-serif;
  text-size: 12px;
}
tbody tr:nth-of-type(even) {
  background-color: rgba(0, 0, 0, 0.05);
}
.select {
  min-width: 120px;
}
.pagination {
  min-width: 400px;
}
</style>
