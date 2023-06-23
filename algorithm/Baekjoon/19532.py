a,b,c,d,e,f = map(int,input().split())
x = (b*f - e*c)//(d*b - a*e)
y = (a*f - c*d)//(a*e - b*d)
print(x, y)