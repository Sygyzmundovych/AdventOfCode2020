
def is_policy_valid(letter: str, pos1: int, pos2: int, password: str) -> bool:
    occur = 0
    if (password[pos1-1]==letter) : occur+=1
    if (password[pos2-1]==letter) : occur+=1
    return (occur==1)

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