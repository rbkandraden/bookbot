def count_words(text): # Conta o número de palavras no texto
    words = text.split() # Divide o texto em palavras
    num_words = len(words) # Conta quantas palavras tem
    return num_words

def count_characters(text): # Conta a frequencia de cada caractere no texto
    characters = {} # Dicionário
    text = text.lower() # Converte para minúsculas
    for character in text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

# A function that takes a dictionary and returns the value of the "num" key
def sort_characters(count_characters): # Ordena caracteres por frequência
    sorted_list = []
    for character, count in count_characters.items():
        if character.isalpha():
            sorted_list.append({"character": character, "num":count})
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list


