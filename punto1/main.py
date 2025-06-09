import re
import tabulate;

def read_file():
    global content
    with open("reglament.txt", mode="r", encoding="utf-8") as file:
        content = file.read()

def find_words1():
    """words that starting with "ac" and finish with "a" or "s" """
    pattern = r'\bac[a-z]*[as]\b'
    # Find all matches in the content
    matches = re.findall(pattern, content)
    # Store all matches in words list
    words.extend(matches)
    table = [[i] for i in words]
    print(tabulate.tabulate(table, headers=["starting with ac and finish with a or s"]))
    print("total words: " + str(len(words)))
    print ("\n")
    words.clear()

def find_words2():
    """words that finish with "n" or "s" or "d" """
    pattern = r'\b\w*[nsdNSD]\b'
    matches = re.findall(pattern, content)
    words.extend(matches)

    #use of set to eleminate the duplicated words :D
    result = set(words)
    table = [[i+1, j] for i, j in enumerate(result)]
    print(tabulate.tabulate(table, headers=["#", "words that finish with n or s or d"]))
    print("total words: " + str(len(result)))
    print("\n")
    words.clear()

def find_words3():
    """start with capital letters and have one or more vocals"""
    pattern = r'\b[A-Z]+[a-zA-Z]*[aeiouAEIOU]+[a-zA-Z]*\b'
    matches = re.findall(pattern, content)
    words.extend(matches)

    result = set(words)
    table = [[i+1, j] for i, j in enumerate(result)]
    print(tabulate.tabulate(table, headers=["#", "Start with capital letters and have one or more vocals"]))
    print("total words: " + str(len(result)))
    print("\n")
    words.clear()

def find_words4():
    """words that have all the vocals with aphostrofies"""
    pattern = r'\b(?=\w*[aá])(?=\w*[eé])(?=\w*[ií])(?=\w*[oó])(?=\w*[uú])[\wáéíóúÁÉÍÓÚ]+\b'
    matches = re.findall(pattern, content)
    words.extend(matches)

    result = set(words)
    table = [[i+1, j] for i, j in enumerate(result)]
    print(tabulate.tabulate(table, headers=["#", "words that have all the vocals with aphostrofies"]))
    print("total words: " + str(len(result)))
    print("\n")
    words.clear()

def find_words5():
    """ Words that have apostrofies """
    pattern = r'\b[a-zA-Z]*\w*[wáéíóúÁÉÍÓÚ][a-zA-Z]*\b'
    matches = re.findall(pattern, content)
    words.extend(matches)

    result = set(words)
    table = [[i+1, j] for i, j in enumerate(result)]
    print(tabulate.tabulate(table, headers=["#", "Words that have apostrofies"]))
    print("total words: " + str(len(result)))
    print("\n")
    words.clear()

def find_words6():
    """words that be interrogative or excalamatived """
    pattern = r'[¡¿][^¡¿!?]+[!?]'

    matches = re.findall(pattern, content)
    words.extend(matches)

    result = set(words)
    table = [[i+1, j] for i, j in enumerate(result)]
    print(tabulate.tabulate(table, headers=["#", "words that be interrogative or excalamatived "]))
    print("total words: " + str(len(result)))
    print("\n")
    words.clear()

def find_word7():
    """Communs abrevuatures """
    pattern = r'\b(?:[a-zA-Z]{1,4}\.){1,3}'
    matches = re.findall(pattern, content)
    words.extend(matches)

    result = set(words)
    table = [[i+1, j] for i, j in enumerate(result)]
    print(tabulate.tabulate(table, headers=["#", "Communs abreviatures: "]))
    print("total words: " + str(len(result)))
    print("\n")
    words.clear()

def find_word8():
    """that have an @ in the text: """
    pattern = r'\b[a-zA-Z]*[@][a-zA-Z]*\b'
    matches = re.findall(pattern, content)
    words.extend(matches)

    result = set(words)
    table = [[i+1, j] for i, j in enumerate(result)]
    print(tabulate.tabulate(table, headers=["#", "that have an @ in the text: "]))
    print("total words: " + str(len(result)))
    print("\n")
    words.clear()



if __name__ == "__main__":
    global words 
    words = []
    read_file()
    find_words1()
    find_words2()
    find_words3()
    find_words4()
    find_words5()
    find_words6()
    find_word7()
    find_word8()
