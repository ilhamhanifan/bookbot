with open("books/frankenstein.txt") as f:
    contents = f.read()
    # print(contents)

    word_count = len(contents.split(" "))
    # print(f"word count = {len(word_count)}")

    letters_dict = {}
    letters = contents
    for letter in letters:
        letter = letter.lower()
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1



    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for letter in letters_dict:
        # print(f"{letter} = {letters_dict[letter]}")
        print(f"The '{letter}' character was found {letters_dict[letter]} times")


