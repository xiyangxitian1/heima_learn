import os

# os.chdir(path)
# cmd = 'copy /b *.ts new.tmp'
# os.system(cmd)
# os.system('del /Q *.ts')
# os.rename('new.tmp', title + '.mp4')

os.chdir('F:')
a = os.system('ssh -tt python@192.168.18.58 ')  # ssh -tt python@192.168.18.58 -p 12   -p意思是端口？  加上-tt强制让系统认为这是终端，否则会报错

print(a)
# 密码不对就会拒绝，所以要多试试  判断不是255的


