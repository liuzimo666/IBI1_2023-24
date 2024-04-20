import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 定义基本参数
N = 10000  # 总人口数
I0 = 1  # 初始感染者数量
S0 = N - I0  # 初始易感者数量
R0 = 0  # 初始康复者数量
V0 = int(0.1 * N)  # 初始接种者数量，占总人口的10%

# 定义疾病传播参数
beta = 0.3  # 感染率
gamma = 0.05  # 康复率

# 定义时间步长和模拟时间
t = np.arange(0, 400, 1)  # 时间步长为1
S, I, R, V = S0, I0, R0, V0

# 存储数据用于绘图
S_data = []
I_data = []
R_data = []
V_data = []

for t_i in t:
    # 计算当前时间步的S, I, R, V
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    dVdt = 0  # 接种者数量不变

    # 更新S, I, R, V
    S += dSdt
    I += dIdt
    R += dRdt
    V += dVdt

    # 存储数据
    S_data.append(S)
    I_data.append(I)
    R_data.append(R)
    V_data.append(V)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(t, I_data, color=cm.viridis(30), label='Infected')
plt.plot(t, R_data, color=cm.viridis(150), label='Recovered')
plt.plot(t, V_data, color=cm.viridis(200), label='Vaccinated')
plt.plot(t, S_data, color=cm.viridis(80), linestyle='--', label='Susceptible')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model with Vaccination')
plt.legend()
plt.show()

