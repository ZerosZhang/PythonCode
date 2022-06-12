"""
这里有50个州和对应的首府
需要生成35份试卷，将50个州作为问题，首府作为答案
随机排列50个问题
每个问题包含4个答案，其中一个正确答案和三个错误答案，随机排列
"""

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 总计35份测验文件
for quizNum in range(35):
    # 创建测验文件和答案文件
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w', encoding='utf-8')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w', encoding='utf-8')

    # 给测验文件编写头信息
    quizFile.write('姓名:\n\n学号:\n\n得分:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # 对问题进行随机排序
    states = list(capitals.keys())
    random.shuffle(states)

    # 对50个问题进行循环
    for questionNum in range(50):
        # 获取正确答案和错误答案
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # 将问题和答案写到试卷中
        quizFile.write(f'{questionNum + 1}. {states[questionNum]}的首府是哪里？\n')
        for i in range(4):
            quizFile.write(f' {"ABCD"[i]}. {answerOptions[i]}')
        quizFile.write('\n')
        # 将答案单独写入一个文件中
        answerKeyFile.write(f'{questionNum + 1}. {"ABCD"[answerOptions.index(correctAnswer)]}\n')
    quizFile.close()
    answerKeyFile.close()
