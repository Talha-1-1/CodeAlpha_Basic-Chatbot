def get_reply(user_input):
    """
    Returns predefined replies based on user input.
    """
    if user_input.lower() == "hello":
        return "Hi!"
    elif user_input.lower() == "how are you":
        return "I'm fine, thanks!"
    elif user_input.lower() == "bye":
        return "Goodbye!"
    else:
        return "I don't understand. Please try again."


def main():
    """
    Main loop for the chatbot.
    """
    print("Chatbot: Hello! How can I help you today?")

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break
            reply = get_reply(user_input)
            print(f"Chatbot: {reply}")
        except EOFError:
            print("\nChatbot: Goodbye!")
            break


if __name__ == "__main__":
    main()
