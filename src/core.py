def eval_condition(cond_str, context):
    ops = ["==", "!=", ">=", "<=", ">", "<"]
    for op in ops:
        if op in cond_str:
            left, right = map(lambda x: x.strip(), cond_str.split(op))
            lval = eval_expression(left, context)
            rval = eval_expression(right, context)
            return eval(f"{repr(lval)} {op} {repr(rval)}")
    return False
import re

def eval_expression(expr, context):
    expr = expr.strip()

    if expr.startswith('"') and expr.endswith('"'):
        return expr[1:-1]
    if expr == "true": return True
    if expr == "false": return False
    if expr.isdigit(): return int(expr)
    if re.match(r'\d+\.\d+', expr): return float(expr)
    if expr.startswith('[') and expr.endswith(']'):
        inner = expr[1:-1]
        parts = [eval_expression(x.strip(), context) for x in inner.split(',')]
        return parts

    if expr.startswith("IF("):
        inner = expr[3:].strip("()")
        cond, val_true, val_false = map(lambda x: x.strip(), split_args(inner))
        condition_result = eval_condition(cond, context)
        return eval_expression(val_true, context) if condition_result else eval_expression(val_false, context)

    match = re.match(r'(\w+)\((.*?)\)', expr)
    if match:
        func_name, args_str = match.groups()
        args = split_args(args_str)
        evaled_args = [eval_expression(arg.strip(), context) for arg in args]
        if func_name in BUILTIN_FUNCTIONS:
            return BUILTIN_FUNCTIONS[func_name](*evaled_args)

    if expr in context:
        return context[expr]["value"]

    raise Exception(f"Unknown expression: {expr}")

def eval_expression(expr, context):
    expr = expr.strip()

    if expr.startswith('"') and expr.endswith('"'):
        return expr[1:-1]
    if expr == "true": return True
    if expr == "false": return False
    if expr.isdigit(): return int(expr)
    if re.match(r'\d+\.\d+', expr): return float(expr)
    if expr.startswith('[') and expr.endswith(']'):
        inner = expr[1:-1]
        parts = [eval_expression(x.strip(), context) for x in inner.split(',')]
        return parts

    if expr.startswith("IF("):
        inner = expr[3:].strip("()")
        cond, val_true, val_false = map(lambda x: x.strip(), split_args(inner))
        condition_result = eval_condition(cond, context)
        return eval_expression(val_true, context) if condition_result else eval_expression(val_false, context)

    match = re.match(r'(\w+)\((.*?)\)', expr)
    if match:
        func_name, args_str = match.groups()
        args = split_args(args_str)
        evaled_args = [eval_expression(arg.strip(), context) for arg in args]
        if func_name in BUILTIN_FUNCTIONS:
            return BUILTIN_FUNCTIONS[func_name](*evaled_args)

    if expr in context:
        return context[expr]["value"]

    raise Exception(f"Unknown expression: {expr}")


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

def builtin_joinTO(*args): return ''.join(map(str, args))
def builtin_len(x): return len(x)
def builtin_sum(x): return sum(x)
def builtin_upper(x): return str(x).upper()
def builtin_lower(x): return str(x).lower()

BUILTIN_FUNCTIONS = {
    "JoinTO": builtin_joinTO,
    "len": builtin_len,
    "sum": builtin_sum,
    "upper": builtin_upper,
    "lower": builtin_lower,
}

def parse_nom(text):
    context = {}
    pattern = r'(\w+)\s*:\s*(.+?)\s*->\s*(\w+),?'

    matches = re.findall(pattern, text)
    for key, raw_value, typ in matches:
        value = eval_expression(raw_value, context)
        context[key] = {
            "value": value,
            "type": typ
        }
    return context
