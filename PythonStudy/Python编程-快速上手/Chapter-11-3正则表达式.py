"""
疯狂填词
读入文本文件，让用户在该文本文件中出现ADJECTIVE、NOUN、ADVERB 或 VERB 等单词的地方，加上自己的文本
"""

import re

origin_string = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

match_regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
while True:
    match_result = match_regex.search(origin_string)
    if not match_result:
        break
    sub_string = input(f'Enter an {match_result.group()}:\n')
    origin_string = match_regex.sub(sub_string, origin_string, count=1)  # count = 1表示最大替换次数

print(origin_string)
