g,h=map(int,input().split())
for n in range(g,h+1):
 order=len(str(n))
 f=0
 v=n
 while v>0:
  digit =v%10
  f +=digit ** 3
  v //=10
 if n==f:
  print(n,end=" ")
