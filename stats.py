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