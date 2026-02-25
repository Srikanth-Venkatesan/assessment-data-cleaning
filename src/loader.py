import pandas as pd


def load_hallticket_mapping(path):
    df = pd.read_csv(path)

    df["Hall Ticket Number"] = (
        df["hall_ticket_file_name"]
        .str.split("/")
        .str[-1]
        .str.replace(".pdf", "", regex=True)
    )

    return df


def load_questionwise_data(path):
    df = pd.read_csv(path)

    df["course_code"] = (
        df["courseid"]
        .str.extract(r'-(\w+)(?:q1|et|q2|qf|qd)-')
        .str.lower()
    )

    return df
