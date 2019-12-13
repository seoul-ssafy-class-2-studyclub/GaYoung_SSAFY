x = -4
y = 13
# print(x//y)
# print(x/y)
a = y % (-x)
print(a)
b = y % abs(-x)
print(b)


NUM -4
DIV
END
2
13
-13

NUM 4
DIV
END
2
13
-13

NUM -4
MOD
END
2
13
-13

NUM 4
MOD
END
2
13
-13

QUIT