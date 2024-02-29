#!/usr/bin/env python

import sys
from openai import OpenAI

client = OpenAI()
content = sys.stdin.read()

response = client.chat.completions.create(
  model="gpt-4-0125-preview", # https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
  messages=[
    {"role": "system", "content": "You are a zsh and bash shell expert on linux. You are also a python and javascript expert. Please help me as a developer when I am using the terminal. Try to give me a few different code or command examples to my question. Be concise. Always use markdown syntax for your response. Please use markdown and have samples of code or terminal commands with fenced code blocks and syntax highlighting."},
    {"role": "user", "content": content}
  ]
)

print(f"INPUT\n{content}\n\nOUTPUT")
print(response.choices[0].message.content)
print("# end of response")

