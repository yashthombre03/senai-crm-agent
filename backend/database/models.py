from sqlalchemy import *
from sqlalchemy.orm import declarative_base

raw_entities = Column(JSON, nullable=True)

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True)

    company = Column(String)

    status = Column(String)

    account_value = Column(Float)

    churn_risk_score = Column(Float)
    
    negative_streak = Column(Integer, default=0)

    average_sentiment = Column(Float, default=0)

    created_at = Column(DateTime)

    last_contact_at = Column(DateTime)

    

class Thread(Base):
    __tablename__ = "threads"

    id = Column(Integer, primary_key=True)

    thread_id = Column(String, unique=True)

    sender_email = Column(String)

    subject = Column(String)

    status = Column(String)

    first_seen_at = Column(DateTime)

    last_updated_at = Column(DateTime)

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True)

    message_id = Column(String, unique=True)

    thread_id = Column(String)

    sender = Column(String)

    subject = Column(String)

    body = Column(Text)

    timestamp = Column(DateTime)

    category = Column(String)

    sentiment_score = Column(Float)

    urgency = Column(String)

    confidence = Column(Float)

    requires_human = Column(Boolean)

    status = Column(String)

class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True)

    email_id = Column(Integer)

    action_type = Column(String)

    proposed_content = Column(Text)

    reasoning_log = Column(Text)

    executed_at = Column(DateTime)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)

    entity_type = Column(String)

    entity_id = Column(Integer)

    action = Column(String)

    performed_by = Column(String)

    timestamp = Column(DateTime)


