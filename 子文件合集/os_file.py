# 名称：收割所有子文件
# 用途：如题，把所有子文件中的文件，全部分类提取出来
# 原理：os
# 版本：1.0 191218

import os
import time
import random
# 计算次数
copyFileCounts = 0


def copy_files(source_dir, target_dir):
    # 全局
    global copyFileCounts

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

    print(u"%s 当前处理文件夹%s已处理%s 个文件" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), source_dir, copyFileCounts))
    for f in os.listdir(source_dir):
        # 获取子文件路径
        # 获取文件名
        name = os.path.basename(f)
        # 拼接路径和名字
        source_file = os.path.join(source_dir, f)

        # 如果是文件夹，就切换到当前文件夹
        if os.path.isdir(source_file):
            target_file = target_dir
        # 如果是文件，直接添加到当前文件夹
        else:
            target_file = os.path.join(target_dir, name)

        if os.path.isfile(source_file):
            # 自动创建目录
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            copyFileCounts += 1
            # 避免重复
            if not os.path.exists(target_file) or (os.path.exists(target_file) and (os.path.getsize(target_file) != os.path.getsize(source_file))):
                # ~ 和 . 为无用文件
                if name.startswith("~") or name.startswith("."):
                    print('该文件被忽略')
                    try:
                        open(target_file[:9] + 'ignore/' + f, "wb").write(open(source_file, "rb").read())
                    except:
                        try:
                            open(target_file[:9] + 'ignore/' + number + f, "wb").write(open(source_file, "rb").read())
                        except:
                            pass
                else:
                    if name.endswith("jpg") or name.endswith("png") or name.endswith("gif") or name.endswith("webp") or name.endswith("JPG"):
                        try:
                            open(target_file[:9] + 'photo/' + f, "wb").write(open(source_file, "rb").read())
                        except:
                            try:
                                open(target_file[:9] + 'photo/' + number + f, "wb").write(open(source_file, "rb").read())
                            except:
                                pass
                    elif name.endswith(".py"):
                        try:
                            open(target_file[:9] + 'py/' + f, "wb").write(open(source_file, "rb").read())
                        except:
                            try:
                                open(target_file[:9] + 'py/' + number + f, "wb").write(open(source_file, "rb").read())
                            except:
                                pass
                    elif name.endswith(".html"):
                        try:
                            open(target_file[:9] + 'html/' + f, "wb").write(open(source_file, "rb").read())
                        except:
                            try:
                                open(target_file[:9] + 'html/' + number + f, "wb").write(open(source_file, "rb").read())
                            except:
                                pass
                    elif name.endswith(".pptx") or name.endswith(".pdf") or name.endswith(".zip") or name.endswith(".md") or name.endswith(".xmind") or name.endswith(".csv") or name.endswith(".exe") or name.endswith(".txt"):
                        try:
                            open(target_file[:9] + 'file/' + f, "wb").write(open(source_file, "rb").read())
                        except:
                            try:
                                open(target_file[:9] + 'file/' + number + f, "wb").write(open(source_file, "rb").read())
                            except:
                                pass
                    elif name.endswith(".xml") or name.endswith(".iml"):
                        try:
                            open(target_file[:9] + 'ignore/' + f, "wb").write(open(source_file, "rb").read())
                        except:
                            try:
                                open(target_file[:9] + 'ignore/' + number + f, "wb").write(
                                    open(source_file, "rb").read())
                            except:
                                pass
                    else:
                        try:
                            # 有一些没有见过，流出空间
                            open(target_file[:9] + 'unknow/' + f, "wb").write(open(source_file, "rb").read())
                        except:
                            try:
                                open(target_file[:9] + 'unknow/' + number + f, "wb").write(
                                    open(source_file, "rb").read())
                            except:
                                pass

                    print(u"%s %s 复制完毕" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), target_file))
            else:
                print(u"%s %s 已存在，不重复复制" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), target_file))

        if os.path.isdir(source_file):
            # print("判断 是目录{}\n".format(source_file))
            copy_files(source_file, target_file)


if __name__ == "__main__":
    copy_files('F:/网课Wk/Python 24期/python课件/18.数据挖掘', 'E:/Files/')

