# PropFunder - Property Investment Platform

## Project Overview
PropFunder is a property-backed investment platform (inspired by EstateGuru) built entirely with FastHTML + SQLAlchemy + PostgreSQL. It connects property developers seeking financing with investors looking for property-backed returns.

## Tech Stack
- **Framework**: FastHTML (Python) - server-rendered hypermedia application
- **CSS**: Tailwind CSS via CDN
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Schema**: `propfunder` schema in PostgreSQL
- **Deployment**: Docker + Docker Compose (Coolify-ready)
- **Server**: Uvicorn (via FastHTML's `serve()`)

## FastHTML Conventions (MUST FOLLOW)
- Always `from fasthtml.common import *`
- Use `app, rt = fast_app(...)` for app initialization
- Use `@rt` decorator for routes; function name = route path
- Use `serve()` at the bottom - never write `if __name__ == "__main__"`
- Return FT components (FastTags) from route handlers
- Use `cls` for CSS classes (maps to HTML `class`)
- Use `_for` for label `for` attribute
- Use `Titled("Page Title", content...)` when a page title is needed
- Prefer Python over JS; never use React/Vue/Svelte
- Use `Style()` for inline CSS, `Script()` for JS
- Use `Link(rel='stylesheet', href=...)` for external CSS
- Use `Beforeware` for auth/middleware
- Use `APIRouter` to organize routes across files
- Use `fill_form()` to populate forms from objects
- Dataclass type annotations auto-unpack form data
- For file uploads, `Form` defaults to multipart/form-data
- Use `setup_toasts(app)` for toast notifications
- Use `RedirectResponse` for redirects (with status_code=303)
- Sessions via `sess` parameter in handlers
- Auth via `req.scope['auth']` in Beforeware

## Project Structure
```
propfunder/
├── main.py              # FastHTML app entry point
├── models.py            # SQLAlchemy models
├── db.py                # Database connection & session management
├── components/
│   └── layout.py        # Navbar, footer, page wrapper
├── pages/
│   ├── home.py          # Landing page
│   ├── how_it_works.py  # How it works page
│   ├── investors.py     # Investor information
│   ├── borrowers.py     # Borrower/developer information
│   ├── about.py         # About page
│   └── contact.py       # Contact page
├── admin/
│   ├── __init__.py      # Admin router
│   └── views.py         # Admin CRUD views
├── api/
│   └── routes.py        # API endpoints
├── sql/
│   └── schema.sql       # Database schema DDL
├── docs/
│   └── fasthtml-ctx.txt # FastHTML reference
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Database
- Connection: `DB_URL` environment variable
- Schema: `propfunder` in PostgreSQL
- ORM: SQLAlchemy with declarative models
- All tables prefixed with schema: `propfunder.table_name`

## Key Domain Concepts
- **Properties**: Real estate projects seeking funding
- **Investment Opportunities**: Loan campaigns for properties
- **Investments**: Individual investor contributions
- **Borrowers/Developers**: Property developers seeking financing
- **Investors**: People investing in property-backed loans
- **Repayments**: Loan repayment tracking
- **Secondary Market**: Trading of investment positions

## Running Locally
```bash
python main.py  # Starts on port 5001
```

## Docker
```bash
docker compose up --build
```
