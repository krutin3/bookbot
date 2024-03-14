def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_num_char(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
#    print(char_dict)
    sorted_list = get_sorted_list(char_dict)
    for i in range(len(sorted_list)):
        print(f"The '{sorted_list[i]['char']}' character was found {sorted_list[i]['num']} time(s)")
    print("--- End Report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(text):
    lower_text = text.lower()
    new_dict = {}
    for char in lower_text:
        if char.isalpha():
            if char in new_dict:
                new_dict[char] += 1
            else:
                new_dict[char] = 1
    return new_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def get_sorted_list(unsorted_dict):
    unsorted_list = []
    for item in unsorted_dict:
        unsorted_list.append({"char":item, "num":unsorted_dict[item]})
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list



main()