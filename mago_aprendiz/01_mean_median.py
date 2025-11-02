# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# %%
pop_renda = np.random.normal(2220, 300, size=300)

# %%
media = pop_renda.mean()
mediana = np.median(pop_renda)

# %%
plt.hist(pop_renda)
plt.vlines( media, ymin=0, ymax=70, color='gold')
plt.vlines( mediana, ymin=0, ymax=70, color='red')
plt.grid(True)
plt.legend([f'Média: {media:.2f}', f'Mediana: {mediana:.2f}'])

# %%
nova_amostra = np.random.exponential(10000, size=150) + media
nova_amostra.sort()
# %%
plt.hist(nova_amostra)

# %%
def animate(i, pop, novos_dados):
    amostra_completa = np.append(pop, novos_dados[0:i])
    media = amostra_completa.mean()
    mediana = np.median(amostra_completa)
    plt.cla()
    plt.hist(amostra_completa)
    plt.vlines( media, ymin=0, ymax=70, color='gold')
    plt.vlines( mediana, ymin=0, ymax=70, color='red')
    plt.grid(True)
    plt.legend([f'Média: {media:.2f}', f'Mediana: {mediana:.2f}'])

fig = plt.figure(figsize=(6,5), dpi=400)

ani = animation.FuncAnimation(fig, 
                              animate,
                              len(nova_amostra),
                              fargs=(pop_renda, nova_amostra),
                              interval=100)


ani.save('hist_media_mediana.gif')