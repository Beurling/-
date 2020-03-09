# txt先另存为ansi
# 再utf-8
# 运行程序
# 安卓端需要将ANSI编码手动转为UTF-16-LE
# mac转为utf-8 手动复制
# mac需要删除原来的，再复制 否则旧的会保留
# PC端复制源文件，而不是txt，因为txt格式已经改变
txt = open('自定义短语导出.txt', 'r', encoding='UTF-8')
Android = open("cphrase.ini", 'w')
Mac = open("用户词典.txt", 'w')

Mac.write('<?xml version="1.0" encoding="UTF-8"?>')
Mac.write("\n")
Mac.write('<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">')
Mac.write("\n")
Mac.write('<plist version="1.0">')
Mac.write("\n")
Mac.write("<array>")
Mac.write("\n")

words = txt.readline()

while words:
    words = words.strip("\n")

    # 安卓
    if "{" in words:
        left_1 = words.split(",")[1]
        Android_left = left_1.split("=")[0]
        Android_right = words.split("}")[1]
        Android_number = words.split(",")[0]

        Android_end = Android_left + "=" + Android_number + "," + Android_right
        # print(Android_end)

        Android.write(Android_end)
        Android.write("\n")

    # MacBook
        Mac_left = Android_left
        Mac_right = Android_right

        Mac_end = Mac_left + "," + Mac_right

        Mac.write("        <dict>")
        Mac.write("\n")
        Mac.write("                <key>phrase</key>")
        Mac.write("\n")
        Mac.write("                <string>{}</string>".format(Mac_right))
        Mac.write("\n")
        Mac.write("                <key>shortcut</key>")
        Mac.write("\n")
        Mac.write("                <string>{}</string>".format(Mac_left))
        Mac.write("\n")
        Mac.write("        </dict>")
        Mac.write("\n")

    words = txt.readline()

Mac.write("</array>")
Mac.write("\n")
Mac.write("</plist>")

txt.close()
Mac.close()
Android.close()