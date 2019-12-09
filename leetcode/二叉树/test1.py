import os
import sys
import stat

path = r'F:\heima\33期就业班\课件\第09天{mysql数据库条件查询和高级使用}\Day09作业'

os.chdir(path)
os.chmod(path + '/Day09作业.txt', stat.S_IWUSR)
