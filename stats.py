def get_book_text(file):
    with open(file) as f:
        #read object
        file_contents = f.read()

    return file_contents

def num_of_words(text):
    split_text = text.split()
    #return split_text
    count = 0
    for i in split_text:
        count += 1
    return count

#takes text from a book as a string and returns the number of times for each character
def get_chars_dict(text):
    #put into a tuple for no duplicates
    chars = {}
    #looping through the text
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#takes the dict of chars and counts, then returns sort list
def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for i in num_chars_dict:
        sorted_list.append({"char": i, "num": num_chars_dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

