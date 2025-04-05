import re
from eval_expr import eval_expression

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
