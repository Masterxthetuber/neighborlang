tape = [0] * 16
pointer = 0
program = []
ip = 0
ret = None
'''
start of loop
'''
while 0 <= ip < len(program):
    oper = program[ip]
    #goto
    if isinstance(oper, int):
        ret = ip + 1
        ip = oper
        continue
    elif oper == "r":
        if ret != None:
            ip = ret
            continue
        pass
    #standard stuff
    elif oper == ">":
        pointer += 1
        print(tape)
    elif oper == "<":
        pointer -= 1
        print(tape)
    elif oper == "+":
        tape[pointer] += 1
        print(tape)
    elif oper == "-":
        #new stuff
        tape[pointer] -= 1
        print(tape)
    elif oper == "#":
        tape[pointer] = 0
        print(tape)
    elif oper == "?":
        if pointer > 0 and tape[pointer - 1] == tape[pointer]:
            tape[pointer] += 1
            print(tape)
        else:
            tape[pointer] -= 1
            print(tape)
    elif oper == "/":
        if pointer > 0 and tape[pointer - 1] != tape[pointer]:
            tape[pointer] += 1
            print(tape)
        else:
            tape[pointer] -= 1
            print(tape)
    elif oper == ";":
        if pointer < len(tape) - 1 and tape[pointer + 1] == tape[pointer]:
            tape[pointer] += 1
            print(tape)
        else:
            tape[pointer] -= 1
            print(tape)
    elif oper == ":":
        if pointer < len(tape) - 1 and tape[pointer + 1] != tape[pointer]:
            tape[pointer] += 1
            print(tape)
        else:
            tape[pointer] -= 1
            print(tape)
    elif oper == "*":
        tape[pointer] += tape[pointer - 1]
        print(tape)
    elif oper == "&":
        tape[pointer] += tape[pointer + 1]
        print(tape)
    elif oper == "^":
        tape[pointer] -= tape[pointer - 1]
        print(tape)
    elif oper == "%":
        tape[pointer] -= tape[pointer + 1]
    else:
        raise ValueError("invalid")
    ip += 1
