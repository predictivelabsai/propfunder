from fasthtml.common import *

# PropFunder color scheme - professional real estate blues/greens
COLORS = {
    'primary': '#1B4D3E',       # Deep forest green
    'primary_dark': '#143D31',
    'primary_light': '#2D7A5F',
    'accent': '#C8A96E',        # Gold accent
    'accent_dark': '#B8954E',
    'dark': '#1A1A2E',
    'darker': '#0F0F1A',
    'light': '#F8F9FA',
    'white': '#FFFFFF',
    'gray': '#6C757D',
    'gray_light': '#E9ECEF',
}

def app_styles():
    return Style("""
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

    :root {
        --primary: #1B4D3E; --primary-dark: #143D31; --primary-light: #2D7A5F;
        --accent: #C8A96E; --accent-dark: #B8954E;
        --dark: #1A1A2E; --darker: #0F0F1A;
        --light: #F8F9FA; --gray: #6C757D; --gray-light: #E9ECEF;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', -apple-system, sans-serif; color: #333; line-height: 1.6; background: var(--light); }
    .font-display { font-family: 'Playfair Display', Georgia, serif; }

    /* Nav */
    .nav-main { background: var(--dark); padding: 0 2rem; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
    .nav-inner { max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; height: 70px; }
    .nav-logo { font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: white; text-decoration: none; }
    .nav-logo span { color: var(--accent); }
    .nav-links { display: flex; align-items: center; gap: 2rem; list-style: none; }
    .nav-links a { color: #ccc; text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: color 0.2s; }
    .nav-links a:hover, .nav-links a.active { color: var(--accent); }
    .nav-cta { background: var(--primary); color: white !important; padding: 0.6rem 1.5rem !important; border-radius: 6px; font-weight: 600 !important; }
    .nav-cta:hover { background: var(--primary-light) !important; }
    .nav-toggle { display: none; background: none; border: none; color: white; font-size: 1.5rem; cursor: pointer; }
    @media (max-width: 768px) {
        .nav-toggle { display: block; }
        .nav-links { display: none; flex-direction: column; position: absolute; top: 70px; left: 0; right: 0; background: var(--dark); padding: 1rem 2rem; gap: 1rem; }
        .nav-links.open { display: flex; }
    }

    /* Sections */
    .section { padding: 5rem 2rem; }
    .section-inner { max-width: 1200px; margin: 0 auto; }
    .section-dark { background: var(--dark); color: white; }
    .section-primary { background: var(--primary); color: white; }

    /* Hero */
    .hero { background: linear-gradient(135deg, var(--dark) 0%, var(--primary-dark) 50%, var(--primary) 100%); color: white; padding: 6rem 2rem; position: relative; overflow: hidden; }
    .hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"); opacity: 0.5; }
    .hero-inner { max-width: 1200px; margin: 0 auto; position: relative; z-index: 1; }
    .hero h1 { font-family: 'Playfair Display', serif; font-size: 3.2rem; font-weight: 800; line-height: 1.2; max-width: 700px; margin-bottom: 1.5rem; }
    .hero p { font-size: 1.15rem; max-width: 600px; opacity: 0.9; margin-bottom: 2rem; line-height: 1.7; }
    .hero-badges { display: flex; gap: 1.5rem; margin-bottom: 2rem; flex-wrap: wrap; }
    .hero-badge { display: flex; align-items: center; gap: 0.5rem; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.15); padding: 0.5rem 1rem; border-radius: 50px; font-size: 0.85rem; }
    @media (max-width: 768px) { .hero h1 { font-size: 2rem; } .hero { padding: 3rem 1.5rem; } }

    /* Buttons */
    .btn { display: inline-block; padding: 0.8rem 2rem; border-radius: 6px; font-weight: 600; font-size: 0.95rem; text-decoration: none; transition: all 0.2s; border: none; cursor: pointer; }
    .btn-primary { background: var(--accent); color: var(--dark); }
    .btn-primary:hover { background: var(--accent-dark); }
    .btn-outline { background: transparent; color: white; border: 2px solid rgba(255,255,255,0.3); }
    .btn-outline:hover { border-color: white; background: rgba(255,255,255,0.1); }
    .btn-green { background: var(--primary); color: white; }
    .btn-green:hover { background: var(--primary-light); }
    .btn-group { display: flex; gap: 1rem; flex-wrap: wrap; }

    /* Stats */
    .stats-bar { background: white; border-bottom: 1px solid var(--gray-light); padding: 2rem; }
    .stats-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 2rem; text-align: center; }
    .stat-item h3 { font-size: 1.8rem; font-weight: 800; color: var(--primary); margin-bottom: 0.25rem; }
    .stat-item p { font-size: 0.85rem; color: var(--gray); text-transform: uppercase; letter-spacing: 0.5px; }

    /* Cards */
    .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; }
    .card { background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 2px 12px rgba(0,0,0,0.06); transition: transform 0.2s, box-shadow 0.2s; border: 1px solid var(--gray-light); }
    .card:hover { transform: translateY(-4px); box-shadow: 0 8px 30px rgba(0,0,0,0.1); }
    .card-icon { width: 48px; height: 48px; background: linear-gradient(135deg, var(--primary), var(--primary-light)); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.25rem; font-size: 1.5rem; color: white; }
    .card h3 { font-size: 1.15rem; font-weight: 700; margin-bottom: 0.75rem; color: var(--dark); }
    .card p { color: var(--gray); font-size: 0.95rem; line-height: 1.6; }

    /* Steps */
    .step { display: flex; gap: 1.5rem; margin-bottom: 2.5rem; }
    .step-num { width: 48px; height: 48px; min-width: 48px; background: var(--accent); color: var(--dark); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.1rem; }
    .step-content h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; }
    .step-content p { color: var(--gray); font-size: 0.95rem; }

    /* CTA */
    .cta-section { background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%); color: white; padding: 5rem 2rem; text-align: center; }
    .cta-section h2 { font-family: 'Playfair Display', serif; font-size: 2.2rem; margin-bottom: 1rem; }
    .cta-section p { font-size: 1.1rem; opacity: 0.9; max-width: 600px; margin: 0 auto 2rem; }

    /* Footer */
    .footer { background: var(--darker); color: #aaa; padding: 4rem 2rem 2rem; }
    .footer-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 2fr repeat(3, 1fr); gap: 3rem; }
    .footer-brand h3 { font-family: 'Playfair Display', serif; color: white; font-size: 1.3rem; margin-bottom: 1rem; }
    .footer-brand h3 span { color: var(--accent); }
    .footer-brand p { font-size: 0.9rem; line-height: 1.6; }
    .footer h4 { color: white; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1rem; }
    .footer ul { list-style: none; }
    .footer ul li { margin-bottom: 0.5rem; }
    .footer ul a { color: #888; text-decoration: none; font-size: 0.9rem; transition: color 0.2s; }
    .footer ul a:hover { color: var(--accent); }
    .footer-bottom { max-width: 1200px; margin: 3rem auto 0; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; }
    @media (max-width: 768px) { .footer-grid { grid-template-columns: 1fr; } .footer-bottom { flex-direction: column; gap: 1rem; text-align: center; } }

    /* Utility */
    .text-center { text-align: center; }
    .text-accent { color: var(--accent); }
    .text-primary { color: var(--primary); }
    .text-gray { color: var(--gray); }
    .mb-1 { margin-bottom: 0.5rem; }
    .mb-2 { margin-bottom: 1rem; }
    .mb-3 { margin-bottom: 1.5rem; }
    .mb-4 { margin-bottom: 2rem; }
    .mt-4 { margin-top: 2rem; }
    .section-header { text-align: center; margin-bottom: 3rem; }
    .section-header h2 { font-family: 'Playfair Display', serif; font-size: 2.2rem; font-weight: 700; color: var(--dark); margin-bottom: 1rem; }
    .section-header p { font-size: 1.05rem; color: var(--gray); max-width: 600px; margin: 0 auto; }
    .section-dark .section-header h2 { color: white; }
    .section-dark .section-header p { color: #ccc; }

    /* Two-column */
    .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }
    @media (max-width: 768px) { .two-col { grid-template-columns: 1fr; gap: 2rem; } }

    /* Property cards */
    .property-card { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border: 1px solid var(--gray-light); transition: transform 0.2s; }
    .property-card:hover { transform: translateY(-4px); }
    .property-card-img { height: 200px; background: linear-gradient(135deg, var(--primary), var(--primary-light)); display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem; opacity: 0.5; }
    .property-card-body { padding: 1.5rem; }
    .property-card-body h3 { font-size: 1.1rem; margin-bottom: 0.5rem; }
    .property-card-meta { display: flex; justify-content: space-between; margin: 1rem 0; font-size: 0.85rem; }
    .property-card-meta span { color: var(--gray); }
    .property-card-meta strong { color: var(--primary); }
    .progress-bar { height: 8px; background: var(--gray-light); border-radius: 4px; overflow: hidden; margin: 1rem 0; }
    .progress-fill { height: 100%; background: linear-gradient(90deg, var(--primary), var(--primary-light)); border-radius: 4px; }

    /* Admin */
    .admin-sidebar { width: 250px; background: var(--dark); color: white; min-height: calc(100vh - 70px); padding: 1.5rem 0; position: fixed; top: 70px; left: 0; }
    .admin-sidebar a { display: block; padding: 0.75rem 1.5rem; color: #aaa; text-decoration: none; font-size: 0.9rem; transition: all 0.2s; }
    .admin-sidebar a:hover, .admin-sidebar a.active { background: rgba(255,255,255,0.1); color: var(--accent); }
    .admin-content { margin-left: 250px; padding: 2rem; min-height: calc(100vh - 70px); }
    .admin-table { width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
    .admin-table th { background: var(--light); padding: 0.75rem 1rem; text-align: left; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; color: var(--gray); border-bottom: 2px solid var(--gray-light); }
    .admin-table td { padding: 0.75rem 1rem; border-bottom: 1px solid var(--gray-light); font-size: 0.9rem; }
    .admin-table tr:hover { background: #f8f9ff; }
    .admin-form { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); max-width: 800px; }
    .admin-form label { display: block; margin-bottom: 0.25rem; font-weight: 600; font-size: 0.9rem; color: var(--dark); }
    .admin-form input, .admin-form select, .admin-form textarea { width: 100%; padding: 0.6rem 0.8rem; border: 1px solid var(--gray-light); border-radius: 6px; font-size: 0.9rem; margin-bottom: 1rem; font-family: inherit; }
    .admin-form textarea { min-height: 100px; resize: vertical; }
    .badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 50px; font-size: 0.75rem; font-weight: 600; }
    .badge-green { background: #d4edda; color: #155724; }
    .badge-yellow { background: #fff3cd; color: #856404; }
    .badge-red { background: #f8d7da; color: #721c24; }
    .badge-blue { background: #cce5ff; color: #004085; }
    .badge-gray { background: #e2e3e5; color: #383d41; }

    /* Flash */
    .flash { padding: 1rem 1.5rem; border-radius: 8px; margin-bottom: 1rem; font-size: 0.9rem; }
    .flash-success { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
    .flash-error { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
    .flash-info { background: #cce5ff; color: #004085; border: 1px solid #b8daff; }
    """)


def NavBar(active='home'):
    nav_items = [
        ('home', '/', 'Home'),
        ('how-it-works', '/how-it-works', 'How It Works'),
        ('investors', '/investors', 'Investors'),
        ('borrowers', '/borrowers', 'Borrowers'),
        ('about', '/about', 'About'),
        ('contact', '/contact', 'Contact'),
    ]
    return Nav(
        Div(
            A('Prop', Span('Funder'), href='/', cls='nav-logo'),
            Button('\u2630', cls='nav-toggle', onclick="document.querySelector('.nav-links').classList.toggle('open')"),
            Ul(
                *[Li(A(label, href=href, cls='active' if key == active else '')) for key, href, label in nav_items],
                Li(A('Login', href='/login', cls='nav-cta')),
                cls='nav-links'
            ),
            cls='nav-inner'
        ),
        cls='nav-main'
    )


def PageFooter():
    from fasthtml.components import Footer as FooterTag
    return FooterTag(
        Div(
            Div(
                Div(
                    H3('Prop', Span('Funder')),
                    P('Property-backed investments made accessible. We connect investors with vetted real estate opportunities, delivering transparent returns secured by tangible assets.'),
                    cls='footer-brand'
                ),
                Div(
                    H4('Platform'),
                    Ul(
                        Li(A('How It Works', href='/how-it-works')),
                        Li(A('Open Investments', href='/investors')),
                        Li(A('For Borrowers', href='/borrowers')),
                        Li(A('About Us', href='/about')),
                    )
                ),
                Div(
                    H4('Resources'),
                    Ul(
                        Li(A('FAQ', href='/faq')),
                        Li(A('Risk Statement', href='/risk')),
                        Li(A('Contact', href='/contact')),
                    )
                ),
                Div(
                    H4('Legal'),
                    Ul(
                        Li(A('Terms of Service', href='/terms')),
                        Li(A('Privacy Policy', href='/privacy')),
                        Li(A('Risk Disclosures', href='/risk')),
                    )
                ),
                cls='footer-grid'
            ),
            Div(
                P('\u00a9 2026 PropFunder. All rights reserved. Investing involves risk and can result in loss of capital.'),
                P('All investments are secured by real estate collateral.'),
                cls='footer-bottom'
            ),
            cls='section-inner'
        ),
        cls='footer'
    )


def Page(content, active='home', title='PropFunder'):
    return (
        Title(f'{title} - Property Investment Platform'),
        NavBar(active),
        Main(content),
        PageFooter()
    )
