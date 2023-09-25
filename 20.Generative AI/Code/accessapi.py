secret_key = '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'
prompt = 'tell me a slogan for a home security company'
prompt = 'Give me an outline for a course on how to make web applications using Bubble'

import openai 
openai.api_key = secret_key

output = openai.Completion.create(
    model = 'text-davinci-003',
    prompt = prompt,
    max_tokens=300,
    temperature=0
)

#print(output)
output_text = output['choices'][0]['text']

print(output_text)