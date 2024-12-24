import json
from query_processor import process_query

if __name__ == "__main__":
    user_query = "What was Amazon's revenue from last year to this year?"
    result = process_query(user_query)

    # Define the output file name
    output_file = "query_result.json"

    # Write the result to a JSON file
    with open(output_file, "w") as json_file:
        json.dump(result, json_file, indent=4)

    print(f"Result has been stored in {output_file}")
