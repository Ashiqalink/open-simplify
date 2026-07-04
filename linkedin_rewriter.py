import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY", "lm-studio")
base_url = os.getenv("OPENAI_BASE_URL", "http://localhost:1234/v1")
model_name = os.getenv("LLM_MODEL", "qwen2.5-coder-7b-instruct")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

# Ensure the 'text' directory exists
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "text")
os.makedirs(output_dir, exist_ok=True)

print("Professional LinkedIn Post Rewriter (type 'exit' or 'quit' to stop)\n")
print(f"Using Model: {model_name}")
print(f"Using API Base: {base_url}\n")

while True:
    user_input = input("Enter the text to rewrite: ")
    if user_input.strip().lower() in ['exit', 'quit']:
        break
    if not user_input.strip():
        continue

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": f"Rewrite this as a professional LinkedIn post: {user_input}"
                }
            ]
        )
        content = response.choices[0].message.content

        print("\n--- LinkedIn Post Draft ---")
        print(content)
        print("----------------------------\n")

        # Save to a text file in the 'text' folder
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"post_{timestamp}.txt"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved draft to: text/{filename}\n")

    except Exception as e:
        print(f"Error: {e}\n")
