from stats import count_words, count_characters

def get_text(filepath): 
    with open(filepath) as f: 
        file_contents = f.read() 
    return file_contents

def main():
    text = get_text('books/frankenstein.txt') 
    num_words = count_words(text) 
    print(f"{num_words} words found in the document")
    character_counts = count_characters(text)
    print(character_counts)

main()