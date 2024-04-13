from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("newjeans.jsonl", "rb"),
  purpose="fine-tune"
)