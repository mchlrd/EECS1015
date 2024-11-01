def count_vowels(word):
    i = 0
    for char in word:
        if char in ['a','e','o','u','i',]:
            i+=1
        else:
            pass
    
    return i

print(count_vowels('hello'))