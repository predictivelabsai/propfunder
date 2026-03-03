from fasthtml.common import *


def contact_page():
    hero = Section(
        Div(
            H1('Contact Us', cls='font-display text-4xl font-extrabold text-white mb-4'),
            P('Get in touch with our team. We are here to help with any questions about investing or borrowing through PropFunder.',
              cls='text-lg text-white/90 max-w-2xl'),
            cls='max-w-7xl mx-auto relative z-10'
        ),
        cls='bg-gradient-to-br from-dark via-primary-dark to-primary py-16 px-8'
    )

    offices = Section(
        Div(
            Div(
                H2('Our Offices', cls='font-display text-3xl font-bold text-gray-900 mb-4'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    H3('London (HQ)', cls='text-lg font-bold text-gray-900 mb-3'),
                    P(Strong('Address'), Br(),
                      '71-75 Shelton Street', Br(),
                      'Covent Garden', Br(),
                      'London WC2H 9JQ', Br(),
                      'United Kingdom', cls='mb-4 text-sm text-gray-600 leading-relaxed'),
                    P(Strong('Email'), Br(),
                      A('london@propfunder.com', href='mailto:london@propfunder.com',
                        cls='text-primary no-underline'), cls='mb-4 text-sm'),
                    P(Strong('Phone'), Br(),
                      A('+44 20 7123 4567', href='tel:+442071234567',
                        cls='text-primary no-underline'), cls='text-sm'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Berlin', cls='text-lg font-bold text-gray-900 mb-3'),
                    P(Strong('Address'), Br(),
                      'Friedrichstra\u00dfe 123', Br(),
                      '10117 Berlin', Br(),
                      'Germany', cls='mb-4 text-sm text-gray-600 leading-relaxed'),
                    P(Strong('Email'), Br(),
                      A('berlin@propfunder.com', href='mailto:berlin@propfunder.com',
                        cls='text-primary no-underline'), cls='mb-4 text-sm'),
                    P(Strong('Phone'), Br(),
                      A('+49 30 1234 5678', href='tel:+493012345678',
                        cls='text-primary no-underline'), cls='text-sm'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Tallinn', cls='text-lg font-bold text-gray-900 mb-3'),
                    P(Strong('Address'), Br(),
                      'Narva mnt 5', Br(),
                      '10117 Tallinn', Br(),
                      'Estonia', cls='mb-4 text-sm text-gray-600 leading-relaxed'),
                    P(Strong('Email'), Br(),
                      A('tallinn@propfunder.com', href='mailto:tallinn@propfunder.com',
                        cls='text-primary no-underline'), cls='mb-4 text-sm'),
                    P(Strong('Phone'), Br(),
                      A('+372 641 2345', href='tel:+3726412345',
                        cls='text-primary no-underline'), cls='text-sm'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    general = Section(
        Div(
            Div(
                H2('General Enquiries', cls='font-display text-3xl font-bold text-white mb-4'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    H3('Investor Support', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Questions about your account, investments, or returns?', cls='text-gray-500 text-sm mb-4'),
                    P(A('investors@propfunder.com', href='mailto:investors@propfunder.com',
                        cls='text-accent no-underline font-semibold')),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Borrower Enquiries', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Want to apply for financing or have questions about the process?', cls='text-gray-500 text-sm mb-4'),
                    P(A('borrowers@propfunder.com', href='mailto:borrowers@propfunder.com',
                        cls='text-accent no-underline font-semibold')),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Press & Media', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Media enquiries, partnership opportunities, or press information?', cls='text-gray-500 text-sm mb-4'),
                    P(A('press@propfunder.com', href='mailto:press@propfunder.com',
                        cls='text-accent no-underline font-semibold')),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='bg-dark text-white py-20 px-8'
    )

    return Div(hero, offices, general)
