def get_cycle(symbol):
    if symbol in cycles_dict: return cycles_dict[symbol]
    res = [0]
    op = equations_dict[symbol].split("(")[0]
    oprand1 = equations_dict[symbol].split("(")[1][0]
    oprand2 = equations_dict[symbol][-2]

    cycle1 = get_cycle(oprand1)
    cycle2 = get_cycle(oprand2)

    if symbol in cycles_dict: return cycles_dict[symbol]

    for x,y in zip(cycle1, cycle2):
        res.append(operator_fns[op](x,y))
    
    cycles_dict[symbol] = res[:t]
    
    return cycles_dict[symbol]


operator_fns = {
    "XOR": lambda x, y: x ^ y,
    "NOR": lambda x, y: int(not (x | y)),
    "NAND": lambda x, y: int(not (x & y)),
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
}
equations_dict = {}
cycles_dict = {}

n = int(input().upper())
for _ in range(n):
    symbol, equation = input().upper().split("=")
    equations_dict[symbol] = equation

t = int(input().upper())
while True:
    line = input().upper().split()
    if len(line) == 1: 
        target = line[0]
        break
    symbol = line[0]
    cycles_dict[symbol] = list(map(int, line[1:]))

for n in get_cycle(target):
    print(n, end=" ")
print()
# print(cycles_dict)