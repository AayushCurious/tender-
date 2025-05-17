from datetime import datetime

def generate_rfp(title, description, deadline):
    """
    Generate RFP document based on input parameters.
    This is a placeholder function that should be replaced with actual LLM integration.
    """
    return f"""
    REQUEST FOR PROPOSAL
    ====================
    
    Title: {title}
    
    Description:
    {description}
    
    Submission Deadline: {deadline}
    
    Requirements:
    1. Detailed company profile
    2. Project approach and methodology
    3. Timeline and milestones
    4. Budget breakdown
    5. Team composition and experience
    6. References from similar projects
    7. Compliance with technical specifications
    
    Evaluation Criteria:
    - Technical approach (40%)
    - Experience and qualifications (30%)
    - Cost proposal (20%)
    - Timeline (10%)
    
    Note: This is a system-generated RFP. Please ensure all information is verified.
    """

def validate_rfp_input(title, description, deadline):
    """Validate RFP input parameters."""
    if not title or not description:
        return False, "Title and description are required"
    if deadline < datetime.now().date():
        return False, "Deadline must be in the future"
    return True, ""
