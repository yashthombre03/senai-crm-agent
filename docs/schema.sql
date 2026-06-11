CREATE TABLE contacts (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE,
    company TEXT,
    status TEXT,
    account_value FLOAT,
    churn_risk_score FLOAT,
    negative_streak INTEGER DEFAULT 0,
    average_sentiment FLOAT DEFAULT 0,
    created_at DATETIME,
    last_contact_at DATETIME
);

CREATE TABLE threads (
    id INTEGER PRIMARY KEY,
    thread_id TEXT UNIQUE,
    sender_email TEXT,
    subject TEXT,
    status TEXT,
    first_seen_at DATETIME,
    last_updated_at DATETIME
);

CREATE TABLE emails (
    id INTEGER PRIMARY KEY,
    message_id TEXT UNIQUE,
    thread_id TEXT,
    sender TEXT,
    subject TEXT,
    body TEXT,
    timestamp DATETIME,
    category TEXT,
    sentiment_score FLOAT,
    urgency TEXT,
    confidence FLOAT,
    requires_human BOOLEAN,
    status TEXT
);

CREATE TABLE actions (
    id INTEGER PRIMARY KEY,
    email_id INTEGER,
    action_type TEXT,
    proposed_content TEXT,
    reasoning_log TEXT,
    executed_at DATETIME
);

CREATE TABLE audit_logs (
    id INTEGER PRIMARY KEY,
    entity_type TEXT,
    entity_id INTEGER,
    action TEXT,
    performed_by TEXT,
    timestamp DATETIME
);