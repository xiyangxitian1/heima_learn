import re

# match 是从第一个匹配，开头不匹配就失败了。

# .	匹配任意1个字符（除了\n）
# result = re.match("[hH]ello", "elloHello")
# if result:
#     print("匹配结果:", result.group())
# else:
#     print("匹配失败！")
# [ ]	匹配[ ]中列举的字符
# \d	匹配数字，即0-9
# \D	匹配非数字，即不是数字
# \s	匹配空白，即 空格，tab键
# result = re.match("a\sb", "a\tb")
# if result:
#     print("匹配结果:", result.group())
# else:
#     print("匹配失败！")
# \S	匹配非空白
# result = re.match("a\Sb", "a张b")
# if result:
#     print("匹配结果:", result.group())
# else:
#     print("匹配失败！")
# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
# result = re.match("a\wb", "a1b")
# if result:
#     print("匹配结果:", result.group())
# else:
#     print("匹配失败！")
# \W	匹配特殊字符，即非字母、非数字、非汉字
# result = re.match("a\Wb", "a&b")
# if result:
#     print("匹配结果:", result.group())
# else:
#     print("匹配失败！")
# result = re.match("[a-zA-Z0-9\W]{8,70}", "abCdE-F0832434")
# if result:
#     print("匹配结果:", result.group())
# else:
#     print("匹配失败！")

# result = re.match("a.?c", "ac")
# if result:
#     print("匹配结果:", result.group())
# else:
#     print("匹配失败！")


# 1.匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
# result = re.match("[a-z_A-Z0-9]{4,20}@163\.com$", "liyan@163acom")
# print(result.group())
# 2.匹配出11位手机号码
# result = re.match("^1\d{9}\d$", "13800138000")
# print(result.group())
# 3.匹配出微博中的话题, 比如: #幸福是奋斗出来的#
# l1 = re.findall("#幸福是奋斗出来的#", "bbb#幸福是奋斗出来的#aaa")
# print(l1)
# result = re.match("^\d{11}$", "13800138000")
# print(result.group())
# result = re.match("[^a-z]","b")
# print(result.group())

# result = re.match("(?P<name1>)(ab)(?P=name1)", "abab")
#
# result = re.match("(?P<name1>ab)(?P=name1)", "abab")
# if result:
#     print(result.group())
# else:
#     print("fail...")
# 0是结果，1是第1个分组（也就是括号）2是第2个分组
# result = re.match("[a-zA-Z_0-9]{4,20}@(163|qq|126)\.com", "hello@126.com")
# if result:
#     print(result.group(0))
#     print(result.group(1))
# else:
#     print("fail...")
# print("\\\\")
# 引用的分组名要在前面，因为这个match是从前后向匹配的，  不知道其他的方法是不是可能调用后面的分组
# result = re.match("(?P<name2>hello).*(?P<name1>(?P=name2))", "hello:obb:applehellobccfef")
# if result:
#     print(result.group())
#     print(result.group(0))
#     print(result.group(1))
#     print(result.group(2))
#
#     # print(result.groupdict(name="name1"))
#
# else:
#     print("失败")

# 匹配  apple:elppa  就是两个单词是相反的

# re.match("","<html></html>")
result = re.match("\s", "\n\v\r\f\n")
if result:
    print(result.group())
else:
    print("fail……")
