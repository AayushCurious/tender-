# Tender Management System

A Streamlit-based web application for generating tenders (RFPs) and evaluating proposals.

## Features

- Generate detailed RFPs based on user input
- Upload and manage up to 5 proposals per tender
- Automated proposal evaluation with scoring
- Clear visualization of evaluation results

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   streamlit run app.py
   ```
4. Open your browser and navigate to `http://localhost:8501`

## Usage

1. **Generate RFP**: Fill in the tender details to generate an RFP
2. **Submit Proposals**: Upload proposals from different companies
3. **Evaluate**: Run the evaluation to see results and the winning proposal

## Note

This is a demo application. For production use, you should:
- Add user authentication
- Implement proper data persistence
- Integrate with your LLM API
- Add input validation and error handling
- Set up proper logging and monitoring
