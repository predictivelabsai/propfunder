from fasthtml.common import *


def contact_page():
    hero = Section(
        Div(
            H1('Contact Us'),
            P('Get in touch with our team. We are here to help with any questions about '
              'investing or borrowing through PropFunder.'),
            cls='hero-inner'
        ),
        cls='hero', style='padding:4rem 2rem;'
    )

    offices = Section(
        Div(
            Div(
                H2('Our Offices'),
                cls='section-header'
            ),
            Div(
                Div(
                    H3('London (HQ)'),
                    P(Strong('Address'), Br(),
                      '71-75 Shelton Street', Br(),
                      'Covent Garden', Br(),
                      'London WC2H 9JQ', Br(),
                      'United Kingdom'),
                    P(Strong('Email'), Br(),
                      A('london@propfunder.com', href='mailto:london@propfunder.com',
                        style='color:var(--primary);text-decoration:none;')),
                    P(Strong('Phone'), Br(),
                      A('+44 20 7123 4567', href='tel:+442071234567',
                        style='color:var(--primary);text-decoration:none;')),
                    cls='card'
                ),
                Div(
                    H3('Berlin'),
                    P(Strong('Address'), Br(),
                      'Friedrichstra\u00dfe 123', Br(),
                      '10117 Berlin', Br(),
                      'Germany'),
                    P(Strong('Email'), Br(),
                      A('berlin@propfunder.com', href='mailto:berlin@propfunder.com',
                        style='color:var(--primary);text-decoration:none;')),
                    P(Strong('Phone'), Br(),
                      A('+49 30 1234 5678', href='tel:+493012345678',
                        style='color:var(--primary);text-decoration:none;')),
                    cls='card'
                ),
                Div(
                    H3('Tallinn'),
                    P(Strong('Address'), Br(),
                      'Narva mnt 5', Br(),
                      '10117 Tallinn', Br(),
                      'Estonia'),
                    P(Strong('Email'), Br(),
                      A('tallinn@propfunder.com', href='mailto:tallinn@propfunder.com',
                        style='color:var(--primary);text-decoration:none;')),
                    P(Strong('Phone'), Br(),
                      A('+372 641 2345', href='tel:+3726412345',
                        style='color:var(--primary);text-decoration:none;')),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    general = Section(
        Div(
            Div(
                H2('General Enquiries'),
                cls='section-header'
            ),
            Div(
                Div(
                    H3('Investor Support'),
                    P('Questions about your account, investments, or returns?'),
                    P(A('investors@propfunder.com', href='mailto:investors@propfunder.com',
                        style='color:var(--accent);text-decoration:none;font-weight:600;')),
                    cls='card'
                ),
                Div(
                    H3('Borrower Enquiries'),
                    P('Want to apply for financing or have questions about the process?'),
                    P(A('borrowers@propfunder.com', href='mailto:borrowers@propfunder.com',
                        style='color:var(--accent);text-decoration:none;font-weight:600;')),
                    cls='card'
                ),
                Div(
                    H3('Press & Media'),
                    P('Media enquiries, partnership opportunities, or press information?'),
                    P(A('press@propfunder.com', href='mailto:press@propfunder.com',
                        style='color:var(--accent);text-decoration:none;font-weight:600;')),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section section-dark'
    )

    return Div(hero, offices, general)
