def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_dict = count_unique_characters(text)
    sorted_dict = sort_characters(character_dict)
    print(f"Report on {book_path}")
    print(f"Word count: {num_words}")
    print("Unique character count:")
    for character in sorted_dict:
        print(f"There are {character["instances"]} instances of the character {character["character"]}")
    print("End report")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    text_as_list = text.split()
    return len(text_as_list)

def count_unique_characters(text):
    character_count = {}
    for character in text:
        if character.isalpha():
            lower_case = character.lower()
            if lower_case in character_count:
                character_count[lower_case] += 1
            else:
                character_count[lower_case] = 1
    return character_count

def sort_on(d):
    return d["instances"]

def sort_characters(dict):
    as_list = []
    for entry in dict:
        as_list.append({"character": entry, "instances": dict[entry]})
    as_list.sort(reverse=True, key=sort_on)
    return as_list

main()