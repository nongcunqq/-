str = "http://www.westca.com/Yellow_Pages/place/place=8/本拿比/lang=schinese.html"

x = str.split('/')

print(x[-2])
print(x)

b = "/".join(x)
print(b)
