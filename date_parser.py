from datetime import datetime, timedelta
import dateparser  # type: ignore

def parse_dates(user_query):
    # Default date range (1 year ago to today)
    today = datetime.today()
    start_date = today - timedelta(days=365)
    end_date = today

    # Attempt to find start and end dates in user query
    start_date_parsed = dateparser.parse(user_query)
    if start_date_parsed:
        start_date = start_date_parsed

    end_date_parsed = dateparser.parse(user_query)
    if end_date_parsed:
        end_date = end_date_parsed

    # Return dates in ISO 8601 format
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
