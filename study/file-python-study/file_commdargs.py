# 导入sys模块
import sys

helpText = """
-mode server/client
-host [localhost]
-port [port]
"""

print(helpText)

# 接受命令行参数
args = sys.argv

if len(args) > 2:
        print('login:', args[1], 'use',args[2])
        for x in args:
            print(x)
else:
    print(helpText)
