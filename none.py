"""Behind the scenes, Python adds return None to the end of any function
definition with no return statement. This is similar to how a while or for
loop implicitly ends with a continue statement. Also, if you use a return
statement without a value (that is, just the return keyword by itself), then
None is returned.
"""
spam = print('Hello!')

if spam is None:
    print('This is true')

