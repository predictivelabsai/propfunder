from fasthtml.common import *


def borrowers_page():
    hero = Section(
        Div(
            H1('Fast, Flexible Property Financing', cls='font-display text-4xl font-extrabold text-white mb-4'),
            P('Access funding for your real estate projects without the red tape, long waits, or excessive admin of traditional banks.',
              cls='text-lg text-white/90 max-w-2xl mb-8'),
            Div(
                A('Apply for Financing', href='/contact',
                  cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-accent text-dark hover:bg-accent-dark transition-colors'),
                cls='flex gap-4 flex-wrap'
            ),
            cls='max-w-7xl mx-auto relative z-10'
        ),
        cls='bg-gradient-to-br from-dark via-primary-dark to-primary py-16 px-8'
    )

    benefits = Section(
        Div(
            Div(
                H2('Why Borrow With PropFunder', cls='font-display text-3xl font-bold text-gray-900 mb-4'),
                P('We help property developers access capital quickly and efficiently.', cls='text-base text-gray-500 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    Div('\u23f1\ufe0f', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Fast Decision Making', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Receive an initial response within 48 hours. Full approval and funding typically completed within 2-4 weeks.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                Div(
                    Div('\U0001f4b5', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Competitive Rates', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Interest rates starting from 8% per annum. Transparent fee structure with no hidden costs or penalties.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                Div(
                    Div('\U0001f4cb', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Flexible Terms', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Loan terms from 6 to 36 months. Bullet, bridge, and development loan structures available to match your project needs.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    eligible = Section(
        Div(
            Div(
                H2('Eligible Property Types', cls='font-display text-3xl font-bold text-white mb-4'),
                P('We finance a wide range of property projects across Europe.', cls='text-base text-gray-300 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    H3('Residential', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Houses, apartments, multi-family developments, and residential conversions.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Commercial', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Office buildings, retail spaces, warehouses, and mixed-use developments.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Development', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('New-build projects, renovations, land purchases with planning permission.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Industrial', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Factories, logistics centres, storage facilities, and industrial conversions.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                cls='grid grid-cols-1 md:grid-cols-2 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='bg-dark text-white py-20 px-8'
    )

    loan_details = Section(
        Div(
            Div(
                H2('Loan Details', cls='font-display text-3xl font-bold text-gray-900 mb-4'),
                cls='text-center mb-12'
            ),
            Div(
                Div(H3('\u20ac50K - \u20ac5M', cls='text-3xl font-extrabold text-primary mb-1'), P('Loan Amount Range', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                Div(H3('6 - 36', cls='text-3xl font-extrabold text-primary mb-1'), P('Term (Months)', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                Div(H3('Up to 75%', cls='text-3xl font-extrabold text-primary mb-1'), P('Loan-to-Value', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                Div(H3('From 8%', cls='text-3xl font-extrabold text-primary mb-1'), P('Interest Rate (p.a.)', cls='text-xs text-gray-500 uppercase tracking-wider'), cls='text-center'),
                cls='max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    def step_item(num, title, desc):
        return Div(
            Div(num, cls='w-12 h-12 min-w-[48px] bg-accent text-dark rounded-full flex items-center justify-center font-extrabold text-lg'),
            Div(
                H3(title, cls='text-lg font-bold mb-2'),
                P(desc, cls='text-gray-500 text-sm'),
            ),
            cls='flex gap-6 mb-10'
        )

    process = Section(
        Div(
            Div(
                H2('Application Process', cls='font-display text-3xl font-bold text-gray-900 mb-4'),
                cls='text-center mb-12'
            ),
            step_item('1', 'Submit Application',
                       'Fill out our online form with your project details, property information, and financing requirements.'),
            step_item('2', 'Property Valuation',
                       'Independent valuers assess the property. We review legal documentation and conduct thorough due diligence.'),
            step_item('3', 'Loan Approved & Listed',
                       'Your loan is listed on the platform for our investor community to fund. Mortgage is registered in favour of investors.'),
            step_item('4', 'Receive Funds',
                       'Once the loan is fully funded, the capital is transferred to your account. Monthly interest payments begin as agreed.'),
            Div(
                A('Apply Now', href='/contact',
                  cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-primary text-white hover:bg-primary-light transition-colors'),
                cls='text-center mt-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    return Div(hero, benefits, eligible, loan_details, process)
