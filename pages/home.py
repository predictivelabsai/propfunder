from fasthtml.common import *


def home_page():
    hero = Section(
        Div(
            Div(
                H1('Invest in Property-Backed Loans for Steady Monthly Income',
                   cls='font-display text-4xl md:text-5xl font-extrabold leading-tight max-w-3xl mb-6 text-white'),
                P('A trusted platform connecting investors with vetted real estate opportunities. '
                  'Earn attractive returns secured by tangible property assets across Europe and beyond.',
                  cls='text-lg max-w-2xl text-white/90 mb-8 leading-relaxed'),
                Div(
                    Span('\u2713 Property-backed security',
                         cls='flex items-center gap-2 bg-white/10 border border-white/15 px-4 py-2 rounded-full text-sm text-white'),
                    Span('\u2713 Monthly interest payments',
                         cls='flex items-center gap-2 bg-white/10 border border-white/15 px-4 py-2 rounded-full text-sm text-white'),
                    Span('\u2713 From \u20ac50 minimum',
                         cls='flex items-center gap-2 bg-white/10 border border-white/15 px-4 py-2 rounded-full text-sm text-white'),
                    cls='flex gap-4 mb-8 flex-wrap'
                ),
                Div(
                    A('Start Investing', href='/investors',
                      cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-accent text-dark hover:bg-accent-dark transition-colors'),
                    A('Raise Capital', href='/borrowers',
                      cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-transparent text-white border-2 border-white/30 hover:border-white hover:bg-white/10 transition-colors'),
                    cls='flex gap-4 flex-wrap'
                ),
                cls='max-w-7xl mx-auto relative z-10'
            ),
            cls='hero-pattern'
        ),
        cls='bg-gradient-to-br from-dark via-primary-dark to-primary py-24 px-8 relative overflow-hidden'
    )

    stats = Section(
        Div(
            Div(H3('9.8%', cls='text-3xl font-extrabold text-primary mb-1'), P('Average Return', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
            Div(H3('\u20ac24.5M', cls='text-3xl font-extrabold text-primary mb-1'), P('Investor Earnings', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
            Div(H3('\u20ac186M', cls='text-3xl font-extrabold text-primary mb-1'), P('Money Lent', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
            Div(H3('12,400+', cls='text-3xl font-extrabold text-primary mb-1'), P('Investors', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
            Div(H3('850+', cls='text-3xl font-extrabold text-primary mb-1'), P('Funded Projects', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
            Div(H3('6', cls='text-3xl font-extrabold text-primary mb-1'), P('Countries', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
            cls='max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-6 gap-8'
        ),
        cls='bg-white border-b border-gray-200 py-8 px-8'
    )

    products = Section(
        Div(
            Div(
                H2('Find Your Perfect Investment Product',
                   cls='font-display text-3xl font-bold text-gray-900 mb-4'),
                P('Whether you prefer hands-on control or automated investing, we have the right solution.',
                  cls='text-base text-gray-500 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    Div('\u26a1', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Auto Invest', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Set your investment preferences once. We handle the rest with smart diversification across property loans.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    A('Learn more \u2192', href='/how-it-works',
                      cls='block mt-4 no-underline font-semibold text-sm text-primary'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                Div(
                    Div('\u270b', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Manual Invest', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Hand-pick every project. Total control over which property loans you invest in, with full transparency.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    A('View open loans \u2192', href='/investors',
                      cls='block mt-4 no-underline font-semibold text-sm text-primary'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                Div(
                    Div('\u21c4', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Secondary Market', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Adjust your portfolio anytime. Buy or sell investments on our secondary market for added liquidity.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    how_it_works = Section(
        Div(
            Div(
                H2('How Does It Work?', cls='font-display text-3xl font-bold text-white mb-4'),
                P('We connect property developers with investors through a transparent, secure platform.',
                  cls='text-base text-gray-300 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    H3('Borrowers', cls='text-accent mb-4 text-lg font-bold'),
                    P('Property developers and SMEs across Europe rely on PropFunder for fast, '
                      'flexible funding to complete projects. Interest rates from 8% per annum.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    A('Need financing? \u2192', href='/borrowers',
                      cls='block mt-4 text-accent no-underline font-semibold text-sm'),
                    cls='bg-white rounded-xl p-8 shadow-sm border-l-4 border-accent'
                ),
                Div(
                    H3('PropFunder', cls='text-primary mb-4 text-lg font-bold'),
                    P('We manage the entire loan lifecycle \u2014 from deal origination and risk analysis '
                      'to collateral security and repayments \u2014 with rigorous oversight and transparency.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border-l-4 border-primary'
                ),
                Div(
                    H3('Investors', cls='text-primary-light mb-4 text-lg font-bold'),
                    P('Join thousands of investors earning consistent returns. Historically, '
                      'PropFunder investors have earned 9.8% p.a. with broad diversification.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    A('Start investing \u2192', href='/investors',
                      cls='block mt-4 text-primary no-underline font-semibold text-sm'),
                    cls='bg-white rounded-xl p-8 shadow-sm border-l-4 border-primary-light'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='bg-dark text-white py-20 px-8'
    )

    security = Section(
        Div(
            Div(
                Div(
                    H2('Mortgage-Backed Investments',
                       cls='font-display text-3xl mb-4'),
                    P('All PropFunder loans are backed by real estate and secured with a mortgage '
                      'in favour of our investors.',
                      cls='text-lg mb-6'),
                    P('In the rare event of borrower default, PropFunder steps in to manage the recovery '
                      'process \u2014 including collateral realisation \u2014 giving you peace of mind.',
                      cls='text-gray-500 mb-8'),
                    A('Learn about risk management', href='/risk',
                      cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-primary text-white hover:bg-primary-light transition-colors'),
                ),
                Div(
                    Div(
                        Div(H3('LTV < 75%', cls='text-3xl font-extrabold text-primary mb-1'), P('Maximum loan-to-value ratio', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                        Div(H3('100%', cls='text-3xl font-extrabold text-primary mb-1'), P('Loans with real estate collateral', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                        cls='grid grid-cols-2 gap-8'
                    ),
                    cls='bg-white p-8 rounded-xl shadow-sm'
                ),
                cls='grid grid-cols-1 md:grid-cols-2 gap-16 items-center'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    cta = Section(
        Div(
            H2('Ready to Start Earning?',
               cls='font-display text-3xl mb-4'),
            P('Join over 12,000 investors earning consistent monthly income from property-backed loans.',
              cls='text-lg text-white/90 max-w-xl mx-auto mb-8'),
            Div(
                A('Create Free Account', href='/register',
                  cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-accent text-dark hover:bg-accent-dark transition-colors'),
                A('Learn More', href='/how-it-works',
                  cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-transparent text-white border-2 border-white/30 hover:border-white hover:bg-white/10 transition-colors'),
                cls='flex gap-4 flex-wrap justify-center'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='bg-gradient-to-br from-primary to-primary-dark text-white py-20 px-8 text-center'
    )

    return Div(hero, stats, products, how_it_works, security, cta)
