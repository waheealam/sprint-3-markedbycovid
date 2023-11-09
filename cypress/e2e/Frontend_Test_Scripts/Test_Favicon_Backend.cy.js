


describe('Favicon Backend', () => {
    beforeEach(() => {
        cy.visit("http://127.0.0.1:8000/")
    })

    it('verify favicon backend', function () {
      cy.get('head').find('link[rel="icon"]').should('have.attr', 'href').
      should('eq', 'static/favicon.ico')
    })
})
