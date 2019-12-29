# mac测试
import os
import re

txt = open('mac.txt', 'r', encoding='UTF-8')
# f = open("new.txt", 'a')

words = txt.readline()



while words:
    words = words.strip("\n")
    print("--" + words + "--")
    # print(type(words))
    # print(words.split(","))
    # print(words.split("="))

    # 删除系统自带
    # if "{" in words:
    #     left_1 = words.split(",")[1]
    #     left = left_1.split("=")[0]
    #     right = words.split("}")[1]
    #     number = words.split(",")[0]

    # print(left)
    # print(right)
    # print(number)

    # 1,ff=#{方法Ff}方法Ff

    # ff=2,方法ff

        # end = left + "=" + number + "," + right
        # print(end)
        #
        # f.write(end)
        # f.write("\n")

    words = txt.readline()

# lines = txt.readline()

# for word in words:
#     print(word)


txt.close()
# f.close()
