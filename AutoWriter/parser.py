def parse(code):
    # Remove closing curly brackets
    # code = code.replace('}', '')

    # Remove indentation except for lines containing an opening bracket
    lines = code.split('\n')
    for i in range(len(lines)):
        if '{' in lines[i]:
            continue  # Skip lines containing an opening bracket
        lines[i] = lines[i].lstrip()

    # Remove blank lines from output
    lines = [line for line in lines if line.strip() != '']
    
    return '\n'.join(lines)

def israndomrandom(x):
    if(x<15):
        flag=False
        for i in range(2,x):
            if (x%i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    else:
        return False
    # check if flag is True
    if flag:
        return True
    else:
        return False