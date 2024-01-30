import random

def simple_chatbot():
    print("Simple Rule-Based Chatbot: Type 'exit' to end the conversation.")

    
    while True:
        
        user_input = input("You: ").lower()

        
        if user_input == 'exit':
            print("Bot: Goodbye!")
            break

        
        if 'hi' in user_input:
            response = random.choice(['Hi there!', 'Hello!', 'Hey!'])
        elif 'how are you' in user_input:
            response = random.choice(['I am good, thank you!', 'Not too bad.'])
        elif 'bye' in user_input:
            response = random.choice(['Goodbye!', 'See you later!', 'Take care!'])
        else:
            response = random.choice(["I'm not sure I understand.", "Can you please clarify?", "I'm a simple bot and can respond to basic queries."])

        
        print("Bot:", response)

if __name__ == "__main__":
    simple_chatbot()
