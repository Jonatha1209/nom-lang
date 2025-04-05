def split_args(s):
    depth, current, args = 0, '', []
    for c in s:
        if c == ',' and depth == 0:
            args.append(current.strip())
            current = ''
        else:
            if c == '(' or c == '[': depth += 1
            if c == ')' or c == ']': depth -= 1
            current += c
    if current: args.append(current.strip())
    return args
