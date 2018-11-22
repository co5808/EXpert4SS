#-*- coding: utf-8 -*-
#import codecs      #인코딩이 utf-8로 되어있을 때 사용되는 라이브러리

path = '.\\Case\\Case_ANSI.txt'

def RuleRead(path):
    lossList = {}
    rules = []
    goal = []
    try:
        with open(path, 'r') as f:
        #with codecs.open(path, 'r', "utf-8") as f:
            lines = f.readlines()
    except:
        print("Can't find file " + path)
        return

    for line in lines:
        print(line)
        if line.startswith('#'):
            for fact in line[1:-1].split(' '):
                print(fact)
                lossList.setdefault(fact, [])

        if line.startswith('+'):
            factName, factList = line[1:].split('=')
            lossList[factName.split(' ')[0]].extend(factList.strip().split(' '))

        if line.startwith('-'):
            goal.extend(line[1:].strip().split(" "))

        if line[:2] == "--":
            print("Input Rules")

        if line.startswith('if'):
            sides = line.replace('if', ' ').split('then')
            print(sides)
            current = {}
            current['LHS'] = sides[0].strip()
            current['RHS'] = sides[1].replace('\\n', '\n')
            rules.append(current)
            
    return lossList, rules, goal


test = RuleRead(path)