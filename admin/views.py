from fasthtml.common import *
from sqlalchemy import inspect, text
from db import SessionLocal, SCHEMA
from models import (
    User, Company, Property, InvestmentOpportunity, Investment,
    ProjectUpdate, Notification, FAQ, Repayment, Dividend,
    InvestorVoting, Payment, SecondaryMarket, AutoInvest
)

ar = APIRouter()

# Model registry for admin CRUD
ADMIN_MODELS = {
    'users': {'model': User, 'label': 'Users', 'list_fields': ['id', 'email', 'first_name', 'last_name', 'role', 'is_active']},
    'companies': {'model': Company, 'label': 'Companies', 'list_fields': ['id', 'name', 'registration_number']},
    'properties': {'model': Property, 'label': 'Properties', 'list_fields': ['id', 'title', 'property_type', 'status', 'city', 'country']},
    'opportunities': {'model': InvestmentOpportunity, 'label': 'Investment Opportunities', 'list_fields': ['id', 'name', 'loan_amount', 'amount_raised', 'interest_rate', 'funding_status']},
    'investments': {'model': Investment, 'label': 'Investments', 'list_fields': ['id', 'opportunity_id', 'investor_id', 'amount', 'status']},
    'updates': {'model': ProjectUpdate, 'label': 'Project Updates', 'list_fields': ['id', 'property_id', 'title', 'update_type', 'created_at']},
    'notifications': {'model': Notification, 'label': 'Notifications', 'list_fields': ['id', 'user_id', 'title', 'is_read']},
    'faqs': {'model': FAQ, 'label': 'FAQs', 'list_fields': ['id', 'question', 'display_order', 'is_active']},
    'repayments': {'model': Repayment, 'label': 'Repayments', 'list_fields': ['id', 'opportunity_id', 'amount', 'repayment_date', 'is_principal']},
    'dividends': {'model': Dividend, 'label': 'Dividends', 'list_fields': ['id', 'investor_id', 'opportunity_id', 'amount', 'is_paid']},
    'votings': {'model': InvestorVoting, 'label': 'Investor Votings', 'list_fields': ['id', 'opportunity_id', 'question', 'is_active']},
    'payments': {'model': Payment, 'label': 'Payments', 'list_fields': ['id', 'investor_id', 'amount', 'payment_status', 'transaction_id']},
    'secondary': {'model': SecondaryMarket, 'label': 'Secondary Market', 'list_fields': ['id', 'investment_id', 'seller_id', 'listing_price', 'status']},
    'autoinvest': {'model': AutoInvest, 'label': 'Auto Invest', 'list_fields': ['id', 'investor_id', 'max_investment_amount', 'is_active']},
}


def admin_sidebar(active=''):
    links = [A(f'\u2302 Dashboard', href='/admin', cls='active' if active == 'dashboard' else '')]
    for key, cfg in ADMIN_MODELS.items():
        links.append(A(cfg['label'], href=f'/admin/{key}', cls='active' if active == key else ''))
    return Div(*links, cls='admin-sidebar')


def admin_layout(content, active='dashboard'):
    return (
        Title('PropFunder Admin'),
        Nav(
            Div(
                A('Prop', Span('Funder', style='color:#C8A96E;'), ' Admin', href='/admin',
                  style='font-family:Playfair Display,serif;font-size:1.3rem;font-weight:700;color:white;text-decoration:none;'),
                Div(
                    A('View Site', href='/', style='color:#ccc;text-decoration:none;font-size:0.9rem;margin-right:1.5rem;'),
                    A('Logout', href='/logout', style='color:#C8A96E;text-decoration:none;font-size:0.9rem;'),
                ),
                cls='nav-inner'
            ),
            cls='nav-main'
        ),
        admin_sidebar(active),
        Div(content, cls='admin-content')
    )


def status_badge(value):
    v = str(value).lower() if value else ''
    if v in ('active', 'open', 'confirmed', 'completed', 'true', 'yes'):
        return Span(str(value), cls='badge badge-green')
    elif v in ('pending', 'listed', 'draft'):
        return Span(str(value), cls='badge badge-yellow')
    elif v in ('defaulted', 'failed', 'cancelled', 'false', 'no'):
        return Span(str(value), cls='badge badge-red')
    elif v in ('funded', 'repaying'):
        return Span(str(value), cls='badge badge-blue')
    return Span(str(value), cls='badge badge-gray')


@ar('/admin')
def admin_dashboard():
    db = SessionLocal()
    try:
        stats = []
        for key, cfg in ADMIN_MODELS.items():
            count = db.query(cfg['model']).count()
            stats.append(
                Div(
                    H3(str(count)),
                    P(cfg['label']),
                    A('View \u2192', href=f'/admin/{key}',
                      style='display:block;margin-top:0.5rem;color:var(--primary);text-decoration:none;font-size:0.85rem;font-weight:600;'),
                    cls='stat-item',
                    style='background:white;padding:1.5rem;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.06);'
                )
            )
        content = Div(
            H1('Dashboard', style='font-size:1.8rem;margin-bottom:2rem;'),
            Div(*stats, style='display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1.5rem;'),
        )
    finally:
        db.close()
    return admin_layout(content, 'dashboard')


@ar('/admin/{model_key}')
def admin_list(model_key: str):
    if model_key not in ADMIN_MODELS:
        return admin_layout(P('Model not found.'), 'dashboard')

    cfg = ADMIN_MODELS[model_key]
    model = cfg['model']
    db = SessionLocal()
    try:
        items = db.query(model).order_by(model.id.desc()).limit(100).all()
        headers = [Th(f.replace('_', ' ').title()) for f in cfg['list_fields']]
        headers.append(Th('Actions'))

        rows = []
        for item in items:
            cells = []
            for f in cfg['list_fields']:
                val = getattr(item, f, '')
                if isinstance(val, bool) or (hasattr(val, 'value') and str(val.value) in ('true', 'false')):
                    cells.append(Td(status_badge(val)))
                elif f in ('status', 'funding_status', 'payment_status', 'role', 'property_type', 'risk_level', 'update_type'):
                    cells.append(Td(status_badge(val.value if hasattr(val, 'value') else val)))
                else:
                    display = str(val)[:50] if val is not None else '-'
                    cells.append(Td(display))
            cells.append(Td(
                A('Edit', href=f'/admin/{model_key}/{item.id}/edit',
                  style='color:var(--primary);text-decoration:none;font-weight:600;margin-right:1rem;'),
                A('Delete', href=f'/admin/{model_key}/{item.id}/delete',
                  style='color:#dc3545;text-decoration:none;font-weight:600;',
                  onclick="return confirm('Are you sure?')")
            ))
            rows.append(Tr(*cells))

        content = Div(
            Div(
                H1(cfg['label'], style='font-size:1.8rem;'),
                A(f'+ Add {cfg["label"]}', href=f'/admin/{model_key}/add', cls='btn btn-green',
                  style='padding:0.5rem 1.2rem;font-size:0.85rem;'),
                style='display:flex;justify-content:space-between;align-items:center;margin-bottom:1.5rem;'
            ),
            P(f'{len(items)} records', style='color:var(--gray);margin-bottom:1rem;font-size:0.9rem;'),
            Table(Thead(Tr(*headers)), Tbody(*rows), cls='admin-table') if rows else P('No records found.'),
        )
    finally:
        db.close()
    return admin_layout(content, model_key)


def get_model_fields(model):
    """Get editable fields for a model."""
    mapper = inspect(model)
    fields = []
    for col in mapper.columns:
        if col.name in ('id', 'created_at', 'updated_at'):
            continue
        field_type = 'text'
        col_type = str(col.type).upper()
        if 'INT' in col_type:
            field_type = 'number'
        elif 'NUMERIC' in col_type or 'DECIMAL' in col_type:
            field_type = 'number'
        elif 'BOOL' in col_type:
            field_type = 'checkbox'
        elif 'TEXT' in col_type:
            field_type = 'textarea'
        elif 'DATE' in col_type and 'TIME' not in col_type:
            field_type = 'date'
        elif 'DATETIME' in col_type or 'TIMESTAMP' in col_type:
            field_type = 'datetime-local'
        elif 'ENUM' in col_type or hasattr(col.type, 'enums'):
            field_type = 'select'

        fields.append({
            'name': col.name,
            'type': field_type,
            'nullable': col.nullable,
            'col': col,
        })
    return fields


def render_form_field(field, value=None):
    name = field['name']
    label_text = name.replace('_', ' ').title()

    if field['type'] == 'checkbox':
        checked = bool(value) if value is not None else False
        return Div(
            Label(
                Input(type='checkbox', name=name, checked=checked, value='true',
                      style='width:auto;margin-right:0.5rem;'),
                label_text
            ),
            style='margin-bottom:1rem;'
        )
    elif field['type'] == 'select' and hasattr(field['col'].type, 'enums'):
        enums = field['col'].type.enums
        options = [Option(e, value=e, selected=(str(value) == e if value else False)) for e in enums]
        options.insert(0, Option('-- Select --', value=''))
        return Div(Label(label_text), Select(*options, name=name))
    elif field['type'] == 'textarea':
        return Div(Label(label_text), Textarea(str(value or ''), name=name))
    else:
        return Div(
            Label(label_text),
            Input(type=field['type'], name=name, value=str(value or ''),
                  step='0.01' if field['type'] == 'number' else None)
        )


@ar('/admin/{model_key}/add', methods=['GET'])
def admin_add_form(model_key: str):
    if model_key not in ADMIN_MODELS:
        return admin_layout(P('Model not found.'), 'dashboard')

    cfg = ADMIN_MODELS[model_key]
    fields = get_model_fields(cfg['model'])
    form_fields = [render_form_field(f) for f in fields]

    content = Div(
        H1(f'Add {cfg["label"]}', style='font-size:1.8rem;margin-bottom:1.5rem;'),
        Form(
            *form_fields,
            Div(
                Button('Save', type='submit', cls='btn btn-green', style='margin-right:1rem;'),
                A('Cancel', href=f'/admin/{model_key}', cls='btn',
                  style='background:var(--gray-light);color:var(--dark);'),
            ),
            method='post', action=f'/admin/{model_key}/add',
            cls='admin-form'
        )
    )
    return admin_layout(content, model_key)


@ar('/admin/{model_key}/add', methods=['POST'])
async def admin_add_save(model_key: str, req):
    if model_key not in ADMIN_MODELS:
        return RedirectResponse('/admin', status_code=303)

    cfg = ADMIN_MODELS[model_key]
    model = cfg['model']
    form = await req.form()
    fields = get_model_fields(model)

    obj = model()
    for field in fields:
        name = field['name']
        val = form.get(name, '')
        if field['type'] == 'checkbox':
            setattr(obj, name, name in form)
        elif field['type'] == 'number' and val:
            try:
                setattr(obj, name, float(val) if '.' in str(val) else int(val))
            except (ValueError, TypeError):
                pass
        elif val:
            setattr(obj, name, val)
        elif field['nullable']:
            setattr(obj, name, None)

    db = SessionLocal()
    try:
        db.add(obj)
        db.commit()
    finally:
        db.close()

    return RedirectResponse(f'/admin/{model_key}', status_code=303)


@ar('/admin/{model_key}/{item_id}/edit', methods=['GET'])
def admin_edit_form(model_key: str, item_id: int):
    if model_key not in ADMIN_MODELS:
        return admin_layout(P('Model not found.'), 'dashboard')

    cfg = ADMIN_MODELS[model_key]
    model = cfg['model']
    db = SessionLocal()
    try:
        obj = db.query(model).get(item_id)
        if not obj:
            return admin_layout(P('Record not found.'), model_key)

        fields = get_model_fields(model)
        form_fields = [render_form_field(f, getattr(obj, f['name'], None)) for f in fields]
    finally:
        db.close()

    content = Div(
        H1(f'Edit {cfg["label"]} #{item_id}', style='font-size:1.8rem;margin-bottom:1.5rem;'),
        Form(
            *form_fields,
            Div(
                Button('Save Changes', type='submit', cls='btn btn-green', style='margin-right:1rem;'),
                A('Cancel', href=f'/admin/{model_key}', cls='btn',
                  style='background:var(--gray-light);color:var(--dark);'),
            ),
            method='post', action=f'/admin/{model_key}/{item_id}/edit',
            cls='admin-form'
        )
    )
    return admin_layout(content, model_key)


@ar('/admin/{model_key}/{item_id}/edit', methods=['POST'])
async def admin_edit_save(model_key: str, item_id: int, req):
    if model_key not in ADMIN_MODELS:
        return RedirectResponse('/admin', status_code=303)

    cfg = ADMIN_MODELS[model_key]
    model = cfg['model']
    form = await req.form()
    fields = get_model_fields(model)

    db = SessionLocal()
    try:
        obj = db.query(model).get(item_id)
        if not obj:
            return RedirectResponse(f'/admin/{model_key}', status_code=303)

        for field in fields:
            name = field['name']
            val = form.get(name, '')
            if field['type'] == 'checkbox':
                setattr(obj, name, name in form)
            elif field['type'] == 'number' and val:
                try:
                    setattr(obj, name, float(val) if '.' in str(val) else int(val))
                except (ValueError, TypeError):
                    pass
            elif val:
                setattr(obj, name, val)
            elif field['nullable']:
                setattr(obj, name, None)

        db.commit()
    finally:
        db.close()

    return RedirectResponse(f'/admin/{model_key}', status_code=303)


@ar('/admin/{model_key}/{item_id}/delete')
def admin_delete(model_key: str, item_id: int):
    if model_key not in ADMIN_MODELS:
        return RedirectResponse('/admin', status_code=303)

    cfg = ADMIN_MODELS[model_key]
    model = cfg['model']
    db = SessionLocal()
    try:
        obj = db.query(model).get(item_id)
        if obj:
            db.delete(obj)
            db.commit()
    finally:
        db.close()

    return RedirectResponse(f'/admin/{model_key}', status_code=303)
