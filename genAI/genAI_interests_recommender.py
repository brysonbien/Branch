from huggingface_hub import InferenceClient

# Ensure you have the necessary packages installed
# pip install huggingface-hub transformers

def get_interests_recommender(interests):
    interests = [interest.lower().strip().replace(" ", "_") for interest in interests]
    # Create the client with the correct model
    client = InferenceClient(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        token="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",
    )

    # Prepare the prompt for the model
    prompt = (
        "Given the following interests: %s, suggest 5 similar interests using 1 word each."
        % ', '.join(interests)
    )

    # Generate text using the InferenceClient
    response = client.text_generation(
        prompt,
        max_new_tokens=100,  # Adjust the number of tokens as needed
        temperature=0.1,    # Adjust the randomness of the output
    )

    # Print the response generated by the model
    print(response)

if __name__ == "__main__":
    result = get_interests_recommender(["coding", "hiking", "tennis", "basketball", "concerts"])
    