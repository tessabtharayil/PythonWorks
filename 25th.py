#                   Types of Functional Arguments
#                   =============================
# Positional arguments
# ====================
def fun1(n,a):
    print("Name is",n)
    print("Age is",a)
fun1('arun',23)
# fun(23,'arun')   # logical error
# fun(23)          # error

# Keyword Argument
# ================
def fun2(n,a):
    print("Name is",n)
    print("Age is",a)
fun2(a=23,n='arun')
# fun2(n='arun',a=23) # This is also valid

# Default Arguments
# =================
def fun3(n,a=23):
    print("Name is",n)
    print("Age is",a)
fun3('arun',25)
# fun3('arun') # default age value is used

# Arbitary/Variable length arguments
# ==================================
# Arbitary positional arguments(*args)
# ------------------------------------
def fun4(*args):
    print(args)
fun4(10,20)
fun4(10,20,30)
fun4(1,2,3,4,5)

# Arbitary keyword arguments(**kwargs)
# ------------------------------------
def fun5(**kwargs):
    print(kwargs)
fun5(a=10,b=20)
fun5(a=10,b=20,c=30)
fun5(a=1,b=2,c=3,d=4,e=5)

# Define a function to find the sum of numbers using arbitary argument type
# -------------------------------------------------------------------------
def fun6(*args):
    sum=0
    for i in args:
        sum+=i
    print("Sum is",sum)
fun6(10,20)
fun6(1,2,3,4,5)



