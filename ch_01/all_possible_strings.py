def generate_combinations(s, path="", results=None):
    """
    Generate all possible non-empty strings that can be formed by using 
    each character of the input string exactly once. The function returns
    a set of strings of length 1 to len(s) created by recursive permutations.

    Parameters:
    - s (str): The input string from which to form combinations.
    - path (str): The current combination being built during recursion.
    - results (set): A set used to collect unique string results.

    Returns:
    - set: A set of all unique strings formed from the characters of 's'.
    """
    
    # Initialize the results set on the first call
    if results is None:
        results = set()

    # Add the current path to the results if it's non-empty
    if path:
        results.add(path)

    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Recurse with the remaining characters excluding the current one
        # Add the current character to the path
        generate_combinations(s[:i] + s[i+1:], path + char, results)

    return results


# Example usage
input_string = "c","a","t","d","o","g"
combinations = generate_combinations(input_string)
print(sorted(combinations))