# 强口令
"""
1. 长度不少于8个字符串
2. 同时包含大写和小写
3. 至少有1位数字
"""
import re

password_regex_match_length = re.compile(r'.{8,}')  # 至少8位
password_regex_match_number = re.compile(r'\d+')  # 至少1个数字
password_regex_match_lower = re.compile(r'[a-z]+')  # 包含小写
password_regex_match_upper = re.compile(r'[A-Z]+')  # 包含大写


def match_strong_password(_password):
    result_match_length = password_regex_match_length.search(_password)
    result_match_number = password_regex_match_number.search(_password)
    result_match_lower = password_regex_match_lower.search(_password)
    result_match_upper = password_regex_match_upper.search(_password)
    return result_match_lower and result_match_upper and result_match_number and result_match_length


text_password = ''
while not match_strong_password(text_password):
    text_password = input("输入口令:")
