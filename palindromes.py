def palindromes(word: str):
    if word == word[::-1]:
        return True
    
    else:
        return False

def repeater():
    while True:
        word = input("Please type in a palindrome: ")
        result = palindromes(word)
        if result:
            print(f"{word} is a palindrome!")
            break
        
        print("that wasn't a palindrome")

repeater()