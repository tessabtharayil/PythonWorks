# Set
# ===
s={1,2,3,4}
s.add(5)
print(s)
s.update((6,7,8,5))
print(s)
s.remove(6)
print(s)
s.discard(5)
print(s)
s.pop()
print(s)
print()

s={1,2,3}
t={3,4,5}
print(s.union(t))
print(s.intersection(t))
print(s.difference(t))
print(s.symmetric_difference(t))
print()

#1). Given a list l=[1,1,2,3,3,4]
# remove the duplicates
# -------------------------------
l=[1,1,2,3,3,4]
s=set(l)
print(s)

#2). Given a list l=[1,1,2,3,3,4]
# remove the duplicates without using set() (order should be preserved)
# ---------------------------------------------------------------------
l=[1,1,2,3,3,4]
new=[]
for i in l:
    if i not in new:
        new.append(i)
print(new)

#3). Given 2 lists l1=[13,27,30,42,57] and l2=[13,57,89,33,80]
# find the common elements
# ------------------------------------------------------------
l1=[13,27,30,42,57]
l2=[13,57,89,33,80]
s1=set(l1)
s2=set(l2)
print("Common elements are",s1.intersection(s2))