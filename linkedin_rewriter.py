import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY", "lm-studio")
base_url = os.getenv("OPENAI_BASE_URL", "http://localhost:1234/v1")
model_name = os.getenv("LLM_MODEL")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

# Dynamically fetch the loaded model from LM Studio if available
try:
    available_models = client.models.list()
    if available_models.data:
        model_name = available_models.data[0].id
except Exception:
    pass

# Ensure the 'text' directory exists and set a single output file
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "text")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "posts.txt")

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
        if content:
            import re
            content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()

        print("\n--- LinkedIn Post Draft ---")
        print(content)
        print("----------------------------\n")

        # Append to a single posts.txt file with a heading
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        heading = f"\n--- Post [{timestamp}] ---\n"
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(heading)
            f.write(content)
            f.write("\n")
        print(f"Saved draft to: text/posts.txt\n")

    except Exception as e:
        print(f"Error: {e}\n")
