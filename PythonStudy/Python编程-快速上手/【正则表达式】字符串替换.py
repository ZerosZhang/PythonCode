import re

"""
\w意思是匹配单词，一个\w表示一个单词
这里的Agent (\w)\w*匹配的是Agent Alice， Agent Carol， Agent Eve，Agent Bob
有意思的是这里的(\w)\w*表示的是一个单词，而(\w)为他的首字母
==========================================================================================

sub()用于替换字符串
第一个参数是一个字符串，用于取代发现的匹配。
在 sub()的第一个参数中，可以输入\1、\2、\3 表示“在替换中输入分组 1、2、3的文本”
比如 Agent Slice 的第一个分组即为"S"，替换字符串为"S****"
用"S****"来替换 Agent Slice 
"""
message = 'Agent Slice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
agentNamesRegex = re.compile(r'Agent (\w)\w*')

print(agentNamesRegex.search(message).group(1))  # 显示为S
print(agentNamesRegex.sub(r'\1****', message))
