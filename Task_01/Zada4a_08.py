# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no

n, m = int(input('Введите перове колличество долек: ')), int(
    input('Введите второе колличество долек: '))
k = int(input('Введите колличество долек, которое нужно отломить: '))

print(f'{n} {m} {k} -> yes' if (n * m - k) % 2 == 0 else f'{n} {m} {k} -> no')