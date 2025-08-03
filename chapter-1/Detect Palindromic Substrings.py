def find_palindromic_substrings(s):
    result=set()
    for i in range(len(s)):
        for j in range(i+2,len(s)+1):
            substr=s[i:j]
            if substr==substr[::-1]:
                result.add(substr)
    return list(result)