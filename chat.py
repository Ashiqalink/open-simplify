
import litert_lm

# Load the model
engine = litert_lm.Engine("gemma-4-E2B-it.litertlm")

# Create a conversation session
with engine.create_conversation() as conversation:
    print("Chat session started! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # Send message and print response
        response = conversation.send_message(user_input)
        print(f"AI: {response['content'][0]['text']}")