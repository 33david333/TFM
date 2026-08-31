"""
config.py

Parámetros compartidos.
Todos los scripts y notebooks importan sus constantes desde aquí,
para garantizar que FDM y PINN resuelven exactamente el mismo problema.
"""

# ECUACIÓN DEL CALOR 1D


L_HEAT = 1.0        # Longitud del dominio espacial [0, L]
T_HEAT = 1.0         # Tiempo final de simulación
ALPHA = 0.05        # Difusividad térmica


NX_HEAT = 100         # Número de nodos espaciales
NT_HEAT = 2000        # Número de pasos temporales
#NT_HEAT = 834        # Para comprobar estabilidad (mu alto)

DX_HEAT = L_HEAT / NX_HEAT
DT_HEAT = T_HEAT / NT_HEAT


MU_HEAT = ALPHA * DT_HEAT / DX_HEAT**2


# ECUACIÓN DE BURGERS 1D

X_MIN_BURGERS = -1.0
X_MAX_BURGERS = 1.0
L_BURGERS = X_MAX_BURGERS - X_MIN_BURGERS   
T_BURGERS = 1.0
NU_BURGERS = 0.001        

NX_BURGERS = 200
NT_BURGERS = 2000


DX_BURGERS = L_BURGERS / NX_BURGERS
DT_BURGERS = T_BURGERS / NT_BURGERS

# Mejoras de la PINN
CURRICULUM_LEARNING = True
RAD = True
NU_PREV = 0.005

MU_BURGERS = NU_BURGERS * DT_BURGERS / DX_BURGERS**2