import streamlit as st
import sqlite3
import pandas as pd
from streamlit_autorefresh import st_autorefresh

#Connection
conn = sqlite3.connect(
    "senai.db",
    check_same_thread=False
)

#Dashboard Title
st.set_page_config(
    page_title="SenAI CRM Dashboard",
    layout="wide"
)

st_autorefresh(
    interval=5000,
    key="refresh"
)

st.title(
    "📧 SenAI CRM Dashboard"
)


#Load Tables
def load_table(table_name):

    query = f"""
    SELECT *
    FROM {table_name}
    """

    return pd.read_sql(
        query,
        conn
    )

emails_df = load_table("emails")

contacts_df = load_table("contacts")

actions_df = load_table("actions")

audit_df = load_table("audit_logs")


#SIDEBAR FILTERS
st.sidebar.header("Filters")

#Category filter
categories = sorted(
    emails_df["category"]
    .dropna()
    .unique()
)

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + list(categories)
)

#Sender filter
senders = sorted(
    emails_df["sender"]
    .dropna()
    .unique()
)

selected_sender = st.sidebar.selectbox(
    "Sender",
    ["All"] + list(senders)
)

#Search box
search_term = st.sidebar.text_input(
    "Search Email Body"
)

#Apply filters
filtered_emails = emails_df.copy()

if selected_category != "All":

    filtered_emails = filtered_emails[
        filtered_emails["category"]
        == selected_category
    ]

if selected_sender != "All":

    filtered_emails = filtered_emails[
        filtered_emails["sender"]
        == selected_sender
    ]

if search_term:

    filtered_emails = filtered_emails[
        filtered_emails["body"]
        .str.contains(
            search_term,
            case=False,
            na=False
        )
    ]

#Top Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Contacts",
    len(contacts_df)
)

col2.metric(
    "Emails",
    len(emails_df)
)

col3.metric(
    "Actions",
    len(actions_df)
)

escalations = len(
    actions_df[
        actions_df["action_type"]
        == "human_escalation"
    ]
)

col4.metric(
    "Escalations",
    escalations
)



escalation_rate = (
    escalations
    / len(emails_df)
) * 100

st.metric(
    "Escalation %",
    round(escalation_rate, 2)
)

#CRM Health
st.subheader(
    "CRM Health"
)

avg_sentiment = emails_df[
    "sentiment_score"
].mean()


col1, col2 = st.columns(2)

col1.metric(
    "Average Sentiment",
    round(avg_sentiment, 2)
)

col2.metric(
    "Escalation Rate %",
    round(escalation_rate, 2)
)


#Filtered Emails
st.subheader(
    "Filtered Emails"
)

st.dataframe(
    filtered_emails
)

threads = sorted(
    emails_df["thread_id"]
    .dropna()
    .unique()
)



#Showcase Feature
selected_email = st.selectbox(
    "Inspect Email",
    emails_df["message_id"]
)

email_data = emails_df[
    emails_df["message_id"]
    == selected_email
].iloc[0]

st.subheader("Email Inspector")

selected_thread = st.selectbox(
    "Select Thread",
    threads
)

thread_df = emails_df[
    emails_df["thread_id"]
    == selected_thread
]

col1, col2 = st.columns(2)

col1.metric(
    "Category",
    str(email_data["category"])
)

col2.metric(
    "Sentiment",
    email_data["sentiment_score"]
)

st.write("### Subject")
st.write(email_data["subject"])

st.write("### Sender")
st.write(email_data["sender"])

st.write("### Email Content")
st.info(email_data["body"])


st.subheader(
    "Thread History"
)

st.dataframe(

    thread_df[
        [
            "timestamp",
            "sender",
            "subject",
            "body"
        ]
    ]
)

#AI Actions Viewer
st.subheader(
    "AI Actions"
)

st.dataframe(
    actions_df.sort_values(
        "id",
        ascending=False
    )
)

st.subheader(
    "Latest Agent Decision"
)

if len(actions_df) > 0:

    latest_action = actions_df.sort_values(
        "id",
        ascending=False
    ).iloc[0]

    st.write(
        f"Action Type: {latest_action['action_type']}"
    )

    st.write(
        "Reasoning:"
    )

    st.info(
        latest_action["reasoning_log"]
    )

    st.write(
        "Generated Response:"
    )

    st.success(
        latest_action["proposed_content"]
    )


#Escalation Monitor
escalations_df = actions_df[
    actions_df["action_type"]
    == "human_escalation"
]

st.subheader(
    "Escalations"
)

st.dataframe(
    escalations_df
)

#Sentiment Chart
st.subheader(
    "Top Senders"
)

top_senders = (
    emails_df["sender"]
    .value_counts()
    .head(10)
)

st.bar_chart(
    top_senders
)

st.subheader(
    "Sentiment Distribution"
)
sentiment_counts = (
    emails_df["sentiment_score"]
    .value_counts()
)

st.bar_chart(
    sentiment_counts
)

#Category Chart
st.subheader(
    "Category Distribution"
)

category_counts = (
    emails_df["category"]
    .value_counts()
)

st.bar_chart(
    category_counts
)

#Audit Logs
st.subheader(
    "Audit Logs"
)

st.dataframe(
    audit_df.sort_values(
        "id",
        ascending=False
    )
)

