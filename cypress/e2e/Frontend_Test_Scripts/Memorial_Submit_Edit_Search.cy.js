// /// <reference types="cypress"/>
// ///import * as cy from "core-js";
// //Create a cypress.env.json file in your root of your project and populate all username, URLs, and passwords in that file.
// //To change the environment that this test script runs in you will need to change the baseurl in the cypress.env.json file
//
//
// import MemorialData from "/cypress/fixtures/SubmitMemorial.json"
// import SearchData from "../../fixtures/SearchMemorial.json";
// import EditMemorialData from "../../fixtures/EditMemorial.json";
//
// it('memorial_submit_edit_search', function () {
//     //cy.viewport(4000, 4000)
//
//     //Submit Memorial
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL"))
//     cy.get('[data-cy="submit_mem"]').click({ multiple: true, force: true })
//     cy.get('[data-cy="first_name"]').parent().should('be.visible').click().type(MemorialData.first_name)
//     cy.get('[data-cy="last_name"]').parent().should('be.visible').click().type(MemorialData.last_name)
//     cy.get('[data-cy="youremail"]').parent().should('be.visible').click().type(MemorialData.your_email)
//     cy.get('[data-cy="yzip"]').parent().should('be.visible').click().type(MemorialData.yzip)
//     cy.get('input[type="checkbox"]').first().check()
//     cy.get('[data-cy="memorial_name"]').parent().should('be.visible').click().type(MemorialData.memorial_name)
//     cy.get('[data-cy="memorial_description"]').parent().should('be.visible').click().type(MemorialData.memorial_description)
//     cy.get('[data-cy="founder_name"]').parent().should('be.visible').click().type(MemorialData.founder_name)
//     cy.get('[data-cy="mem_location"]').click().type(MemorialData.mem_location)
//     cy.get('input[class="pac-target-input"]').click().wait(1000).type('{downArrow}{enter}')
//     cy.get('[data-cy="mem_type"]').parent().should('be.visible').click().type(MemorialData.mem_type)
//     cy.get('label[class="v-label v-label--clickable"]').contains('Virtual').parent().within(() => {
//         cy.get('input[type="checkbox"]').check()
//     })
//     cy.get('label[class="v-label v-label--clickable"]').contains('Temporary').parent().within(() => {
//         cy.get('input[type="checkbox"]').check()
//     })
//     cy.get('[data-cy="date"]').parent().click().type(MemorialData.date)
//     cy.get('[data-cy="end_date"]').parent().click().type(MemorialData.end_date)
//     cy.get('[data-cy="memorial_website"]').parent().click().type(MemorialData.memorial_website)
//     cy.get('[data-cy="memorial_email"]').parent().click().type(MemorialData.memorial_email)
//     cy.get('[data-cy="memorial_profile_link"]').parent().click().type(MemorialData.memorial_profile_link)
//     cy.get('[data-cy="virtual_tour"]').parent().click().type(MemorialData.virtual_tour)
//     cy.get('[data-cy="photo_links"]').parent().click().type(MemorialData.photo_links)
//     cy.get('[data-cy="video_links"]').parent().click().type(MemorialData.video_links)
//     cy.get('[data-cy="press_links"]').parent().click().type(MemorialData.press_links)
//     cy.get('[data-cy="twitter"]').parent().click().type(MemorialData.twitter)
//     cy.get('[data-cy="instagram"]').parent().click().type(MemorialData.instagram)
//     cy.get('[data-cy="facebook"]').parent().click().type(MemorialData.facebook)
//     cy.get('label[class="v-label v-label--clickable"]').contains('Yes, I agree').parent().within(() => {
//         cy.get('input[type="checkbox"]').check()
//     })
//     cy.get('[data-cy="review"]').click()
//     cy.get('[data-cy="submit"]').click()
//     cy.wait(5000)
//
//     //Approve memorial
//     cy.visit(Cypress.env("ADMIN_URL"))
//     cy.get('input[id="id_username"]').click().type(Cypress.env("USERNAME"))
//     cy.get('input[id="id_password"]').click().type(Cypress.env("PASSWORD"))
//     cy.get('input[class="grp-button grp-default').click()
//     cy.get('#model-memorial > a:nth-child(1) > strong:nth-child(1)').click()
//     cy.get('#grp-changelist-search').type(SearchData.memorial_name)
//     cy.get('.grp-search-button').click()
//     cy.get('tr.grp-row:nth-child(1) > th:nth-child(2) > a:nth-child(1)').click()
//     cy.get('#id_is_approved').select('Approved')
//     cy.get('.grp-default').click()
//
//     // //Edit Memorial
//     // cy.visit(Cypress.env("MEMORIAL_MATRIX_URL"))
//     // cy.get('[data-cy="search_memorial"]').click({ multiple: true, force: true })
//     // cy.get('[data-cy="searchName"]').click().type(SearchData.memorial_name)
//     // cy.get('[data-cy="searchButton"]').click()
//     // cy.get('a[href*="memorialdetail"]').first().click()
//     // cy.get('[data-cy="edit_memorial"]').click()
//     // cy.get('[data-cy="mod_first_name"]').parent().click().type(MemorialData.first_name)
//     // cy.get('[data-cy="mod_last_name"]').parent().click().type(MemorialData.last_name)
//     // cy.get('[data-cy="mod_youremail"]').parent().click().type(MemorialData.your_email)
//     // cy.get('[data-cy="mod_yzip"]').parent().click().type(MemorialData.yzip)
//     // cy.get('[data-cy="mod_memorial_name"]').click().focused().clear().type(EditMemorialData.memorial_name)
//     // cy.get('[data-cy="update"]').click()
//     // cy.get('label[class="v-label v-label--clickable"]').contains('Yes, I agree').parent().within(() => {
//     //     cy.get('input[type="checkbox"]').check()
//     // })
//     // cy.wait(2000)
//     // cy.visit(Cypress.env("ADMIN_URL"))
//     // cy.get('#model-history_memorial > a:nth-child(1)').click()
//     // cy.get('#grp-changelist-search').click().type(SearchData.memorial_name)
//     // cy.get('.grp-search-button').click()
//     // cy.get('tr.grp-row:nth-child(1) > th:nth-child(2) > a:nth-child(1)').first().click()
//     // cy.get('#id_is_approved').select('Approved')
//     // cy.get('#id_history_change_reason').click().type(EditMemorialData.history_change_reason)
//     // cy.get('.grp-default').click()
//     // cy.visit(Cypress.env("ADMIN_URL"))
//     // cy.get('#model-memorial > a:nth-child(1)').click()
//     // cy.get('tr.grp-row:nth-child(1) > th:nth-child(2) > a:nth-child(1)').click()
//     // cy.get('#id_is_approved').select('Approved')
//     // cy.get('.grp-default').click()
//     // cy.visit(Cypress.env("MEMORIAL_MATRIX_URL"))
//     // cy.get('[data-cy="search_memorial"]').click({ multiple: true, force: true })
//     // cy.get('[data-cy="searchName"]').click().type(SearchData.memorial_name)
//     // cy.get('[data-cy="searchButton"]').click()
//
//     //Search Memorial
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL"))
//     cy.get('[data-cy="search_memorial"]').click({ multiple: true, force: true })
//     cy.get('[data-cy="searchName"]').click().type(SearchData.memorial_name)
//     cy.get('[data-cy="searchButton"]').click()
//     cy.get('[data-cy="searchName"]').click().focused().clear()
//     cy.get('[data-cy="searchFounderName"]').click().type(SearchData.founder_name)
//     cy.get('[data-cy="searchButton"]').should('be.visible').click()
//     cy.get('[data-cy="searchFounderName"]').click().focused().clear()
//     cy.get('[data-cy="searchCity"]').click().type(SearchData.city)
//     cy.get('[data-cy="searchButton"]').should('be.visible').click()
//     cy.get('[data-cy="searchCity"]').should('be.visible').click().focused().clear()
//     cy.get('[data-cy="searchButton"]').should('be.visible').click()
//     cy.get('[data-cy="searchZip"]').click().type(SearchData.zip)
//     cy.get('[data-cy="searchButton"]').click()
//     cy.get('[data-cy="searchZip"]').click().focused().clear()
//     cy.get('[data-cy="searchState"]').click().type(SearchData.state)
//     cy.get('[data-cy="searchButton"]').click()
//     cy.get('[data-cy="searchState"]').click().focused().clear()
//     cy.get('[data-cy="searchType"]').click().type(SearchData.mem_type)
//     cy.get('[data-cy="searchButton"]').should('be.visible').click()
//     cy.get('[data-cy="searchButton"]').should('be.visible').click()
//     cy.get('[data-cy="searchButton"]').should('be.visible').click()
//     cy.get('[data-cy="searchType"]').should('be.visible').click().focused().clear()
//     cy.get('[data-cy="searchButton"]').should('be.visible').click()
//     cy.get('[data-cy="searchStartDate"]').should('be.visible').click().type(SearchData.date)
//     cy.get('[data-cy="searchButton"]').should('be.visible').click()
//     cy.get('[data-cy="searchStartDate"]').should('be.visible').click().focused().clear()
//     cy.get('[data-cy="searchEndDate"]').should('be.visible').click().type(SearchData.date)
//     cy.get('[data-cy="searchButton"]').should('be.visible').click()
//     cy.get('[data-cy="searchEndDate"]').should('be.visible').click().focused().clear()
//     cy.get('[data-cy="searchButton"]').should('be.visible').click()
//
//
//
//
// })