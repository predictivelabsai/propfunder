import os
from fasthtml.common import *
from starlette.responses import RedirectResponse
import hashlib

# Components & pages
from components.layout import app_styles, Page
from pages.home import home_page
from pages.how_it_works import how_it_works_page
from pages.investors import investors_page
from pages.borrowers import borrowers_page
from pages.about import about_page
from pages.contact import contact_page

# Admin & API
from admin.views import ar as admin_router
from api.routes import ar as api_router

# Database
from db import init_db, SessionLocal
from models import User

# Initialize app with styles
app, rt = fast_app(
    hdrs=(app_styles(),),
    secret_key='propfunder-test-app-2026',
)

# Register routers
admin_router.to_app(app)
api_router.to_app(app)


# --- Auth helpers ---

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def check_auth(sess):
    return sess.get('auth')


# --- Public pages ---

@rt
def index():
    return Page(home_page(), active='home')

@rt('/how-it-works')
def how_it_works():
    return Page(how_it_works_page(), active='how-it-works', title='How It Works')

@rt
def investors():
    return Page(investors_page(), active='investors', title='Investors')

@rt
def borrowers():
    return Page(borrowers_page(), active='borrowers', title='Borrowers')

@rt
def about():
    return Page(about_page(), active='about', title='About')

@rt
def contact():
    return Page(contact_page(), active='contact', title='Contact')


# --- Auth pages ---

def login_form(error=None, email=''):
    return Page(
        Section(
            Div(
                Div(
                    Div(error, cls='flash flash-error') if error else '',
                    H2('Login', cls='font-display', style='font-size:2rem;margin-bottom:1.5rem;text-align:center;'),
                    Form(
                        Div(
                            Label('Email'),
                            Input(type='email', name='email', placeholder='you@example.com', value=email, required=True),
                        ),
                        Div(
                            Label('Password'),
                            Input(type='password', name='password', placeholder='Your password', required=True),
                        ),
                        Button('Sign In', type='submit', cls='btn btn-green', style='width:100%;margin-top:0.5rem;'),
                        method='post', action='/login',
                        cls='admin-form', style='max-width:400px;margin:0 auto;'
                    ),
                    Div(
                        P("Don't have an account? ", A('Register', href='/register', style='color:var(--primary);'),
                          style='text-align:center;margin-top:1.5rem;color:var(--gray);font-size:0.9rem;'),
                    ),
                ),
                cls='section-inner'
            ),
            cls='section', style='min-height:60vh;display:flex;align-items:center;'
        ),
        active='', title='Login'
    )

@rt('/login', methods=['GET'])
def login_get():
    return login_form()

@rt('/login', methods=['POST'])
async def login_post(req, sess):
    form = await req.form()
    email = form.get('email', '')
    password = form.get('password', '')

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if user and user.password_hash == hash_password(password):
            sess['auth'] = user.id
            sess['email'] = user.email
            sess['role'] = user.role.value if hasattr(user.role, 'value') else user.role
            sess['name'] = user.full_name
            if user.is_staff:
                return RedirectResponse('/admin', status_code=303)
            return RedirectResponse('/', status_code=303)
    finally:
        db.close()

    return login_form(error='Invalid email or password.', email=email)


@rt('/register', methods=['GET'])
def register():
    return Page(
        Section(
            Div(
                H2('Create Account', cls='font-display', style='font-size:2rem;margin-bottom:1.5rem;text-align:center;'),
                Form(
                    Div(Label('First Name'), Input(type='text', name='first_name', required=True)),
                    Div(Label('Last Name'), Input(type='text', name='last_name', required=True)),
                    Div(Label('Email'), Input(type='email', name='email', required=True)),
                    Div(Label('Password'), Input(type='password', name='password', minlength='8', required=True)),
                    Div(
                        Label('I am a'),
                        Select(
                            Option('Investor', value='investor'),
                            Option('Borrower / Developer', value='borrower'),
                            name='role'
                        ),
                    ),
                    Button('Create Account', type='submit', cls='btn btn-green', style='width:100%;margin-top:0.5rem;'),
                    method='post', action='/register',
                    cls='admin-form', style='max-width:400px;margin:0 auto;'
                ),
                P('Already have an account? ', A('Login', href='/login', style='color:var(--primary);'),
                  style='text-align:center;margin-top:1.5rem;color:var(--gray);font-size:0.9rem;'),
                cls='section-inner'
            ),
            cls='section', style='min-height:60vh;display:flex;align-items:center;'
        ),
        active='', title='Register'
    )


@rt('/register', methods=['POST'])
async def register_post(req, sess):
    form = await req.form()
    email = form.get('email', '')
    password = form.get('password', '')
    first_name = form.get('first_name', '')
    last_name = form.get('last_name', '')
    role = form.get('role', 'investor')

    db = SessionLocal()
    try:
        existing = db.query(User).filter(User.email == email).first()
        if existing:
            return Page(
                Section(Div(
                    Div('An account with this email already exists.', cls='flash flash-error'),
                    H2('Create Account', cls='font-display', style='font-size:2rem;margin-bottom:1.5rem;text-align:center;'),
                    P(A('Login instead', href='/login', style='color:var(--primary);'), style='text-align:center;'),
                    cls='section-inner'
                ), cls='section'),
                active='', title='Register'
            )

        user = User(
            email=email,
            password_hash=hash_password(password),
            first_name=first_name,
            last_name=last_name,
            role=role,
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        sess['auth'] = user.id
        sess['email'] = user.email
        sess['role'] = role
        sess['name'] = f'{first_name} {last_name}'.strip()
    finally:
        db.close()

    return RedirectResponse('/', status_code=303)


@rt
def logout(sess):
    sess.clear()
    return RedirectResponse('/', status_code=303)


# --- FAQ page ---

@rt
def faq():
    from models import FAQ
    db = SessionLocal()
    try:
        faqs = db.query(FAQ).filter(FAQ.is_active == True).order_by(FAQ.display_order).all()
        faq_items = []
        for f in faqs:
            faq_items.append(Div(
                H3(f.question, style='margin-bottom:0.75rem;'),
                P(f.answer, style='color:var(--gray);'),
                cls='card'
            ))
        if not faq_items:
            faq_items = [P('No FAQs available yet.', style='color:var(--gray);text-align:center;')]
    finally:
        db.close()

    return Page(
        Div(
            Section(
                Div(H1('Frequently Asked Questions'), P('Find answers to common questions about PropFunder.'), cls='hero-inner'),
                cls='hero', style='padding:4rem 2rem;'
            ),
            Section(
                Div(*faq_items, cls='section-inner', style='max-width:800px;'),
                cls='section'
            ),
        ),
        active='', title='FAQ'
    )


# --- Initialize DB on startup ---

@app.on_event("startup")
async def startup():
    try:
        init_db()
        # Create default admin if not exists
        db = SessionLocal()
        try:
            admin = db.query(User).filter(User.email == 'admin@propfunder.com').first()
            if not admin:
                admin = User(
                    email='admin@propfunder.com',
                    password_hash=hash_password('admin123'),
                    first_name='Admin',
                    last_name='User',
                    role='admin',
                    is_verified=True,
                    is_active=True,
                    is_staff=True,
                )
                db.add(admin)
                db.commit()
        finally:
            db.close()
    except Exception as e:
        print(f"DB init warning: {e}")


serve(port=int(os.environ.get('PORT', 5001)))
