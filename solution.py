
def reverse_string(text: str) -> str:
    return text[::-1]


def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


# Test cases
if __name__ == "__main__":
    print(reverse_string("hello"))       # olleh
    print(reverse_string("Python"))      # nohtyP
    print(reverse_string(""))            # ''

    print(count_vowels("Hello World"))   # 3
    print(count_vowels("AEIOU"))          # 5
    print(count_vowels("Python"))         # 1
    print(count_vowels(""))               # 0
