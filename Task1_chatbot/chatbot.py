# CodSoft Task 1
# Rule-Based Chatbot

print("===================================")
print("🤖 Welcome to CodSoft Chatbot")
print("Type 'bye' to exit.")
print("===================================")

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot: My name is CodSoft Rule-Based Chatbot.")

    elif "who made you" in user or "developer" in user:
        print("Bot: I was created by an AI Intern using Python.")

    elif "python" in user:
        print("Bot: Python is a popular programming language used for AI, Machine Learning, Web Development, and more.")

    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: Artificial Intelligence enables machines to learn and make decisions like humans.")

    elif "thank" in user:
        print("Bot: You're welcome! 😊")

    elif "bye" in user:
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please ask something else.")
