from eval_expr import eval_expression

def eval_condition(cond_str, context):
    ops = ["==", "!=", ">=", "<=", ">", "<"]
    for op in ops:
        if op in cond_str:
            left, right = map(lambda x: x.strip(), cond_str.split(op))
            lval = eval_expression(left, context)
            rval = eval_expression(right, context)
            return eval(f"{repr(lval)} {op} {repr(rval)}")
    return False
