import types
from dis import dis

def test():
    c = compile(open("bytecode.py").read(), '<string>', 'exec')
    fn_code = c.co_consts[5]
    ex_code = c.co_consts[7]
    dis(fn_code)
    bytecode = fn_code.co_code
    bytecode = replace_op(bytecode, 4, "\x13")
    print(bytecode)
    print("="*30)
    dis(ex_code)
    print(ex_code.co_code)
    # bytecode[3] = 
    b = write_to_bytecode(c, fn_code, bytecode)
    dis(b)
    exec(b)

def roots(a,b,c):
    d = b*2 - (4*a*c)
    if d < 0: return None
    r_1 = (-b+sqrt(b**2 + 4*a*c))/(2*a)
    r_2 = (-b-sqrt(b**2 - 4*a*c))
    return (r_1, r_2)

def ex():
    d = 2**a

def replace_op(bytecode, index, new):
    return bytecode[0:index] + bytes(new, "utf-8") + bytecode[index+1:]
    
def write_to_bytecode(code, fn_code, new_bytes):
    return types.CodeType(fn_code.co_argcount, code.co_kwonlyargcount, code.co_posonlyargcount,
                          fn_code.co_nlocals, fn_code.co_stacksize, fn_code.co_flags,
                          new_bytes, fn_code.co_consts, fn_code.co_names,
                          fn_code.co_varnames, fn_code.co_filename, fn_code.co_name, fn_code.co_firstlineno,
                          fn_code.co_lnotab, fn_code.co_freevars, fn_code.co_cellvars)

test()
