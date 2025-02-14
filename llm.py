from models import Output
from openai import OpenAI
from PyPDF2 import PdfReader

client = OpenAI()

def call_llm(text):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a legal assistant that extracts specific information from contracts."},
            {"role": "user", "content": f"This is the text: {text}"}, 
        ],
        response_format=Output,
    )
    parsed_output = completion.choices[0].message.parsed
    print(parsed_output)
    return parsed_output
