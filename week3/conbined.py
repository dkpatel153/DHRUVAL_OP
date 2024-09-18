def fun3(word):
    first = word[0]
    last = word[len(word)-12]
    conbined = first + last
    return conbined

word = input("Enter the word:")
print(fun3(word))

