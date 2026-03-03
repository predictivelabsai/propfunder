from fasthtml.common import *


def borrowers_page():
    hero = Section(
        Div(
            H1('Fast, Flexible Property Financing'),
            P('Access funding for your real estate projects without the red tape, long waits, '
              'or excessive admin of traditional banks.'),
            Div(
                A('Apply for Financing', href='/contact', cls='btn btn-primary'),
                cls='btn-group'
            ),
            cls='hero-inner'
        ),
        cls='hero', style='padding:4rem 2rem;'
    )

    benefits = Section(
        Div(
            Div(
                H2('Why Borrow With PropFunder'),
                P('We help property developers access capital quickly and efficiently.'),
                cls='section-header'
            ),
            Div(
                Div(
                    Div('\u23f1\ufe0f', cls='card-icon'),
                    H3('Fast Decision Making'),
                    P('Receive an initial response within 48 hours. Full approval and funding '
                      'typically completed within 2-4 weeks.'),
                    cls='card'
                ),
                Div(
                    Div('\U0001f4b5', cls='card-icon'),
                    H3('Competitive Rates'),
                    P('Interest rates starting from 8% per annum. Transparent fee structure '
                      'with no hidden costs or penalties.'),
                    cls='card'
                ),
                Div(
                    Div('\U0001f4cb', cls='card-icon'),
                    H3('Flexible Terms'),
                    P('Loan terms from 6 to 36 months. Bullet, bridge, and development loan '
                      'structures available to match your project needs.'),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    eligible = Section(
        Div(
            Div(
                H2('Eligible Property Types'),
                P('We finance a wide range of property projects across Europe.'),
                cls='section-header'
            ),
            Div(
                Div(
                    H3('Residential'),
                    P('Houses, apartments, multi-family developments, and residential conversions.'),
                    cls='card'
                ),
                Div(
                    H3('Commercial'),
                    P('Office buildings, retail spaces, warehouses, and mixed-use developments.'),
                    cls='card'
                ),
                Div(
                    H3('Development'),
                    P('New-build projects, renovations, land purchases with planning permission.'),
                    cls='card'
                ),
                Div(
                    H3('Industrial'),
                    P('Factories, logistics centres, storage facilities, and industrial conversions.'),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section section-dark'
    )

    loan_details = Section(
        Div(
            Div(
                H2('Loan Details'),
                cls='section-header'
            ),
            Div(
                Div(H3('\u20ac50K - \u20ac5M'), P('Loan Amount Range'), cls='stat-item'),
                Div(H3('6 - 36'), P('Term (Months)'), cls='stat-item'),
                Div(H3('Up to 75%'), P('Loan-to-Value'), cls='stat-item'),
                Div(H3('From 8%'), P('Interest Rate (p.a.)'), cls='stat-item'),
                cls='stats-grid'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    process = Section(
        Div(
            Div(
                H2('Application Process'),
                cls='section-header'
            ),
            Div(
                Div('1', cls='step-num'),
                Div(
                    H3('Submit Application'),
                    P('Fill out our online form with your project details, property information, '
                      'and financing requirements.'),
                    cls='step-content'
                ),
                cls='step'
            ),
            Div(
                Div('2', cls='step-num'),
                Div(
                    H3('Property Valuation'),
                    P('Independent valuers assess the property. We review legal documentation '
                      'and conduct thorough due diligence.'),
                    cls='step-content'
                ),
                cls='step'
            ),
            Div(
                Div('3', cls='step-num'),
                Div(
                    H3('Loan Approved & Listed'),
                    P('Your loan is listed on the platform for our investor community to fund. '
                      'Mortgage is registered in favour of investors.'),
                    cls='step-content'
                ),
                cls='step'
            ),
            Div(
                Div('4', cls='step-num'),
                Div(
                    H3('Receive Funds'),
                    P('Once the loan is fully funded, the capital is transferred to your account. '
                      'Monthly interest payments begin as agreed.'),
                    cls='step-content'
                ),
                cls='step'
            ),
            Div(
                A('Apply Now', href='/contact', cls='btn btn-green'),
                style='text-align:center;margin-top:2rem;'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    return Div(hero, benefits, eligible, loan_details, process)
