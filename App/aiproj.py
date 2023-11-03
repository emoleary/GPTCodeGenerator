import readline
import sys

import os
import openai
openai.api_key = "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"

# message = input("enter prompt")

# Roles: User, Assistant, System

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are detail-oriented senior software engineer who produces highly readable, standardized code. Produce only code and include no additional explanation."},
    {"role": "user", "content": "Write a python test file that checks for a sorted array [1, 4, 6, 2, 5, 10, 9]"}
  ]
)

print(completion.choices[0]["message"]["content"])

def test_sorted_array(self):
      array = [1, 4, 6, 2, 5, 10, 9]
      sorted_array = sorted(array)
      self.assertEqual(array, sorted_array)

if __name__ == '__main__':
    test_sorted_array.main()
