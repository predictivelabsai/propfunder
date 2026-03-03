from fasthtml.common import *


def investors_page():
    hero = Section(
        Div(
            H1('Invest in Property-Backed Loans'),
            P('Earn attractive returns secured by real estate. Diversify your portfolio with '
              'investments starting from just \u20ac50.'),
            cls='hero-inner'
        ),
        cls='hero', style='padding:4rem 2rem;'
    )

    benefits = Section(
        Div(
            Div(
                H2('Why Invest With PropFunder'),
                P('Property-backed returns with transparency and security.'),
                cls='section-header'
            ),
            Div(
                Div(
                    Div('\U0001f4c8', cls='card-icon'),
                    H3('Attractive Returns'),
                    P('Historically, our investors have earned an average of 9.8% per annum. '
                      'Interest is paid monthly directly to your account.'),
                    cls='card'
                ),
                Div(
                    Div('\U0001f3e0', cls='card-icon'),
                    H3('Real Estate Security'),
                    P('All investments are backed by property collateral with conservative LTV ratios, '
                      'providing tangible security for your capital.'),
                    cls='card'
                ),
                Div(
                    Div('\U0001f4ca', cls='card-icon'),
                    H3('Portfolio Diversification'),
                    P('Spread your investment across multiple property types, countries, and risk levels. '
                      'An uncorrelated asset class for your portfolio.'),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    investment_options = Section(
        Div(
            Div(
                H2('Investment Options'),
                P('Choose the approach that suits your style.'),
                cls='section-header'
            ),
            Div(
                Div(
                    H3('Auto Invest', style='color:var(--accent);margin-bottom:1rem;'),
                    P('Set your criteria and let our algorithm invest for you automatically.',
                      style='margin-bottom:1.5rem;'),
                    Div(
                        P('\u2713 Automated portfolio building', style='margin-bottom:0.5rem;'),
                        P('\u2713 Custom risk and return preferences', style='margin-bottom:0.5rem;'),
                        P('\u2713 Broad diversification', style='margin-bottom:0.5rem;'),
                        P('\u2713 Reinvestment of returns', style='margin-bottom:0.5rem;'),
                    ),
                    cls='card'
                ),
                Div(
                    H3('Manual Invest', style='color:var(--primary);margin-bottom:1rem;'),
                    P('Browse and select individual property loans yourself.',
                      style='margin-bottom:1.5rem;'),
                    Div(
                        P('\u2713 Full control over selections', style='margin-bottom:0.5rem;'),
                        P('\u2713 Detailed project information', style='margin-bottom:0.5rem;'),
                        P('\u2713 Choose by location, type, LTV', style='margin-bottom:0.5rem;'),
                        P('\u2713 Direct project monitoring', style='margin-bottom:0.5rem;'),
                    ),
                    cls='card'
                ),
                Div(
                    H3('Secondary Market', style='color:var(--primary-light);margin-bottom:1rem;'),
                    P('Buy and sell existing investment positions.',
                      style='margin-bottom:1.5rem;'),
                    Div(
                        P('\u2713 Added liquidity for your portfolio', style='margin-bottom:0.5rem;'),
                        P('\u2713 Access seasoned investments', style='margin-bottom:0.5rem;'),
                        P('\u2713 Adjust portfolio anytime', style='margin-bottom:0.5rem;'),
                        P('\u2713 Competitive pricing', style='margin-bottom:0.5rem;'),
                    ),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section section-dark'
    )

    key_figures = Section(
        Div(
            Div(
                H2('Investment at a Glance'),
                cls='section-header'
            ),
            Div(
                Div(H3('\u20ac50'), P('Minimum Investment'), cls='stat-item'),
                Div(H3('8-12%'), P('Annual Interest Rate'), cls='stat-item'),
                Div(H3('6-36'), P('Loan Term (Months)'), cls='stat-item'),
                Div(H3('< 75%'), P('Maximum LTV Ratio'), cls='stat-item'),
                cls='stats-grid'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    cta = Section(
        Div(
            H2('Start Building Your Property Portfolio'),
            P('Create your free account and make your first investment in minutes.'),
            A('Create Account', href='/register', cls='btn btn-primary'),
        ),
        cls='cta-section'
    )

    return Div(hero, benefits, investment_options, key_figures, cta)
