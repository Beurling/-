# 名称：收割所有子文件
# 用途：如题，把所有子文件中的文件，全部分类提取出来
# 原理：os
# 版本：1.0 191218

import os
import time
import random
import sys
import filecmp
import winshell
import pypandoc
import pdfkit
# import pandoc
config = pdfkit.configuration(wkhtmltopdf=r"E:\OneDrive\编程 Computer Programming\IDE\wkhtmltox\bin\wkhtmltopdf.exe")


# 计算次数
folders = 0
file_copy_times = 0
repeat_times = 0
file_same_times = 0

new_name_number = 0
not_same = True

file_limit = 50

big_file_times = 0

name_list = []
size_list = []
name_size_dict = {}
big_file_dict = {}
big_file_path = []
big_file_size = []


def short_cut(new_dir, old_dir):
    # -*-code: utf-8 -*-
    # filename = "myShortcut"
    # target = r"D:\Python"

    winshell.CreateShortcut(
        Path=os.path.join(new_dir + ".lnk"),
        Target=old_dir,
        Icon=(old_dir, 0),
        Description="")


def file_size(path):
    # Path = unicode(Path, 'utf8')
    size = os.path.getsize(path)
    bytes_size = size
    size = size / float(1024*1024)
    # 返回MB格式，和原格式，原格式用于精确对比
    return round(size, 2), bytes_size


def init_file(new_dir):
    # 创建分类相应文件夹
    py = os.path.join(new_dir, 'py')
    photo = os.path.join(new_dir, 'photo')
    html = os.path.join(new_dir, 'html')
    ignore = os.path.join(new_dir, 'ignore')
    file = os.path.join(new_dir, 'file')
    unknow = os.path.join(new_dir, 'unknow')

    try:
        os.makedirs(py)
        os.makedirs(photo)
        os.makedirs(html)
        os.makedirs(ignore)
        os.makedirs(file)
        os.makedirs(unknow)
    except:
        pass


def copy_files(old_dir, new_dir):
    global file_copy_times, big_file_dict, size_list, big_file_path, big_file_size, not_same, new_name_number, file_same_times, file_limit, name_list, name_size_dict, repeat_times, folders, big_file_times

    # 用于随机命名文件，避免重复
    number = str(random.uniform(2, 4))

    # print(u"%s 当前处理文件夹%s已处理%s 个文件 | 重复%s个文件" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), old_dir, file_copy_times, repeat_times))
    for name in os.listdir(old_dir):
        # 文件名 name

        new_file = os.path.join(new_dir, name)

        # 文件路径 | 拼接路径和名字
        old_file_path = os.path.join(old_dir, name)
        new_file_path = os.path.join(new_dir, name)

        # print(old_file_path)

        # 如果是文件夹，就切换到当前文件夹
        if os.path.isdir(old_file_path):
            # print("文件夹")
            # 用于递归
            new_file = new_dir
            # 文件夹次数+1
            folders += 1

            # 进入子文件夹
            copy_files(old_file_path, new_file)

        # 如果是文件，直接添加到当前文件夹
        else:
            # print("文件")

            size = file_size(old_file_path)[0]
            bytes_size = file_size(old_file_path)[1]
            size_list.append(bytes_size)

            try:
                if filecmp.cmp(old_file_path, new_file_path):
                    not_same = False
                    file_same_times += 1
                    # print("文件完全重复 all_same, 文件目录为{}".format(old_file_path))
            except:
                pass

            if size > 100:
                # print("文件过大 too big，文件目录为{}".format(new_file))
                big_file_size.append(size)
                big_file_path.append(name)

                big_file_dict = dict(zip(big_file_path, big_file_size))
                big_file_times += 1

                short_cut(new_file_path, old_file_path)
            elif not_same:
                file_copy_times += 1
                try:
                    open(new_file[:9] + name, "wb").write(open(old_file_path, "rb").read())
                except:
                    try:
                        open(new_file[:9] + number + name, "wb").write(open(old_file_path, "rb").read())
                    except:
                        pass
            else:
                not_same = True


def class_file(new_dir):
    global name_size_dict, big_file_dict, big_file_path, big_file_size, big_file_times, file_limit
    for name in os.listdir(new_dir):
        # print(name)
        new_file = os.path.join(new_dir, name)

        size = file_size(new_file)[0]
        name_list.append(name)
        size_list.append(size)

        name_size_dict = dict(zip(name_list, size_list))

        if size > 50:
            pass
        elif name.endswith('lnk'):
            pass
        elif name.startswith("~") or name.startswith("."):
            # print('该文件被忽略')
            try:
                open(new_file[:9] + 'ignore/' + name, "wb").write(open(new_file, "rb").read())
            except:
                pass

            os.remove(new_file)
        elif name.endswith("jpg") or name.endswith("png") or name.endswith("gif") or name.endswith("webp") or name.endswith("JPG"):
            try:
                open(new_file[:9] + 'photo/' + name, "wb").write(open(new_file, "rb").read())
            except:
                pass

            os.remove(new_file)
        elif name.endswith(".py"):
            try:
                open(new_file[:9] + 'py/' + name, "wb").write(open(new_file, "rb").read())
            except:
                pass

            os.remove(new_file)
        elif name.endswith(".html"):
            try:
                open(new_file[:9] + 'html/' + name, "wb").write(open(new_file, "rb").read())
            except:
                pass

            os.remove(new_file)
        elif name.endswith(".pptx") or name.endswith(".pdf") or name.endswith(".zip") or name.endswith(".xmind") or name.endswith(".csv") or name.endswith(".exe") or name.endswith(".txt") or name.endswith(".docx") or name.endswith(".xlsx"):
            try:
                open(new_file[:9] + 'file/' + name, "wb").write(open(new_file, "rb").read())
            except:
                pass

            os.remove(new_file)
        # ipynb 转 html 再转 docx
        # jupyter nbconvert --to html day01_matplotlib.ipynb
        elif name.endswith(".ipynb"):
            try:
                open(new_file[:9] + 'file/' + name, "wb").write(open(new_file, "rb").read())
                os.chdir("E:\\" + "Giles\\" + "file\\")
                os.system("jupyter nbconvert --to html " + name)

                pdfkit.from_file(new_file[:9] + 'file/' + name[:-6] + ".html", new_file[:9] + 'file/' + name[:-6] + ".pdf", configuration=config)
                # pypandoc.convert_file(new_file[:9] + 'file/' + name, 'pdf', format='html', outputfile=new_file[:9] + 'file/' + name[:-6] + ".docx")
                # os.remove(new_file[:9] + 'file/' + name)

            except:
                pass

            os.remove(new_file)
        # 直接md转word
        elif name.endswith(".md"):
            try:
                open(new_file[:9] + 'file/' + name, "wb").write(open(new_file, "rb").read())
                pypandoc.convert_file(new_file[:9] + 'file/' + name, 'docx', format='md', outputfile=new_file[:9] + 'file/' + name[:-3] + ".docx")
                os.remove(new_file[:9] + 'file/' + name)
            except:
                pass

            os.remove(new_file)

        elif name.endswith(".xml") or name.endswith(".iml"):
            try:
                open(new_file[:9] + 'ignore/' + name, "wb").write(open(new_file, "rb").read())
            except:
                pass

            os.remove(new_file)
        else:
            try:
                # 有一些没有见过，流出空间
                open(new_file[:9] + 'unknow/' + name, "wb").write(open(new_file, "rb").read())
                os.remove(new_file)
            except:
                pass

        # print(u"%s %s 复制完毕" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), new_file))


def summary():
    print("共处理{}个文件，{}个文件夹\n复制{}个文件\n完全重复{}个文件\n超过{}MB文件{}个\n超大文件目录{}\n目录{}".format(file_copy_times + file_same_times, folders, file_copy_times, file_same_times, file_limit, big_file_times, big_file_dict, name_size_dict))


if __name__ == "__main__":
    # print("请输入源文件路径 [空格] 目标路径")
    # [0] 是py文件本身 [1] 是第一个输入的 [2]第二个

    # old_dir = sys.argv[1]
    # old_dir = old_dir.replace("\\", "/")
    #
    # new_dir = sys.argv[2]
    # new_dir = new_dir.replace("\\", "/")
    # new_dir = new_dir.replace('"', "/")

    # new_dir = new_dir + '/'

    # print(old_dir)
    # print(new_dir)

    # copy_files(old_dir, new_dir)
    file_path = 'E:/Giles/'
    init_file(file_path)
    # copy_files('F:/网课Wk/Python 24期/python课件/18.数据挖掘', 'E:/Files/')
    # 手动 右斜杠 改为 左斜杠
    old_path = 'F:/网课/Python/2019 24期 黑马/Python 24期/18.数据挖掘'
    copy_files(old_path, file_path)
    class_file(file_path)
    summary()

