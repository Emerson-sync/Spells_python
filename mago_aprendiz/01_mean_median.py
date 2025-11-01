# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
pop_renda = np.random.normal(2220, 300, size=300)

# %%
media = pop_renda.mean()
mediana = np.median(pop_renda)
plt.hist(pop_renda)
plt.vlines( media, ymin=0, ymax=70, color='gold')
plt.vlines( mediana, ymin=0, ymax=70, color='red')
plt.grid(True)
plt.legend([f'Média: {media:.2f}', f'Mediana: {mediana:.2f}'])