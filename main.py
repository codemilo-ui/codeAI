import json
import random
import string

# Load the responses from the JSON file
with open('messages.json', 'r') as file:
    messages = json.load(file)

# Define a function to save the responses to the JSON file
def save_messages(messages):
    with open('messages.json', 'w') as file:
        json.dump(messages, file, indent=4)

# Define a function to generate a response
def generate_response(message):
    global messages
    message = message.lower()  # Convert the message to lowercase
    message = message.translate(str.maketrans('', '', string.punctuation))  # Remove all punctuation characters from the message
    message = ''.join(message.split())  # Remove all whitespace characters from the message
    for msg in messages:
        msg_without_punc = msg['message'].translate(str.maketrans('', '', string.punctuation))  # Remove all punctuation characters from the message in the data
        msg_without_punc = ''.join(msg_without_punc.split())  # Remove all whitespace characters from the message in the data
        if msg_without_punc.lower() == message:  # Convert the message in the data to lowercase for comparison
            return random.choice(msg['response'])
    else:
        # Ask the user for a response and add it to the JSON data
        response = input("I'm sorry, I don't understand. Please provide me with a response: ")
        messages.append({"message": message, "response": [response]})
        save_messages(messages)
        return "Thank you for letting me know. I will remember that for next time."

# Main loop to handle user input and generate responses
while True:
    # Get user input
    message = input("You: ")
    
    # Generate a response
    response = generate_response(message)
    
    # Print the response
    print("Chatbot:", response)
