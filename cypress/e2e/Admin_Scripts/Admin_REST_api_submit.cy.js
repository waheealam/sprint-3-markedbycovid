/// <reference types="cypress"/>
///import * as cy from "core-js";

import RestAPIData from '/cypress/fixtures/RESTAPIs.json'


it('REST_api_submit', function () {
    cy.visit(Cypress.env("ADMIN_URL"))
    cy.get('input[id="id_username"]').click().type(Cypress.env("USERNAME"))
    cy.get('input[id="id_password"]').click().type(Cypress.env("PASSWORD"))
    cy.get('input[class="grp-button grp-default"]').click()
    cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + RestAPIData.LOCATION_API_LIST)
    cy.get('textarea[id="id__content"]').click().type('{\n' +
        '                "id": "b25e7422-d0ea-48fa-a084-296a3927dcad",\n' +
        '                "location_number": "",\n' +
        '                "type": "",\n' +
        '                "address": "6001 Dodge St",\n' +
        '                "city": "Omaha",\n' +
        '                "state": "NE",\n' +
        '                "zipcode": "68182",\n' +
        '                "time_active_start": "2020-04-14",\n' +
        '                "time_active_end": "2020-04-15",\n' +
        '                "lat_coord": "41.259598300000000",\n' +
        '                "long_coord": "-96.005007900000000",\n' +
        '                "permanent": "temporary",\n' +
        '                "location_approval": "True",\n' +
        '                "last_modified": ""\n' +
        '}', {
    parseSpecialCharSequences: false,})
    cy.get('button[class="btn btn-primary js-tooltip"]').last().click()
    cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + RestAPIData.MEMORIAL_API_LIST)
    cy.get('textarea[id="id__content"]').click().type('{\n' +
        '    "id": "535d3f17-b835-4d3a-adf3-e73a9908ea95",\n' +
        '    "name": "Memorial Name Test",\n' +
        '    "type": "virtual",\n' +
        '    "founder_name": "Stephan Perez",\n' +
        '    "email": "spress61@live.com",\n' +
        '    "is_approved": "approved",\n' +
        '    "profile_picture": "https://imgur.com/t/cat/ei8Hbua",\n' +
        '    "google_virtual_tour": "https://www.google.com/maps",\n' +
        '    "website": "https://www.iamawebsite.com",\n' +
        '    "description": "Memorial Description Test",\n' +
        '    "social_media_twitter": "https://twitter.com/JeffBezos",\n' +
        '    "social_media_instagram": "https://www.instagram.com/pain1666/",\n' +
        '    "social_media_facebook": "https://www.facebook.com/zuck",\n' +
        '    "mem_location": {' +
        '          "id": "1a5e4e67-8c25-466b-97f4-7c67d59e85e1"\n' +
        '    },\n' +
        '    "mem_submitter": null\n' +
        '}', {
    parseSpecialCharSequences: false,})
    cy.get('button[class="btn btn-primary js-tooltip"]').last().click()
    cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + RestAPIData.MEDIALINK_API_LIST)
    cy.get('textarea[id="id__content"]').click().type('{\n' +
        '                "mem_medialinks": "535d3f17-b835-4d3a-adf3-e73a9908ea95",\n' +
        '                "id": "fc673868-e1d7-4689-befa-ef9a6305cb7e",\n' +
        '                "medialinks_number": "",\n' +
        '                "type": "press coverage",\n' +
        '                "url": "https://www.cnn.com/style/article/supertall-skyscraper-austin-texas-wilson-tower/index.html"         \n' +
        '}', {
    parseSpecialCharSequences: false,})
    cy.get('button[class="btn btn-primary js-tooltip"]').last().click()
    cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + RestAPIData.CREATE_MEMORIAL_API,{failOnStatusCode: false})
    cy.get('textarea[id="id__content"]').click().type('{\n' +
        '            "id": "",\n' +
        '            "name": "Memorial Name REST Serializer",\n' +
        '            "type": "virtual",\n' +
        '            "founder_name": "Stephan Perez",\n' +
        '            "email": "ebrousseau@unomaha.edu",\n' +
        '            "profile_picture": "https://imgur.com/t/cat/ei8Hbua",\n' +
        '            "google_virtual_tour": "https://www.google.com/maps",\n' +
        '            "website": "https://www.iamawebsite.com",\n' +
        '            "description": "Memorial Description Test",\n' +
        '            "social_media_twitter": "https://twitter.com/JeffBezos",\n' +
        '            "social_media_instagram": "https://www.instagram.com/pain1666/",\n' +
        '            "social_media_facebook": "https://www.facebook.com/zuck",\n' +
        '            "is_approved": "approved",\n' +
        '            "mem_location": {\n' +
        '                "id": "",\n' +
        '                "location_number": "",\n' +
        '                "type": "",\n' +
        '                "address": "6001 Dodge St",\n' +
        '                "city": "Omaha",\n' +
        '                "state": "NE",\n' +
        '                "zipcode": "68182",\n' +
        '                "time_active_start": "2020-04-14",\n' +
        '                "time_active_end": "2020-04-15",\n' +
        '                "lat_coord": "41.259598300000000",\n' +
        '                "long_coord": "-96.005007900000000",\n' +
        '                "permanent": null,\n' +
        '                "location_approval": false,\n' +
        '                "last_modified": ""\n' +
        '            },\n' +
        '            "mem_submitter": {\n' +
        '                "id": "",\n' +
        '                "webuser_number": "",\n' +
        '                "first_name": "Danquiesha",\n' +
        '                "last_name": "Millerino",\n' +
        '                "email": "iamanemail@live.com",\n' +
        '                "zipcode": "68106",\n' +
        '                "web_user_loss": true,\n' +
        '                "email_updates": true,\n' +
        '                "created_date": ""\n' +
        '            }\n' +
        '        }', {
    parseSpecialCharSequences: false,})
    cy.get('button[class="btn btn-primary js-tooltip"]').last().click()
    cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + RestAPIData.MEMORIAL_API_LIST, {failOnStatusCode: false})
    //cy.get('pre.prettyprint').contains('Memorial Name REST Serializer').should('not.be.empty')


})
