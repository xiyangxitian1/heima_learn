import re

if __name__ == '__main__':
    result = re.match('hel', 'hellohello')
    rs = result.groups()
    # re.search()
    # re.findall()
    # re.finditer()
    # re.sub()   #替换
    if result:
        print("匹配结果：", result.group())
    else:
        print("匹配失败")
