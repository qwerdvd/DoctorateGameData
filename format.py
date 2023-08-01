# coding:utf8
# 批量格式化当前目录下所有的json

import os
import json
import sys
import codecs

def formatJson(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            formatJson(path + '/' + file)
    elif os.path.isfile(path):
        if path.endswith('.json'):
            with codecs.open(path, 'r', 'utf-8') as f:
                content = f.read()
                try:
                    json.loads(content)
                except Exception as e:
                    print(path)
                    print(e)
                    sys.exit(1)
                else:
                    with codecs.open(path, 'w', 'utf-8') as f:
                        f.write(json.dumps(json.loads(content), ensure_ascii=False, indent=4))
                        print(path)
        else:
            pass
    else:
        pass

if __name__ == '__main__':
    formatJson(os.getcwd())
