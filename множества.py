#n = 10
#m = 100

#print('первая переменная -', n, ', Вторая переменная -', m, 'm/n =', m//n)


#print('первая переменная - "%d", Вторая переменная - "%d", m/n = "%d"'%(n,m, m//n))
#print('первая переменная - "{}", Вторая переменная - "{}", m/n = "{}"'. format(n,m, m//n))
#print(f'первая переменная - {n}, Вторая переменная - {m}, m/n = "{m // n}"')


##""Множество (set) неупорядоченный набор уникальных объектов ""
##(любые неизменяемые типы данных)

ls = [22, 22, 22, 33, 44]
st = set(ls)
print(st)
st.clear()
st = {22, 33, 44}
print(st)

st.add(100)               # добавляет один объект
st.update({2, 3})
print(st)
n = st.pop()
st.remove(3)               # Выполняют одну и ту же задачу
st.discard(2)             # не останавливает не выдаёт ошибку удаляет только то что указано
print(n)
print(st)

#for i in st:
#    print(i)

st1 = {3, 4, 33}
st2 = {3, 4, 44}

#res = st1.union(st2)      # Объединение множества
res = st1 | st2

res = st1.intersection(st2)      #  пересечение множеств
res = st1 & st2                  # альтернативное выражение

res = st1.difference(st2)       # Вычетание множеств
res = st2 - st1
res = st1.symmetric_difference(st2)
res = st1 ^ st2                     #альтернативное выражение
print(res)

st3 = {3, 4}
print(st3.issubset(st2))
print(st1.issuperset(st3))
