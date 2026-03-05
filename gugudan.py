def print_gugudan():
    print("구구단 출력")
    for step in range(1, 20, 4):
        headers = [f"--- {i}단 ---" for i in range(step, min(step + 4, 10))]
        print("\t".join(headers))
        for j in range(1, 10):
            row = [f"{i} x {j} = {i * j:<2}" for i in range(step, min(step + 4, 10))]
            print("\t".join(row))
        print()

if __name__ == "__main__":
    print(__name__)
    print_gugudan()
