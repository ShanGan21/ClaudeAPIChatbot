# Load env var
from dotenv import load_dotenv
load_dotenv()


# create api client
from anthropic import Anthropic

client = Anthropic()


conversation = []

while True:
    user_message = input("You: ")

    if user_message.lower() == 'exit':
        print("Chat ended. Goodbye!")
        break

    # Add user message to the conversation
    conversation.append({'role': 'user', 'content': user_message})

    response = client.messages.create(
        model='claude-sonnet-5-5',
        max_tokens=1000,
        messages=conversation
    )

    # The response may start with a thinking block, so keep only the text blocks
    bot_message = "".join(
        block.text for block in response.content if block.type == 'text'
    )
    print(f"Claude: {bot_message}")

    # Add chatbot response to the conversation
    conversation.append({'role': 'assistant', 'content': bot_message})