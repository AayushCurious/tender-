import streamlit as st
import os
from tender_generator import generate_rfp
from proposal_evaluator import evaluate_proposals

# Page configuration
st.set_page_config(page_title="Tender Management System", layout="wide")

def main():
    st.title("Tender Management System")
    
    # Tender Generation Section
    st.header("1. Generate Tender (RFP)")
    with st.form("tender_form"):
        tender_title = st.text_input("Tender Title")
        tender_description = st.text_area("Tender Description")
        submission_deadline = st.date_input("Submission Deadline")
        submit_tender = st.form_submit_button("Generate RFP")
    
    if submit_tender and tender_title and tender_description:
        with st.spinner('Generating RFP...'):
            rfp_content = generate_rfp(tender_title, tender_description, submission_deadline)
            st.subheader("Generated RFP")
            st.text_area("RFP Content", rfp_content, height=300)
            
            # Save RFP for evaluation
            st.session_state.current_rfp = rfp_content
            st.session_state.proposals = []
    
    # Proposal Submission Section
    if 'current_rfp' in st.session_state:
        st.header("2. Submit Proposals")
        with st.form("proposal_form"):
            company_name = st.text_input("Company Name")
            proposal_file = st.file_uploader("Upload Proposal (TXT or PDF)", 
                                          type=['txt', 'pdf'],
                                          accept_multiple_files=False)
            submit_proposal = st.form_submit_button("Submit Proposal")
            
            if submit_proposal and company_name and proposal_file:
                if len(st.session_state.get('proposals', [])) >= 5:
                    st.error("Maximum of 5 proposals reached")
                else:
                    # Save proposal
                    proposal_text = proposal_file.read().decode()
                    if 'proposals' not in st.session_state:
                        st.session_state.proposals = []
                    st.session_state.proposals.append({
                        'company': company_name,
                        'content': proposal_text
                    })
                    st.success(f"Proposal from {company_name} submitted successfully!")
        
        # Display submitted proposals
        if st.session_state.get('proposals'):
            st.subheader("Submitted Proposals")
            for i, proposal in enumerate(st.session_state.proposals, 1):
                st.write(f"{i}. {proposal['company']}")
    
    # Evaluation Section
    if st.session_state.get('proposals'):
        st.header("3. Evaluate Proposals")
        if st.button("Run Evaluation"):
            with st.spinner('Evaluating proposals...'):
                evaluation_results = evaluate_proposals(
                    st.session_state.current_rfp,
                    st.session_state.proposals
                )
                
                st.subheader("Evaluation Results")
                st.write(f"Awarded to: **{evaluation_results['awarded_company']}**")
                st.subheader("Justification")
                st.write(evaluation_results['justification'])
                
                # Display scores
                st.subheader("Scores")
                for score in evaluation_results['scores']:
                    st.write(f"{score['company']}: {score['score']}/100")

if __name__ == "__main__":
    main()
