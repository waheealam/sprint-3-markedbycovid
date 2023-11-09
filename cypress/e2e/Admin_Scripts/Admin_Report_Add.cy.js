/// <reference types="cypress"/>
///import * as cy from "core-js";
//Create a cypress.env.json file in your root of your project and populate all username, URLs, and passwords in that file.
//To change the environment that this test script runs in you will need to change the baseurl in the cypress.env.json
//to change the test data modify the AdminReportAdd.json file in the fixtures folder


import ReportData from "/cypress/fixtures/AdminReportAdd.json"

it('admin_add_report', function () {

    cy.visit(Cypress.env("ADMIN_URL"))
    cy.get('input[id="id_username"]').click().type(Cypress.env("USERNAME"))
    cy.get('input[id="id_password"]').click().type(Cypress.env("PASSWORD"))
    cy.get('input[class="grp-button grp-default').click()
    cy.get('div[id="model-report"]').click()
    cy.get('a[href*="/admin/report_builder/report/add/"]').click()
    cy.get('input[id="id_name"]').click().type(ReportData.report_name)
    cy.get('select[id="id_root_model"]').select('Memorialmatrix | memorial')
    cy.get('input[class="grp-button grp-default"]').click()
    cy.get('button[class="button"]').click()
    cy.get('button[class="add-button"]').click({ multiple: true })
    cy.get('div[aria-posinset="3"]').click()
    cy.get('button[class="mat-focus-indicator mat-button mat-button-base"]').contains('Save').click()
    // cy.get('button[class="mat-focus-indicator mat-button mat-button-base"]').contains('XLSX').click()

})
