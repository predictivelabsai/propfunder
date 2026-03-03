from fasthtml.common import *


def how_it_works_page():
    hero = Section(
        Div(
            H1('How PropFunder Works'),
            P('A transparent, secure process connecting property developers with investors through mortgage-backed loans.'),
            cls='hero-inner'
        ),
        cls='hero', style='padding:4rem 2rem;'
    )

    for_investors = Section(
        Div(
            Div(
                H2('For Investors'),
                P('Start earning returns in three simple steps.'),
                cls='section-header'
            ),
            Div(
                Div(
                    Div('1', cls='step-num'),
                    Div(
                        H3('Create Your Account'),
                        P('Sign up in minutes. Complete a quick verification process to start investing. '
                          'No minimum balance required to open an account.'),
                        cls='step-content'
                    ),
                    cls='step'
                ),
                Div(
                    Div('2', cls='step-num'),
                    Div(
                        H3('Choose Your Investment Strategy'),
                        P('Browse open property loans and invest manually, or set up Auto Invest to '
                          'automatically diversify across opportunities matching your criteria. Minimum investment from \u20ac50.'),
                        cls='step-content'
                    ),
                    cls='step'
                ),
                Div(
                    Div('3', cls='step-num'),
                    Div(
                        H3('Earn Monthly Returns'),
                        P('Receive monthly interest payments directly to your account. Track your portfolio '
                          'performance in real-time through your dashboard. Typical returns of 8-12% per annum.'),
                        cls='step-content'
                    ),
                    cls='step'
                ),
            ),
            Div(
                A('Start Investing Now', href='/register', cls='btn btn-green'),
                style='text-align:center;margin-top:2rem;'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    for_borrowers = Section(
        Div(
            Div(
                H2('For Borrowers & Developers'),
                P('Fast, flexible financing for your property projects.'),
                cls='section-header'
            ),
            Div(
                Div(
                    Div('1', cls='step-num'),
                    Div(
                        H3('Submit Your Project'),
                        P('Tell us about your property project, financing needs, and timeline. '
                          'We review applications within 48 hours and provide initial feedback.'),
                        cls='step-content'
                    ),
                    cls='step'
                ),
                Div(
                    Div('2', cls='step-num'),
                    Div(
                        H3('Due Diligence & Valuation'),
                        P('Our team conducts thorough property valuation, legal review, and risk assessment. '
                          'We work with independent valuers to ensure accurate LTV ratios.'),
                        cls='step-content'
                    ),
                    cls='step'
                ),
                Div(
                    Div('3', cls='step-num'),
                    Div(
                        H3('Receive Funding'),
                        P('Once approved and funded by our investor community, funds are disbursed '
                          'typically within 2-4 weeks. Loan terms from 6 to 36 months.'),
                        cls='step-content'
                    ),
                    cls='step'
                ),
            ),
            Div(
                A('Apply for Financing', href='/borrowers', cls='btn btn-green'),
                style='text-align:center;margin-top:2rem;'
            ),
            cls='section-inner'
        ),
        cls='section section-dark'
    )

    loan_types = Section(
        Div(
            Div(
                H2('Loan Types We Offer'),
                P('Flexible financing solutions for different property needs.'),
                cls='section-header'
            ),
            Div(
                Div(
                    Div('\U0001f3d7\ufe0f', cls='card-icon'),
                    H3('Development Loans'),
                    P('Finance new construction or major renovation projects. Staged drawdowns available '
                      'based on construction milestones. Terms: 12-36 months.'),
                    cls='card'
                ),
                Div(
                    Div('\U0001f309', cls='card-icon'),
                    H3('Bridge Loans'),
                    P('Short-term financing for property purchases, refinancing, or capital release. '
                      'Fast approval and funding. Terms: 6-18 months.'),
                    cls='card'
                ),
                Div(
                    Div('\U0001f4b0', cls='card-icon'),
                    H3('Bullet Loans'),
                    P('Interest-only payments with principal repaid at maturity. Ideal for projects '
                      'with a clear exit strategy. Terms: 6-24 months.'),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    risk = Section(
        Div(
            Div(
                H2('Risk Management'),
                P('How we protect your investments.'),
                cls='section-header'
            ),
            Div(
                Div(
                    H3('Property-Backed Security'),
                    P('Every loan is secured with a first or second-rank mortgage on real estate, '
                      'providing tangible collateral for your investment.'),
                    cls='card'
                ),
                Div(
                    H3('Conservative LTV Ratios'),
                    P('We maintain strict loan-to-value limits, typically below 75%, ensuring '
                      'a safety buffer between the loan amount and property value.'),
                    cls='card'
                ),
                Div(
                    H3('Independent Valuations'),
                    P('All properties are valued by certified independent appraisers before '
                      'any loan is listed on the platform.'),
                    cls='card'
                ),
                Div(
                    H3('Default Recovery'),
                    P('In case of borrower default, PropFunder manages the full recovery process '
                      'including collateral realisation on behalf of investors.'),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section section-dark'
    )

    return Div(hero, for_investors, for_borrowers, loan_types, risk)
