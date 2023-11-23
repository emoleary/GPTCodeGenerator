import readline
import sys
import subprocess
import modules.codeoutput 
import os
import openai
import pytest

openai.api_key = "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"
import random

import os

# message = input("enter prompt")

G_ARRAY = []
# Roles: User, Assistant, System
def main():
  
  file = "modules/codeoutput.py"
  os.remove(file)

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are detail-oriented senior software engineer who produces highly readable, standardized code. Produce only code and include no additional explanation."},
      {"role": "user", "content": "Write a python file that sorts array [1, 4, 6, 2, 5, 10, 9]. Include this in a function called sorting and return the sorted array and call it arr. Contain all code in this function"}
    ]
  )

  with open(file, 'w') as filetowrite:
    filetowrite.write(completion.choices[0]["message"]["content"])
  #file.write(completion.choices[0]["message"]["content"])
  
  G_ARRAY.append(completion.choices[0]["message"]["content"])

  filetowrite.close()
 
  print(completion.choices[0]["message"]["content"])
  subprocess.call(["python3", "codeoutput.py"])
  retcode = pytest.main()
  return retcode==pytest.ExitCode.OK


if __name__ == "__main__":
    for i in range(10):
      ret = main()
      if ret==True:
        i += 1
    print()

with open('newfile.txt', 'w') as filetowrite:
    filetowrite.write(G_ARRAY[0])
  
for i in range(1, len(G_ARRAY)):
  with open('newfile.txt', 'a') as filetowrite:
    filetowrite.write(G_ARRAY[i])
  #file.write(completion.choices[0]["message"]["content"])
  
    

