def multiplica(a,b):
	return a*b
# variables y strings
a=5
for i in range(5):
	print(str(i)+'*'+str(a)+'='+str(multiplica(i,a)))
# tuplas (inmutables) === array inmutable
b=(1,2,4,5)
print(b[1])
# listas === array enumerado
c=[1,2,4,5]
c[2]=8
print(c)
# diccionario === array asociativo
d={ '1':"texto", 'cuatro':'texto2', 'lista':c}
print(d)