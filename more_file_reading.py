count = 0

phrase_to_find = input("enter letter or phrase to count: ")

file_name = f"{phrase_to_find}_matches.txt"

with open("DATA/words.txt") as words_in:
    with open(file_name, "w") as words_out:
        for raw_word in words_in: # get word with \n
            word = raw_word.rstrip()
            if word.endswith(phrase_to_find):
                words_out.write(raw_word)
                count += 1
    # words_in.close()

print(f"{phrase_to_find} occurs at the end of {count} words")