describe('Favicon Frondend', () => {
    beforeEach(() => {
        cy.visit(Cypress.env("MEMORIAL_MATRIX_URL"))
    })

    it('verify favicon frontend', function () {
        cy.get('head').find('link[rel="icon"]').should('have.attr', 'href').
        should('eq', '/favicon.ico')
    })
})

