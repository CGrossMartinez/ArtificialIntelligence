import openai

openai.api_key = "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"

def generate_response(prompt):

    model_engine = "text-davinci-003"

    prompt = (f"{prompt}")

    completetions = openai.Completion.create(
        
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5       
        
        )

    message = completetions.choices[0].text

    return message.strip()


print(generate_response("create a continuing story about florida and boca raton involving two characters Sam and Bob"))


