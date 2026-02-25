import argparse
from src.pipeline import run_quiz_cleaning


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--hallticket_path", required=True)
    parser.add_argument("--questionwise_path", required=True)
    parser.add_argument("--term_code", required=True)
    parser.add_argument("--hall_ticket_type", required=True)
    parser.add_argument("--course_code", required=True)
    parser.add_argument("--output_path", required=True)

    args = parser.parse_args()

    run_quiz_cleaning(
        hallticket_path=args.hallticket_path,
        questionwise_path=args.questionwise_path,
        term_code=args.term_code,
        hall_ticket_type=args.hall_ticket_type,
        course_code=args.course_code,
        output_path=args.output_path
    )


if __name__ == "__main__":
    main()
