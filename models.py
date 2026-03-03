from datetime import datetime, date
from decimal import Decimal
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime, Date,
    Numeric, ForeignKey, UniqueConstraint, Enum as SAEnum
)
from sqlalchemy.orm import relationship
from db import Base, SCHEMA
import enum


# --- Enums ---

class UserRole(str, enum.Enum):
    investor = "investor"
    borrower = "borrower"
    admin = "admin"

class PropertyType(str, enum.Enum):
    residential = "residential"
    commercial = "commercial"
    mixed_use = "mixed_use"
    land = "land"
    industrial = "industrial"

class PropertyStatus(str, enum.Enum):
    draft = "draft"
    active = "active"
    funded = "funded"
    completed = "completed"
    defaulted = "defaulted"

class FundingStatus(str, enum.Enum):
    open = "open"
    funded = "funded"
    closed = "closed"
    repaying = "repaying"

class RiskLevel(str, enum.Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"

class InvestmentStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    completed = "completed"
    cancelled = "cancelled"

class PaymentStatus(str, enum.Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"

class ListingStatus(str, enum.Enum):
    listed = "listed"
    sold = "sold"
    withdrawn = "withdrawn"

class UpdateType(str, enum.Enum):
    status_update = "status_update"
    construction_update = "construction_update"
    financial_update = "financial_update"
    milestone = "milestone"

class NotificationType(str, enum.Enum):
    general = "general"
    investment = "investment"
    repayment = "repayment"
    project_update = "project_update"


# --- Models ---

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False, default="")
    last_name = Column(String(100), nullable=False, default="")
    role = Column(SAEnum(UserRole, name="user_role", schema=SCHEMA), default=UserRole.investor, nullable=False)
    phone = Column(String(50))
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    properties = relationship("Property", back_populates="developer")
    investments = relationship("Investment", back_populates="investor")
    notifications = relationship("Notification", back_populates="user")
    follows = relationship("FollowProperty", back_populates="user")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.email


class Company(Base):
    __tablename__ = "companies"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    registration_number = Column(String(100), unique=True)
    address = Column(Text)
    user_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)


class Property(Base):
    __tablename__ = "properties"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    property_type = Column(SAEnum(PropertyType, name="property_type", schema=SCHEMA), nullable=False)
    status = Column(SAEnum(PropertyStatus, name="property_status", schema=SCHEMA), default=PropertyStatus.draft)
    address = Column(String(500))
    city = Column(String(100))
    country = Column(String(100))
    postal_code = Column(String(20))
    land_area_sqm = Column(Numeric(12, 2))
    building_area_sqm = Column(Numeric(12, 2))
    valuation = Column(Numeric(14, 2))
    ltv_ratio = Column(Numeric(5, 2))  # Loan-to-value ratio
    developer_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"))
    image_url = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    developer = relationship("User", back_populates="properties")
    funding = relationship("InvestmentOpportunity", back_populates="prop", uselist=False)
    updates = relationship("ProjectUpdate", back_populates="prop")


class InvestmentOpportunity(Base):
    __tablename__ = "investment_opportunities"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    property_id = Column(Integer, ForeignKey(f"{SCHEMA}.properties.id"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    loan_amount = Column(Numeric(14, 2), nullable=False)
    amount_raised = Column(Numeric(14, 2), default=0)
    minimum_investment = Column(Numeric(10, 2), default=50)
    interest_rate = Column(Numeric(5, 2), nullable=False)  # Annual %
    loan_term_months = Column(Integer, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    funding_status = Column(SAEnum(FundingStatus, name="funding_status", schema=SCHEMA), default=FundingStatus.open)
    risk_level = Column(SAEnum(RiskLevel, name="risk_level", schema=SCHEMA), default=RiskLevel.B)
    loan_type = Column(String(50), default="bridge_loan")  # bridge_loan, development, bullet
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    prop = relationship("Property", back_populates="funding")
    investments = relationship("Investment", back_populates="opportunity")
    repayments = relationship("Repayment", back_populates="opportunity")
    votes = relationship("InvestorVoting", back_populates="opportunity")

    @property
    def funding_progress(self):
        if self.loan_amount and self.loan_amount > 0:
            return float((self.amount_raised or 0) / self.loan_amount * 100)
        return 0


class Investment(Base):
    __tablename__ = "investments"
    __table_args__ = (
        UniqueConstraint("opportunity_id", "investor_id", name="uq_opportunity_investor"),
        {"schema": SCHEMA},
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    opportunity_id = Column(Integer, ForeignKey(f"{SCHEMA}.investment_opportunities.id"), nullable=False)
    investor_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"), nullable=False)
    amount = Column(Numeric(14, 2), nullable=False)
    ownership_percentage = Column(Numeric(5, 2))
    expected_return = Column(Numeric(14, 2))
    status = Column(SAEnum(InvestmentStatus, name="investment_status", schema=SCHEMA), default=InvestmentStatus.pending)
    invested_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    opportunity = relationship("InvestmentOpportunity", back_populates="investments")
    investor = relationship("User", back_populates="investments")
    payments = relationship("Payment", back_populates="investment")
    secondary_listing = relationship("SecondaryMarket", back_populates="investment", uselist=False)


class ProjectUpdate(Base):
    __tablename__ = "project_updates"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    property_id = Column(Integer, ForeignKey(f"{SCHEMA}.properties.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    update_type = Column(SAEnum(UpdateType, name="update_type", schema=SCHEMA), default=UpdateType.status_update)
    created_at = Column(DateTime, default=datetime.utcnow)

    prop = relationship("Property", back_populates="updates")


class Notification(Base):
    __tablename__ = "notifications"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    message = Column(Text)
    notification_type = Column(SAEnum(NotificationType, name="notification_type", schema=SCHEMA), default=NotificationType.general)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="notifications")


class FollowProperty(Base):
    __tablename__ = "follow_properties"
    __table_args__ = (
        UniqueConstraint("user_id", "property_id", name="uq_user_property_follow"),
        {"schema": SCHEMA},
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"), nullable=False)
    property_id = Column(Integer, ForeignKey(f"{SCHEMA}.properties.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="follows")


class FAQ(Base):
    __tablename__ = "faqs"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)


class Repayment(Base):
    __tablename__ = "repayments"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    opportunity_id = Column(Integer, ForeignKey(f"{SCHEMA}.investment_opportunities.id"), nullable=False)
    amount = Column(Numeric(14, 2), nullable=False)
    repayment_date = Column(Date, nullable=False)
    is_principal = Column(Boolean, default=False)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    opportunity = relationship("InvestmentOpportunity", back_populates="repayments")


class Dividend(Base):
    __tablename__ = "dividends"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    investor_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"), nullable=False)
    opportunity_id = Column(Integer, ForeignKey(f"{SCHEMA}.investment_opportunities.id"), nullable=False)
    amount = Column(Numeric(14, 2), nullable=False)
    is_paid = Column(Boolean, default=False)
    paid_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)


class InvestorVoting(Base):
    __tablename__ = "investor_votings"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    opportunity_id = Column(Integer, ForeignKey(f"{SCHEMA}.investment_opportunities.id"), nullable=False)
    question = Column(Text, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    opportunity = relationship("InvestmentOpportunity", back_populates="votes")
    user_votes = relationship("UserVote", back_populates="voting")


class UserVote(Base):
    __tablename__ = "user_votes"
    __table_args__ = (
        UniqueConstraint("user_id", "voting_id", name="uq_user_voting"),
        {"schema": SCHEMA},
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"), nullable=False)
    voting_id = Column(Integer, ForeignKey(f"{SCHEMA}.investor_votings.id"), nullable=False)
    vote_choice = Column(String(10), nullable=False)  # yes/no
    created_at = Column(DateTime, default=datetime.utcnow)

    voting = relationship("InvestorVoting", back_populates="user_votes")


class Payment(Base):
    __tablename__ = "payments"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    investor_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"), nullable=False)
    investment_id = Column(Integer, ForeignKey(f"{SCHEMA}.investments.id"), nullable=False)
    amount = Column(Numeric(14, 2), nullable=False)
    payment_status = Column(SAEnum(PaymentStatus, name="payment_status", schema=SCHEMA), default=PaymentStatus.pending)
    transaction_id = Column(String(100), unique=True)
    reference_number = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

    investment = relationship("Investment", back_populates="payments")


class SecondaryMarket(Base):
    __tablename__ = "secondary_market"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    investment_id = Column(Integer, ForeignKey(f"{SCHEMA}.investments.id"), nullable=False)
    seller_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"), nullable=False)
    listing_price = Column(Numeric(14, 2), nullable=False)
    status = Column(SAEnum(ListingStatus, name="listing_status", schema=SCHEMA), default=ListingStatus.listed)
    listed_at = Column(DateTime, default=datetime.utcnow)
    sold_at = Column(DateTime)

    investment = relationship("Investment", back_populates="secondary_listing")


class AutoInvest(Base):
    __tablename__ = "auto_invest"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    investor_id = Column(Integer, ForeignKey(f"{SCHEMA}.users.id"), nullable=False)
    max_investment_amount = Column(Numeric(14, 2), nullable=False)
    min_interest_rate = Column(Numeric(5, 2))
    max_ltv = Column(Numeric(5, 2))
    preferred_risk_levels = Column(String(20))  # comma-separated: A,B,C
    preferred_property_types = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
