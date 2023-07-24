def longest_common_subsequence(string1: str, string2: str) -> str:
    """
    Finds the longest common subsequence of two strings using dynamic programming.

    Args:
    - string1 (str): The first string.
    - string2 (str): The second string.

    Returns:
    - The longest common subsequence of the two strings.
    """

    # Determine the length of each string.
    m = len(string1)
    n = len(string2)

    # Create a table to store the results for different substrings.
    lcs_table = [[0] * (n + 1) for i in range(m + 1)]

    # Fill the table using dynamic programming.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # Find the longest common subsequence using the table.
    lcs_result = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            lcs_result = string1[i - 1] + lcs_result
            i -= 1
            j -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_result


if __name__ == '__main__':
    str1 = input('Enter the first string: ')
    str2 = input('Enter the second string: ')
    lcs = longest_common_subsequence(str1, str2)
    print(f'The longest common subsequence is: {lcs}')
    input('Press Enter to Exit')