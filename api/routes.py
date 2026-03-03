from fasthtml.common import *
from starlette.responses import JSONResponse
from db import SessionLocal
from models import (
    User, Property, InvestmentOpportunity, Investment,
    FAQ, Notification, ProjectUpdate, Payment
)

ar = APIRouter()


def _serialize(val):
    if val is None:
        return None
    if hasattr(val, 'value'):
        return val.value
    return str(val)

def to_dict(obj, fields=None):
    if fields:
        return {f: _serialize(getattr(obj, f, '')) for f in fields}
    mapper = obj.__class__.__mapper__
    return {col.key: _serialize(getattr(obj, col.key, '')) for col in mapper.columns}


# Properties API
@ar('/api/properties')
def api_properties():
    db = SessionLocal()
    try:
        props = db.query(Property).filter(Property.status.in_(['active', 'funded'])).order_by(Property.id.desc()).all()
        return JSONResponse([to_dict(p, ['id', 'title', 'property_type', 'status', 'city', 'country', 'valuation']) for p in props])
    finally:
        db.close()


@ar('/api/properties/{pid}')
def api_property_detail(pid: int):
    db = SessionLocal()
    try:
        p = db.query(Property).get(pid)
        if not p:
            return JSONResponse({'error': 'Not found'}, status_code=404)
        return JSONResponse(to_dict(p))
    finally:
        db.close()


# Investment Opportunities API
@ar('/api/opportunities')
def api_opportunities():
    db = SessionLocal()
    try:
        opps = db.query(InvestmentOpportunity).filter(
            InvestmentOpportunity.funding_status == 'open'
        ).order_by(InvestmentOpportunity.id.desc()).all()
        result = []
        for o in opps:
            d = to_dict(o, ['id', 'name', 'loan_amount', 'amount_raised', 'interest_rate',
                            'loan_term_months', 'funding_status', 'risk_level'])
            d['funding_progress'] = str(o.funding_progress)
            result.append(d)
        return JSONResponse(result)
    finally:
        db.close()


@ar('/api/opportunities/{oid}')
def api_opportunity_detail(oid: int):
    db = SessionLocal()
    try:
        o = db.query(InvestmentOpportunity).get(oid)
        if not o:
            return JSONResponse({'error': 'Not found'}, status_code=404)
        d = to_dict(o)
        d['funding_progress'] = str(o.funding_progress)
        return JSONResponse(d)
    finally:
        db.close()


# FAQs API
@ar('/api/faqs')
def api_faqs():
    db = SessionLocal()
    try:
        faqs = db.query(FAQ).filter(FAQ.is_active == True).order_by(FAQ.display_order).all()
        return JSONResponse([to_dict(f, ['id', 'question', 'answer']) for f in faqs])
    finally:
        db.close()


# Stats API
@ar('/api/stats')
def api_stats():
    db = SessionLocal()
    try:
        return JSONResponse({
            'total_investors': db.query(User).filter(User.role == 'investor').count(),
            'total_properties': db.query(Property).count(),
            'total_investments': db.query(Investment).count(),
            'open_opportunities': db.query(InvestmentOpportunity).filter(
                InvestmentOpportunity.funding_status == 'open'
            ).count(),
        })
    finally:
        db.close()


# Health check
@ar('/api/health')
def api_health():
    return JSONResponse({'status': 'ok', 'service': 'propfunder'})
