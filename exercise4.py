def order(str1,str2):
    return (str1[0]+ str2[0]+ (str1[int(len(str1)/2)]) + (str2[int(len(str2)/2)])+ str1[-1]+ str2[-1])


word1 = "Python"
word2 = "Developer"
print (order(word1,word2))


