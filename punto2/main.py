import re
import tabulate;

def read_file():
    global content
    with open("text.txt", mode="r", encoding="utf-8") as file:
        content = file.read()

def find_words():
    """expressions of questions"""
    #USE THE REGEX TON FIND USING THE RE LIBRARY
    # This pattern matches questions that start with '¿' and end with '?' or those that do not start with '¿' but end with '?'
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
    #USE THE REGEX TON FIND USING THE RE LIBRARY
    # This pattern matches exclamations that start with '¡' and end with '!' or those that do not start with '¡' but end with '!'
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
    #USE THE REGEX TON FIND USING THE RE LIBRARY
    # This pattern matches common abbreviations that consist of 1 to 4 letters followed by a dot, repeated 1 to 3 times
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

