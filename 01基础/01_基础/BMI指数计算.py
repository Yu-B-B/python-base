# BMI指数计算
# BMI = weight / height ^ 2
height = float(input("请输入升高："))
weight = float(input("请输入体重："))

sys_bmi = weight / height ** 2

# print(f"身高为：{height},体重为：{weight},BMI指数为：{sys_bmi}")
print(f"身高为：{height}", end="")
print(f"体重为：{weight}", end="")
print("BMI指数为：%.2f" % sys_bmi)
