# TFM — PINNs vs. Diferencias Finitas para EDPs

Código del Trabajo de Fin de Máster en Modelización e Investigación Matemática, Estadística y Computación (UPV/EHU): comparación entre **Redes Neuronales Informadas por la Física (PINNs)** y el método clásico de **Diferencias Finitas (FDM)** para resolver dos ecuaciones en derivadas parciales de distinta complejidad:

- **Ecuación del Calor 1D** — lineal, parabólica, suave.
- **Ecuación de Burgers 1D** — no lineal, con formación de frentes de choque.

## Estructura del repositorio

| Archivo | Contenido |
|---|---|
| `config.py` | Parámetros compartidos por todos los notebooks (dominio, viscosidad, resolución de malla, hiperparámetros de las PINNs). Todo el código lee de aquí para garantizar que FDM y PINN resuelven exactamente el mismo problema. |
| `01_fdm_heat.ipynb` | FDM para la Ecuación del Calor: esquema explícito con matriz de propagación tridiagonal periódica. Validación contra la solución analítica exacta. |
| `02_fdm_burgers.ipynb` | FDM para Burgers: esquema explícito no lineal (sin matriz fija, mediante `np.roll` para la periodicidad). Barrido de viscosidades, análisis del número de Péclet de malla, y estudio del caso límite de divergencia. |
| `03_pinn_heat.ipynb` | PINN para el Calor con DeepXDE: arquitectura `[2]+[50]×4+[1]`, activación `tanh`, condiciones de contorno periódicas, entrenamiento en dos fases (Adam + L-BFGS). |
| `04_pinn_burgers.ipynb` | PINN para Burgers: activación SiLU, y estrategias avanzadas (curriculum learning, muestreo adaptativo residual) para los casos de viscosidad baja. |
| `05_pinn_burgers_barrido.ipynb` | Barrido automatizado de la PINN sobre varios valores de viscosidad. |
| `06_analisis.ipynb` | Generación de las gráficas y métricas comparativas finales, cargando siempre desde los resultados guardados (nunca reentrena). |

## Requisitos

```
pip install deepxde torch numpy matplotlib
```

Backend de DeepXDE fijado a PyTorch (variable de entorno `DDE_BACKEND=pytorch`).

## Flujo de trabajo

Todos los notebooks siguen el mismo patrón:

1. **Entrenar / resolver** — ejecutar el FDM o la PINN correspondiente.
2. **Guardar** — resultados en `.npz`, pesos de red en `.pt`.
3. **Analizar** — las gráficas y métricas se generan siempre a partir de los archivos guardados, no reentrenando.

> **Nota:** los archivos de datos generados (`.npz`, `.pt`) no se incluyen en este repositorio por su tamaño — algunas referencias de malla fina superan los 6 GB. Ejecuta los notebooks en el orden indicado para regenerarlos localmente.

## Resultados principales

- **Calor:** error L2 relativo de 0.00032 (FDM) frente a 0.00086 (PINN), ambos frente a la solución analítica.
- **Burgers:** la PINN es sistemáticamente más precisa que el FDM de malla estándar en todo el barrido de viscosidades, aunque ambos métodos muestran limitaciones propias en el régimen de viscosidad muy baja (formación de frente de choque pronunciado).

## Autor

David — TFM, Máster en Modelización e Investigación Matemática, Estadística y Computación, UPV/EHU.
Director: Francisco de la Hoz Méndez.
