# Table of Contents

* [Anagram Tester](#Anagram-Tester)
* [English Word Tester](#English-Word-Tester)
* [Password Strength](#Password-Strength)

# Anagram Tester

```python
def isAnagram(test, original):
    for letter in test.lower():
        if letter not in original.lower():
            return False
    for letter in original.lower():
        if letter not in test.lower():
            return False
    return True
```

# English Word Tester

```python
def is_english_word(string):
    with open('english_words.txt') as f:
        f_contents = f.read()
        if string.lower() in f_contents:
            return True
        else:
            return False
```

# Password Strength

Conditions for password strength:
* Weak: less than 8 characters or an English word (as defined by the English Word Tester)
* Strong: at least 11 characters long and contain at least 1 upper case, 1 lower case and 1 numeric character
* Medium: everything else

```python
def password_strength(string):
    if len(string) < 8 or is_english_word(string) == True:
        strength = "WEAK"

    elif len(string) >= 11:
        uc = 0
        lc = 0
        nc = 0
        for i in string:
            if i.isupper():
                uc += 1
            if i.islower():
                lc += 1
            if i.isnumeric():
                nc += 1

        if uc >= 1 and nc >= 1 and lc >= 1:
            strength = "STRONG"
        else:
            strength = "MEDIUM"

    return strength
```
