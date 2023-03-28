import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

datos = {'A': 1000000, 'B': 2000000, 'C': 3000000, 'D': 4000000}
nombres = list(datos.keys())
valores = list(datos.values())

# Crear el gráfico de barras
fig, ax = plt.subplots()
ax.bar(nombres, valores)

# Formatear los valores del eje y en millones
fmt = '%.0fM'  # formato en millones
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

# Mostrar el gráfico
plt.show()