h='pop、no、zip、zotz、tzec、xul、yoxkin、mol、chen、yax、zac、ceh、mac、kankin、muan、pax、koyab、cumhu、uayet'.split('、')
t1='imix、ik、akbal、kan、chicchan、cimi、manik、lamat、muluk、ok、chuen、eb、ben、ix、mem、cib、caban、eznab、canac、ahau'.split("、")
k=range(1,14)
def find():
    l=input().split()
    day=365*int(l[2])
    i=h.index(l[1])
    day+=i*20+int(l[0][:-1])+1
    y=day//260
    d=day%260
    d_1=d%20-1
    d_2=d%13-1
    if d==0:
        y-=1
    print(f'{k[d_2]} {t1[d_1]} {y}')
n=int(input())
print(n)
for i in range(n):
    find()
