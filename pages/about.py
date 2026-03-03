from fasthtml.common import *


def about_page():
    hero = Section(
        Div(
            H1('About PropFunder', cls='font-display text-4xl font-extrabold text-white mb-4'),
            P('We are building the future of property investment \u2014 making real estate-backed '
              'lending accessible, transparent, and rewarding for everyone.',
              cls='text-lg text-white/90 max-w-2xl'),
            cls='max-w-7xl mx-auto relative z-10'
        ),
        cls='bg-gradient-to-br from-dark via-primary-dark to-primary py-16 px-8'
    )

    mission = Section(
        Div(
            Div(
                Div(
                    H2('Our Mission', cls='font-display text-3xl mb-6'),
                    P('PropFunder was founded with a simple belief: property investment should not be '
                      'reserved for institutions and the ultra-wealthy. By leveraging technology, '
                      'we connect everyday investors with vetted real estate opportunities, creating '
                      'value for both investors and property developers.',
                      cls='text-base leading-relaxed mb-6'),
                    P('Our platform enables investors to earn attractive, steady returns backed by '
                      'tangible property assets, while giving developers access to fast, flexible '
                      'financing outside the traditional banking system.',
                      cls='text-base leading-relaxed text-gray-500'),
                ),
                Div(
                    Div(
                        Div(H3('2020', cls='text-3xl font-extrabold text-primary mb-1'), P('Founded', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                        Div(H3('45+', cls='text-3xl font-extrabold text-primary mb-1'), P('Team Members', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                        Div(H3('6', cls='text-3xl font-extrabold text-primary mb-1'), P('Countries', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                        Div(H3('\u20ac186M', cls='text-3xl font-extrabold text-primary mb-1'), P('Loans Funded', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
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

    values = Section(
        Div(
            Div(
                H2('Our Values', cls='font-display text-3xl font-bold text-white mb-4'),
                P('The principles that guide everything we do.', cls='text-base text-gray-300 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    Div('\U0001f50d', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Transparency', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Full disclosure on every loan. Investors see detailed property information, valuations, risk ratings, and borrower profiles before investing.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    Div('\U0001f6e1\ufe0f', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Security', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Every loan is backed by real estate collateral. We maintain strict LTV limits and work with independent valuers to protect investor capital.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    Div('\U0001f91d', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Accessibility', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Investments from \u20ac50 mean anyone can build a diversified property portfolio. No exclusive clubs, no high minimums, no barriers.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='bg-dark text-white py-20 px-8'
    )

    presence = Section(
        Div(
            Div(
                H2('Our Presence', cls='font-display text-3xl font-bold text-gray-900 mb-4'),
                P('Operating across key European markets with a growing footprint.', cls='text-base text-gray-500 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    H3('Headquarters', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('London, United Kingdom', cls='text-gray-900 mb-1'),
                    P('Our main office and technology hub.', cls='text-gray-500 text-sm'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Continental Europe', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Berlin, Germany', cls='text-gray-900 mb-1'),
                    P('Serving the DACH region and Central European markets.', cls='text-gray-500 text-sm'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Baltics', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Tallinn, Estonia', cls='text-gray-900 mb-1'),
                    P('Our Baltic hub covering Estonia, Latvia, and Lithuania.', cls='text-gray-500 text-sm'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    cta = Section(
        Div(
            H2('Join the PropFunder Community', cls='font-display text-3xl mb-4'),
            P('Whether you are an investor looking for returns or a developer seeking financing, we are here to help.',
              cls='text-lg text-white/90 max-w-xl mx-auto mb-8'),
            Div(
                A('Start Investing', href='/investors',
                  cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-accent text-dark hover:bg-accent-dark transition-colors'),
                A('Apply for Financing', href='/borrowers',
                  cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-transparent text-white border-2 border-white/30 hover:border-white hover:bg-white/10 transition-colors'),
                cls='flex gap-4 flex-wrap justify-center'
            ),
        ),
        cls='bg-gradient-to-br from-primary to-primary-dark text-white py-20 px-8 text-center'
    )

    return Div(hero, mission, values, presence, cta)
