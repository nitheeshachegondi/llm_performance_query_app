import json

def format_json(entities, parameters, start_date, end_date):
    json_data = []

    for entity in entities:
        json_data.append({
            "company": entity,
            "parameter": parameters,
            "start_date": start_date,
            "end_date": end_date
        })

    return json.dumps(json_data, indent=4)
