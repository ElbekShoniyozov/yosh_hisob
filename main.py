from datetime import datetime

year = datetime.now().year
now=year
f1=input("1-Foydalanuvchi Ismingizni kiririting:  ")
y1=int(input("Tug'ulgan yilingizni kiriting:  "))
yosh1=now-y1

f2=input("2-Foydalanuvchi Ismingizni kiriting:  ")
y2=int(input("Tug'ulgan yilingizni kiriting:  "))
yosh2=now-y2
katta=yosh1-yosh2
kichik=yosh2-yosh1
print(f1,"siz", yosh1, 'yoshdasiz!')
print(f2,"siz", yosh2, 'yoshdasiz!')
if yosh1>yosh2:
    print(f1, 'siz', f2+'dan', katta,'yosh kattasiz!')
elif yosh1<yosh2:
    print(f1, "siz", f2+'dan', kichik, 'yosh kichkinasiz!' )

print("Dasturdan foydalanganinggiz uchun tashakkur!")
