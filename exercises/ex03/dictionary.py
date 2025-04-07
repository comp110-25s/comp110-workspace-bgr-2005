"""Exercise three"""

__author__ = "730769478"

"""python -m pytest exercises/ex03"""


def invert(dicte: dict[str, str]) -> dict[str, str]:
    """placeholder1 : str;
    placeholder2: str;
    for key in dicte :
        placeholder1 = key;
        placeholder2= value;
        key = value
        dicte(key) = placeholder1"""
    keyes: list[str] = []
    for x in dicte:
        if dicte[x] in keyes:
            raise KeyError("keyError")
        else:
            keyes.append(dicte[x])

    """got smarter"""
    return {value: key for key, value in dicte.items()}


def count(liste: list[str]) -> dict[str, int]:
    """counts the amount of times a word shows up in a list of words"""
    builtDict: dict[str, int] = {}

    for x in liste:
        if x in builtDict.keys():
            builtDict[x] = builtDict[x] + 1
        else:
            builtDict[x] = 1
    return builtDict


def favorite_color(namesAndColors: dict[str, str]) -> str:
    """given a dict of ppl and their corrosponding favorite color,
    give me the most favorite color"""
    colors: list[str] = []
    mostCommon = int(0)
    mostCommonWord = str("")
    for keys in namesAndColors:
        colors.append(namesAndColors[keys])

    counted = count(colors)

    for keys in counted:
        if counted[keys] > mostCommon:
            mostCommon = counted[keys]
            mostCommonWord = keys

    return mostCommonWord


def bin_len(givenWords: list[str]) -> dict[int, set[str]]:
    """given a list of strings,
    break it up into a dictionary by how long each word is"""
    wordLen: int = 0
    newDict: dict[int, set] = {}

    for x in givenWords:
        wordLen = len(x)

        if wordLen in newDict.keys():
            newDict[wordLen].add(x)
        else:
            placeholderset: set = {0}
            placeholderset.clear()
            placeholderset.add(x)
            newDict[wordLen] = placeholderset

    return newDict
