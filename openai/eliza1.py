# Eliza's 'intelligence'
def elizaResponse(message):
    # default response
    response = "I don't understand"

    # Keywords
    if message.endswith("?"):
        # Questions end with question marks
        if "your" in message:
            # if the user asks about the bot, it should respond differently
            response = "Why are you asking me that?"
        else:
            response = "I don't know"
    elif message.endswith("!"):
        # exclamation marks express emotion
        response = "Calm down, I know what I'm doing"
    elif "hate" in message or "bad" in message:
        # user is angry
        response = "Please don't be so negative"
    else:
        # anything else
        response = "I don't understand"

    return response

# main loop
while True:
    message = input("You: ")
    response = elizaResponse(message)
    print("Eliza: " + response)
