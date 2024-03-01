#!/usr/bin/env python

import os
import sys
from openai import OpenAI

client = OpenAI()
prompt = sys.stdin.read()

script_dir = os.path.dirname(os.path.abspath(__file__))
instructions_path = os.path.join(script_dir, 'sage.instructions')
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

