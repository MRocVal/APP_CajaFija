# APP_CajaFija

## Análisis de Caja Fija UPV

Esta aplicación desarrollada con **Streamlit** permite analizar los datos relacionados con la **Caja Fija** de la Universidad Politécnica de Valencia (UPV). Proporciona herramientas visuales e interactivas para explorar estadísticas descriptivas, gráficos y relaciones entre los diferentes conceptos económicos y centros directivos.

---

## Funcionalidades

### 1. Introducción

La aplicación comienza con una sección introductoria que explica el propósito y las funcionalidades principales. Además, incluye imágenes relacionadas con la UPV y un resumen de los objetivos de la herramienta.

### 2. Estadísticas Descriptivas

Muestra un resumen estadístico del campo `IMPORTE` del conjunto de datos. Incluye las siguientes métricas:

- **Count**: Cantidad total de registros analizados.
- **Mean**: Importe promedio.
- **Std**: Desviación estándar.
- **Min y Max**: Valores mínimo y máximo del importe.
- **Percentiles**: Percentiles 25%, 50% (mediana) y 75%.

Este análisis ayuda a comprender la distribución general de los datos.

### 3. Gráficos Interactivos

#### a) Evolución del gasto total por año

Un gráfico de líneas que muestra cómo ha evolucionado el gasto total a lo largo de los años seleccionados. Permite identificar tendencias como aumentos o disminuciones significativas en los gastos.

#### b) Importe por Centros Directivos

Un gráfico de barras dinámico que muestra el importe total asociado a los centros directivos seleccionados. Incluye:

- La suma total de los importes seleccionados.
- Colores diferenciados para cada centro directivo.
- Escala logarítmica en el eje Y para facilitar la comparación de valores con rangos amplios.

#### c) Importe por Conceptos Económicos

Un gráfico similar al anterior, pero enfocado en los conceptos económicos seleccionados. Permite analizar cómo se distribuyen los recursos entre las categorías de gasto más relevantes.

#### d) Relación entre Centro Directivo y Concepto Económico

Esta sección permite:

- Filtrar los datos por un rango de años seleccionado.
- Seleccionar un concepto económico específico y observar cómo se distribuye el gasto entre los diferentes centros directivos.
- Mostrar una tabla con los cinco principales centros directivos según el gasto en el concepto seleccionado.
- Complementar con un gráfico de barras que resalta visualmente los datos.

### 4. Análisis por Top 10

Gráficos que analizan los 10 principales:

- **Centros Directivos**: Evolución del gasto total en los centros más relevantes.
- **Conceptos Económicos**: Evolución del gasto total en los conceptos económicos más utilizados.

---

## Cómo usar la aplicación

1. **Cargar datos**  
   La aplicación requiere un archivo CSV con los siguientes campos principales:
   - `AÑO`
   - `CENTRO DIRECTIVO`
   - `CONCEPTO ECONÓMICO`
   - `IMPORTE`

2. **Interacción con los filtros**  
   - Seleccionar rangos de años para ajustar los datos mostrados.
   - Elegir centros directivos o conceptos económicos específicos para personalizar los gráficos y análisis.

3. **Explorar**  
   - Analizar las estadísticas descriptivas, explorar las visualizaciones y extraer conclusiones basadas en los gráficos y tablas.

---

## Desarrollado por

- **Maniel Rocamora**
- **Adrian Tallec**
- **Anselmo Rodríguez**
- **Evgeniy Gracev**

---

## Requisitos para ejecutar la aplicación

1. **Instalar dependencias**  
   - Python 3.7+  
   - Bibliotecas necesarias:  
     ```bash
     pip install streamlit pandas plotly seaborn matplotlib
     ```

2. **Ejecutar la aplicación**  
   - Coloca los datos en el archivo `CajaFija_UPV.csv`.  
   - Lanza la aplicación con el comando:  
     ```bash
     streamlit run app.py
     ```

---

## Estructura del proyecto

- **app.py**: Código principal de la aplicación Streamlit.
- **CajaFija_UPV.csv**: Archivo con los datos utilizados para los análisis.
- **Imagenes**: Carpeta con imágenes relacionadas con la UPV (opcional).

---

¿Te gustaría guardar este archivo directamente como `README.md`? 😊