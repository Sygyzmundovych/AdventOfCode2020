
def is_policy_valid(letter: str, min: int, max: int, password: str) -> bool:
    occur = 0
    for i in range(0,len(password)):
        if (password[i]==letter) : occur+=1
    return occur in range(min, max+1)

def calculate_bruteforce(input) -> int:
    result = 0
    for i in input:
        minmax, letter, pwd = i.split()
        min, max=minmax.split('-')
        letter=letter[0]
        if is_policy_valid(letter, int(min), int(max), pwd): result+=1
    return result

data=open("./aoc_2002_prod.txt").read().splitlines()

print(f"Brute-force: {calculate_bruteforce(data)}\n")