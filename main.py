import sys
from stats import num_of_words, get_book_text, get_chars_dict, chars_dict_to_sorted_list

def main():
    file_path = "books/frankenstein.txt"
    results = get_book_text(sys.argv)
    #print(results)
    num_words = num_of_words(results)
    #call on char_dict
    chars_dict = get_chars_dict(results)
    #call upon chars_dict_to_sorted_list
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(file_path, num_words, chars_sorted_list)


#display message function
def print_report(file_path, num_words, chars_sorted_list):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print(f"============= END ===============")

main()