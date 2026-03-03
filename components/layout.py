from fasthtml.common import *


def app_styles():
    """Tailwind CDN with custom config + minimal custom styles."""
    return (
        # Google Fonts
        Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap'),
        # Tailwind CDN
        Script(src='https://cdn.tailwindcss.com'),
        Script("""
        tailwind.config = {
          theme: {
            extend: {
              colors: {
                primary: { DEFAULT: '#1B4D3E', dark: '#143D31', light: '#2D7A5F' },
                accent: { DEFAULT: '#C8A96E', dark: '#B8954E' },
                dark: { DEFAULT: '#1A1A2E', deeper: '#0F0F1A' },
              },
              fontFamily: {
                display: ['Playfair Display', 'Georgia', 'serif'],
                sans: ['Inter', 'system-ui', 'sans-serif'],
              },
            },
          },
        }
        """),
        # Minimal custom styles for things Tailwind CDN can't easily do
        Style("""
        body { font-family: 'Inter', system-ui, sans-serif; }
        .hero-pattern { background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"); }
        """),
    )


def NavBar(active='home'):
    nav_items = [
        ('home', '/', 'Home'),
        ('how-it-works', '/how-it-works', 'How It Works'),
        ('investors', '/investors', 'Investors'),
        ('borrowers', '/borrowers', 'Borrowers'),
        ('about', '/about', 'About'),
        ('contact', '/contact', 'Contact'),
    ]

    def nav_link(key, href, label):
        base = 'text-sm font-medium no-underline transition-colors duration-200'
        if key == active:
            return A(label, href=href, cls=f'{base} text-accent')
        return A(label, href=href, cls=f'{base} text-gray-400 hover:text-accent')

    return Nav(
        Div(
            A('Prop', Span('Funder', cls='text-accent'), href='/',
              cls='font-display text-2xl font-bold text-white no-underline'),
            Button('\u2630',
                   cls='md:hidden bg-transparent border-none text-white text-2xl cursor-pointer',
                   onclick="document.getElementById('nav-links').classList.toggle('hidden')"),
            Ul(
                *[Li(nav_link(key, href, label)) for key, href, label in nav_items],
                Li(A('Login', href='/login',
                     cls='bg-primary text-white px-5 py-2.5 rounded-md font-semibold text-sm no-underline hover:bg-primary-light transition-colors')),
                id='nav-links',
                cls='hidden md:flex items-center gap-8 list-none'
            ),
            cls='max-w-7xl mx-auto flex items-center justify-between h-[70px]'
        ),
        cls='bg-dark px-8 sticky top-0 z-50 shadow-md'
    )


def PageFooter():
    from fasthtml.components import Footer as FooterTag
    return FooterTag(
        Div(
            Div(
                Div(
                    H3('Prop', Span('Funder', cls='text-accent'),
                       cls='font-display text-white text-xl mb-4'),
                    P('Property-backed investments made accessible. We connect investors with vetted real estate opportunities, delivering transparent returns secured by tangible assets.',
                      cls='text-sm leading-relaxed text-gray-400'),
                ),
                Div(
                    H4('Platform', cls='text-white text-sm uppercase tracking-wider mb-4'),
                    Ul(
                        Li(A('How It Works', href='/how-it-works', cls='text-gray-500 no-underline text-sm hover:text-accent transition-colors'), cls='mb-2'),
                        Li(A('Open Investments', href='/investors', cls='text-gray-500 no-underline text-sm hover:text-accent transition-colors'), cls='mb-2'),
                        Li(A('For Borrowers', href='/borrowers', cls='text-gray-500 no-underline text-sm hover:text-accent transition-colors'), cls='mb-2'),
                        Li(A('About Us', href='/about', cls='text-gray-500 no-underline text-sm hover:text-accent transition-colors'), cls='mb-2'),
                        cls='list-none'
                    )
                ),
                Div(
                    H4('Resources', cls='text-white text-sm uppercase tracking-wider mb-4'),
                    Ul(
                        Li(A('FAQ', href='/faq', cls='text-gray-500 no-underline text-sm hover:text-accent transition-colors'), cls='mb-2'),
                        Li(A('Risk Statement', href='/risk', cls='text-gray-500 no-underline text-sm hover:text-accent transition-colors'), cls='mb-2'),
                        Li(A('Contact', href='/contact', cls='text-gray-500 no-underline text-sm hover:text-accent transition-colors'), cls='mb-2'),
                        cls='list-none'
                    )
                ),
                Div(
                    H4('Legal', cls='text-white text-sm uppercase tracking-wider mb-4'),
                    Ul(
                        Li(A('Terms of Service', href='/terms', cls='text-gray-500 no-underline text-sm hover:text-accent transition-colors'), cls='mb-2'),
                        Li(A('Privacy Policy', href='/privacy', cls='text-gray-500 no-underline text-sm hover:text-accent transition-colors'), cls='mb-2'),
                        Li(A('Risk Disclosures', href='/risk', cls='text-gray-500 no-underline text-sm hover:text-accent transition-colors'), cls='mb-2'),
                        cls='list-none'
                    )
                ),
                cls='max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12'
            ),
            Div(
                P('\u00a9 2026 PropFunder. All rights reserved. Investing involves risk and can result in loss of capital.'),
                P('All investments are secured by real estate collateral.'),
                cls='max-w-7xl mx-auto mt-12 pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center text-sm gap-4'
            ),
        ),
        cls='bg-dark-deeper text-gray-400 pt-16 pb-8 px-8'
    )


def Page(content, active='home', title='PropFunder'):
    return (
        Title(f'{title} - Property Investment Platform'),
        NavBar(active),
        Main(content),
        PageFooter()
    )
