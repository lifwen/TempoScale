import numpy as np
import matplotlib.pyplot as plt
from PyEMD import CEEMDAN
import numpy as np
import pandas as pd

df = pd.read_csv('Machine_usage_groupby.csv')


signal = np.array(df['0'])
t = np.linspace(0, 1, len(signal))

# print(desired_column_array)


# t = np.linspace(0, 1, 1000)
# signal = 3 * np.sin(2 * np.pi * 7 * t) + 2 * np.sin(2 * np.pi * 15 * t) + np.random.randn(1000)


ceemdan = CEEMDAN(max_imf=0)

emd = ceemdan(signal)

plt.figure(figsize=(6, 12))

plt.subplot(len(emd) + 1, 1, 1)
plt.plot(t, signal, label='Original signal', color='#3b0f70', linewidth=1)
# plt.title('Original Signal')
for i, mode in enumerate(emd):
    if i == 0:
        plt.subplot(len(emd) + 1, 1, i + 2)
        plt.plot(t, mode, label=f'Mode {i + 1}', linewidth=1, color='#de4968')
        # print(mode)
        np.savetxt('R.csv', mode, delimiter=',')
    if i == 1:
        plt.subplot(len(emd) + 1, 1, i + 2)
        plt.plot(t, mode, label=f'Mode {i + 1}', linewidth=1, color='#8c2981')
        # print(mode)
        np.savetxt('Short.csv', mode, delimiter=',')
    if i == 2:
        plt.subplot(len(emd) + 1, 1, i + 2)
        plt.plot(t, mode, label=f'Mode {i + 1}', linewidth=1, color='#fe9f6d')
        # print(mode)
        np.savetxt('Long.csv', mode, delimiter=',')

plt.tight_layout()
plt.show()
# plt.savefig('my_plot.png', dpi=300)
