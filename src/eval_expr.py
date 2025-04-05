import re
from builtin import BUILTIN_FUNCTIONS
from eval_cond import eval_condition
from split_args import split_args

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
