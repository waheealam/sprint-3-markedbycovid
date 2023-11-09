// /// <reference types="cypress"/>
// ///import * as cy from "core-js";
// //Create a cypress.env.json file in your root of your project and populate all username, URLs, and passwords in that file.
// //To change the environment that this test script runs in you will need to change the baseurl in the cypress.env.json file
//
//
// import MemorialData from "/cypress/fixtures/SubmitMemorial.json";
//
// it('memorial_edit_review_submission_form', function () {
//     //cy.viewport(4000, 4000)
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL"))
//     cy.get('[data-cy="submit_mem"]').should('be.visible').click({ multiple: true, force: true })
//     cy.get('[data-cy="first_name"]').parent().should('be.visible').click().type(MemorialData.first_name)
//     cy.get('[data-cy="last_name"]').parent().should('be.visible').click().type(MemorialData.last_name)
//     cy.get('[data-cy="youremail"]').parent().should('be.visible').click().type(MemorialData.your_email)
//     cy.get('[data-cy="yzip"]').parent().should('be.visible').click().type(MemorialData.yzip)
//     cy.get('input[type="checkbox"]').first().check()
//     cy.get('[data-cy="memorial_name"]').parent().should('be.visible').click().type(MemorialData.memorial_name)
//     cy.get('[data-cy="memorial_description"]').parent().should('be.visible').click().type(MemorialData.memorial_description)
//     cy.get('[data-cy="founder_name"]').parent().should('be.visible').click().type(MemorialData.founder_name)
//     cy.get('[data-cy="mem_location"]').should('be.visible').click().type(MemorialData.mem_location)
//     cy.get('input[class="pac-target-input"]').should('be.visible').click().wait(2000).type('{downArrow}{enter}')
//     cy.get('[data-cy="mem_type"]').parent().should('be.visible').click().type(MemorialData.mem_type)
//     cy.get('label[class="v-label v-label--clickable"]').contains('Virtual').parent().within(() => {
//         cy.get('input[type="checkbox"]').check()
//     })
//     cy.get('label[class="v-label v-label--clickable"]').contains('Temporary').parent().within(() => {
//         cy.get('input[type="checkbox"]').check()
//     })
//     cy.get('[data-cy="date"]').parent().should('be.visible').click().type(MemorialData.date)
//     cy.get('[data-cy="end_date"]').parent().should('be.visible').click().type(MemorialData.end_date)
//     cy.get('[data-cy="memorial_website"]').parent().should('be.visible').click().type(MemorialData.memorial_website)
//     cy.get('[data-cy="memorial_email"]').parent().should('be.visible').click().type(MemorialData.memorial_email)
//     cy.get('[data-cy="memorial_profile_link"]').parent().should('be.visible').click().type(MemorialData.memorial_profile_link)
//     cy.get('[data-cy="virtual_tour"]').parent().should('be.visible').click().type(MemorialData.virtual_tour)
//     cy.get('[data-cy="photo_links"]').parent().should('be.visible').click().type(MemorialData.photo_links)
//     cy.get('[data-cy="video_links"]').parent().should('be.visible').click().type(MemorialData.video_links)
//     cy.get('[data-cy="press_links"]').parent().should('be.visible').click().type(MemorialData.press_links)
//     cy.get('[data-cy="twitter"]').parent().should('be.visible').click().type(MemorialData.twitter)
//     cy.get('[data-cy="instagram"]').parent().should('be.visible').click().type(MemorialData.instagram)
//     cy.get('[data-cy="facebook"]').parent().should('be.visible').click().type(MemorialData.facebook)
//     cy.get('label[class="v-label v-label--clickable"]').contains('Yes, I agree').parent().within(() => {
//         cy.get('input[type="checkbox"]').check()
//     })
//     cy.get('[data-cy="review"]').should('be.visible').click()
//     cy.get('[data-cy="edit"]').should('be.visible').click()
//     cy.get('[data-cy="memorial_description"]').parent().should('be.visible').click().type(MemorialData.memorial_description)
//     cy.get('[data-cy="review"]').should('be.visible').click()
//     cy.get('[data-cy="submit"]').should('be.visible').click()
//
//
// })
