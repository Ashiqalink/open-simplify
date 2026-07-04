
import litert_lm

# Load the model
engine = litert_lm.Engine("qwen3.5-4b-chatmde-v1.0.litertlm")

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