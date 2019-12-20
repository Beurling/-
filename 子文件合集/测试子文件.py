# 名称：收割所有子文件
# 用途：如题，把所有子文件中的文件，全部分类提取出来
# 原理：os
# 版本：1.0 191218

import os
import time
import random
import sys

# 计算次数
folders = 0
copy_times = 0
repeat_times = 0

name_list = []
size_list = []
name_size_dict = {}


def file_size(path):
    # Path = unicode(Path, 'utf8')
    size = os.path.getsize(path)
    size = size / float(1024 * 1024)
    # 返回MB格式，和原格式，原格式用于精确对比
    return round(size, 2), size


def copy_files(source_dir, target_dir):
    global copy_times, size_list, name_list, name_size_dict, repeat_times, folders

    # 用于随机命名文件，避免重复
    number = str(random.uniform(2, 4))

    # 创建分类相应文件夹
    py = os.path.join(target_dir, 'py')
    photo = os.path.join(target_dir, 'photo')
    html = os.path.join(target_dir, 'html')
    ignore = os.path.join(target_dir, 'ignore')
    file = os.path.join(target_dir, 'file')
    unknow = os.path.join(target_dir, 'unknow')

    try:
        os.makedirs(py)
        os.makedirs(photo)
        os.makedirs(html)
        os.makedirs(ignore)
        os.makedirs(file)
        os.makedirs(unknow)
    except:
        pass

    print(u"%s 当前处理文件夹%s已处理%s 个文件 | 重复%s个文件" % (
    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), source_dir, copy_times, repeat_times))
    for name in os.listdir(source_dir):
        # 文件名 name

        # 文件路径 | 拼接路径和名字
        source_file_path = os.path.join(source_dir, name)
        print(source_file_path)

        size = file_size(source_file_path)[0]
        size_list.append(size)

        name_size_dict = dict(zip(name_list, size_list))

        print(name_size_dict)

        if size == 0:
            # 说明是文件夹
            folders += 1
            # 构建文件列表，用于查重，顺序：size后，不统计文件夹名字
            name_list.append(name)
        elif size > 200:
            print("文件过大 too big，文件目录为{}".format(source_file_path))
        # elif name in name_list and size == name_size_dict['name']:
        #     print("文件重复 same, 文件目录为{}".format(source_file_path))
        else:

            # 获取文件大小

            # 如果是文件夹，就切换到当前文件夹
            if os.path.isdir(source_file_path):
                target_file = target_dir
            # 如果是文件，直接添加到当前文件夹
            else:
                target_file = os.path.join(target_dir, name)

            if os.path.isfile(source_file_path):
                # 自动创建目录
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                copy_times += 1
                # 避免重复,清晰
                if not os.path.exists(target_file) or (os.path.exists(target_file) and (
                        os.path.getsize(target_file) != os.path.getsize(source_file_path))):
                    # ~ 和 . 为无用文件
                    if name.startswith("~") or name.startswith("."):
                        print('该文件被忽略')
                        try:
                            open(target_file[:9] + 'ignore/' + name, "wb").write(open(source_file_path, "rb").read())
                        except:
                            try:
                                open(target_file[:9] + 'ignore/' + number + name, "wb").write(
                                    open(source_file_path, "rb").read())
                            except:
                                pass
                    else:
                        if name.endswith("jpg") or name.endswith("png") or name.endswith("gif") or name.endswith(
                                "webp") or name.endswith("JPG"):
                            try:
                                open(target_file[:9] + 'photo/' + name, "wb").write(open(source_file_path, "rb").read())
                            except:
                                try:
                                    open(target_file[:9] + 'photo/' + number + name, "wb").write(
                                        open(source_file_path, "rb").read())
                                except:
                                    pass
                        elif name.endswith(".py"):
                            try:
                                open(target_file[:9] + 'py/' + name, "wb").write(open(source_file_path, "rb").read())
                            except:
                                try:
                                    open(target_file[:9] + 'py/' + number + name, "wb").write(
                                        open(source_file_path, "rb").read())
                                except:
                                    pass
                        elif name.endswith(".html"):
                            try:
                                open(target_file[:9] + 'html/' + name, "wb").write(open(source_file_path, "rb").read())
                            except:
                                try:
                                    open(target_file[:9] + 'html/' + number + name, "wb").write(
                                        open(source_file_path, "rb").read())
                                except:
                                    pass
                        elif name.endswith(".pptx") or name.endswith(".pdf") or name.endswith(".zip") or name.endswith(
                                ".md") or name.endswith(".xmind") or name.endswith(".csv") or name.endswith(
                                ".exe") or name.endswith(".txt") or name.endswith(".ipynb") or name.endswith(
                                ".docx") or name.endswith(".xlsx"):
                            try:
                                open(target_file[:9] + 'file/' + name, "wb").write(open(source_file_path, "rb").read())
                            except:
                                try:
                                    open(target_file[:9] + 'file/' + number + name, "wb").write(
                                        open(source_file_path, "rb").read())
                                except:
                                    pass
                        elif name.endswith(".xml") or name.endswith(".iml"):
                            try:
                                open(target_file[:9] + 'ignore/' + name, "wb").write(
                                    open(source_file_path, "rb").read())
                            except:
                                try:
                                    open(target_file[:9] + 'ignore/' + number + name, "wb").write(
                                        open(source_file_path, "rb").read())
                                except:
                                    pass
                        else:
                            try:
                                # 有一些没有见过，流出空间
                                open(target_file[:9] + 'unknow/' + name, "wb").write(
                                    open(source_file_path, "rb").read())
                            except:
                                try:
                                    open(target_file[:9] + 'unknow/' + number + name, "wb").write(
                                        open(source_file_path, "rb").read())
                                except:
                                    pass

                        print(u"%s %s 复制完毕" % (
                        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), target_file))
                else:
                    print(u"%s %s 已存在，不重复复制 repeat" % (
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), target_file))

        if os.path.isdir(source_file_path):
            # print("判断 是目录{}\n".format(source_file_path))
            copy_files(source_file_path, target_file)


def summary():
    print("共处理{}个文件夹".format(folders))


if __name__ == "__main__":
    # print("请输入源文件路径 [空格] 目标路径")
    # [0] 是py文件本身 [1] 是第一个输入的 [2]第二个

    # source_dir = sys.argv[1]
    # source_dir = source_dir.replace("\\", "/")
    #
    # target_dir = sys.argv[2]
    # target_dir = target_dir.replace("\\", "/")
    # target_dir = target_dir.replace('"', "/")

    # target_dir = target_dir + '/'

    # print(source_dir)
    # print(target_dir)

    # copy_files(source_dir, target_dir)
    copy_files('F:/网课Wk/Python 24期/python课件/18.数据挖掘', 'E:/Files/')
    summary()

