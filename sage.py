#!/usr/bin/env python

import sys
from openai import OpenAI

client = OpenAI()
content = sys.stdin.read()

response = client.chat.completions.create(
  model="gpt-4-0125-preview", # https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
  messages=[
    {"role": "system", "content": "You are a zsh and bash shell expert on linux, please help me at the terminal complete the following command, you should output the completed command with a few different examples. Be concise. Always use markdown syntax for your response. Please use markdown."},
    {"role": "user", "content": content}
  ]
)

print(response.choices[0].message.content)

