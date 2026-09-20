import numpy as np
import pandas as pd
from scipy import integrate, interpolate
import matplotlib.pyplot as plt

# 1. Cargar datos
# Si lees desde CSV:
df = pd.read_csv('Datos.csv')
# Si lees directo de Excel, descomenta la siguiente:
# df = pd.read_excel('tu_archivo.xlsx')

# 2. Limpieza y conversión a número (reemplaza comas por puntos si existen)
serie_totales = df['Total Wh'].astype(str).str.replace(',', '.')
y = pd.to_numeric(serie_totales, errors='coerce').to_numpy(dtype=float)

# Eje X: 0, 1, 2, ..., N-1
x = np.arange(len(y), dtype=float)

# Eliminar posibles filas que hayan quedado como NaN (por si había filas vacías al final)
valido = ~np.isnan(y)
x = x[valido]
y = y[valido]

# ==========================================================
# 3. Integración Numérica
# ==========================================================

# Método A: Trapecio
area_trapecio = getattr(integrate, 'trapezoid', getattr(np, 'trapz', None))(y, x)

# Método B: Simpson
simpson_func = getattr(integrate, 'simpson', getattr(integrate, 'simps', None))
area_simpson = simpson_func(y, x=x)

# Método C: Spline Cúbico
spline = interpolate.CubicSpline(x, y)
area_spline = spline.integrate(x[0], x[-1])

# Integral acumulada
integral_acumulada = integrate.cumulative_trapezoid(y, x, initial=0)

# ==========================================================
# 4. Resultados
# ==========================================================
print(f"Integral (Regla del Trapecio): {area_trapecio:.2f}")
print(f"Integral (Regla de Simpson) : {area_simpson:.2f}")
print(f"Integral (Spline Cúbico)    : {area_spline:.2f}")

# ==========================================================
# 5. Gráfica
# ==========================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

x_suave = np.linspace(x[0], x[-1], 300)
y_suave = spline(x_suave)

ax1.plot(x, y, 'o', color='#1f77b4', label='Datos discretos (Total Wh)')
ax1.plot(x_suave, y_suave, '-', color='#ff7f0e', label='Curva Spline Cúbico')
ax1.fill_between(x_suave, y_suave, color='#ff7f0e', alpha=0.25, label=f'Área (Spline): {area_spline:.1f}')
ax1.set_ylabel('Total Wh')
ax1.set_title('Consumo Horario e Integración Numérica', fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left')

ax2.plot(x, integral_acumulada, 's-', color='#2ca02c', label='Integral acumulada')
ax2.set_xlabel('Hora')
ax2.set_ylabel('Energía Acumulada')
ax2.set_xticks(x)
ax2.set_xticklabels(df['Hora'].iloc[valido], rotation=45, ha='right', fontsize=9)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left')

plt.tight_layout()
plt.show()