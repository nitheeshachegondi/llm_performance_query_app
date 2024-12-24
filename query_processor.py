from datetime import datetime, timedelta
import dateparser # type: ignore

def process_query(user_query):
    """
    Process a user query and return a structured JSON response.
    
    Args:
        user_query (str): The user's natural language query.
    
    Returns:
        dict: A structured JSON response containing extracted details.
    """
    # Example logic for entity extraction
    entity = None
    if "Amazon" in user_query:
        entity = "Amazon"
    elif "Flipkart" in user_query:
        entity = "Flipkart"

    # Example logic for metric extraction
    metric = None
    if "revenue" in user_query:
        metric = "revenue"
    elif "profit" in user_query:
        metric = "profit"
    
    # Example date extraction and defaults
    start_date = None
    end_date = None
    if "last year" in user_query:
        start_date = (datetime.now() - timedelta(days=365)).date()
        end_date = datetime.now().date()
    elif "this year" in user_query:
        start_date = datetime(datetime.now().year, 1, 1).date()
        end_date = datetime.now().date()

    # Fallback to defaults if dates are not mentioned
    if not start_date:
        start_date = (datetime.now() - timedelta(days=365)).date()
    if not end_date:
        end_date = datetime.now().date()

    # Convert dates to ISO 8601 format
    start_date = start_date.isoformat()
    end_date = end_date.isoformat()

    # Return structured JSON
    result = {
        "entity": entity,
        "parameter": metric,
        "start_date": start_date,
        "end_date": end_date
    }
    return result
