n=int(input())
p=0
h=n
while h>0:
 digit =h%10
 p += digit ** 3
 h //=10
if n==p:
 print("yes")
else:
 print("no")
