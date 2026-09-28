# List
# ====
# ________________________________________________________________.
# list is a collection in python that supports heterogeneous data |
# list is mutable                                                 |
# insertion order is preserved                                    |
# duplicates are allowed                                          |
# ________________________________________________________________|
lst=[101,102,103]
l1=[101,"hi",25.9]
print(lst)
print(l1)

# Using append function we can add elements to exsisting list
# -----------------------------------------------------------
lst=[105]
print(lst)
lst.append(100)
print(lst)

print(l1[1])
l1[1]="tessa" #modification
print(l1)
print(l1[-2])
print(l1[1:])
