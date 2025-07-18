import string

def rm_punct(text: str) -> str:
    """
    Remove all punctuation from the input string and return the cleaned version.
    """
    return ''.join(char for char in text if char not in string.punctuation)
if __name__ == "__main__":
    st="Let's go and, there. Cod is good fish."
    print(rm_punct(st))