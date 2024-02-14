def main():
  book_path = "/Users/joshuanewe/workspace/github.com/joshuanewe/bookbot/books/frankenstein.txt"
  text = get_book_text(book_path)
  num_of_words = get_num_words(text)
  letters = count_letters(text)

  print(f"--- Begin report of {book_path} ---")
  print(f"{num_of_words} words found in document.")
  sorted = sort_on(letters)
  for letter in sorted:
    print(f"The '{letter[0]}' character was found {letter[1]} times")

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def get_num_words(text):
  words = text.split()
  return len(words)

def count_letters(text):
  letters = {}
  for letter in text:
    lowered = letter.lower()
    if lowered in letters:
      letters[lowered] += 1
    else:
      if lowered.isalpha():
        letters[lowered] = 1
  return(letters)

def sort_on(dict):
  return sorted(dict.items(), key=lambda x: x[1], reverse=True)
main()