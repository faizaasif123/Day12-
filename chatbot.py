import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not configured.")

client = genai.Client(api_key=API_KEY)


def load_user_data():

    with open(
        "data/users_financial_data.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def find_user(user_id):

    data = load_user_data()

    # Your JSON has a "users" key
    users = data["users"]

    for user in users:

        if user["user_id"] == user_id:
            return user

    raise ValueError("User ID not found.")


def ask_ai(user_id, question):

    user = find_user(user_id)

    prompt = f"""
You are the HisabDo AI Financial Assistant.

Answer the user's question using ONLY the financial
information provided below.

Do not invent financial numbers.

If the requested information is not available,
clearly say that the information is not available.

USER FINANCIAL DATA:
{json.dumps(user, indent=2)}

USER QUESTION:
{question}

Give a short, clear and helpful answer.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    if not response or not response.text:
        raise ValueError("AI returned an empty response.")

    return response.text.strip()