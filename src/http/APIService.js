/* eslint-disable */
import axios from "axios";
const API_URL = process.env.VUE_APP_API_ENDPOINT;
// const API_URL="http://127.0.0.1:8000/";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export class APIService {
  constructor() {}

  async getMemorials() {
    const url = `${API_URL}api/mapMemorials`;
    let jwtToken = localStorage.getItem("token");
    const headers = { Authorization: `jwt ${jwtToken}` };
    return await axios.get(url, {
      headers: { Authorization: `jwt ${jwtToken}` },
    });
  }

  async submitMemorial() {
    const url = `${API_URL}api/create`;
    let jwtToken = localStorage.getItem("token");
    const headers = { Authorization: `jwt ${jwtToken}` };
    return await axios.post(url, {
      headers: { Authorization: `jwt ${jwtToken}` },
    });
  }

  async contact() {
    const url = `${API_URL}api/contact`;
    let jwtToken = localStorage.getItem("token");
    const headers = { Authorization: `jwt ${jwtToken}` };
    return await axios.post(url, {
      headers: { Authorization: `jwt ${jwtToken}` },
    });
  }

  getMemorialList(queryParams='undefined') {
    if(queryParams != 'undefined') {
      const params = new URLSearchParams(queryParams);
      let url= new URL(`${API_URL}api/memorial/list?${params}`);
      return axios.get(url);
    }
    else {
      const url = `${API_URL}api/memorial/list`;
      return axios.get(url);
    }
  }

  getMemorialListPage(url) {
    return axios.get(url);
  }

  getUpcomingEvents() {
    const url = `${API_URL}api/memorial/upcomingEvents`;
    return axios.get(url);
  }

  getFeaturedMemorials() {
    const url = `${API_URL}api/memorial/featuredMemorials`;
    return axios.get(url);
  }
  getMemorialCount() {
    const url = `${API_URL}api/memorial/count`;
    return axios.get(url);
  }

  getMemorialProfilePhotoUrl(id) {
    const url = `${API_URL}api/memorial/profilePhoto/${id}`;
    return axios.get(url);
  }

  getWebsiteConfigurationParameter(parameter_name) {
    const url = `${API_URL}api/website/configuration/parameter/${parameter_name}`;
    return axios.get(url);
  }

  getMemorialView(id) {
    const url = `${API_URL}api/memorial/detail/${id}`;

    return axios.get(url);
  }
  getMediaLinksView(id) {
    const url = `${API_URL}api/medialink/${id}`;

    return axios.get(url);
  }

  async getAboutPageContent(){
    const url = `${API_URL}api/v2/pages/?type=WagtailApp.AboutPage&fields=pageTitle,body,coreStaffTitle,coreStaffs`;
    return await axios.get(url);
  }
  async getFaqPageContent(){
    const url = `${API_URL}api/v2/pages/?type=WagtailApp.FaqPage&fields=questions`;
    return await axios.get(url);
  }
  async getFooterContent(){
    const url = `${API_URL}api/v2/pages/?type=WagtailApp.FooterPage&fields=donate,facebookLink,instagramLink,twitterLink,shareStoryLink `;
    return await axios.get(url);
  }
    async getSponsorsPageContent(){
    const url = `${API_URL}api/v2/pages/?type=WagtailApp.SponsorPage&fields=sponsors,advisors,volunteers`;
    return await axios.get(url);
  }
  
}
