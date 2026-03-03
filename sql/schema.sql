-- PropFunder Database Schema
-- PostgreSQL schema for property-backed investment platform

CREATE SCHEMA IF NOT EXISTS propfunder;

-- Enum types
DO $$ BEGIN
    CREATE TYPE propfunder.user_role AS ENUM ('investor', 'borrower', 'admin');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE propfunder.property_type AS ENUM ('residential', 'commercial', 'mixed_use', 'land', 'industrial');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE propfunder.property_status AS ENUM ('draft', 'active', 'funded', 'completed', 'defaulted');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE propfunder.funding_status AS ENUM ('open', 'funded', 'closed', 'repaying');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE propfunder.risk_level AS ENUM ('A', 'B', 'C', 'D');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE propfunder.investment_status AS ENUM ('pending', 'confirmed', 'completed', 'cancelled');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE propfunder.payment_status AS ENUM ('pending', 'completed', 'failed');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE propfunder.listing_status AS ENUM ('listed', 'sold', 'withdrawn');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE propfunder.update_type AS ENUM ('status_update', 'construction_update', 'financial_update', 'milestone');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE propfunder.notification_type AS ENUM ('general', 'investment', 'repayment', 'project_update');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- Users
CREATE TABLE IF NOT EXISTS propfunder.users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL DEFAULT '',
    last_name VARCHAR(100) NOT NULL DEFAULT '',
    role propfunder.user_role NOT NULL DEFAULT 'investor',
    phone VARCHAR(50),
    is_verified BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    is_staff BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_users_email ON propfunder.users(email);
CREATE INDEX IF NOT EXISTS idx_users_role ON propfunder.users(role);

-- Companies
CREATE TABLE IF NOT EXISTS propfunder.companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    registration_number VARCHAR(100) UNIQUE,
    address TEXT,
    user_id INTEGER REFERENCES propfunder.users(id),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Properties
CREATE TABLE IF NOT EXISTS propfunder.properties (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    property_type propfunder.property_type NOT NULL,
    status propfunder.property_status DEFAULT 'draft',
    address VARCHAR(500),
    city VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(20),
    land_area_sqm NUMERIC(12,2),
    building_area_sqm NUMERIC(12,2),
    valuation NUMERIC(14,2),
    ltv_ratio NUMERIC(5,2),
    developer_id INTEGER REFERENCES propfunder.users(id),
    image_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_properties_status ON propfunder.properties(status);
CREATE INDEX IF NOT EXISTS idx_properties_type ON propfunder.properties(property_type);
CREATE INDEX IF NOT EXISTS idx_properties_developer ON propfunder.properties(developer_id);

-- Investment Opportunities (loans against properties)
CREATE TABLE IF NOT EXISTS propfunder.investment_opportunities (
    id SERIAL PRIMARY KEY,
    property_id INTEGER NOT NULL REFERENCES propfunder.properties(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    loan_amount NUMERIC(14,2) NOT NULL,
    amount_raised NUMERIC(14,2) DEFAULT 0,
    minimum_investment NUMERIC(10,2) DEFAULT 50,
    interest_rate NUMERIC(5,2) NOT NULL,
    loan_term_months INTEGER NOT NULL,
    start_date DATE,
    end_date DATE,
    funding_status propfunder.funding_status DEFAULT 'open',
    risk_level propfunder.risk_level DEFAULT 'B',
    loan_type VARCHAR(50) DEFAULT 'bridge_loan',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_opportunities_status ON propfunder.investment_opportunities(funding_status);
CREATE INDEX IF NOT EXISTS idx_opportunities_property ON propfunder.investment_opportunities(property_id);

-- Investments
CREATE TABLE IF NOT EXISTS propfunder.investments (
    id SERIAL PRIMARY KEY,
    opportunity_id INTEGER NOT NULL REFERENCES propfunder.investment_opportunities(id),
    investor_id INTEGER NOT NULL REFERENCES propfunder.users(id),
    amount NUMERIC(14,2) NOT NULL,
    ownership_percentage NUMERIC(5,2),
    expected_return NUMERIC(14,2),
    status propfunder.investment_status DEFAULT 'pending',
    invested_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(opportunity_id, investor_id)
);
CREATE INDEX IF NOT EXISTS idx_investments_investor ON propfunder.investments(investor_id);
CREATE INDEX IF NOT EXISTS idx_investments_opportunity ON propfunder.investments(opportunity_id);

-- Project Updates
CREATE TABLE IF NOT EXISTS propfunder.project_updates (
    id SERIAL PRIMARY KEY,
    property_id INTEGER NOT NULL REFERENCES propfunder.properties(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    update_type propfunder.update_type DEFAULT 'status_update',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Notifications
CREATE TABLE IF NOT EXISTS propfunder.notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES propfunder.users(id),
    title VARCHAR(255) NOT NULL,
    message TEXT,
    notification_type propfunder.notification_type DEFAULT 'general',
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_notifications_user ON propfunder.notifications(user_id);

-- Follow Properties
CREATE TABLE IF NOT EXISTS propfunder.follow_properties (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES propfunder.users(id),
    property_id INTEGER NOT NULL REFERENCES propfunder.properties(id),
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, property_id)
);

-- FAQs
CREATE TABLE IF NOT EXISTS propfunder.faqs (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    display_order INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE
);

-- Repayments
CREATE TABLE IF NOT EXISTS propfunder.repayments (
    id SERIAL PRIMARY KEY,
    opportunity_id INTEGER NOT NULL REFERENCES propfunder.investment_opportunities(id),
    amount NUMERIC(14,2) NOT NULL,
    repayment_date DATE NOT NULL,
    is_principal BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Dividends
CREATE TABLE IF NOT EXISTS propfunder.dividends (
    id SERIAL PRIMARY KEY,
    investor_id INTEGER NOT NULL REFERENCES propfunder.users(id),
    opportunity_id INTEGER NOT NULL REFERENCES propfunder.investment_opportunities(id),
    amount NUMERIC(14,2) NOT NULL,
    is_paid BOOLEAN DEFAULT FALSE,
    paid_date DATE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Investor Votings
CREATE TABLE IF NOT EXISTS propfunder.investor_votings (
    id SERIAL PRIMARY KEY,
    opportunity_id INTEGER NOT NULL REFERENCES propfunder.investment_opportunities(id),
    question TEXT NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- User Votes
CREATE TABLE IF NOT EXISTS propfunder.user_votes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES propfunder.users(id),
    voting_id INTEGER NOT NULL REFERENCES propfunder.investor_votings(id),
    vote_choice VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, voting_id)
);

-- Payments
CREATE TABLE IF NOT EXISTS propfunder.payments (
    id SERIAL PRIMARY KEY,
    investor_id INTEGER NOT NULL REFERENCES propfunder.users(id),
    investment_id INTEGER NOT NULL REFERENCES propfunder.investments(id),
    amount NUMERIC(14,2) NOT NULL,
    payment_status propfunder.payment_status DEFAULT 'pending',
    transaction_id VARCHAR(100) UNIQUE,
    reference_number VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Secondary Market
CREATE TABLE IF NOT EXISTS propfunder.secondary_market (
    id SERIAL PRIMARY KEY,
    investment_id INTEGER NOT NULL REFERENCES propfunder.investments(id),
    seller_id INTEGER NOT NULL REFERENCES propfunder.users(id),
    listing_price NUMERIC(14,2) NOT NULL,
    status propfunder.listing_status DEFAULT 'listed',
    listed_at TIMESTAMP DEFAULT NOW(),
    sold_at TIMESTAMP
);

-- Auto Invest Settings
CREATE TABLE IF NOT EXISTS propfunder.auto_invest (
    id SERIAL PRIMARY KEY,
    investor_id INTEGER NOT NULL REFERENCES propfunder.users(id),
    max_investment_amount NUMERIC(14,2) NOT NULL,
    min_interest_rate NUMERIC(5,2),
    max_ltv NUMERIC(5,2),
    preferred_risk_levels VARCHAR(20),
    preferred_property_types VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Seed admin user (password: admin123 - change in production)
-- Password hash is bcrypt of 'admin123'
INSERT INTO propfunder.users (email, password_hash, first_name, last_name, role, is_verified, is_active, is_staff)
VALUES ('admin@propfunder.com', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'Admin', 'User', 'admin', true, true, true)
ON CONFLICT (email) DO NOTHING;
