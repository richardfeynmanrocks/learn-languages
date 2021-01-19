def test():
    file = open("bytecode.py")
    a = file.read()
    c = compile(a, '<string>', 'exec')
    fn_code = c.co_consts[0] # Pick up the function code from the main code
    print (c.co_consts)
    from dis import dis
    dis(fn_code)

def write_to_bytecode(code):
    return types.CodeType(fn_code.co_argcount,
                          c.co_kwonlyargcount,  # Add this in Python3
                          c.co_posonlyargcount, # Add this in Python 3.8+
                          fn_code.co_nlocals,
                          fn_code.co_stacksize,
                          fn_code.co_flags,
                          x,  # fn_code.co_code: this you changed
                          fn_code.co_consts,
                          fn_code.co_names,
                          fn_code.co_varnames,
                          fn_code.co_filename,
                          fn_code.co_name,
                          fn_code.co_firstlineno,
                          fn_code.co_lnotab,   # In general, You should adjust this
                          fn_code.co_freevars,
                          fn_code.co_cellvars)
                          
    
test()
# print("=" * 30)

# x = fn_code.co_code[6:16] # modify bytecode

# import types
# opt_fn_code = types.CodeType(fn_code.co_argcount,
#                              c.co_kwonlyargcount,  # Add this in Python3
#                              c.co_posonlyargcount, # Add this in Python 3.8+
#                              fn_code.co_nlocals,
#                              fn_code.co_stacksize,
#                              fn_code.co_flags,
#                              x,  # fn_code.co_code: this you changed
#                              fn_code.co_consts,
#                              fn_code.co_names,
#                              fn_code.co_varnames,
#                              fn_code.co_filename,
#                              fn_code.co_name,
#                              fn_code.co_firstlineno,
#                              fn_code.co_lnotab,   # In general, You should adjust this
#                              fn_code.co_freevars,
#                              fn_code.co_cellvars)
# dis(opt_fn_code)
# print("=" * 30)
# print("Result is", eval(fn_code))
# #print("Result is", eval(opt_fn_code))

# # Now let's change the value of what's returned
# co_consts = list(opt_fn_code.co_consts)
# co_consts[-1] = 10

# opt_fn_code = types.CodeType(fn_code.co_argcount,
#                              # c.co_kwonlyargcount,  Add this in Python3
#                              # c.co_posonlyargcount, Add this in Python 3.8+
#                              fn_code.co_nlocals,
#                              fn_code.co_stacksize,
#                              fn_code.co_flags,
#                              x,  # fn_code.co_code: this you changed
#                              tuple(co_consts), # this is now changed too
#                              fn_code.co_names,
#                              fn_code.co_varnames,
#                              fn_code.co_filename,
#                              fn_code.co_name,
#                              fn_code.co_firstlineno,
#                              fn_code.co_lnotab,   # In general, You should adjust this
#                              fn_code.co_freevars,
#                              fn_code.co_cellvars)

# dis(opt_fn_code)
# print("=" * 30)
# print("Result is now", eval(opt_fn_code))
