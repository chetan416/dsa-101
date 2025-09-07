from collections import Counter

def valid_anagram(first_string,second_string):
    if len(first_string) != len(second_string):
        return False
    s_dict = Counter(first_string)
    t_dict = Counter(second_string)
    return s_dict == t_dict

print(valid_anagram("anagram","nagaram"))