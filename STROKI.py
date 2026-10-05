

s = 'Здравствуйте, гости'
print(n := s.lower())
print(s.upper())      # все слова начинаются с большой буквы
print(s.capitalize()) # переменная начинается с большой буквы
print(s.rjust(40))    # переменная пишется в 40 знакоместах выравнивание по правому краю
print(s.ljust(40))   #
print(s.center(40))  # выравнивание по центру
print(s.strip())       # удаляем пробелы по краям
print(s.strip('! Зд'))
print(s.rstrip())   # убирает пробелы справа
print(s.lstrip())
#print(s.index(sub:'т',start 8,end ='11')) # поиск индекса
# символа или начала подстроки
#print(s.replace('т','LN')).replace(',',''))
ls = s.split() # создаёт список разделяя слова по запятой
ls = s.split(', ') # создает список разделяя слова по запятой с пробелом
print(ls)
print(", ".join(ls))
