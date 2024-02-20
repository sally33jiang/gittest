num_str  = '''800.00,
-3.00,
-8000.00,
8.00,
3.00,
-1000.00'''

b=num_str .split(",")


# 使用split()函数将字符串按逗号分割，然后转换为列表
num_list = [float(num) for num in num_str.split(",")]

123

# 求和
sum = sum(num_list)

print(sum)  # 输出：15



