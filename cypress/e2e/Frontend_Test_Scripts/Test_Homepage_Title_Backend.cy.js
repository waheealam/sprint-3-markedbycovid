


describe('Title Backend', () => {
    beforeEach(() => {
        cy.visit(Cypress.env("ADMIN_URL"))
    })

    it('verify title of backend home page', function () {
        cy.title().should('eq', 'Log in | Memorial Matrix Administration')
   })
})
