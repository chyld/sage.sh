#!/usr/bin/env python

from os.path import dirname, abspath, join
import sys
from openai import OpenAI

client = OpenAI()
prompt = sys.stdin.read()
context = sys.argv[1]

script_dir = dirname(abspath(__file__))
instructions_path = join(script_dir, f"sage.{context}-instructions")
with open(instructions_path, 'r') as f:
    instructions = f.read()

response = client.chat.completions.create(
  model="gpt-4-0125-preview", # https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
  messages=[
    {"role": "system", "content": instructions},
    {"role": "user", "content": prompt}
  ]
)

print(f"INPUT\n> instructions\n\n{instructions}\n> prompt\n\n{prompt}\n\nOUTPUT")
print(response.choices[0].message.content)
print("\n\n# end of response")

