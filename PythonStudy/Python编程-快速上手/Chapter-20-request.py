import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    # 当我打开了代理的时候，直接显示报错
    res.raise_for_status()
    play_file = open('罗密欧与朱丽叶.txt', 'wb')
    # 每次写100000字节
    for chunk in res.iter_content(100000):
        play_file.write(chunk)
    play_file.close()
except Exception as exc:
    print(f'加载网页代码失败，错误码为{exc}')
