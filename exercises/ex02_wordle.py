"""wordle assignment"""

__author__ = "730769478"


def contains_char(anyL: str, single: str) -> bool:
    """checks if it contains the same character"""
    assert len(single) == 1, f"len('{single}') is not 1"

    i: int = 0
    while i < len(anyL):
        if anyL[i] == single:
            return True
        else:
            i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """emofifies some guesses idk"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i: int = 0
    result: str = ""
    while i < len(secret):
        if secret[i] == guess[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i = i + 1
    return result


def input_guess(expectedLength: int) -> str:
    word: str = input(f"Enter a {expectedLength} letter word:")

    while len(word) != expectedLength:
        word = input(f"That wasn't {expectedLength} chars! Try again:")
    return word


def main(secret: str) -> None:
    """does the overhead"""
    turn: int = 1

    while turn <= 6:
        """and input_guess(len(secret)) != secret"""

        print(f"=== Turn {turn}/6 ===")
        guesss: str = input_guess(len(secret))
        print(emojified(guesss, secret))
        if guesss == secret:
            print(f"You won in {turn}/6 turns!")
            return
        else:
            turn = turn + 1

    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
