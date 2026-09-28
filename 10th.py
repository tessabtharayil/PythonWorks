# Tuple
# =====
t=() #empty
t=(10,20,30,40)
print(t)
print(t[1])

#t[1]=30  #invalid (immutable)

t=(10,"102",[10,20])  #heterogeneous
print(t)
t=t+(100,)
print(t)


