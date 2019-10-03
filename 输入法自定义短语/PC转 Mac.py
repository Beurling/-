import os
import re

txt = open('words.txt', 'r', encoding='UTF-8')
f = open("new.txt", 'w')

words = txt.readline()

while words:
    words = words.strip("\n")
    print("--" + words + "--")
    # print(type(words))
    # print(words.split(","))
    # print(words.split("="))

    # 删除系统自带

    left = words.split("=")[0]
    right = words.split(",")[1]

    # print(left)
    # print(right)
    # print(number)

    # 1,ff=#{方法Ff}方法Ff

    # ff=2,方法ff

    end = left + "," + right
    print(end)



    f.write("	<dict>")
    f.write("\n")
    f.write("		<key>phrase</key>")
    f.write("\n")
    f.write("		<string>{}</string>".format(right))
    f.write("\n")
    f.write("		<key>shortcut</key>")
    f.write("\n")
    f.write("		<string>{}</string>".format(left))
    f.write("\n")
    f.write("	</dict>")
    f.write("\n")

    words = txt.readline()

# lines = txt.readline()

# for word in words:
#     print(word)


txt.close()
f.close()
