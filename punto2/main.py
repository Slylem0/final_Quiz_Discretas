import re
import tabulate;

def read_file():
    global content
    with open("text.txt", mode="r", encoding="utf-8") as file:
        content = file.read()

def find_words():
    """expressions of questions"""
    pattern = r'\¿[^\n\¡\!]+\?|[^\n\¿\¡\!]+\?'
    matches = re.findall(pattern, content)

    words.extend(matches)

    result = set(words)
    table = [[i+1, j] for i, j in enumerate(result)]
    print(tabulate.tabulate(table, headers=["#", "Expression of questions"]))
    print("total words: " + str(len(result)))
    print("\n")
    words.clear()

def find_words1():
    """expression of aclamacion"""
    pattern = r'¡[^¡!¿\?]*?!|[^¡!¿\?\n]+!'
    matches = re.findall(pattern, content)

    words.extend(matches)

    result = set(words)
    table = [[i+1, j] for i, j in enumerate(result)]
    print(tabulate.tabulate(table, headers=["#", "expression of aclamacion"]))
    print("total words: " + str(len(result)))
    print("\n")
    words.clear()
    

def find_words2():
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

    

if __name__ == "__main__":
    global words 
    words = []
    read_file()
    find_words()
    find_words1()
    find_words2()

