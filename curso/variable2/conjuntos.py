#crear un conjunto con set()
conjunto = set(["dato1", "dato2"])

#meter un conjunto dentro de otro conjunto
conjunto1 = frozenset({"dato3", "dato4"})
conjunto2 = {"dato5", conjunto1}

print(conjunto2)

#teoria de conhjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {1, 2, 3, 4, 5}

#verificar si es un subconjunto
resultado = conjunto_a.issubset(conjunto_b)
resultado = conjunto_a <= conjunto_b

#verificar si es un superconjunto
resultado = conjunto_b.issuperset(conjunto_a)
resultado = conjunto_b > conjunto_a

#verificar si los conjuntos son disjuntos (no tienen elementos en comun)
resultado = conjunto_a.isdisjoint(conjunto_b)

print(resultado)