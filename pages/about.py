from fasthtml.common import *


def about_page():
    hero = Section(
        Div(
            H1('About PropFunder'),
            P('We are building the future of property investment \u2014 making real estate-backed '
              'lending accessible, transparent, and rewarding for everyone.'),
            cls='hero-inner'
        ),
        cls='hero', style='padding:4rem 2rem;'
    )

    mission = Section(
        Div(
            Div(
                Div(
                    H2('Our Mission', cls='font-display',
                       style='font-size:2.2rem;margin-bottom:1.5rem;'),
                    P('PropFunder was founded with a simple belief: property investment should not be '
                      'reserved for institutions and the ultra-wealthy. By leveraging technology, '
                      'we connect everyday investors with vetted real estate opportunities, creating '
                      'value for both investors and property developers.',
                      style='font-size:1.05rem;line-height:1.8;margin-bottom:1.5rem;'),
                    P('Our platform enables investors to earn attractive, steady returns backed by '
                      'tangible property assets, while giving developers access to fast, flexible '
                      'financing outside the traditional banking system.',
                      style='font-size:1.05rem;line-height:1.8;color:var(--gray);'),
                ),
                Div(
                    Div(
                        Div(H3('2020'), P('Founded'), cls='stat-item'),
                        Div(H3('45+'), P('Team Members'), cls='stat-item'),
                        Div(H3('6'), P('Countries'), cls='stat-item'),
                        Div(H3('\u20ac186M'), P('Loans Funded'), cls='stat-item'),
                        style='display:grid;grid-template-columns:1fr 1fr;gap:2rem;'
                    ),
                    style='background:white;padding:2rem;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.06);'
                ),
                cls='two-col'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    values = Section(
        Div(
            Div(
                H2('Our Values'),
                P('The principles that guide everything we do.'),
                cls='section-header'
            ),
            Div(
                Div(
                    Div('\U0001f50d', cls='card-icon'),
                    H3('Transparency'),
                    P('Full disclosure on every loan. Investors see detailed property information, '
                      'valuations, risk ratings, and borrower profiles before investing.'),
                    cls='card'
                ),
                Div(
                    Div('\U0001f6e1\ufe0f', cls='card-icon'),
                    H3('Security'),
                    P('Every loan is backed by real estate collateral. We maintain strict LTV limits '
                      'and work with independent valuers to protect investor capital.'),
                    cls='card'
                ),
                Div(
                    Div('\U0001f91d', cls='card-icon'),
                    H3('Accessibility'),
                    P('Investments from \u20ac50 mean anyone can build a diversified property portfolio. '
                      'No exclusive clubs, no high minimums, no barriers.'),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section section-dark'
    )

    presence = Section(
        Div(
            Div(
                H2('Our Presence'),
                P('Operating across key European markets with a growing footprint.'),
                cls='section-header'
            ),
            Div(
                Div(
                    H3('Headquarters'),
                    P('London, United Kingdom'),
                    P('Our main office and technology hub.', style='color:var(--gray);font-size:0.9rem;'),
                    cls='card'
                ),
                Div(
                    H3('Continental Europe'),
                    P('Berlin, Germany'),
                    P('Serving the DACH region and Central European markets.', style='color:var(--gray);font-size:0.9rem;'),
                    cls='card'
                ),
                Div(
                    H3('Baltics'),
                    P('Tallinn, Estonia'),
                    P('Our Baltic hub covering Estonia, Latvia, and Lithuania.', style='color:var(--gray);font-size:0.9rem;'),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    cta = Section(
        Div(
            H2('Join the PropFunder Community'),
            P('Whether you are an investor looking for returns or a developer seeking financing, '
              'we are here to help.'),
            Div(
                A('Start Investing', href='/investors', cls='btn btn-primary'),
                A('Apply for Financing', href='/borrowers', cls='btn btn-outline'),
                cls='btn-group', style='justify-content:center;'
            ),
        ),
        cls='cta-section'
    )

    return Div(hero, mission, values, presence, cta)
