def animal_chatbot(user_input):
    
    rules = {
        "Hello | Hi | Hi there": "Hello this is a chatBOT.",
        "What is your name?": "My name is ELISA.",
        "What can you do for me?": "I can answer about all your queries.",
        "OK": "Any more queries?",
        "NO!": "THANK YOU :)",
        "Default": "I'm sorry, I don't have information about that."
    }

    
    for question, response in rules.items():
        if user_input.lower() in question.lower():
            return response

    
    return rules["Default"]


if __name__ == "__main__":
    print("Hello! I am ELISA, your personal chatBOT. Ask me anything or type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit" or user_input.lower() == "bye":
            print("ChatBOT: Goodbye!")
            break
        response = animal_chatbot(user_input)
        print("ChatBOT:", response)

