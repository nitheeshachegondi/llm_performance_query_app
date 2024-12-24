from llama_query_handler import handle_query
from date_parser import parse_dates
from json_formatter import format_json
from utils.error_handler import handle_error

def process_query(user_query):
    try:
        # Step 1: Handle query with LLM to extract entities and metrics
        entities, parameters = handle_query(user_query)

        # Step 2: Parse dates from the query, if available
        start_date, end_date = parse_dates(user_query)

        # Step 3: Format the extracted data into JSON
        json_output = format_json(entities, parameters, start_date, end_date)
        return json_output
    except Exception as e:
        handle_error(e)
