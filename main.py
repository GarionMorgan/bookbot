from stats import num_of_words, get_book_text, get_chars_dict

def main():
    results = get_book_text("books/frankenstein.txt")
    #print(results)
    num_words = num_of_words(results)
    #call on char_dict
    chars_dict = get_chars_dict(results)
    print(f"{num_words} words found in the document")
    print(chars_dict)

main()