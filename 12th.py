# Dictionary
# ==========
# _____________________________________________.
# It is a collection of items (key:value pair) |
# _____________________________________________|
d={'id':100,'name':'tessa','place':'vazhakulam'}
print(d)
d['name']='athulya'
print(d)
d['prof']='doctor'
print(d)
d['mark']=30
d['mark']=35
print(d)
d['mark1']=35
print(d)

#1). Create a dictionary
# add salary as a new key value pair
# modify value of prof
# ----------------------------------
d={'id':100,'name':'tessa','age':21,'prof':'engineer','place':'vazhakulam'}
print(d)
d['salary']=25000
print(d)
d['prof']='developer'
print(d)

print(d['name'])
print(d.values())
print(d.keys())
print(d.items())