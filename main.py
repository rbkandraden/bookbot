from stats import count_words

def get_text(filepath): 
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_text('books/frankenstein.txt')
    num_words = count_words(text)
    print(f"{75767} words found in the document")

main()