# LLM-powered Performance Query Application

## Overview
This application processes user queries related to company performance metrics and converts them into structured JSON format. It uses the Llama-3.1-8b-instant model for natural language understanding and performs extraction of entities, parameters, and dates.

## Setup
1. Clone the repository.
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Set up your API credentials in a `.env` file:
    ```
    LLM_API_URL=<your_llama_api_url>
    LLM_API_KEY=<your_llama_api_key>
    ```
4. Run the application:
    ```python
    python main.py (then it storages in query_result.json)
    ```

## Usage
Simply pass a query string to `process_query()` to get a JSON output with the company's performance metric information.
