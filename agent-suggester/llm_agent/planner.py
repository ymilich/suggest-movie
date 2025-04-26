import openai
import anthropic
import os
from anthropic import Client

def handle_request(input_text):
    return anthropic_request(input_text)
    
def anthropic_test():
    return anthropic_request("Are we humans?")

def anthropic_request(input_text):
    client = Client(api_key=os.getenv("ANTHROPIC_API_KEY"))
    if not client.api_key:
        return "Anthropic API key is not set. Please set the ANTHROPIC_API_KEY environment variable."

    try:
        response = client.completion(
            prompt=f"{anthropic.HUMAN_PROMPT} {input_text}{anthropic.AI_PROMPT}",
            model="claude-instant-1",  # Use the best free model
            max_tokens_to_sample=100
        )
        return response["completion"].strip()
    except Exception as e:
        return f"An error occurred: {e}"
    
def openai_request(input_text):
    # Replace 'your-api-key' with your actual OpenAI API key
    openai.api_key = 'your-api-key'
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the model you want to use
            prompt=input_text,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"
    
