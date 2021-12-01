f = open('Day8.txt','r').read()
lines = f.split('\n')

flag = False

def check(index,accumulator):
    if index > len(lines)-1:
        global flag
        flag = True
        return
    doInstruction(index, accumulator)

instructions = []
def doInstruction(index, accumulator):
    instruction = lines[index]
    global instructions
    #print(instructions)
    if index in instructions:
        global flag
        flag = False
        #print(accumulator)
        return
    instructions.append(index)
    if instruction.startswith('nop'):
        check(index+1,accumulator)
    elif instruction.startswith('acc'):
        accumulator += int(instruction[4:])
        check(index+1,accumulator)
    elif instruction.startswith('jmp'):
        index += int(instruction[4:])
        check(index,accumulator)
    
def reset():
    f = open('Day8.txt','r').read()
    l = f.split('\n')
    global lines
    lines = l
    return

doInstruction(0,0)

for instruction in lines:
    reset()
    instructions = []
    if instruction.startswith('jmp'):
        lines[lines.index(instruction)] = 'nop' + instruction[3:]
        doInstruction(0,0)
    elif instruction.startswith('nop'):
        lines[lines.index(instruction)] = 'jmp' + instruction[3:]
        doInstruction(0,0)