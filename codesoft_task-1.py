def animal_chatbot(user_input):
    # Predefined rules and responses for the chatbot
    rules = {
        "What does a dog eat?": "Dogs typically eat dog food, but they can also have meats, vegetables, and grains.",
        "What are the colors of a peacock?": "A peacock has beautiful and vibrant colors like blue, green, and gold.",
        "How fast can a cheetah run?": "Cheetahs are the fastest land animals and can run at speeds up to 60-70 mph.",
        "What is the lifespan of an elephant?": "Elephants can live up to 60-70 years in the wild.",
        "What do pandas like to eat?": "Pandas mainly eat bamboo, but they are also known to consume small mammals and fruits occasionally.",
        "Default": "I'm sorry, I don't have information about that animal at the moment. Please ask about dogs, peacocks, cheetahs, elephants, or pandas."
    }

    # Check if the user input matches any predefined rules
    for question, response in rules.items():
        if user_input.lower() in question.lower():
            return response

    # If no match found, return the default response
    return rules["Default"]

# Main loop to run the chatbot
if __name__ == "__main__":
    print("Hello! I am the Animal Chatbot. Ask me about different animals or type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Animal Chatbot: Goodbye!")
            break
        response = animal_chatbot(user_input)
        print("Animal Chatbot:", response)












