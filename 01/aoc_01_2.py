
def calculate_bruteforce(input, target) -> int:
    result = 0
    for i in input:
        for j in input:
            for k in input:
                if (int(i)+int(j)+int(k)==target):
                    print(f"i={i} and j={j} and k={k}")
                    result = int(i)*int(j)*int(k)
    return result

def calculate_smarter(input, target) -> int:
    result = 0
    input_j = input.copy()
    
    for i in input:
        input_j.remove(i)
        input_k = input_j.copy()
        for j in input_j:
            input_k.remove(j)
            for k in input_k:
                if (int(i)+int(j)+int(k)==target):
                    print(f"i={i} and j={j} and k={k}")
                    result = int(i)*int(j)*int(k)
                    return result

data=open("./aoc_2001_prod.txt").read().splitlines()

print(f"Brute-force: {calculate_bruteforce(data, 2020)}\n")
print(f"Smart: {calculate_smarter(data, 2020)}\n")