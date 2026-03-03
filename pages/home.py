from fasthtml.common import *


def home_page():
    hero = Section(
        Div(
            H1('Invest in Property-Backed Loans for Steady Monthly Income'),
            P('A trusted platform connecting investors with vetted real estate opportunities. '
              'Earn attractive returns secured by tangible property assets across Europe and beyond.'),
            Div(
                Span('\u2713 Property-backed security', cls='hero-badge'),
                Span('\u2713 Monthly interest payments', cls='hero-badge'),
                Span('\u2713 From \u20ac50 minimum', cls='hero-badge'),
                cls='hero-badges'
            ),
            Div(
                A('Start Investing', href='/investors', cls='btn btn-primary'),
                A('Raise Capital', href='/borrowers', cls='btn btn-outline'),
                cls='btn-group'
            ),
            cls='hero-inner'
        ),
        cls='hero'
    )

    stats = Section(
        Div(
            Div(H3('9.8%'), P('Average Return'), cls='stat-item'),
            Div(H3('\u20ac24.5M'), P('Investor Earnings'), cls='stat-item'),
            Div(H3('\u20ac186M'), P('Money Lent'), cls='stat-item'),
            Div(H3('12,400+'), P('Investors'), cls='stat-item'),
            Div(H3('850+'), P('Funded Projects'), cls='stat-item'),
            Div(H3('6'), P('Countries'), cls='stat-item'),
            cls='stats-grid'
        ),
        cls='stats-bar'
    )

    products = Section(
        Div(
            Div(
                H2('Find Your Perfect Investment Product'),
                P('Whether you prefer hands-on control or automated investing, we have the right solution.'),
                cls='section-header'
            ),
            Div(
                Div(
                    Div('\u26a1', cls='card-icon'),
                    H3('Auto Invest'),
                    P('Set your investment preferences once. We handle the rest with smart diversification across property loans.'),
                    A('Learn more \u2192', href='/how-it-works', cls='text-primary',
                      style='display:block;margin-top:1rem;text-decoration:none;font-weight:600;font-size:0.9rem'),
                    cls='card'
                ),
                Div(
                    Div('\u270b', cls='card-icon'),
                    H3('Manual Invest'),
                    P('Hand-pick every project. Total control over which property loans you invest in, with full transparency.'),
                    A('View open loans \u2192', href='/investors', cls='text-primary',
                      style='display:block;margin-top:1rem;text-decoration:none;font-weight:600;font-size:0.9rem'),
                    cls='card'
                ),
                Div(
                    Div('\u21c4', cls='card-icon'),
                    H3('Secondary Market'),
                    P('Adjust your portfolio anytime. Buy or sell investments on our secondary market for added liquidity.'),
                    cls='card'
                ),
                cls='card-grid'
            ),
            cls='section-inner'
        ),
        cls='section'
    )

    how_it_works = Section(
        Div(
            Div(
                H2('How Does It Work?'),
                P('We connect property developers with investors through a transparent, secure platform.'),
                cls='section-header'
            ),
            Div(
                Div(
                    Div(
                        H3('Borrowers', style='color:var(--accent);margin-bottom:1rem;'),
                        P('Property developers and SMEs across Europe rely on PropFunder for fast, '
                          'flexible funding to complete projects. Interest rates from 8% per annum.'),
                        A('Need financing? \u2192', href='/borrowers',
                          style='color:var(--accent);text-decoration:none;font-weight:600;display:block;margin-top:1rem;font-size:0.9rem'),
                        cls='card', style='border-left: 4px solid var(--accent);'
                    ),
                    Div(
                        H3('PropFunder', style='color:var(--primary);margin-bottom:1rem;'),
                        P('We manage the entire loan lifecycle \u2014 from deal origination and risk analysis '
                          'to collateral security and repayments \u2014 with rigorous oversight and transparency.'),
                        cls='card', style='border-left: 4px solid var(--primary);'
                    ),
                    Div(
                        H3('Investors', style='color:var(--primary-light);margin-bottom:1rem;'),
                        P('Join thousands of investors earning consistent returns. Historically, '
                          'PropFunder investors have earned 9.8% p.a. with broad diversification.'),
                        A('Start investing \u2192', href='/investors',
                          style='color:var(--primary);text-decoration:none;font-weight:600;display:block;margin-top:1rem;font-size:0.9rem'),
                        cls='card', style='border-left: 4px solid var(--primary-light);'
                    ),
                    cls='card-grid'
                ),
                cls='section-inner'
            ),
            cls='section-inner'
        ),
        cls='section section-dark'
    )

    security = Section(
        Div(
            Div(
                Div(
                    H2('Mortgage-Backed Investments', cls='font-display',
                       style='font-size:2.2rem;margin-bottom:1rem;'),
                    P('All PropFunder loans are backed by real estate and secured with a mortgage '
                      'in favour of our investors.',
                      style='font-size:1.15rem;margin-bottom:1.5rem;'),
                    P('In the rare event of borrower default, PropFunder steps in to manage the recovery '
                      'process \u2014 including collateral realisation \u2014 giving you peace of mind.',
                      style='color:var(--gray);margin-bottom:2rem;'),
                    A('Learn about risk management', href='/risk', cls='btn btn-green'),
                ),
                Div(
                    Div(
                        Div(H3('LTV < 75%'), P('Maximum loan-to-value ratio'), cls='stat-item'),
                        Div(H3('100%'), P('Loans with real estate collateral'), cls='stat-item'),
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

    cta = Section(
        Div(
            H2('Ready to Start Earning?'),
            P('Join over 12,000 investors earning consistent monthly income from property-backed loans.'),
            Div(
                A('Create Free Account', href='/register', cls='btn btn-primary'),
                A('Learn More', href='/how-it-works', cls='btn btn-outline'),
                cls='btn-group', style='justify-content:center;'
            ),
        ),
        cls='cta-section'
    )

    return Div(hero, stats, products, how_it_works, security, cta)
