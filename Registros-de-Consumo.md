# SIMULACRO DE CONSUMO ELÉCTRICO RESIDENCIAL

**Casa:** 3 habitaciones | **Período de muestreo:** 24 horas (intervalos horarios discretos $\Delta t = 1\text{ h}$)  
**Instrumentación:** Medidor digital inteligente IoT / Analizador de redes en tablero principal (registro horario de energía activa con fluctuaciones de red, consumos basales *standby* y ruido de sensórica real).  
**Equipos monitoreados:** 1 TV Smart LED 55", 3 laptops (heterogéneas), refrigerador no-frost (compresor cíclico + ciclo *defrost*), cocina eléctrica (2 discos con termostato), 8 focos LED de diferentes potencias, router WiFi/ONT, microondas con reloj digital, 3 cargadores de teléfono móvil (diferentes protocolos).

---

## 1. Inventario de cargas y caracterización técnica

| Dispositivo / Circuito | Cant. | Potencia unitaria nominal (W) | Potencia total instalada (W) | Observaciones y régimen de operación |
|---|:---:|:---:|:---:|---|
| **Televisor LED 55" Smart** | 1 | 120 W | 120 W | Potencia variable según brillo dinámico y audio (114–124 W activo). Consumo en *standby* continuo de ~1.2–1.4 W. |
| **Laptops (3 unidades heterogéneas)** | 3 | Variada | 200 W | Cargas asimétricas según prestaciones:<br>• **Laptop 1 (Gaming / CAD):** 90 W nominal (cargador 135 W, consumo 75–110 W)<br>• **Laptop 2 (Oficina / Universidad):** 65 W nominal (consumo 35–55 W)<br>• **Laptop 3 (Ultrabook ligera):** 45 W nominal (consumo 22–38 W)<br>*Standby* en suspensión: ~0.8–1.4 W combinadas. |
| **Refrigerador no-frost (compresor cíclico)** | 1 | 160 W | 160 W | Compresor cíclico (108–195 W según temperatura ambiente y aperturas de puerta). A las 03:00–04:00 h activa resistencia de descongelación (*defrost*) generando un pico térmico de ~238 W. |
| **Cocina eléctrica (2 discos calefactores)** | 1 | 2500 W | 2500 W | • **Disco grande:** 1500 W<br>• **Disco mediano:** 1000 W<br>Regulada mediante termostato bimetálico (ciclos PWM mecánicos de encendido/apagado fraccionado). |
| **Focos LED (8 unidades distribuidas)** | 8 | Variada | 81 W | Potencias asimétricas según requerimiento lumínico por habitación:<br>• **Foco 1 (Cocina - luz blanca intensa):** 15 W<br>• **Foco 2 (Sala principal - plafón):** 12 W<br>• **Foco 3 (Comedor):** 10 W<br>• **Foco 4 (Dormitorio principal):** 9 W<br>• **Foco 5 (Dormitorio secundario):** 9 W<br>• **Foco 6 (Estudio / Dormitorio 3):** 8 W<br>• **Foco 7 (Baño):** 11 W<br>• **Foco 8 (Pasillo / Acceso exterior):** 7 W |
| **Router WiFi dual-band + ONT Fibra** | 1 | 12 W | 12 W | Conexión permanente 24/7. Fluctuación activa de 9.4 W a 11.9 W en función del tráfico de datos y transmisiones inalámbricas. |
| **Horno microondas** | 1 | 1150 W | 1150 W | Operación fraccionada por minutos en recalentado y descongelación (3 a 11 min de uso real en la hora). Reloj y display digital en *standby* constante de ~2.3–2.4 W. |
| **Cargadores de teléfonos móviles** | 3 | Variada | 58 W | • **Cargador 1 (USB-C Power Delivery 30 W):** Carga rápida activa 18–28 W, en vacío 0.3 W<br>• **Cargador 2 (Quick Charge 18 W):** Carga media activa 12–16 W, en vacío 0.2 W<br>• **Cargador 3 (Estándar 5V/2A 10 W):** Carga lenta activa 6–9 W, en vacío 0.2 W<br>Consumo fantasma conjunto cuando quedan conectados sin teléfono: ~0.7 W. |
| **Total conectado nominal** | **19** | — | **4281 W** | Potencia pico teórica máxima instalada si todos los elementos operaran simultáneamente a plena carga. |

---

## 2. Patrón de consumo horario registrado (Wh)

> **Nota de medición:** Los valores corresponden a la integral horaria de energía activa ($E_k = \int_{t_{k-1}}^{t_k} P(t)\,dt$) capturada por la telemetría en vatios-hora ($\text{Wh}$), reflejando decimales provenientes de fluctuaciones del voltaje de red, conmutación termostática, curvas de carga de batería no lineales y consumos residuales en reposo (*standby*).

| Hora | TV (Wh) | Laptops (Wh) | Refri (Wh) | Cocina (Wh) | Luces (Wh) | Router (Wh) | Micro (Wh) | Carg. Cel. (Wh) | **Total Wh** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **00–01** | 1.3 | 0.9 | 114.2 | 0.0 | 0.0 | 9.5 | 2.3 | 36.4 | **164.6** |
| **01–02** | 1.3 | 0.8 | 108.6 | 0.0 | 0.0 | 9.4 | 2.4 | 18.2 | **140.7** |
| **02–03** | 1.2 | 0.8 | 112.4 | 0.0 | 1.2 | 9.4 | 2.3 | 4.5 | **131.8** |
| **03–04** | 1.3 | 0.9 | 238.4 | 0.0 | 0.0 | 9.5 | 2.4 | 0.7 | **253.2** |
| **04–05** | 1.2 | 0.8 | 118.5 | 0.0 | 0.0 | 9.4 | 2.3 | 0.7 | **132.9** |
| **05–06** | 1.3 | 0.8 | 115.2 | 0.0 | 0.0 | 9.6 | 2.3 | 0.7 | **129.9** |
| **06–07** | 1.4 | 0.9 | 126.8 | 0.0 | 15.6 | 10.1 | 2.4 | 0.7 | **157.9** |
| **07–08** | 1.3 | 58.4 | 154.3 | 0.0 | 22.4 | 10.5 | 59.8 | 12.8 | **319.5** |
| **08–09** | 1.2 | 124.6 | 162.1 | 0.0 | 8.7 | 10.8 | 2.4 | 0.7 | **310.5** |
| **09–10** | 1.3 | 138.2 | 141.5 | 0.0 | 0.0 | 11.2 | 2.3 | 0.7 | **295.2** |
| **10–11** | 1.4 | 142.5 | 138.9 | 0.0 | 0.0 | 11.0 | 2.4 | 0.7 | **296.9** |
| **11–12** | 1.2 | 131.8 | 149.2 | 0.0 | 4.2 | 10.9 | 2.3 | 0.7 | **300.3** |
| **12–13** | 1.3 | 64.2 | 178.6 | 0.0 | 13.8 | 11.1 | 98.1 | 19.5 | **386.6** |
| **13–14** | 1.3 | 59.8 | 172.4 | 0.0 | 9.5 | 11.3 | 2.4 | 0.7 | **257.4** |
| **14–15** | 1.4 | 71.3 | 146.1 | 0.0 | 0.0 | 10.7 | 2.3 | 0.7 | **232.5** |
| **15–16** | 1.2 | 66.7 | 139.8 | 0.0 | 0.0 | 10.8 | 2.4 | 0.7 | **221.6** |
| **16–17** | 1.3 | 82.4 | 144.5 | 0.0 | 0.0 | 11.0 | 2.3 | 0.7 | **242.2** |
| **17–18** | 1.3 | 61.5 | 151.2 | 0.0 | 18.2 | 11.2 | 2.4 | 0.7 | **246.5** |
| **18–19** | 116.4 | 134.8 | 163.4 | 0.0 | 36.5 | 11.6 | 79.0 | 21.4 | **563.1** |
| **19–20** | 121.8 | 128.4 | 182.7 | 1420.5 | 48.2 | 11.8 | 2.4 | 32.8 | **1948.6** |
| **20–21** | 119.5 | 146.2 | 194.2 | 2340.0 | 64.8 | 11.9 | 213.1 | 38.6 | **3128.3** |
| **21–22** | 123.1 | 112.6 | 168.5 | 915.0 | 52.3 | 11.7 | 2.4 | 24.2 | **1409.8** |
| **22–23** | 114.7 | 42.1 | 142.8 | 0.0 | 23.4 | 10.8 | 2.3 | 31.5 | **367.6** |
| **23–00** | 68.3 | 1.4 | 122.1 | 0.0 | 8.1 | 10.2 | 2.4 | 37.2 | **249.7** |
| **Subtotal** | **687.0** | **1572.8** | **3586.4** | **4675.5** | **326.9** | **255.4** | **497.1** | **286.2** | **11,887.3 Wh** |

### Parámetros energéticos consolidados:
- **Consumo total diario registrado ($E_{total}$):** **11,887.3 Wh = 11.887 kWh**
- **Potencia pico horaria ($P_{pico}$):** **3,128.3 W** (ocurrida en el intervalo **20:00–21:00 h**)
- **Potencia promedio horaria ($P_{prom}$):** **495.30 W**
- **Factor de carga residencial ($FC = P_{prom} / P_{pico}$):** **0.1583 (15.83%)**

---

## 3. Fórmulas de referencia y aplicación al Cálculo II

En el contexto de Cálculo Integral aplicado a la ingeniería de sistemas y energía, el consumo energético acumulado a partir de datos discretos se analiza mediante las siguientes relaciones y métodos de aproximación numérica:

### 3.1. Fundamento continuo del consumo de energía
La energía acumulada $E$ en un intervalo de tiempo $[a, b]$ equivale al área bajo la curva de potencia instantánea $P(t)$:

$$E = \int_{a}^{b} P(t) \, dt$$

Donde:
- $P(t)$: Potencia en vatios ($\text{W}$) o kilovatios ($\text{kW}$).
- $t$: Tiempo en horas ($\text{h}$).
- $E$: Energía resultante en vatios-hora ($\text{Wh}$) o kilovatios-hora ($\text{kWh}$).

---

### 3.2. Métodos de integración numérica para datos discretos y no ideales

Dado que los datos de sensores de campo presentan ruido, valores no uniformes y consumos basales, no existe una función analítica simple $P(t)$. Se aplican cuadraturas numéricas con partición uniforme $\Delta t = 1\text{ h}$ y $n = 24$ subintervalos sobre el dominio $[0, 24]$:

#### A. Sumas de Riemann
Aproximación por rectángulos según la evaluación en los extremos de cada subintervalo $[t_{k-1}, t_k]$:

- **Suma de Riemann por la izquierda ($L_{24}$):**
  $$E_{izq} = \Delta t \sum_{k=0}^{n-1} P(t_k)$$

- **Suma de Riemann por la derecha ($R_{24}$):**
  $$E_{der} = \Delta t \sum_{k=1}^{n} P(t_k)$$

#### B. Regla del Trapecio
Asume interpolación lineal por tramos entre muestras adyacentes:

$$E_{Trap} = \frac{\Delta t}{2} \left[ P(t_0) + 2 \sum_{k=1}^{n-1} P(t_k) + P(t_n) \right]$$

*Evaluación sobre el registro (asumiendo cierre de ciclo diario $P(t_{24}) \approx P(t_0)$):*  
$$E_{Trap} \approx 11,887.3\text{ Wh} \quad (11.887\text{ kWh})$$

#### C. Regla de Simpson 1/3
Ajusta polinomios de segundo grado (parábolas) sobre pares sucesivos de subintervalos (válido para $n = 24$, número par):

$$E_{Simp} = \frac{\Delta t}{3} \left[ P(t_0) + 4 \sum_{k=1, 3, 5}^{n-1} P(t_k) + 2 \sum_{k=2, 4, 6}^{n-2} P(t_k) + P(t_n) \right]$$

*Evaluación sobre el registro:*  
$$E_{Simp} \approx 11,773.1\text{ Wh} \quad (11.773\text{ kWh})$$

---

### 3.3. Estadísticos y teoremas de valor medio

1. **Teorema del Valor Medio para Integrales (Potencia promedio):**
   Existe al menos un instante $c \in [a, b]$ tal que:
   $$P_{prom} = P(c) = \frac{1}{b - a} \int_{a}^{b} P(t) \, dt = \frac{E_{total}}{24 - 0} = \frac{11,887.3\text{ Wh}}{24\text{ h}} \approx 495.30\text{ W}$$

2. **Potencia máxima (Pico de demanda):**
   $$P_{pico} = \max_{t \in [0, 24]} \{ P(t) \} = 3,128.3\text{ W} \quad (\text{a las 20:00–21:00 h})$$

3. **Factor de carga ($FC$):**
   Indica el grado de aprovechamiento de la capacidad instalada frente a la demanda máxima de la instalación:
   $$FC = \frac{P_{prom}}{P_{pico}} = \frac{495.30\text{ W}}{3,128.3\text{ W}} \approx 0.1583 \quad (15.83\%)$$

---

### 3.4. Justificación técnica de las "impurezas" y variaciones en los datos

Para efectos de modelado matemático, simulación o ajuste por mínimos cuadrados / *splines*, los datos reflejan los siguientes fenómenos físicos reales:
1. **Consumo fantasma (*vampire power* / *standby*):** La TV mantiene receptores de infrarrojo y módulos WiFi activos (~1.3 W). El microondas mantiene un oscilador y display LED encendido 24/7 (~2.4 W). Los cargadores conectados sin dispositivo presentan pérdidas de magnetización en el transformador de conmutación (~0.2–0.3 W c/u).
2. **Ciclo de descongelación forzada (*defrost*) en el refrigerador:** Entre las 03:00 y 04:00 h se activa una resistencia de cuarzo/aluminio para disipar escarcha en el evaporador, generando una anomalía térmica típica de 238.4 Wh en plena madrugada.
3. **Curva de carga no lineal de acumuladores electroquímicos (Li-Ion):** Los celulares y laptops no absorben potencia constante. Inician con corriente constante (alta absorción), pasan a tensión constante con decaimiento exponencial de corriente (*tapering*) y finalizan en corriente de mantenimiento (*trickle charge*).
4. **Ciclos termostáticos PWM en cocina eléctrica:** Las resistencias de vitrocerámica o espiral conmutan periódicamente mediante bimetálico o triac para no sobrecalentar, por lo que el consumo horario no es un múltiplo exacto de su potencia de catálogo.
5. **Asimetría luminotécnica:** Los focos LED no son idénticos; cada recinto tiene un foco de diferente flujo luminoso y potencia (7 W a 15 W), y su activación en diferentes horas genera sumas irregulares.
