from fasthtml.common import *


def investors_page():
    hero = Section(
        Div(
            H1('Invest in Property-Backed Loans', cls='font-display text-4xl font-extrabold text-white mb-4'),
            P('Earn attractive returns secured by real estate. Diversify your portfolio with investments starting from just \u20ac50.',
              cls='text-lg text-white/90 max-w-2xl'),
            cls='max-w-7xl mx-auto relative z-10'
        ),
        cls='bg-gradient-to-br from-dark via-primary-dark to-primary py-16 px-8'
    )

    benefits = Section(
        Div(
            Div(
                H2('Why Invest With PropFunder', cls='font-display text-3xl font-bold text-gray-900 mb-4'),
                P('Property-backed returns with transparency and security.', cls='text-base text-gray-500 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    Div('\U0001f4c8', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Attractive Returns', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Historically, our investors have earned an average of 9.8% per annum. Interest is paid monthly directly to your account.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                Div(
                    Div('\U0001f3e0', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Real Estate Security', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('All investments are backed by property collateral with conservative LTV ratios, providing tangible security for your capital.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                Div(
                    Div('\U0001f4ca', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Portfolio Diversification', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Spread your investment across multiple property types, countries, and risk levels. An uncorrelated asset class for your portfolio.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    investment_options = Section(
        Div(
            Div(
                H2('Investment Options', cls='font-display text-3xl font-bold text-white mb-4'),
                P('Choose the approach that suits your style.', cls='text-base text-gray-300 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    H3('Auto Invest', cls='text-accent mb-4 text-lg font-bold'),
                    P('Set your criteria and let our algorithm invest for you automatically.', cls='mb-6 text-gray-500 text-sm'),
                    Div(
                        P('\u2713 Automated portfolio building', cls='mb-2 text-sm text-gray-500'),
                        P('\u2713 Custom risk and return preferences', cls='mb-2 text-sm text-gray-500'),
                        P('\u2713 Broad diversification', cls='mb-2 text-sm text-gray-500'),
                        P('\u2713 Reinvestment of returns', cls='mb-2 text-sm text-gray-500'),
                    ),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Manual Invest', cls='text-primary mb-4 text-lg font-bold'),
                    P('Browse and select individual property loans yourself.', cls='mb-6 text-gray-500 text-sm'),
                    Div(
                        P('\u2713 Full control over selections', cls='mb-2 text-sm text-gray-500'),
                        P('\u2713 Detailed project information', cls='mb-2 text-sm text-gray-500'),
                        P('\u2713 Choose by location, type, LTV', cls='mb-2 text-sm text-gray-500'),
                        P('\u2713 Direct project monitoring', cls='mb-2 text-sm text-gray-500'),
                    ),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Secondary Market', cls='text-primary-light mb-4 text-lg font-bold'),
                    P('Buy and sell existing investment positions.', cls='mb-6 text-gray-500 text-sm'),
                    Div(
                        P('\u2713 Added liquidity for your portfolio', cls='mb-2 text-sm text-gray-500'),
                        P('\u2713 Access seasoned investments', cls='mb-2 text-sm text-gray-500'),
                        P('\u2713 Adjust portfolio anytime', cls='mb-2 text-sm text-gray-500'),
                        P('\u2713 Competitive pricing', cls='mb-2 text-sm text-gray-500'),
                    ),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='bg-dark text-white py-20 px-8'
    )

    key_figures = Section(
        Div(
            Div(
                H2('Investment at a Glance', cls='font-display text-3xl font-bold text-gray-900 mb-4'),
                cls='text-center mb-12'
            ),
            Div(
                Div(H3('\u20ac50', cls='text-3xl font-extrabold text-primary mb-1'), P('Minimum Investment', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                Div(H3('8-12%', cls='text-3xl font-extrabold text-primary mb-1'), P('Annual Interest Rate', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                Div(H3('6-36', cls='text-3xl font-extrabold text-primary mb-1'), P('Loan Term (Months)', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                Div(H3('< 75%', cls='text-3xl font-extrabold text-primary mb-1'), P('Maximum LTV Ratio', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                cls='max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    cta = Section(
        Div(
            H2('Start Building Your Property Portfolio', cls='font-display text-3xl mb-4'),
            P('Create your free account and make your first investment in minutes.',
              cls='text-lg text-white/90 max-w-xl mx-auto mb-8'),
            A('Create Account', href='/register',
              cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-accent text-dark hover:bg-accent-dark transition-colors'),
        ),
        cls='bg-gradient-to-br from-primary to-primary-dark text-white py-20 px-8 text-center'
    )

    return Div(hero, benefits, investment_options, key_figures, cta)
