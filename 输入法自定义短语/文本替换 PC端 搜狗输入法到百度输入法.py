import os
import re

txt = open('words.txt', 'r')
f = open("new.txt", 'a')

words = txt.readline()

while words:
    words = words.strip("\n")
    # print("--" + words + "--")
    # print(type(words))
    # print(words.split(","))
    # print(words.split("="))

    left = words.split(",")[0]
    right = words.split("=")[1]
    number = words.split("=")[0][-1:]

    # print(left)
    # print(right)
    # print(number)

    end = number + ',' + left + "=#{" + right + "}" + right
    print(end)

    f.write(end)
    f.write("\n")

    words = txt.readline()



# lines = txt.readline()

# for word in words:
#     print(word)


txt.close()
f.close()
