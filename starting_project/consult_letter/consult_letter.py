"""
Your task is to implement `create_consult_letter` function to generate a consult letter based on the SOAP note.

The input parameters are:
- user_info: a dictionary contains the bio of the doctor, such as
    {
        "name": "Dr. John Doe", # the name of the doctor
        "email": "drjohndoe@clinic.com", # the email of the doctor
    }
- specialty: a string represents the specialty of the doctor, such as "Otolaryngology"
- note_content: a dictionary contains the content of the SOAP note, where the key is the section name and the value is the content of the section, such as
    {
        "Patient Name": "Betty",
        "Chief Complaint": "Ear pain",
        "History of Present Illness": "\n• Left-sided ear pain\n• No drainage noted\n• Intermittent hearing loss reported\n• Pain worsens with chewing\n• Inconsistent use of mouthpiece for teeth clenching\n• Pain relief when lying on contralateral side",
        "Social History": "\n• Occasional Reactive use for allergies\n• Allergy to salt",
        "The Review of Systems": "\n• Intermittent hearing loss\n• No swallowing issues\n• No nasal congestion\n• Allergies present, takes Reactive occasionally",
        "Current Medications": "\n• Reactive for allergies",
        "Allergies": "\n• Allergic to salt",
        "Physical Examination": "\n• Right ear canal clear\n• Right tympanic membrane intact\n• Right ear space aerated\n• Left ear canal normal\n• Left eardrum normal, no fluid or infection\n• Nose patent\n• Paranasal sinuses normal\n• Oral cavity clear\n• Tonsils absent\n• Good dentition\n• Pain along pterygoid muscles\n• Heart and lungs clear\n• No neck tenderness or lymphadenopathy",
        "Assessment and Plan": "Problem 1:\nEar pain\nDDx:\n• Temporomandibular joint disorder: Likely given the jaw pain, history of teeth clenching, and normal ear examination.\nPlan:\n- Ordered audiogram to check hearing\n- Advised to see dentist for temporomandibular joint evaluation\n- Recommended ibuprofen for pain\n- Suggested soft foods diet\n- Avoid chewing gum, hard candies, hard fruits, ice, and nuts\n- Follow-up if symptoms persist"
    }
- note_date: a string represents the date of the SOAP note, such as "2022-01-01"
"""

import json
from typing import Optional

from pyexpat.errors import messages

from openai_chat import chat_content


def create_consult_letter(
    user_info: dict,
    specialty: str,
    note_content: dict[str, Optional[str]],
    note_date: str,
) -> str:
    """
    Generate a consult letter based on the provided SOAP note content, specialty, and doctor info.
    """
    # Extract doctor info
    full_name = user_info.get("name", "").strip()
    doctor_email = user_info.get("email", "").strip()

    soap_lines = []
    for section, content in note_content.items():
        if content:
            soap_lines.append(f"{section}: {content.strip()}")
    soap_text = "\n".join(soap_lines)

    # Build prompt for AI
    system_msg = (
        f"You are a medical specialist in {specialty}. "
        "Draft a concise, professional consult‐letter email to the referring family doctor. "
        "Do not begin with any greeting such as “Dear Dr. X.” "
        "Begin by thanking them for the referral and stating the patient’s name, consultation type, and exam date in one sentence. "
        "Weave all SOAP‐note details into a smooth narrative (chief complaint, history of present illness, review of systems, social/developmental/pregnancy/nutritional history, current medications, allergies, pertinent negatives, physical exam, assessment, plan). "
        "Use full sentences and paragraphs—no headings, labels, lists, or bullet points. "
        "If any usual section (e.g. past surgical history or test results) is missing, briefly note its absence. "
        "Close with an invitation for questions, then write “Sincerely,” on its own line. "
        "On the following three lines, _exactly_ include your full name, your specialty and your email address as provided in the referring‐physician details. "
        "Do not use any placeholders or extraneous text."
    )

    user_msg = ()

    response = chat_content(
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
        temperature=0.7,
    )

    return response
