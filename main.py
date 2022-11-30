
yemekler=["Çorba",15,"Kebap",60,"Salata",10,"Baklava",40]
icecekler=list(("Kola","Ayran","Şalgam","Soda"))


yemekler.insert(2,"İçli Köfte")
yemekler.append("Künefe")

yemekler.extend(icecekler)

yemekler.remove("Baklava")
yemekler.pop(2)
del yemekler[0]
yemekler.clear()

print(yemekler)
print(len(yemekler))
print(type(yemekler))
print(yemekler[1:])
