def read_file_contents(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

def get_word_count(str):
  return len(str.split())

def get_letter_count(str):
  letter_dict = {}
  lowercase_text = str.lower()
  for letter in lowercase_text:
    if letter in letter_dict:
      letter_dict[letter] += 1
    else:
      letter_dict[letter] = 1
  return letter_dict

def get_letter_count_report(letter_dict):
  character_list = list(letter_dict)
  character_list.sort()
  for char in character_list:
    if char.isalpha():
      print(f"The {char} character was found {letter_dict[char]} times")

book_file = 'books/frankenstein.txt'
print(f"--- Begin report of {book_file} ---")
file_contents = read_file_contents(book_file)
print(f"{get_word_count(file_contents)} words found in the document")
letter_counts = get_letter_count(file_contents)
get_letter_count_report(letter_counts)
print("--- End report ---")