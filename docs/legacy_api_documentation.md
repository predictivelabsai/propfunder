# Litfunder REST API Documentation

## Overview

The Litfunder API provides complete access to the litigation finance platform without authentication. All endpoints are public and return JSON responses.

**Base URL**: `http://localhost:8000/api/`

**API Version**: 1.0.0

**Authentication**: None Required (AllowAny)

---

## Quick Start

### Installation

```bash
git clone https://github.com/predictivelabsai/litfunder-backend.git
cd litfunder-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### Access API

- **REST API**: http://localhost:8000/api/
- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/
- **Schema**: http://localhost:8000/api/schema/

---

## API Endpoints

### Legal Cases

#### List All Legal Cases
```bash
curl -X GET http://localhost:8000/api/legal-cases/
```

**Response:**
```json
{
  "count": 7,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "case_id": "TEST-003",
      "case_title": "Test Case 3",
      "case_description": "Test Description",
      "case_type": "commercial",
      "jurisdiction": "New York",
      "court_name": "NY District Court",
      "plaintiff_name": "Plaintiff",
      "defendant_name": "Defendant",
      "attorney_name": "Attorney",
      "attorney_contact": "attorney@example.com",
      "claim_amount": "1000000.00",
      "estimated_legal_costs": "100000.00",
      "estimated_duration_months": 12,
      "case_filed_date": "2025-11-28",
      "created_by": 1,
      "created_at": "2025-11-28T19:57:00Z",
      "updated_at": "2025-11-28T19:57:00Z"
    }
  ]
}
```

#### Get Single Legal Case
```bash
curl -X GET http://localhost:8000/api/legal-cases/1/
```

#### Create Legal Case
```bash
curl -X POST http://localhost:8000/api/legal-cases/ \
  -H "Content-Type: application/json" \
  -d '{
    "case_id": "NEW-001",
    "case_title": "New Case",
    "case_type": "commercial",
    "jurisdiction": "California",
    "court_name": "CA Superior Court",
    "plaintiff_name": "John Doe",
    "defendant_name": "Jane Smith",
    "attorney_name": "Attorney Name",
    "attorney_contact": "attorney@example.com",
    "claim_amount": "500000",
    "estimated_legal_costs": "50000",
    "estimated_duration_months": 12,
    "case_filed_date": "2025-11-28",
    "created_by": 1
  }'
```

#### Update Legal Case
```bash
curl -X PUT http://localhost:8000/api/legal-cases/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "case_title": "Updated Case Title"
  }'
```

#### Delete Legal Case
```bash
curl -X DELETE http://localhost:8000/api/legal-cases/1/
```

---

### Case Fundings

#### List All Case Fundings
```bash
curl -X GET http://localhost:8000/api/case-fundings/
```

**Response:**
```json
{
  "count": 6,
  "results": [
    {
      "id": 1,
      "name": "Test Funding 2",
      "legal_case": 1,
      "funding_goal": "500000.00",
      "amount_raised": "0.00",
      "funding_status": "open",
      "risk_level": "B",
      "start_date": "2025-11-28",
      "end_date": "2025-12-28",
      "description": "Funding Round 1",
      "created_at": "2025-11-28T19:57:00Z",
      "updated_at": "2025-11-28T19:57:00Z"
    }
  ]
}
```

#### Filter Case Fundings by Status
```bash
curl -X GET "http://localhost:8000/api/case-fundings/?funding_status=open"
```

#### Filter by Risk Level
```bash
curl -X GET "http://localhost:8000/api/case-fundings/?risk_level=B"
```

---

### Case Investments

#### List All Case Investments
```bash
curl -X GET http://localhost:8000/api/case-investments/
```

**Response:**
```json
{
  "count": 16,
  "results": [
    {
      "id": 1,
      "case_funding": 1,
      "investor": 1,
      "investment_amount": "50000.00",
      "status": "confirmed",
      "investment_date": "2025-11-28",
      "created_at": "2025-11-28T19:57:00Z",
      "updated_at": "2025-11-28T19:57:00Z"
    }
  ]
}
```

#### Filter Investments by Status
```bash
curl -X GET "http://localhost:8000/api/case-investments/?status=confirmed"
```

#### Create Investment
```bash
curl -X POST http://localhost:8000/api/case-investments/ \
  -H "Content-Type: application/json" \
  -d '{
    "case_funding": 1,
    "investor": 1,
    "investment_amount": "100000",
    "status": "pending",
    "investment_date": "2025-11-28"
  }'
```

---

### Case Updates

#### List All Case Updates
```bash
curl -X GET http://localhost:8000/api/case-updates/
```

#### Create Case Update
```bash
curl -X POST http://localhost:8000/api/case-updates/ \
  -H "Content-Type: application/json" \
  -d '{
    "legal_case": 1,
    "update_title": "New Development",
    "update_description": "Description of update",
    "update_date": "2025-11-28"
  }'
```

---

### Notifications

#### List All Notifications
```bash
curl -X GET http://localhost:8000/api/notifications/
```

#### Filter Unread Notifications
```bash
curl -X GET "http://localhost:8000/api/notifications/?is_read=false"
```

---

### Users

#### List All Users
```bash
curl -X GET http://localhost:8000/api/users/
```

**Response:**
```json
{
  "count": 19,
  "results": [
    {
      "id": 1,
      "email": "admin@litfunder.com",
      "first_name": "",
      "last_name": "",
      "role": "investor",
      "is_verified": true,
      "created_at": "2025-11-28T19:57:00Z"
    }
  ]
}
```

#### Filter Users by Role
```bash
curl -X GET "http://localhost:8000/api/users/?role=investor"
```

#### Filter Verified Users
```bash
curl -X GET "http://localhost:8000/api/users/?is_verified=true"
```

---

### FAQs

#### List All FAQs
```bash
curl -X GET http://localhost:8000/api/faqs/
```

#### Search FAQs
```bash
curl -X GET "http://localhost:8000/api/faqs/?search=litigation"
```

---

### Settlements

#### List All Settlements
```bash
curl -X GET http://localhost:8000/api/settlements/
```

#### Filter by Settlement Status
```bash
curl -X GET "http://localhost:8000/api/settlements/?settlement_status=completed"
```

---

### Dividends

#### List All Dividends
```bash
curl -X GET http://localhost:8000/api/dividends/
```

#### Filter by Distribution Status
```bash
curl -X GET "http://localhost:8000/api/dividends/?distribution_status=pending"
```

---

### Case Votings

#### List All Case Votings
```bash
curl -X GET http://localhost:8000/api/case-votings/
```

#### Filter by Voting Status
```bash
curl -X GET "http://localhost:8000/api/case-votings/?voting_status=active"
```

---

### User Votes

#### List All User Votes
```bash
curl -X GET http://localhost:8000/api/user-votes/
```

---

### Payments

#### List All Payments
```bash
curl -X GET http://localhost:8000/api/payments/
```

#### Filter by Payment Status
```bash
curl -X GET "http://localhost:8000/api/payments/?payment_status=completed"
```

---

### Secondary Markets

#### List All Secondary Market Listings
```bash
curl -X GET http://localhost:8000/api/secondary-markets/
```

#### Filter by Market Status
```bash
curl -X GET "http://localhost:8000/api/secondary-markets/?market_status=open"
```

---

### Auto Invests

#### List All Auto Investment Settings
```bash
curl -X GET http://localhost:8000/api/auto-invests/
```

#### Filter Active Auto Invests
```bash
curl -X GET "http://localhost:8000/api/auto-invests/?is_active=true"
```

---

### Companies

#### List All Companies
```bash
curl -X GET http://localhost:8000/api/companies/
```

---

## Pagination

All list endpoints support pagination with the following parameters:

```bash
curl -X GET "http://localhost:8000/api/legal-cases/?page=1&page_size=10"
```

**Response Headers:**
```
X-Total-Count: 7
X-Page-Count: 1
```

---

## Filtering & Search

### Search
```bash
curl -X GET "http://localhost:8000/api/legal-cases/?search=commercial"
```

### Ordering
```bash
curl -X GET "http://localhost:8000/api/legal-cases/?ordering=-created_at"
```

---

## Response Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 201 | Created - Resource created |
| 204 | No Content - Resource deleted |
| 400 | Bad Request - Invalid parameters |
| 404 | Not Found - Resource not found |
| 500 | Server Error |

---

## Error Responses

```json
{
  "detail": "Not found."
}
```

---

## Database Configuration

The API uses PostgreSQL with the following configuration:

**Environment Variables:**
```bash
DB_URL=postgresql://indurent_db_user:mORTX4lmewn7ZJsMiU7Ox7Qb8gnxPRgf@dpg-d40gneur433s738clpeg-a.frankfurt-postgres.render.com/indurent_db
DATABASE_SCHEMA=litfunder
```

**Connection String:**
```
postgresql://indurent_db_user:mORTX4lmewn7ZJsMiU7Ox7Qb8gnxPRgf@dpg-d40gneur433s738clpeg-a.frankfurt-postgres.render.com/indurent_db
```

---

## Swagger Documentation

Access the interactive Swagger UI at:
```
http://localhost:8000/api/docs/
```

This provides:
- Interactive API exploration
- Request/response examples
- Parameter documentation
- Try-it-out functionality

---

## ReDoc Documentation

Access the ReDoc documentation at:
```
http://localhost:8000/api/redoc/
```

---

## OpenAPI Schema

Download the OpenAPI schema at:
```
http://localhost:8000/api/schema/
```

---

## Example: Complete Workflow

### 1. Get All Legal Cases
```bash
curl -X GET http://localhost:8000/api/legal-cases/
```

### 2. Get Specific Case
```bash
curl -X GET http://localhost:8000/api/legal-cases/1/
```

### 3. Get Case Fundings for That Case
```bash
curl -X GET "http://localhost:8000/api/case-fundings/?legal_case=1"
```

### 4. Get Investments in That Funding
```bash
curl -X GET "http://localhost:8000/api/case-investments/?case_funding=1"
```

### 5. Get Case Updates
```bash
curl -X GET "http://localhost:8000/api/case-updates/?legal_case=1"
```

---

## Rate Limiting

Currently, no rate limiting is implemented. For production deployment, consider adding:
- Django REST Framework throttling
- API key management
- Request rate limiting

---

## Authentication

**Current Status**: No authentication required (AllowAny)

For production, consider implementing:
- Token-based authentication (JWT)
- OAuth2
- API key authentication

---

## CORS Configuration

CORS is enabled for all origins. For production, configure:

```python
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
]
```

---

## Support

For issues or questions:
1. Check the Swagger documentation at `/api/docs/`
2. Review the ReDoc at `/api/redoc/`
3. Check the database schema in `sql/` folder
4. Review the models in `cases/models.py` and `accounts/models.py`

---

**Last Updated**: November 28, 2025  
**API Version**: 1.0.0  
**Status**: Production Ready
