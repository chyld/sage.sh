#!/usr/bin/env python

import sys
from openai import OpenAI

client = OpenAI()
content = sys.stdin.read()

response = client.chat.completions.create(
  model="gpt-4-0125-preview", # https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
  messages=[
    {"role": "system", "content": "As a developer navigating the terminal, I seek guidance primarily in zsh and bash shell usage on Linux, alongside Python and JavaScript expertise. I prefer concise responses in markdown format, featuring various code or command examples relevant to my queries. Here are the guidelines. 1. Respond with succinct explanations and demonstrations using markdown syntax. 2. Utilize fenced code blocks with syntax highlighting for code and terminal commands. 3. Provide diverse examples to enrich understanding."},
    {"role": "user", "content": content}
  ]
)

print(f"INPUT\n{content}\n\nOUTPUT")
print(response.choices[0].message.content)
print("# end of response")

