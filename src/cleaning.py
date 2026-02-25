import pandas as pd


def filter_term_and_type(df, term_code, hall_ticket_type):
    df_term = df[df["term_code"] == term_code]
    return df_term[df_term["hall_ticket_type"] == hall_ticket_type]


def filter_course(df, course_code):
    return df[df["course_code"] == course_code]


def merge_student_email(df_q, df_mapping):
    return pd.merge(
        df_q,
        df_mapping,
        on="Hall Ticket Number",
        how="left"
    )


def final_selection(df):
    df = df[
        [
            "Hall Ticket Number",
            "hall_ticket_type",
            "Question Id",
            "Question Type",
            "Score",
            "Mark",
            "student_email"
        ]
    ]

    df = df.dropna()

    df = df.drop_duplicates(
        subset=["student_email", "Question Id"]
    )

    return df
