# Arquivo.py

# =========================================
# BOOLEANOS
# =========================================

# TRUE
# FALSE

print(1 == '1')
print(2 > 1)
print(2 < 1)
print(bool(2 == 2))
print(bool(0))
print(bool(' '))
print(bool(None))


# =========================================
# OPERAÇÕES
# =========================================

# ==  igual
# !=  diferente que
# <   menor
# >   maior
# <=  menor igual
# >=  maior igual


# =========================================
# OPERAÇÕES COM BOOL
# =========================================

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # TRUE

c = a

print(a is b)  # False
print(a is c)  # True

print(id(a))
print(id(b))
print(id(c))