from .models import Email
from .models import Thread
from .models import Contact
from datetime import datetime
from backend.database.models import Action
from backend.database.models import AuditLog
from datetime import datetime

def get_email_by_message_id(db, message_id):

    return (
        db.query(Email)
        .filter(Email.message_id == message_id)
        .first()
    )


def create_thread(
    db,
    thread_id,
    sender_email,
    subject
):

    thread = Thread(
        thread_id=thread_id,
        sender_email=sender_email,
        subject=subject,
        status="Open",
        first_seen_at=datetime.utcnow(),
        last_updated_at=datetime.utcnow()
    )

    db.add(thread)
    db.commit()
    db.refresh(thread)

    return thread

def get_thread(db, thread_id):

    return (
        db.query(Thread)
        .filter(Thread.thread_id == thread_id)
        .first()
    )


def save_email(db, email_data,sentiment,category):

    email = Email(
        message_id=email_data.message_id,
        thread_id=email_data.thread_id,
        sender=email_data.sender,
        subject=email_data.subject,
        body=email_data.body,
        timestamp=email_data.timestamp,
        sentiment_score=sentiment,
        category=category,
        status="Received"
        
    )

    db.add(email)

    db.commit()

    db.refresh(email)

    return email


def get_contact_by_email(
    db,
    email
):
    return (
        db.query(Contact)
        .filter(Contact.email == email)
        .first()
    )

def create_contact(
    db,
    email
):

    contact = Contact(
        email=email,
        status="Active",
        account_value=0,
        churn_risk_score=0,
        created_at=datetime.utcnow(),
        last_contact_at=datetime.utcnow()
    )

    db.add(contact)

    db.commit()

    db.refresh(contact)

    return contact

def create_action(
    db,
    email_id,
    action_type,
    content,
    reasoning
):

    action = Action(
        email_id=email_id,
        action_type=action_type,
        proposed_content=content,
        reasoning_log=reasoning,
        executed_at=datetime.utcnow()
    )

    db.add(action)

    db.commit()

    db.refresh(action)

    return action

def create_audit_log(
    db,
    entity_type,
    entity_id,
    action
):

    log = AuditLog(

        entity_type=entity_type,

        entity_id=entity_id,

        action=action,

        performed_by="system",

        timestamp=datetime.utcnow()
    )

    db.add(log)

    db.commit()

    db.refresh(log)

    return log