import random

def random_split_non_zero(total):
    """将一个数随机拆分为两个非零数的和"""
    if isinstance(total, int):
        # 生成1到total-1之间的整数
        num1 = random.randint(1, total - 1)
    else:
        # 生成一个接近0但不为0的随机浮点数
        num1 = random.uniform(0.0001, total - 0.0001)

    num2 = total - num1
    return num1, num2

# 大衍之数初始化
dayanzhishu = 50
dayanzhishu = dayanzhishu - 1  # 其用四十有九

# 存储六爻的结果
yao_list = []

print("开始大衍之数卜卦过程...")

# 六爻，每爻三变
for i in range(6):
    print(f"\n第{i+1}爻开始")
    current_number = dayanzhishu
    gua_le_sum = 0  # 挂扐数累计
    
    # 三变过程
    for j in range(3):
        print(f"  第{j+1}变:")
        
        # 第一变：分二
        tian, di = random_split_non_zero(current_number)
        tian = int(tian)
        di = int(di)
        print(f"    分二: 天={tian}, 地={di}")
        
        # 挂一
        di = di - 1
        print(f"    挂一: 地={di}")
        
        # 揲四归奇
        tian_remainder = tian % 4
        di_remainder = di % 4
        
        # 归奇：如果余数为0，则取4
        if tian_remainder == 0:
            tian_remainder = 4
        if di_remainder == 0:
            di_remainder = 4
        
        remainder = tian_remainder + di_remainder
        gua_le_sum += remainder
        
        print(f"    揲四归奇: 天余={tian_remainder}, 地余={di_remainder}, 挂扐={remainder}")
        
        # 计算下一变的数
        current_number = current_number - remainder
        print(f"    剩余: {current_number}")
    
    # 计算爻值
    yao_value = current_number // 4
    print(f"  挂扐累计: {gua_le_sum}, 爻值计算: {current_number}//4 = {yao_value}")
    
    # 根据挂扐数确定爻的性质
    if gua_le_sum == 24:
        yao = 6  # 老阴
    elif gua_le_sum == 20:
        yao = 7  # 少阳
    elif gua_le_sum == 16:
        yao = 8  # 少阴
    elif gua_le_sum == 12:
        yao = 9  # 老阳
    else:
        yao = yao_value  #  fallback
    
    yao_list.insert(0, yao)  # 从下往上排爻
    print(f"  确定爻值: {yao}")

# 输出完整卦象
print("\n===== 卜卦结果 =====")
print(f"六爻卦象: {yao_list}")
print("\n卦象解释:")
print("6: 老阴（变爻）")
print("7: 少阳")
print("8: 少阴")
print("9: 老阳（变爻）")
print("\n卦象顺序: 从下往上（初爻到上爻）")
        

