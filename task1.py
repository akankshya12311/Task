a=[[1,2,3]]
r=[[e1,e2,e3] for e1 in a[0] for e2 in a[0] for e3 in a[0] if e1!=e2 and e1!=e3 and e2!=e3]
print(r)
