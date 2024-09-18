def fun1(word1,word2):
    len1 = len(word1)
    len2 = len(word2)
    shorter_length = max(len1,len2)
    return shorter_length

word1 = str(input("Enter the word1:"))
word2 = str(input("Enter the word2:"))
print(fun1(word1,word2))


