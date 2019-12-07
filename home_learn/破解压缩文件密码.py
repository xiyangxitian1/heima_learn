# 目标F:\test1\123.zip
# 生成000000到999999的密码表
import zipfile


def genPwd():
    """生成密码本"""
    f = open(r'F:\test1\pwd.txt', "w")
    for id in range(1000000):
        #  str.zfill(width)  zifill是字符串的一个方法
        #  width -- 这是字符串的最终宽度，即填充零后得到的宽度。
        pwd = str(id).zfill(6) + '\n'
        f.write(pwd)
    f.close()


def extractFile(zipFile1, password):
    try:
        # print('下面破解')
        zipFile1.extractall(path=r'F:\test1\aa', pwd=bytes(password, 'utf8'))
        print('密码是：', password)
        return True
    except Exception:
        # print('失败')
        return False


def main():
    zipFile = zipfile.ZipFile(r'F:\test1\123.zip')
    PwdLists = open(r'F:\test1\pwd.txt')  # 读取所有密码
    for line in PwdLists.readlines():  # 挨个挨个的写入密码
        Pwd = line.rstrip('\n')
        # print(Pwd)
        guess = extractFile(zipFile, Pwd)
        if guess:
            break


if __name__ == '__main__':
    main()
