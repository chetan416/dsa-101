from collections import Counter

def valid_anagram(first_string,second_string):
    if len(first_string) != len(second_string):
        return False
    first_string_dict = Counter(first_string)
    second_string_dict = Counter(second_string)
    return first_string_dict == second_string_dict

print(valid_anagram("anagram","nagaram"))