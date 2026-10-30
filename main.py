#Problem 5 — En Uzun Artan Ardışık Dizi

#Kullanıcıdan 10 adet tam sayı al ve bir listede sakla.

#Programın:

#Listedeki en uzun kesintisiz artan sayı dizisini bulsun.
#Bu dizinin kaç elemandan oluştuğunu yazdırsın.
#Bu dizinin ortalamasını hesaplasın.

li = []
q = 0

while True:
    if q <= 9:
        n = int(input(f"lütfen {q+1}. sayıyı giriniz"))
        li.append(n)
        q +=1
        print(li)
    else:
        break

di = []

for i in range(9):

    if li[i] < li[i+1]:
        di.append(li[i])
    elif li[i] > li[i+1]:
        di.append(li[i+1])


if li[9] > li[8]:
    di.append(li[9])


p=1

f = {}
d = len(di)

for s in range(d-1):
    
    if di[s]> di[s+1]:
        f[p] = di[:s+1]
        di = di[s+1:]
        d = len(di)
        p +=1
        
    
        
print(f)
