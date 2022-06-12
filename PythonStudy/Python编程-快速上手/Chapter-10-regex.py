import re

import pyperclip
"""
复制这段内容，然后运行程序
Phone: 800.420.7240 
or +1 415.863.9900 ext.123 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950
"""

phoneRegex = re.compile(r'''(
                            (\d{3}|\(\d{3}\))?              # area code   
                            (\s|-|\.)?                      # separator
                            (\d{3})                         # first 3 digits 
                            (\s|-|\.)                       # separator
                            (\d{4})                         # last 4 digits
                            (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
                            )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])

    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

if len(matches) > 0:
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
