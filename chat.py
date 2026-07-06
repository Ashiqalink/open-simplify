
import glob
import os
import litert_lm

# Auto-detect any available .litertlm model in the workspace
litert_files = glob.glob("*.litertlm") + glob.glob("**/*.litertlm", recursive=True)
if litert_files:
    model_path = litert_files[0]
    print(f"Auto-detected model: {model_path}")
else:
    model_path = "qwen2.5-coder-7b-instruct.litertlm"
    print(f"No .litertlm files found. Falling back to: {model_path}")

# Load the model
engine = litert_lm.Engine(model_path)

# Create a conversation session
with engine.create_conversation() as conversation:
    print("Chat session started! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # Send message and print response
        response = conversation.send_message(user_input)
        text = response['content'][0]['text']
        if text:
            import re
            text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
        print(f"AI: {text}")