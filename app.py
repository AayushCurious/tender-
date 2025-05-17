import streamlit as st
from streamlit_chat import message
import os
import base64
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="AFAQ Proposal Assistant",
    page_icon="📝",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main container */
    .main {
        max-width: 900px;
        margin: 0 auto;
        padding: 2rem 1rem;
    }
    
    /* Logo */
    .logo {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Chat container */
    .chat-container {
        margin-bottom: 100px;
    }
    
    /* Input area */
    .stTextInput > div > div > input {
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    
    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    
    /* Download buttons */
    .stDownloadButton {
        margin-top: 1rem;
    }
    
    /* Input area */
    .stTextInput > div > div > input {
        border-radius: 20px !important;
        padding: 10px 20px !important;
    }
    
    /* Hide Streamlit's footer */
    .stApp > footer {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    
    # Initialize messages in session state
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": """Welcome to the MTCIT RFP Assistant! I can help you with:
                
- Generating a complete RFP document
- Creating evaluation criteria
- Downloading RFP templates
- Answering RFP-related questions

To get started, you can type:
- 'Generate RFP for [project name]'
- 'I need to create an RFP for MTCIT'
- 'Help me write a tender document'
- Or simply 'Generate RFP' to download the standard templates"""
            }
        ]
    
    # Initialize show_download_buttons in session state
    if 'show_download_buttons' not in st.session_state:
        st.session_state.show_download_buttons = False
    
    # Display the logo
    try:
        st.markdown(
            f"""
            <div class="logo">
                <img src="data:image/png;base64,{base64.b64encode(open('AFAQ_AI.png', 'rb').read()).decode()}" alt="AFAQ Logo" style="max-width: 200px;">
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Error loading logo: {e}")
    
    # Display chat messages
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Display all messages
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            message(msg["content"], is_user=True, key=f"user_{i}")
        else:
            message(msg["content"], is_user=False, key=f"assistant_{i}")
    
    # Display download buttons if flag is set
    if st.session_state.show_download_buttons:
        display_download_buttons()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Chat input
    user_input = st.chat_input("Type your RFP request or 'generate RFP'...")
    
    if user_input:
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Check if user wants to generate RFP or mentions RFP generation
        if "rfp" in user_input.lower() and ("generate" in user_input.lower() or "write" in user_input.lower() or "create" in user_input.lower() or "need" in user_input.lower()):
            # Check if PDF files exist
            if check_pdf_files():
                st.session_state.show_download_buttons = True
                response = "I've prepared the RFP and evaluation criteria documents for MTCIT. You can download them using the buttons below.\n\nThe RFP includes:\n- Project scope and objectives\n- Technical requirements\n- Submission guidelines\n- Evaluation criteria\n- Timeline and deliverables\n\nThe evaluation criteria document outlines the scoring methodology and selection process."
            else:
                st.session_state.show_download_buttons = False
                response = "I'm sorry, but I'm having trouble accessing the required documents. The RFP and evaluation criteria files (A.pdf and B.pdf) could not be found in the output directory.\n\nPlease ensure the files are in the 'output' folder and try again."
        else:
            # Default response for other queries
            response = "I can help you with RFP generation and evaluation criteria. To get started with downloading the MTCIT RFP documents, please type 'generate RFP' or let me know if you need assistance with a specific aspect of the RFP process."
        
        # Add assistant response to chat
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to update the UI
        st.rerun()

def check_pdf_files():
    """Check if the required PDF files exist and return their status"""
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    
    # Check if files exist
    file_a_exists = os.path.exists(os.path.join('output', 'A.pdf'))
    file_b_exists = os.path.exists(os.path.join('output', 'B.pdf'))
    
    return file_a_exists and file_b_exists

def display_download_buttons():
    """Display buttons to download A.pdf and B.pdf if they exist"""
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("📥 Download Files")
    
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    
    # Define file paths
    file_a_path = os.path.abspath(os.path.join('output', 'A.pdf'))
    file_b_path = os.path.abspath(os.path.join('output', 'B.pdf'))
    
    # Check if files exist
    file_a_exists = os.path.exists(file_a_path)
    file_b_exists = os.path.exists(file_b_path)
    
    if not file_a_exists and not file_b_exists:
        st.error("No files found in the output directory. Please make sure A.pdf and B.pdf are in the 'output' folder.")
        st.info("The app is looking for files at: " + os.path.dirname(file_a_path))
        return
    
    # Create columns for the download buttons
    col1, col2 = st.columns(2)
    
    # Display download button for A.pdf if it exists
    with col1:
        if file_a_exists:
            try:
                with open(file_a_path, 'rb') as f:
                    st.download_button(
                        label="📄 Download A.pdf",
                        data=f,
                        file_name="A.pdf",
                        mime="application/pdf",
                        key="a_download"
                    )
            except Exception as e:
                st.error(f"Error reading A.pdf: {str(e)}")
        else:
            st.warning("A.pdf not found in the output directory")
    
    # Display download button for B.pdf if it exists
    with col2:
        if file_b_exists:
            try:
                with open(file_b_path, 'rb') as f:
                    st.download_button(
                        label="📊 Download B.pdf",
                        data=f,
                        file_name="B.pdf",
                        mime="application/pdf",
                        key="b_download"
                    )
            except Exception as e:
                st.error(f"Error reading B.pdf: {str(e)}")
        else:
            st.warning("B.pdf not found in the output directory")


if __name__ == "__main__":
    main()

