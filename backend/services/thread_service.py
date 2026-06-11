from backend.database.models import Email

def get_thread_history(
    db,
    thread_id
):

    emails = (
        db.query(Email)
        .filter(
            Email.thread_id == thread_id
        )
        .order_by(
            Email.timestamp.asc()
        )
        .all()
    )

    return emails


def get_thread_history(
    db,
    thread_id
):

    emails = (
        db.query(Email)
        .filter(
            Email.thread_id == thread_id
        )
        .order_by(
            Email.timestamp.asc()
        )
        .all()
    )

    return emails