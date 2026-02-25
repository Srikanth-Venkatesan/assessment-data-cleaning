from .loader import load_hallticket_mapping, load_questionwise_data
from .cleaning import (
    filter_term_and_type,
    filter_course,
    merge_student_email,
    final_selection
)


def run_quiz_cleaning(
    hallticket_path,
    questionwise_path,
    term_code,
    hall_ticket_type,
    course_code,
    output_path
):
    # Load data
    df_map = load_hallticket_mapping(hallticket_path)
    df_q = load_questionwise_data(questionwise_path)

    # Filter
    df_map_filtered = filter_term_and_type(
        df_map,
        term_code,
        hall_ticket_type
    )

    df_q_filtered = filter_course(df_q, course_code)

    # Merge
    df_merged = merge_student_email(
        df_q_filtered,
        df_map_filtered
    )

    # Final selection
    df_final = final_selection(df_merged)

    df_final.to_csv(output_path, index=False)

    print(f"Saved cleaned file to: {output_path}")
    print(f"Unique students: {df_final['student_email'].nunique()}")
