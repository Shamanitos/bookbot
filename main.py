def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    characters = character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()


    # Print all alpha charasters and how many times they appear in the doc

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


# Count the words of the document

def get_word_count(text):
  words = text.split()
  return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


# Count the characters fo the document

def character_count(text):
    chars = {}
    text = text.lower()

    for c in text:
      if c in chars:
        chars[c] += 1
      else:
        chars[c] = 1
    return chars


# Open the file in read mode and print its contents

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()