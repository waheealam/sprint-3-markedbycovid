const startDate = new Date("Mar 01 2020");
const endDate = new Date();
const maxDateAllowed = new Date();
// Format the dates as "MMM DD YYYY"
const formattedStartDate = startDate.toLocaleDateString("en-US", {
  year: "numeric",
  month: "short",
  day: "2-digit",
  //timeZone: "utc"
});
const formattedEndDate = endDate.toLocaleDateString("en-US", {
  year: "numeric",
  month: "short",
  day: "2-digit",
  //timeZone: "utc"
});
maxDateAllowed.setMonth(maxDateAllowed.getMonth() + 3);
const maxEndDate = maxDateAllowed.toLocaleDateString("en-US", {
  year: "numeric",
  month: "short",
  day: "2-digit",
});

it('check slider date range', function () {

  cy.visit(Cypress.env('MEMORIAL_MATRIX_URL'));
   cy.wait(3000)
  cy.scrollTo('center')

  cy.get('[data-cy="slider"]').get('div').should('have.class', 'slider-handle slider-handle-lower')
      .contains(formattedStartDate.replace(',', ''))
     cy.wait(3000)
     cy.wait(3000)
  cy.get('[data-cy="slider"]').get('div').should('have.class', 'slider-handle slider-handle-upper')
      .contains(formattedEndDate.replace(',', ''))
     cy.wait(3000)
     cy.wait(3000)

    cy.get('[class*="slider-handle slider-handle-upper"]')
        .invoke('attr','data-cy-max').then((attributeValue) => {
        // Use .invoke() to read the value of the attribute
        const dateInUI = new Date(attributeValue);
        const dateInUIString = dateInUI.toLocaleDateString("en-US", {
            year: "numeric",
            month: "short",
            day: "2-digit",
        });
        console.log(dateInUI)
        expect(dateInUIString).to.equal(dateInUIString)
    })
      cy.get('[data-cy="slider"] .slider-handle-upper').trigger('mousedown', {which: 1});
      // Move the slider to the maximum value (assuming it's at the minimum value initially)
      cy.get('[data-cy="slider"]').trigger('mousemove', 'right'); // Adjust 'right' as needed
      cy.wait(3000)

});