# AFAQ RFP Assistant

A Streamlit-based web application for accessing and downloading RFP (Request for Proposal) documents and evaluation criteria for MTCIT (Ministry of Transport, Communications and Information Technology).

## Features

- Download RFP templates and documents
- Access evaluation criteria for tenders
- User-friendly chat interface
- Secure file handling

## Setup for Local Development

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd afaq
   ```

2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Add your RFP documents:
   - Place `A.pdf` and `B.pdf` in the `output` directory
   - The app will create the directory if it doesn't exist

5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Deployment to Streamlit Cloud

1. Push your code to a GitHub repository
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Click "New app" and connect your GitHub account
4. Select the repository and branch
5. Set the main file path to `app.py`
6. Click "Deploy!"

## File Structure

- `app.py` - Main application code
- `AFAQ_AI.png` - Application logo
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore file

## Requirements

- Python 3.8+
- Streamlit
- Streamlit-chat
- Pillow (for image handling)

## Usage

1. **Access the Application**: Open the app in your web browser
2. **Request Documents**: Type any of the following in the chat:
   - "Generate RFP"
   - "I need an RFP template"
   - "Download evaluation criteria"
3. **Download Files**: Click the download buttons that appear to get your documents

## Note

This application is designed to work with pre-existing RFP documents. For the app to function correctly:
- Place your RFP documents (A.pdf and B.pdf) in the `output` directory
- Ensure all sensitive information is removed from documents before deployment
- The app is designed for internal use and does not include user authentication by default

## Support

For support or questions, please contact the AFAQ IT department.
