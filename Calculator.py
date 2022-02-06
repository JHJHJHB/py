import Fourcal

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
result = Fourcal.fourcal(num1, num2)
#값 입력 및 지정 완료
print("리셋하기 전까지 결과값은 num1에 저장됩니다.")

#어떤 연산을 할것인지 결정
action = int(input("1.add 2.min 3.mul 4.div 0.reset 99.End\n"))
while(action != 99):
    
    if action == 1:
        print(result.add())
        num2 = int(input("Num2: "))
        result.num2 = num2
    elif action == 2:
        print(result.min())
        num2 = int(input("Num2: "))
        result.num2 = num2
    elif action == 3:
        print(result.mul())
        num2 = int(input("Num2: "))
        result.num2 = num2
    elif action == 4:
        print(result.div())
        num2 = int(input("Num2: "))
        result.num2 = num2
    elif action == 0:
        print("값을 초기화 합니다. Num1과 Num2를 다시 입력해주세요.")
        num1 = int(input("Num1: "))
        num2 = int(input("Num2: "))
    action = int(input("1.add 2.min 3.mul 4.div 0.reset 99.End\n"))
