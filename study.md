# Python Study Record

## 字符串逆置

给定一个字符串，然后将其翻转，逆序输出。

### 使用字符串切片

```python
print(str[::-1])
```

### 使用 reversed()

```python
print(''.join(reversed(str)))
```

## Python ASCII 码与字符相互转换

```python
c = input("请输入一个字符: ")
a = int(input("请输入一个ASCII码: "))
print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))
```

## range() 函数

函数语法

```python
range(stop)
range(start, stop[, step])
```

实例

```python
list(range(0, 30, 5))
# [0, 5, 10, 15, 20, 25]
list(range(0, 10, 2))
# [0, 2, 4, 6, 8]
list(range(0, -10, -1))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
list(range(1, 0))
# []
```

## unittest 模块中的断言方法

| 方法                    | 用途                   |
| ----------------------- | ---------------------- |
| assertEqual(a, b)       | 核实 a == b            |
| assertNotEqual(a, b)    | 核实 a != b            |
| assertTrue(x)           | 核实 x 为 True         |
| assertFalse(x)          | 核实 x 为 False        |
| assertIn(item, list)    | 核实 item 在 list 中   |
| assertNotIn(item, list) | 核实 item 不在 list 中 |
