# v0.2
import random

# def calculate_fee(*args):

def calculate_fee(args) -> list:
    """
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: [전체 인원 수, 어른 수, 아이 수, 지불할 총 입장료]
    """
    total = 0
    adults = 0
    kids = 0
    for age in args:
        if 19 <= age:  # adult
            total = total + 10000
            adults = adults + 1
        else:
            total = total + 3000
            kids = kids + 1
    return [len(args), adults, kids, total]


no_of_visitor = int(input('몇 분 이세요? '))
ages = [random.randint(1, 60) for age in range(no_of_visitor)]
results = calculate_fee(ages)
print(f'{results[0]}명 방문 하셨고 어른 {results[1]}명, 아이 {results[2]}명 총 요금은 {results[-1]}원 입니다')
