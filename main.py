import RuleParser

def main():
    lossList = {}   #case 별 처리를 위한 장치 목록
    rules = []      #Rule에 대한 반환값
    goal = []       # gola 지정
    #loading rule txt
        # '#' : lossList의 목록 나열
        # '+' : 각 LossList가 가질수 있는 값
        # if ~ then : Rule
        # '/' : goal 지정

    lostList, rules, goal = RuleParser.RuleRead('.\\Case\\Case_ANSI.txt')


if __name__ == '__main__':
    main()