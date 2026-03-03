# PropFunder - Property Investment Platform

A property-backed investment platform connecting investors with vetted real estate opportunities. Built with FastHTML, SQLAlchemy, and PostgreSQL.

**Live Demo**: [propfunder.predictivelabs.ai](https://propfunder.predictivelabs.ai)

## Features

### For Investors
- Browse property-backed loan opportunities
- Auto Invest and Manual Invest modes
- Secondary market for investment trading
- Monthly interest payments (avg. 9.8% p.a.)
- Minimum investment from EUR 50
- Portfolio dashboard and tracking

### For Borrowers / Developers
- Fast property financing (2-4 weeks)
- Loan amounts EUR 50K - EUR 5M
- Bridge, development, and bullet loans
- Terms from 6 to 36 months
- Competitive rates from 8% p.a.

### Platform
- Full admin interface at `/admin` with CRUD for all models
- JSON API at `/api/*`
- Session-based authentication
- Mobile-responsive design
- Health check endpoint

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Framework | [FastHTML](https://fastht.ml) (Python) |
| Database | PostgreSQL + SQLAlchemy |
| CSS | Custom design system (Inter + Playfair Display) |
| Server | Uvicorn |
| Deployment | Docker / Docker Compose / Coolify |

## Quick Start

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DB_URL=postgresql://user:pass@host:5432/dbname

# Run the app
python main.py
# Access at http://localhost:5001
```

### Docker

```bash
docker compose up --build
# Access at http://localhost:5001
```

### Default Admin

- URL: `http://localhost:5001/admin`
- Email: `admin@propfunder.com`
- Password: `admin123`

## Project Structure

```
propfunder/
├── main.py                 # App entry point, routes, auth
├── db.py                   # SQLAlchemy engine & session
├── models.py               # 15 data models
├── components/
│   └── layout.py           # Design system, nav, footer
├── pages/
│   ├── home.py             # Landing page
│   ├── how_it_works.py     # Process explanation
│   ├── investors.py        # Investor info
│   ├── borrowers.py        # Borrower info
│   ├── about.py            # About page
│   └── contact.py          # Contact page
├── admin/
│   └── views.py            # Admin CRUD interface
├── api/
│   └── routes.py           # JSON API endpoints
├── sql/
│   └── schema.sql          # Full database DDL
├── docs/                   # Documentation
├── Dockerfile              # Production container
├── docker-compose.yml      # Full stack with PostgreSQL
└── requirements.txt        # Python dependencies
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/health` | Health check |
| `GET /api/stats` | Platform statistics |
| `GET /api/properties` | List active properties |
| `GET /api/properties/{id}` | Property details |
| `GET /api/opportunities` | Open investment opportunities |
| `GET /api/opportunities/{id}` | Opportunity details |
| `GET /api/faqs` | Active FAQs |

## Database

The app uses PostgreSQL with a dedicated `propfunder` schema. Tables are auto-created on startup via SQLAlchemy, or you can apply the DDL manually:

```bash
psql -h host -U user -d dbname -f sql/schema.sql
```

### Models

- **User** - Investors, borrowers, admins
- **Company** - Borrower companies
- **Property** - Real estate projects
- **InvestmentOpportunity** - Loan campaigns
- **Investment** - Individual investments
- **ProjectUpdate** - Construction/status updates
- **Repayment** - Loan repayments
- **Dividend** - Interest distributions
- **Payment** - Transaction records
- **SecondaryMarket** - Investment trading
- **AutoInvest** - Automated investing rules
- **InvestorVoting / UserVote** - Governance
- **Notification** - User notifications
- **FAQ** - Platform FAQs

## Deployment (Coolify)

1. Connect the GitHub repo in Coolify
2. Set build pack to **Dockerfile**
3. Set environment variables:
   - `DB_URL` - PostgreSQL connection string
   - `PORT` - Server port (default: 5001)
4. Set domain to `propfunder.predictivelabs.ai`
5. Deploy

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DB_URL` | *(required)* | PostgreSQL connection string |
| `PORT` | `5001` | Server port |

## License

Proprietary - Predictive Labs AI
