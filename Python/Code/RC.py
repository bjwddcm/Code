import numpy as np
import matplotlib.pyplot as plt

# 定义RC电路参数
R = 1000   # 电阻值为1000欧姆
C = 1e-6   # 电容值为1微法

# 定义采样率和信号频率
fs = 100000  # 采样率为100kHz
f_signal = 5000  # 信号频率为5kHz

# 计算RC电路的截止频率fc
fc = 1 / (2 * np.pi * R * C)

# 定义时间轴和信号
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * f_signal * t)

# 计算一阶低通滤波器的系数
alpha = fs / (2 * np.pi * (fc + fs))
b = [1-alpha]
a = [1, -alpha]

# 用lfilter函数进行滤波
filtered_signal = signal.copy()   # 先将滤波后的信号初始化为原始信号
filtered_signal = np.array(filtered_signal)
filtered_signal = np.round(np.real(np.fft.ifft(np.fft.fft(filtered_signal)*np.fft.fftshift(np.fft.ifftshift(np.fft.fft(a,len(filtered_signal)))))))
filtered_signal = np.round(np.real(np.fft.ifft(np.fft.fft(filtered_signal)*np.fft.fftshift(np.fft.ifftshift(np.fft.fft(b,len(filtered_signal)))))))

# 绘制原始信号和滤波后的信号的频谱和时域波形
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

ax[0][0].plot(t, signal)
ax[0][0].set_title('原始信号')
ax[0][0].set_xlabel('时间/s')
ax[0][0].set_ylabel('幅值')

ax[0][1].magnitude_spectrum(signal, fs=fs)
ax[0][1].set_xlim([0, 20000])
ax[0][1].set_ylim([-60, 20])
ax[0][1].set_title('原始信号频谱')
ax[0][1].set_xlabel('频率/Hz')
ax[0][1].set_ylabel('幅值/dB')

ax[1][0].plot(t, filtered_signal)
ax[1][0].set_title('滤波后的信号')
ax[1][0].set_xlabel('时间/s')
ax[1][0].set_ylabel('幅值')

ax[1][1].magnitude_spectrum(filtered_signal, fs=fs)
ax[1][1].set_xlim([0, 20000])
ax[1][1].set_ylim([-60, 20])
ax[1][1].set_title('滤波后的信号频谱')
ax[1][1].set_xlabel('频率/Hz')
ax[1][1].set_ylabel('幅值/dB')

plt.show()
