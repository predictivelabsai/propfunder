from fasthtml.common import *


def how_it_works_page():
    hero = Section(
        Div(
            H1('How PropFunder Works', cls='font-display text-4xl font-extrabold text-white mb-4'),
            P('A transparent, secure process connecting property developers with investors through mortgage-backed loans.',
              cls='text-lg text-white/90 max-w-2xl'),
            cls='max-w-7xl mx-auto relative z-10'
        ),
        cls='bg-gradient-to-br from-dark via-primary-dark to-primary py-16 px-8'
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

    for_investors = Section(
        Div(
            Div(
                H2('For Investors', cls='font-display text-3xl font-bold text-gray-900 mb-4'),
                P('Start earning returns in three simple steps.', cls='text-base text-gray-500 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            step_item('1', 'Create Your Account',
                       'Sign up in minutes. Complete a quick verification process to start investing. No minimum balance required to open an account.'),
            step_item('2', 'Choose Your Investment Strategy',
                       'Browse open property loans and invest manually, or set up Auto Invest to automatically diversify across opportunities matching your criteria. Minimum investment from \u20ac50.'),
            step_item('3', 'Earn Monthly Returns',
                       'Receive monthly interest payments directly to your account. Track your portfolio performance in real-time through your dashboard. Typical returns of 8-12% per annum.'),
            Div(
                A('Start Investing Now', href='/register',
                  cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-primary text-white hover:bg-primary-light transition-colors'),
                cls='text-center mt-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    for_borrowers = Section(
        Div(
            Div(
                H2('For Borrowers & Developers', cls='font-display text-3xl font-bold text-white mb-4'),
                P('Fast, flexible financing for your property projects.', cls='text-base text-gray-300 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            step_item('1', 'Submit Your Project',
                       'Tell us about your property project, financing needs, and timeline. We review applications within 48 hours and provide initial feedback.'),
            step_item('2', 'Due Diligence & Valuation',
                       'Our team conducts thorough property valuation, legal review, and risk assessment. We work with independent valuers to ensure accurate LTV ratios.'),
            step_item('3', 'Receive Funding',
                       'Once approved and funded by our investor community, funds are disbursed typically within 2-4 weeks. Loan terms from 6 to 36 months.'),
            Div(
                A('Apply for Financing', href='/borrowers',
                  cls='inline-block px-8 py-3 rounded-md font-semibold text-base no-underline bg-primary text-white hover:bg-primary-light transition-colors'),
                cls='text-center mt-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='bg-dark text-white py-20 px-8'
    )

    loan_types = Section(
        Div(
            Div(
                H2('Loan Types We Offer', cls='font-display text-3xl font-bold text-gray-900 mb-4'),
                P('Flexible financing solutions for different property needs.', cls='text-base text-gray-500 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    Div('\U0001f3d7\ufe0f', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Development Loans', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Finance new construction or major renovation projects. Staged drawdowns available based on construction milestones. Terms: 12-36 months.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                Div(
                    Div('\U0001f309', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Bridge Loans', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Short-term financing for property purchases, refinancing, or capital release. Fast approval and funding. Terms: 6-18 months.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                Div(
                    Div('\U0001f4b0', cls='w-12 h-12 bg-gradient-to-br from-primary to-primary-light rounded-xl flex items-center justify-center mb-5 text-2xl text-white'),
                    H3('Bullet Loans', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Interest-only payments with principal repaid at maturity. Ideal for projects with a clear exit strategy. Terms: 6-24 months.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100 hover:-translate-y-1 hover:shadow-lg transition-all'
                ),
                cls='grid grid-cols-1 md:grid-cols-3 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='py-20 px-8'
    )

    risk = Section(
        Div(
            Div(
                H2('Risk Management', cls='font-display text-3xl font-bold text-white mb-4'),
                P('How we protect your investments.', cls='text-base text-gray-300 max-w-xl mx-auto'),
                cls='text-center mb-12'
            ),
            Div(
                Div(
                    H3('Property-Backed Security', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('Every loan is secured with a first or second-rank mortgage on real estate, providing tangible collateral for your investment.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Conservative LTV Ratios', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('We maintain strict loan-to-value limits, typically below 75%, ensuring a safety buffer between the loan amount and property value.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Independent Valuations', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('All properties are valued by certified independent appraisers before any loan is listed on the platform.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                Div(
                    H3('Default Recovery', cls='text-lg font-bold text-gray-900 mb-3'),
                    P('In case of borrower default, PropFunder manages the full recovery process including collateral realisation on behalf of investors.',
                      cls='text-gray-500 text-sm leading-relaxed'),
                    cls='bg-white rounded-xl p-8 shadow-sm border border-gray-100'
                ),
                cls='grid grid-cols-1 md:grid-cols-2 gap-8'
            ),
            cls='max-w-7xl mx-auto'
        ),
        cls='bg-dark text-white py-20 px-8'
    )

    return Div(hero, for_investors, for_borrowers, loan_types, risk)
