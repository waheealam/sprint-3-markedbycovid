


describe('Title Backend', () => {
    beforeEach(() => {
        cy.visit(Cypress.env("MEMORIAL_MATRIX_URL"))
    })

    it('verify title of frontend home page', function () {
//cy.visit(Cypress.env("MEMORIAL_MATRIX_URL"))
        cy.title().should('eq', 'Memorial Matrix')
    })
})
