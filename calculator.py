def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("간단한 계산기입니다.")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("q. 종료")

    while True:
        choice = input("\n선택하세요 (1/2/3/4/q): ")

        if choice == 'q':
            print("계산기를 종료합니다.")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("첫 번째 숫자를 입력하세요: "))
                num2 = float(input("두 번째 숫자를 입력하세요: "))
            except ValueError:
                print("유효한 숫자가 아닙니다. 다시 시도해주세요.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error: Division by zero":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    calculator()
