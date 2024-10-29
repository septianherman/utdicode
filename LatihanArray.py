arraybuah = ["apel","semangka","pisang"]
print("panjang array=",len(arraybuah),"\n")
print(arraybuah[1],"\n")
for x in arraybuah:
    print(x)

arraybuah.append("alpukat")
print(arraybuah[3])
arraybuah.pop(0)
print(arraybuah)
arraybuah.remove("pisang")
print(arraybuah)