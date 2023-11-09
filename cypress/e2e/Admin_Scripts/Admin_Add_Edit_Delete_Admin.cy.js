//Create a cypress.env.json file in your root of your project and populate all username, URLs, and passwords in that file.
//To change the environment that this test script runs in you will need to change the baseurl in the cypress.env.json file
//to change the test data modify the AddAdmin.json and EditAdmin.json file in the fixtures folder
import AdminData from "/cypress/fixtures/AddAdmin.json"
import AdminEditData from "/cypress/fixtures/EditAdmin.json"

it('admin_add_edit_delete_admin', function () {

  //Add Admin

  cy.visit(Cypress.env("ADMIN_URL"))
  cy.get('input[id="id_username"]').click().type(Cypress.env("USERNAME"))
  cy.get('input[id="id_password"]').click().type(Cypress.env("PASSWORD"))
  cy.get('input[class="grp-button grp-default').click()
  cy.get('#model-customuser').contains('Admins').click()
  cy.get('a[href*="/admin/Memorialmatrix/customuser/add/"]').click()
  cy.get('input[id="id_email"]').click().type(AdminData.email_address)
  cy.get('input[id="id_password1"]').click().type(AdminData.password)
  cy.get('input[id="id_password2"]').click().type(AdminData.password)
  cy.get('input[id="id_first_name"]').click().type(AdminData.first_name)
  cy.get('input[id="id_last_name"]').click().type(AdminData.last_name)
  cy.get('input[id="id_phone"]').click().type(AdminData.phone)
  cy.get('input[id="id_address"]').click().type(AdminData.address)
  cy.get('input[id="id_city"]').click().type(AdminData.city)
  cy.get('input[id="id_state"]').click().type(AdminData.state)
  cy.get('input[id="id_zipcode"]').click().type(AdminData.zip)
  cy.get('.grp-default').contains('Save').click()

  //Edit Admin
  cy.get('input[class="grp-button grp-default').click()
  cy.get("tr.grp-row:nth-child(2) > th:nth-child(2) > a:nth-child(1)").click()
  cy.get('input[id="id_first_name"]').click().clear().type(AdminEditData.first_name)
  cy.get('input[id="id_city"]').click().clear().type(AdminEditData.city)
  cy.get('.grp-default').click()


  //Delete Admin
  cy.get('tr.grp-row:nth-child(2) > th:nth-child(2) > a:nth-child(1)').contains('youremail2@gmail.com').click()
  cy.get('a.grp-button').click()
  cy.get('input.grp-button').click()

})