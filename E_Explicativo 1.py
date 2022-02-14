'''listas-se puede almacenar todo tipo de dato'''
print("Inerta un elemento en la lista 'append'")
lista=[1,2,3,4,5]
lista.append(6) #Append(agrega el elemento al final de la lista)
lista.append("Estudiante")
print(lista)
print("")
print("Inserta un elemento en una posicion especifica 'insert'")
lista=[1,2,4,5]
lista.insert(2,3) #insert(indice,valor)--inserta un elemento en una posicion especifica
print(lista)
print("")
print("Unir listas 'extend'")
lista=[1,2,3,4,5]
lista.extend([6,7,8,9,10]) #extend(une o concatena con otra lista)
print(lista)
#otra forma de unir o concatenar listas
print("Unir listas 'lista2=lista+lista1'")
lista=[1,2,3,4,5]
lista1=[6,7,8,9,10]
lista2=lista+lista1
print(lista2)
print("")
#buscar un elemento dentro de la lista
print("Busqueda de una valor en la lista '3 in lista'")
lista=[1,2,3,4,5,"Roy"]
print(3 in lista)
print("")
#obtener el indice del elemento de una lista
print("Obtener el indice del elemento de una lista")
lista=[1,2,3,4,5,"Roy"]
print(lista.index(2))
print("")
#contar elementos repitidos
lista=[1,2,3,4,5,"Roy",1,2,3,"Roy",1,1,1]
print(lista.count(1))#count(indice)
#eliminar un elemento de la lista
lista=[1,2,3,4,5,"Roy"]
lista.pop()#sin parametros elimina el ultimo elemento
lista.pop(3)#pop(indice) eliminar el dato
lista.remove(5)#remove(valor)
lista.clear()#limpia la lista-elimina todo
print(lista)
lista.reverse()#invertir el orden de los elementos
lista.sort()#ordena la lista ascendentemente- solo si es puro numeros
lista.sort(reverse=True)#ordena la lista descendentemente- solo si es puro numeros