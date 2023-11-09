const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    experimentalRunAllSpecs: false,
    "retries": 2,
    experimentalMemoryManagement: true,
    "numTestsKeptInMemory": 0,
    setupNodeEvents(on, config) {
      // implement node event listeners here
      // config.baseUrl = 'place the base URL under test';
    },
    testingType: 'e2e',
    specPattern: [
      'cypress/e2e/adminScripts.cy.js',
      'cypress/e2e/frontEndScripts.cy.js',
    ],
  },
});
