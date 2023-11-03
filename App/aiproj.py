import readline
import sys
import subprocess
import modules.codeoutput 
import os
import openai
openai.api_key = "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"
import random
# message = input("enter prompt")

# Roles: User, Assistant, System
def main():
  file = open("codeoutput.py", 'w')
  
  
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are detail-oriented senior software engineer who produces highly readable, standardized code. Produce only code and include no additional explanation."},
      {"role": "user", "content": "Write a python file that sorts array [1, 4, 6, 2, 5, 10, 9]. Include this in a function called sorting"}
    ]
  )
  file.write(completion.choices[0]["message"]["content"])
  file.close()
  print("yay!")
  subprocess.call(["python3", "codeoutput.py"])


if __name__ == "__main__":
    main()

