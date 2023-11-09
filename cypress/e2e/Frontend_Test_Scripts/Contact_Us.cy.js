/// <reference types="cypress"/>
///import * as cy from "core-js";
//To change the environment that this test script runs in you will need to change the baseurl in the cypress.env.json file

import ContactUsData from "/cypress/fixtures/contactUs.json";


// it('contactUs ', function () {
//     ///change url on line 5 as needed
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL"))
//     cy.get('[data-cy="resources"]').click({force:true})
//     cy.get('[data-cy="mbc_contact_us"]').click({ multiple: true, force: true })
//     cy.get('[data-cy="first_name"]').parent().should('be.visible').click().type(ContactUsData.first_name)
//     cy.get('[data-cy="last_name"]').parent().should('be.visible').click().type(ContactUsData.last_name)
//     cy.get('[data-cy="inquiry_type"]').parent().should('be.visible').click({force:true}).type(ContactUsData.inquiry_type)
//     cy.get('[data-cy="email_id"]').parent().should('be.visible').click({force:true}).type(ContactUsData.email_id)
//     cy.get('[data-cy="message"]').parent().should('be.visible').click().type(ContactUsData.message)
//     cy.get('[data-cy="Submit"]').should('be.visible').click({ multiple: true, force: true })
//
//       });
