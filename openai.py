import openai

# Set the API key for the openai library
openai.api_key = "API_KEY"

# Define a function called generate_text that takes two parameters: prompt and max_tokens
def generate_text(prompt, max_tokens):
    # Use the openai.Completion.create method to generate text based on the prompt and max_tokens parameters
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens
        )
    # Return the generated text
    return response["choices"][0]["text"]

# Start a while loop that continues indefinitely
while True:
    # Prompt the user to enter a question
    Q = input("Question : ")
    # If the user enters "exit", break out of the loop
    if Q == "exit":
        break
    # Otherwise, call the generate_text function with the user's question and a maximum of 200 tokens
    generated_text = generate_text(Q, 200)
    # Print the generated text
    print(generated_text)
