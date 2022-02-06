import Fourcal

print("리셋하기 전까지 결과값은 num1에 저장됩니다. 걊을 초기화 하려면 'reset을 입력하세요. 프로그램을 종료하려면 'end'를 입력하세요.")
num1 ,action, num2 = input().split()
num1= int(num1)
num2 = int(num2)
result = Fourcal.fourcal(num1, num2)
#값 입력 및 지정 완료

while(action != 'end'):
    
    if action == '+':
        print(result.add())
        try:
            action, num2 = input().split()
        except ValueError:
            pass
        num2 = int(num2)
        result.num2 = num2
    elif action == '-':
        print(result.min())
        action, num2 = input().split()
        num2 = int(num2)
        result.num2 = num2
    elif action == '*':
        print(result.mul())
        action, num2 = input().split()
        num2 = int(num2)
        result.num2 = num2
    elif action == '/':
        print(result.div())
        action, num2 = input().split()
        num2 = int(num2)
        result.num2 = num2
    elif action == 'reset':
        print("초기화 되었습니다. 수식을 다시 입력해주세요.")
        num1, action, num2 = input().split()
        num1 =int(num1)
        num2 = int(num2)
        result = Fourcal.fourcal(num1, num2)
