def resolve_company_name(query):
    company_list = ["Flipkart", "Amazon", "Walmart"]  # Example list
    for company in company_list:
        if company.lower() in query.lower():
            return company
    return None

def resolve_performance_parameter(query):
    metric_list = ["GMV", "Revenue", "Profit"]  # Example list
    for metric in metric_list:
        if metric.lower() in query.lower():
            return metric
    return None
