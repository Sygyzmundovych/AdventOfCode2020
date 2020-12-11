
def calculate_bruteforce(input, target) -> int:
    result = 0
    for i in input:
        for j in input:
            if (int(i)+int(j)==target):
                print(f"i={i} and j={j}")
                result = int(i)*int(j)
    return result

def calculate_smarter(input, target) -> int:
    result = 0
    input_j = input.copy()
    for i in input:
        input_j.remove(i)
        print(i, input_j)
        for j in input_j:
            if (int(i)+int(j)==target):
                print(f"i={i} and j={j}")
                result = int(i)*int(j)
                return result

data=open("./aoc_2001_test.txt").read().splitlines()

print(f"Brute-force: {calculate_bruteforce(data, 2020)}\n")
print(f"Smart: {calculate_smarter(data, 2020)}\n")