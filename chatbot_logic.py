# chatbot_logic.py

from datetime import datetime

# Hospital data (keep your original dictionary)
hospital_data = {
    "departments": "Our hospital has several departments including Cardiology, Oncology, Pediatrics, and Emergency. Which one are you interested in?",
    "doctors": "We have a team of highly qualified doctors across various specialties. Please specify a department or specialty to find the right doctor.",
    "hours": "Our hospital operates 24/7 for emergencies. For specific department hours or appointments, please refer to our website or call us directly.",
    "contact": "You can contact us at our main reception at (123) 456-7890, or visit our website for more contact options and a detailed directory.",
    "appointment": "To book an appointment, please visit our website at www.hospital.com/appointments or call our scheduling desk at (123) 456-7891. Please have your patient ID ready.",
    "location": "Our main hospital campus is located at 123 Healthway, Medical City, ST 98765. We also have several satellite clinics; please visit our website for more details.",
    "department_details": {
        "cardiology": {
            "description": "Our Cardiology department specializes in heart health, offering diagnostics, treatment, and preventive care for cardiovascular diseases.",
            "doctors": ["Dr. Sarah Chen (Cardiologist)", "Dr. David Lee (Electrophysiologist)"]
        },
        "oncology": {
            "description": "The Oncology department provides comprehensive cancer care, including chemotherapy, radiation therapy, and surgical oncology, with a focus on personalized treatment plans.",
            "doctors": ["Dr. Emily White (Oncologist)", "Dr. Robert Green (Radiation Oncologist)"]
        },
        "pediatrics": {
            "description": "Our Pediatrics department offers specialized medical care for infants, children, and adolescents, covering general health, vaccinations, and childhood illnesses.",
            "doctors": ["Dr. Lisa Brown (Pediatrician)", "Dr. Michael Adams (Pediatric Surgeon)"]
        },
        "emergency": {
            "description": "The Emergency department operates 24/7, providing immediate medical attention for acute illnesses and injuries, staffed by experienced emergency physicians and nurses.",
            "doctors": ["Dr. Jessica Kim (Emergency Physician)", "Dr. Tom Hall (Emergency Physician)"]
        }
    },
    "services": {
        "radiology": "Our Radiology department offers X-rays, MRI, CT scans, and ultrasound for diagnostic imaging.",
        "physical therapy": "Our Physical Therapy department helps patients recover from injuries and improve mobility through personalized exercise programs.",
        "pharmacy": "Our Pharmacy provides prescription fulfillment, medication counseling, and over-the-counter medications."
    },
    "faqs": {
        "visiting hours": "Our general visiting hours are from 9 AM to 8 PM daily. Please check with specific department for exceptions.",
        "wifi access": "Yes, free Wi-Fi is available throughout the hospital. Connect to 'HospitalGuest' network.",
        "parking": "Paid parking is available in the multi-story car park adjacent to the main entrance.",
        "billing": "For billing inquiries, please contact our patient accounts department at (123) 456-7892 during business hours."
    },
    "feedback": "We value your feedback! Please visit our feedback form at www.hospital.com/feedback or email us at feedback@hospital.com for any suggestions or support requests."
}

def generate_greeting(username: str) -> str:
    """Return greeting based on time of day."""
    if not username:
        return ""
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon"
    elif 17 <= current_hour < 22:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"
    return f"{greeting}, {username}!"

def get_chatbot_response(query: str, username: str = "") -> str:
    """Main chatbot logic simplified for Streamlit."""
    query = query.lower()
    response = ""

    # Check departments
    for dept_key, dept_info in hospital_data["department_details"].items():
        if dept_key in query:
            response = f"{dept_key.capitalize()} Department: {dept_info['description']} Doctors: {', '.join(dept_info['doctors'])}."
            return response

    # Check services
    for service_key, service_desc in hospital_data["services"].items():
        if service_key in query:
            response = f"{service_key.capitalize()}: {service_desc}"
            return response

    # Check FAQs
    for faq_q, faq_a in hospital_data["faqs"].items():
        if faq_q in query:
            response = f"{faq_q.capitalize()}: {faq_a}"
            return response

    # Check general queries
    if "departments" in query:
        response = "Our departments include: " + ", ".join([d.capitalize() for d in hospital_data["department_details"].keys()]) + "."
    elif "services" in query:
        response = "We offer services: " + ", ".join([s.capitalize() for s in hospital_data["services"].keys()]) + "."
    elif "faq" in query:
        response = "I can answer questions about: " + ", ".join([q.capitalize() for q in hospital_data["faqs"].keys()]) + "."
    elif "feedback" in query:
        response = hospital_data["feedback"]
    elif "hours" in query:
        response = hospital_data["hours"]
    elif "contact" in query:
        response = hospital_data["contact"]
    elif "appointment" in query:
        response = hospital_data["appointment"]
    elif "location" in query:
        response = hospital_data["location"]
    elif "doctors" in query:
        all_doctors = []
        for dept_info in hospital_data["department_details"].values():
            all_doctors.extend(dept_info['doctors'])
        response = "Our doctors include: " + ", ".join(all_doctors)
    else:
        response = "Sorry, I don't understand your question. Try asking about departments, doctors, services, FAQs, hours, contact, appointment, location, or feedback."

    if username:
        response = f"{username} asked: {query}\nChatbot: {response}"

    return response