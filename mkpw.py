import random
import string
import sys


def randomname(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    randstr = ''.join(randlst)
    split_str = [randstr[i:i+8] for i in range(0, len(randstr), 8)]
    return '-'.join(split_str)


if __name__ == '__main__':
    # 第一引数で指定された数のパスワードを生成
    try:
        n = int(sys.argv[1])
        print(randomname(n))
    except Exception:
        print('Usage: python mkpw.py [n] (n: number of characters) (e.g. python mkpw.py 16)')
