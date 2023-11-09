//Create a cypress.env.json file in your root of your project and populate all username, URLs, and passwords in that file.
//To change the environment that this test script runs in you will need to change the adminurl in the cypress.env.json file
//Deletes a contact in the contact us admin page.
//Will need to change the elements that are selected from lines 14 - 15 when testing against heroku.
// to change the data you can edit the AddContact.json and EditContact.json files

import ContactUsData from '/cypress/fixtures/AddContact.json'
import EditContactUsData from '/cypress/fixtures/EditContact.json'

it('admin_add_edit_delete_contact', function () {

  // Create Contact
  cy.visit(Cypress.env("ADMIN_URL"))
  cy.get('input[id="id_username"]').click().type(Cypress.env("USERNAME"))
  cy.get('input[id="id_password"]').click().type(Cypress.env("PASSWORD"))
  cy.get('input[class="grp-button grp-default').click()
  cy.get('#model-contactus > a:nth-child(1)').click()
  cy.get('.grp-add-link').click()
  cy.get('#id_first_name').click().type(ContactUsData.contact_first_name)
  cy.get('#id_last_name').click().type(ContactUsData.contact_last_name)
  cy.get('#id_inquiry').click().type(ContactUsData.inquiry)
  cy.get('#id_email').click().type(ContactUsData.email)
  cy.get('#id_message').click().type(ContactUsData.message)
  cy.get('.grp-default').click()

  //Edit Contact
  cy.get('.field-first_name > a:nth-child(1)').click()
  cy.get('#id_first_name').click().clear().type(EditContactUsData.contact_first_name)
  cy.get('#id_email').click().clear().type(EditContactUsData.email)


  //Delete Contact

  cy.get('input[class="grp-button grp-default').click()
  cy.get('.field-first_name > a:nth-child(1)').click()
  cy.get('a.grp-button').click()
  cy.get('input.grp-button').click()

})
