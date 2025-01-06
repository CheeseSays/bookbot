def sort_on(dict):
    return dict[list(dict.keys())[0]]

def chars():
    letters = "abcdefghijklmnopqrstuvwxyz"
    dic_chars = {letter: 0 for letter in letters}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    for char in file_contents.lower():
        if char in letters:
            dic_chars[char] += 1
    list_dic_chars = [{key: value}for key, value in dic_chars.items()]
    list_dic_chars.sort(reverse=True, key=sort_on)
    for dic in list_dic_chars:
        for key, value in dic.items():
            print(f"The {key} character was found {value} times")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    count = 0
    for n in words:
        count += 1
    print(f"{count} words found in the document")



def runtime():
    print(f"--- Begin report of books/frankenstein.txt ---")
    main()
    print("")
    chars()
    print(f"--- End report ---")

runtime()
