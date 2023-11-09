/// <reference types="cypress"/>
///import * as cy from "core-js";

//Create a cypress.env.json file in your root of your project and populate all username, URLs, and passwords in that file.
//To change the environment that this test script runs in you will need to change the baseurl in the cypress.env.json file
//Update the WagtailData.json file if you want to change the test data for this test script

//Note this test script was not working really well with the CircleCI deployment so it is commented out
//Left this test script so it can be enhanced and fixed to work with CircleCI.


import WagtailData from '/cypress/fixtures/WagtailData.json'
import FaqData from "/cypress/fixtures/CreateFAQPage.json"
import SponsorData from "/cypress/fixtures/SponsorPage.json"
import EditAboutUsData from "/cypress/fixtures/EditWagtailAboutUs.json"
import EditFooterData from "/cypress/fixtures/EditWagtailFooter.json"
import EditFAQData from "/cypress/fixtures/EditFAQQuestionAnswer.json"
import EditSponsorsData from "/cypress/fixtures/EditWagtailSponsors.json"


// it('admin_wagtail_add_edit_delete', function () {
//
//     // must delete all existing wagtail pages or this will break
//     //Configures the root, about and footer pages
//     cy.visit(Cypress.env("ADMIN_URL"))
//     cy.get('input[id="id_username"]').click().type(Cypress.env("USERNAME"))
//     cy.get('input[id="id_password"]').click().type(Cypress.env("PASSWORD"))
//     cy.get('input[class="grp-button grp-default"]').click()
//     cy.wait(1000)
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_URL)
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1) > span:nth-child(2)').click()
//     cy.get('.c-page-explorer__header__title__inner > span:nth-child(2)').click()
//     cy.get('.bulk-action-checkbox').check()
//     cy.get('.serious').click()
//     cy.get('input.button').click()
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_URL)
//     cy.get('a[href*="/cms/pages/1"]').first().click()
//     cy.get('.icon-dots-horizontal').click({force: true})
//     cy.get('a.w-group:nth-child(1)').click({force: true})
//     cy.get('.listing > li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
//     cy.get('input[id="id_title"]').click().type(WagtailData.title)
//     cy.get('input[id="id_pageTitle"]').click().type(WagtailData.page_title)
//     cy.get('div[id="panel-child-content-body-content"]').click().type(WagtailData.about_body)
//     cy.wait(1000)
//     cy.get('div[class="dropdown-toggle"]').click()
//     cy.get('button[name="action-publish"]').click()
//     cy.get('svg[class="icon icon-cogs icon--menuitem"]').click()
//     cy.get('a[href*="/cms/sites/"]').first().click()
//     cy.get('a[href*="/cms/sites/new/"]').click()
//     cy.get('input[id="id_hostname"]').click().type(WagtailData.host_name)
//     cy.get('input[id="id_port"]').click().clear().type(WagtailData.port)
//     cy.get('input[id="id_site_name"]').click().type(WagtailData.site_name)
//     cy.get('button[class="button action-choose button-small button-secondary chooser__choose-button"]').click()
//     cy.get('a[data-title="Wagtail About Page Title"]').first().click()
//     cy.get('#id_is_default_site').check()
//     cy.get('input.button').first().click()
//     cy.wait(2000)
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1)').click()
//     cy.get('.c-page-explorer__item__title').click()
//     cy.get('.no-results-message > p:nth-child(1) > a:nth-child(1)').click()
//     cy.get('.listing > li:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
//     cy.get('input[id="id_title"]').click().type(WagtailData.footer_title)
//     cy.get('input[name="generalEmail"]').click({ force: true }).type(WagtailData.general_email)
//     cy.get('input[name="pressEmail"]').click({ force: true }).type(WagtailData.press_email)
//     cy.get('input[name="facebookLink"]').click({ force: true }).type(WagtailData.facebook_link)
//     cy.get('input[name="donate"]').click({ force: true }).type(WagtailData.donate)
//     cy.get('input[name="emailLink"]').click({ force: true }).type(WagtailData.email_link)
//     cy.get('input[name="hashTag"]').click({ force: true }).type(WagtailData.hash_tag)
//     cy.get('input[name="instagramLink"]').click({ force: true }).type(WagtailData.instagram_link)
//     cy.get('input[name="twitterLink"]').click({ force: true }).type(WagtailData.twitter_link)
//     cy.get('div[class="dropdown-toggle"]').click()
//     cy.get('button[name="action-publish"]').click()
//     cy.wait(300)
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_ABOUT_PAGE)
//
//     //Add FAQ Page
//
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_URL)
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1)').click()
//     cy.get('.c-page-explorer__item__title').click()
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1)').click()
//     cy.get('.c-page-explorer__header__title__inner > span:nth-child(2)').click()
//     cy.get('.actions > li:nth-child(3) > a:nth-child(1)').click({force: true})
//     cy.get('.listing > li:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
//     cy.get('#id_title').click().type(FaqData.title)
//     cy.get('.c-sf-add-button').click()
//     cy.get('.w-combobox__option-text').click()
//     cy.get('#questions-0-value-question').click().type(FaqData.Question)
//     cy.wait(300)
//     cy.get('.notranslate').click().type(FaqData.Answer)
//     cy.get('.dropdown-toggle').click()
//     cy.get('button[name="action-publish"]').click()
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_FAQ_PAGE)
//
//     //Add Sponsor Page
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_URL)
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1)').click()
//     cy.get('.c-page-explorer__item__title').click()
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1)').click()
//     cy.get('.c-page-explorer__header__title__inner > span:nth-child(2)').click()
//     cy.get('.actions > li:nth-child(3) > a:nth-child(1)').click({force: true})
//     cy.get('.listing > li:nth-child(4) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
//     cy.get('.icon-plus').click()
//     cy.get('#id_title').click().type(SponsorData.sponsor_page_title)
//     cy.get('.icon-plus').click()
//     cy.get('.w-combobox__option-text').click()
//     cy.get('#sponsors-0-value-sponsorName').click().type(SponsorData.sponsor_name)
//     cy.get('.notranslate').click().type(SponsorData.sponsor_description)
//     cy.get('#sponsors-0-value-photoUrl').type(SponsorData.photo_url)
//     cy.get('.dropdown-toggle').click()
//     cy.get('button[name="action-publish"]').click()
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_SPONSORS_PAGE)
//
//     //Edit About Page
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_URL)
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1) > span:nth-child(2)').click()
//     cy.get('.icon-edit').click()
//     cy.get('#id_pageTitle').click().clear().type(EditAboutUsData.about_us_title)
//     cy.get('.notranslate').click().clear().type(EditAboutUsData.about_us_body)
//     cy.get('.dropdown-toggle').click()
//     cy.get('button[name="action-publish"]').click()
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_ABOUT_PAGE)
//
//     //Edit Footer Page
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_URL)
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1)').click()
//     //cy.get('.c-page-explorer__item__title').click()
//     cy.get('svg.icon-arrow-right:nth-child(1)').click()
//     cy.get('div.c-page-explorer__item:nth-child(1) > a:nth-child(2) > svg:nth-child(1)').click()
//     cy.get('#id_generalEmail').click().clear().type(EditFooterData.general_email)
//     cy.get('#id_pressEmail').click().clear().type(EditFooterData.press_email)
//     cy.get('.dropdown-toggle').click()
//     cy.get('button[name="action-publish"]').click()
//
//     //Edit FAQ Page
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_URL)
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1) > span:nth-child(2)').click()
//     cy.get('svg.icon-arrow-right:nth-child(1)').click()
//     cy.get('div.c-page-explorer__item:nth-child(2) > a:nth-child(2)').click()
//     cy.get('#questions-0-value-question').click().clear().type(EditFAQData.Question)
//     cy.get('.notranslate').click().clear().type(EditFAQData.Answer)
//     cy.get('.dropdown-toggle').click()
//     cy.get('button[name="action-publish"]').click()
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_FAQ_PAGE)
//
//     //Edit Sponsors Page
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_URL)
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1) > span:nth-child(2)').click()
//     cy.get('svg.icon-arrow-right:nth-child(1)').click()
//     cy.get('div.c-page-explorer__item:nth-child(3) > a:nth-child(2)').click()
//     cy.get('#sponsors-0-value-sponsorName').click().clear().type(EditSponsorsData.sponsor_name)
//     cy.get('.dropdown-toggle').click()
//     cy.get('button[name="action-publish"]').click()
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_SPONSORS_PAGE)
//
//     //Delete All Pages
//     cy.visit(Cypress.env("MEMORIAL_MATRIX_URL")  + WagtailData.WAGTAIL_URL)
//     cy.get('.sidebar-page-explorer-item > button:nth-child(1) > span:nth-child(2)').click()
//     cy.get('.c-page-explorer__header__title__inner > span:nth-child(2)').click()
//     cy.get('.bulk-action-checkbox').check()
//     cy.get('.serious').click()
//     cy.get('input.button').click()
//
// })
