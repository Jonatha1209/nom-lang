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
