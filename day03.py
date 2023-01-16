subjects = ' $ python, data structure, database    $$$'
print(subjects.title())
print(subjects.count('data'))
print(subjects.rfind('data'), subjects.rindex('data'))
print(subjects.find('data'), subjects.index('data'))
print(subjects.find('inha'))  # -1 return
# print(subjects.index('inha'))  # Exception!

# subjects = ' $ python, data structure, database    $$$'
# print(subjects.strip('$'))
#
# inha = 'a duck goes into a sea'
# print(inha.replace('a', 'a nice'))
#
# pokemons_list = ['피카츄', '꼬부기', '이상해', '파이리']
# pokemons_string = '/'.join(pokemons_list)
# print(pokemons_string)
#
# univ = 'Inha University'
# print(univ.split())
#
# print(len(univ))
# print(univ[-10:-6])
# print(univ[5:-6])
# print(univ[::2])
# print(univ[5:])
# print(univ[5:15])
# print(univ[-10:])
#
