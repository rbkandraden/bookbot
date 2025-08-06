import sys
from stats import count_words, count_characters, sort_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_text(filepath): 
    with open(filepath) as f: 
        file_contents = f.read() 
    return file_contents

def main():
    filepath = sys.argv[1]
    text = get_text(filepath) 
    
    num_words = count_words(text) 

    character_counts = count_characters(text)

    sorted_characters = sort_characters(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['character']}: {item['num']}")
    print("============= END ===============")

main()