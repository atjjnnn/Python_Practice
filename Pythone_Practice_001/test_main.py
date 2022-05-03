#coding: UTF-8

# '__name__'は別ファイルからインポートされるとインポート元のモジュール名が格納される
# 一方ファイルをコマンドラインからスクリプトとして実行すると'__main__'が格納される

import test_module

print('This is test_main.py')
print('test_modeule.__name__ is', test_module.__name__)

print('---')
print('call test_module.func()')

test_module.func()
