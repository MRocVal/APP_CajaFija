#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:50:30 2024

@author: manuelrocamoravalenti
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Cargar datos
df = pd.read_csv('CajaFija_UPV.csv')

# Configuración de la app
st.set_page_config(page_title="Caja Fija UPV", layout="wide")

# Barra lateral para navegación entre páginas
pagina = st.sidebar.selectbox(
    "Selecciona la página:",
    ["Introducción", "Gráficos", "Estadísticas Descriptivas"])

if pagina == "Introducción":
    
    st.image("logo.png", width=400)  # Logo de la UPV
    
    st.title("Introducción a la Aplicación de Caja Fija UPV")
    
    st.markdown("""
    ## Bienvenido a la Aplicación de Análisis de Caja Fija UPV
    
    La Universidad Politécnica de Valencia (UPV) es una institución de prestigio que fomenta la excelencia académica, investigativa y administrativa. En esta aplicación, se presenta un análisis detallado de los datos financieros relacionados con la **Caja Fija** de la UPV, que incluye estadísticas, gráficos interactivos y herramientas avanzadas para la exploración de datos.
    """)
    
    #st.image("https://upload.wikimedia.org/wikipedia/commons/8/8d/Universitat_Politécnica_de_València.jpg", caption="Campus de la UPV", width=700)
    
    st.markdown("""
    ---
    
    ### Funcionalidades Principales
    Esta aplicación está diseñada para ayudarte a explorar los datos de manera interactiva y eficiente. Entre las funcionalidades principales se incluyen:
    
    1. **Estadísticas Descriptivas**: Accede a estadísticas básicas para comprender los patrones y tendencias en los datos financieros.
    2. **Gráficos Interactivos**: Explora gráficos dinámicos que permiten analizar la evolución de los importes por centro directivo, concepto económico, y más.
    3. **Relaciones Complejas**: Visualiza cómo interactúan los centros directivos y los conceptos económicos más relevantes.
    
    ---
    
    ### Sobre la Caja Fija de la UPV
    La **Caja Fija** es un mecanismo administrativo que permite a la UPV gestionar gastos menores o recurrentes de manera ágil. Algunos ejemplos de gastos incluyen:
    - Material de oficina.
    - Actividades de formación y eventos.
    - Mantenimiento menor en las instalaciones universitarias.
    
    En esta aplicación, analizamos los datos de los distintos centros directivos de la universidad y los desglosamos por conceptos económicos clave para una gestión financiera más transparente.
    
    ---
    
    ### Cómo Navegar por la Aplicación
    - Usa la barra lateral para cambiar entre las diferentes secciones.
    - Explora los gráficos interactivos y ajusta los filtros para personalizar la visualización.
    - Descubre las relaciones entre los conceptos económicos y los centros directivos con nuestras herramientas avanzadas.
    
    ---
    
    ### Objetivos de la Aplicación
    - Ofrecer una herramienta visual para analizar los datos financieros de la Caja Fija.
    - Facilitar la toma de decisiones basada en datos para optimizar recursos.
    - Fomentar la transparencia en la gestión financiera de la universidad.

    ---
    """)
    
    
    st.markdown("""
    ¡Comienza ahora explorando las estadísticas descriptivas o los gráficos interactivos para descubrir más sobre la Caja Fija de la UPV!""")
    
    st.markdown("""#### Desarrollado por:
- **Adrian Tallec**
- **Anselmo Rodríguez**
- **Evgeny Grachev**
- **Manuel Rocamora**""")

elif pagina == "Estadísticas Descriptivas":
    st.title("Estadísticas Descriptivas")
    st.subheader("Estadísticas Básicas")
    
    st.write(df['IMPORTE'].describe())
    st.markdown("""
En esta tabla se presentan **estadísticas descriptivas** relacionadas con el importe total de los registros disponibles en el conjunto de datos. Los valores más relevantes son los siguientes:

- **Count**: Indica la cantidad total de registros analizados, en este caso, **3,767**.
- **Mean**: Representa el importe promedio, que asciende a **2,126.89**.
- **Std**: La desviación estándar es de **10,358.35**, lo que sugiere una alta variabilidad en los valores de importe.
- **Min y Max**:
  - El importe mínimo registrado es de **0.02**.
  - El importe máximo alcanza los **367,728.52**, mostrando una amplia disparidad en los montos.
- **Percentiles**: Los valores en los percentiles clave proporcionan una visión de cómo están distribuidos los importes:
  - **25%** de los valores están por debajo de **118.12**.
  - **50%** de los valores están por debajo de **433.71** (mediana).
  - **75%** de los valores están por debajo de **1,579.86**.

Esta información permite tener una **perspectiva general** de la distribución de los importes y su variación dentro del conjunto de datos.
""")
    st.markdown(""" --- """)
    
       # Cargar datos
    df = pd.read_csv('CajaFija_UPV.csv')
    
    # Filtrar por años
    st.subheader("Filtrar por Años")
    min_year = int(df['AÑO'].min())
    max_year = int(df['AÑO'].max())
    
    # Crear un control de rango de años
    years_selected = st.slider(
        "Selecciona el rango de años:",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )
    
    # Filtrar el DataFrame según el rango de años seleccionado
    df_filtrado = df[(df['AÑO'] >= years_selected[0]) & (df['AÑO'] <= years_selected[1])]
    
    # Crear una tabla pivote con los datos filtrados
    tabla_pivote = pd.pivot_table(df_filtrado, values='IMPORTE', index='CENTRO DIRECTIVO', columns='CONCEPTO ECONÓMICO', aggfunc='sum', fill_value=0)
    
    # Calcula el gasto total por concepto económico
    gasto_total_por_concepto = tabla_pivote.sum()
    
    # Selecciona los 10 conceptos económicos con mayor gasto total
    top_10_conceptos = gasto_total_por_concepto.sort_values(ascending=False).head(10).index
    
    # Filtra la tabla pivote para incluir solo los 10 conceptos económicos principales
    tabla_pivote_filtrada = tabla_pivote[top_10_conceptos]
    
    # Sección de análisis descriptivo
    st.subheader("Relación entre Centro Directivo y Concepto Económico")
    
    # Seleccionar un concepto económico del top 10
    concepto_seleccionado = st.selectbox(
        "Selecciona un Concepto Económico:",
        options=top_10_conceptos,
        help="Muestra los Centros Directivos con mayor gasto para el concepto seleccionado."
    )
    
    # Mostrar la tabla correspondiente al concepto seleccionado
    if concepto_seleccionado:
        # Ordenar y filtrar los 5 Centros Directivos con mayor gasto para el concepto seleccionado
        tabla_ordenada = tabla_pivote_filtrada[concepto_seleccionado].sort_values(ascending=False).head(5)
    
        # Mostrar los resultados en un formato claro
        st.write(f"### Concepto Económico: {concepto_seleccionado}")
        st.dataframe(tabla_ordenada.reset_index().rename(columns={concepto_seleccionado: "Gasto"}))
    
        # Crear un gráfico de barras con Plotly
        fig = px.bar(
            tabla_ordenada.reset_index(),
            x='CENTRO DIRECTIVO',
            y=concepto_seleccionado,
            title=f"Gasto por Centro Directivo para {concepto_seleccionado} (Años {years_selected[0]}-{years_selected[1]})",
            labels={concepto_seleccionado: "Gasto", 'CENTRO DIRECTIVO': "Centro Directivo"},
            text=concepto_seleccionado,
            color='CENTRO DIRECTIVO',
            color_discrete_sequence=px.colors.qualitative.Plotly  # Paleta de colores
        )
    
        # Ajustar el tamaño del gráfico
        fig.update_layout(
            width=1000,  # Ancho del gráfico
            height=600,  # Alto del gráfico
            xaxis_tickangle=-45,  # Rotar las etiquetas del eje X
            template="plotly_white"
        )
    
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True) 
        
    
    st.markdown("""
### Relación entre Centro Directivo y Concepto Económico  

Esta sección permite analizar el gasto de los **centros directivos** de la UPV en un **concepto económico específico** durante un rango de años seleccionado.

1. **Filtro por años**:  
   - El control deslizante en la parte superior permite seleccionar un rango de años, lo que filtra los datos para mostrar únicamente los gastos registrados en ese período (2011-2022 en este caso).  
   - Esto ayuda a enfocarse en un rango temporal relevante para el análisis.

2. **Selección de Concepto Económico**:  
   - El usuario puede elegir un concepto económico del listado desplegable (en este caso, **"Transferencias corrientes: Ayudas y becas"**).  
   - Esto filtra los datos para mostrar únicamente los gastos relacionados con ese concepto.

3. **Tabla de resultados**:  
   - La tabla muestra el importe gastado por cada centro directivo en el concepto seleccionado, ordenado de mayor a menor.  
   - En este ejemplo, el **DTOR ACCIÓN INTERNACIONAL** es el único con un gasto significativo (**1,345,563.76**), mientras que otros centros no registraron gastos en este concepto durante el rango seleccionado.

4. **Gráfico de barras**:  
   - Complementa la tabla con una visualización clara del gasto por centro directivo.  
   - La barra más alta (en este caso, el **DTOR ACCIÓN INTERNACIONAL**) resalta visualmente el centro con mayor gasto, mientras que las barras de los demás centros reflejan la ausencia de gastos.

Esta combinación de filtros, tabla y gráfico proporciona una herramienta eficaz para explorar cómo se distribuyen los gastos en función de los conceptos económicos y los centros directivos en un rango de tiempo específico.
""")
    st.markdown(""" --- """)

elif pagina == "Gráficos":
    st.title("Gráficos")

    # Cargar datos
    df = pd.read_csv('CajaFija_UPV.csv')
    
    # 1. Gráfico: IMPORTE por CENTRO DIRECTIVO
    st.subheader("IMPORTE por CENTRO DIRECTIVO")
    
    # Lista de opciones para CENTRO DIRECTIVO
    centros_disponibles = list(df['CENTRO DIRECTIVO'].unique())
    centros_seleccionados = st.multiselect(
        "Selecciona uno o más Centros Directivos:",
        options=centros_disponibles
    )
    
    # Mostrar el gráfico solo si hay selección
    if centros_seleccionados:
        # Filtrar datos por los Centros Directivos seleccionados
        df_centro_filtrado = df[df['CENTRO DIRECTIVO'].isin(centros_seleccionados)]
        
        # Calcular la suma total
        total_importe = df_centro_filtrado['IMPORTE'].sum()
        
        # Crear el gráfico dinámico
        fig_centro = px.bar(
            df_centro_filtrado,
            x="CENTRO DIRECTIVO",
            y="IMPORTE",
            color="CENTRO DIRECTIVO",
            title="IMPORTE por Centros Directivos seleccionados",
            log_y=True
        )
        
        # Añadir una traza adicional para la suma total
        fig_centro.add_annotation(
            text=f"Suma total: {total_importe:,.2f}",
            xref="paper", yref="paper",
            x=0.5, y=1.1, showarrow=False,
            font=dict(size=14, color="black")
        )
        
        fig_centro.update_layout(
            hovermode="x unified",  # Modo hover unificado
            xaxis_title="Centro Directivo",
            yaxis_title="IMPORTE (escala log)"
        )
        st.plotly_chart(fig_centro)
    else:
        st.info("Por favor, selecciona al menos un Centro Directivo para visualizar el gráfico.")
    
    st.markdown(""" El gráfico muestra el desglose del importe total 
                asignado a diferentes centros directivos seleccionados dentro del rango de años analizado. 
                La escala logarítmica en el eje Y permite visualizar tanto valores pequeños como grandes en un mismo gráfico, 
                destacando las diferencias significativas entre los centros. Además, se incluye la suma total de los importes de todos los centros seleccionados,
                facilitando la interpretación global de los datos.""")
    st.markdown(""" --- """)

    # 2. Gráfico: IMPORTE por CONCEPTO ECONÓMICO
    st.subheader("IMPORTE por CONCEPTO ECONÓMICO")
    
    # Lista de opciones para CONCEPTO ECONÓMICO
    conceptos_disponibles = list(df['CONCEPTO ECONÓMICO'].unique())
    conceptos_seleccionados = st.multiselect(
        "Selecciona uno o más Conceptos Económicos:",
        options=conceptos_disponibles
    )
    
    # Mostrar el gráfico solo si hay selección
    if conceptos_seleccionados:
        # Filtrar datos por los Conceptos Económicos seleccionados
        df_concepto_filtrado = df[df['CONCEPTO ECONÓMICO'].isin(conceptos_seleccionados)]
        
        # Calcular la suma total
        total_importe = df_concepto_filtrado['IMPORTE'].sum()
        
        # Crear el gráfico dinámico
        fig_concepto = px.bar(
            df_concepto_filtrado,
            x="CONCEPTO ECONÓMICO",
            y="IMPORTE",
            color="CONCEPTO ECONÓMICO",
            title="IMPORTE por Conceptos Económicos seleccionados",
            log_y=True
        )
        
        # Añadir una traza adicional para la suma total
        fig_concepto.add_annotation(
            text=f"Suma total: {total_importe:,.2f}",
            xref="paper", yref="paper",
            x=0.5, y=1.1, showarrow=False,
            font=dict(size=14, color="black")
        )
        
        fig_concepto.update_layout(
            hovermode="x unified",  # Modo hover unificado
            xaxis_title="Concepto Económico",
            yaxis_title="IMPORTE (escala log)"
        )
        st.plotly_chart(fig_concepto)
    else:
        st.info("Por favor, selecciona al menos un Concepto Económico para visualizar el gráfico.")
        
        
    st.markdown(""" El gráfico muestra la distribución del importe total asociado a los conceptos económicos seleccionados dentro del rango de años definido. 
                La escala logarítmica en el eje Y permite observar tanto los conceptos con menor gasto como aquellos con importes significativamente altos. 
                La suma total del gasto para los conceptos seleccionados se presenta como un indicador general para facilitar la interpretación y comparación entre categorías.""")
    st.markdown(""" --- """)

    # 3. Gráfico de línea temporal interactivo
    st.subheader("Total IMPORTE por Año")
        
    # Asegurarnos de que los años son numéricos
    df['AÑO'] = pd.to_numeric(df['AÑO'], errors='coerce')
    
    # 3. Gráfico de línea temporal interactivo
    st.subheader("Total IMPORTE por Año")
    
    # Selección de rango de años
    min_year = int(df['AÑO'].min())
    max_year = int(df['AÑO'].max())
    years_selected = st.slider(
        "Selecciona el rango de años:",
        min_year, max_year, (min_year, max_year)
    )
    
    # Filtrar datos según los años seleccionados
    filtered_data = df[(df['AÑO'] >= years_selected[0]) & (df['AÑO'] <= years_selected[1])]
    
    # Agrupar los datos por año y calcular el total de 'IMPORTE'
    yearly_importe = filtered_data.groupby('AÑO')['IMPORTE'].sum().reset_index()
    
    # Crear el gráfico dinámico con Plotly
    fig_line = px.line(
        yearly_importe,
        x="AÑO",
        y="IMPORTE",
        title="Total IMPORTE por Año (rango seleccionado)",
        markers=True
    )
    
    # Añadir formato para mostrar total acumulado al pasar el mouse
    fig_line.update_traces(
        hovertemplate='<b>Año:</b> %{x}<br><b>IMPORTE:</b> %{y:,.2f}<extra></extra>'
    )
    
    # Personalizar diseño del gráfico
    fig_line.update_layout(
        xaxis_title="Año",
        yaxis_title="Total IMPORTE",
        hovermode="x unified",  # Unificar el hover
        template="plotly_white"
    )
    
    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig_line)
    
    
    st.markdown(""" Este gráfico muestra la tendencia del importe total asignado a lo largo de los años dentro del rango seleccionado. 
                Cada punto en la línea representa el importe acumulado en un año específico, permitiendo observar patrones de aumento o d
                isminución en el gasto. Esta visualización es útil para identificar posibles cambios en las prioridades presupuestarias o 
                eventos que impactaron significativamente en los gastos anuales.""")
    st.markdown(""" --- """)
    
    # 4. Gráficos de lienas
    
    # Cargar datos
    df = pd.read_csv('CajaFija_UPV.csv')
    
    # Sección: Evolución del gasto por Centro Directivo
    st.subheader("Evolución del gasto total por Centro Directivo (Top 10)")
    
    # Agrupa por CENTRO DIRECTIVO y suma el IMPORTE
    df_agrupado_total = df.groupby('CENTRO DIRECTIVO')['IMPORTE'].sum().reset_index()
    
    # Ordena por IMPORTE de mayor a menor y selecciona los 10 primeros
    top_10_centros = df_agrupado_total.sort_values(by=['IMPORTE'], ascending=False).head(10)['CENTRO DIRECTIVO'].tolist()
    
    # Filtra el DataFrame original para incluir solo los 10 centros directivos principales
    df_filtrado_centros = df[df['CENTRO DIRECTIVO'].isin(top_10_centros)]
    
    # Agrupa por AÑO y CENTRO DIRECTIVO y suma el IMPORTE
    df_agrupado_centros = df_filtrado_centros.groupby(['AÑO', 'CENTRO DIRECTIVO'])['IMPORTE'].sum().reset_index()
    
    # Crear gráfico dinámico para Centros Directivos
    fig_centros = px.line(
        df_agrupado_centros,
        x="AÑO",
        y="IMPORTE",
        color="CENTRO DIRECTIVO",
        title="Evolución del gasto total por Centro Directivo (Top 10)",
        markers=True
    )
    
    fig_centros.update_layout(
        xaxis_title="Año",
        yaxis_title="Importe total",
        legend_title="Centro Directivo",
        hovermode="x unified",  # Hover unificado por año
        template="plotly_white"
    )
    
    st.plotly_chart(fig_centros)
    
    # Sección: Evolución del gasto por Concepto Económico
    st.subheader("Evolución del gasto total por Concepto Económico (Top 10)")
    
    # Agrupa por CONCEPTO ECONÓMICO y suma el IMPORTE
    df_agrupado_total_conceptos = df.groupby('CONCEPTO ECONÓMICO')['IMPORTE'].sum().reset_index()
    
    # Ordena por IMPORTE de mayor a menor y selecciona los 10 primeros
    top_10_conceptos = df_agrupado_total_conceptos.sort_values(by=['IMPORTE'], ascending=False).head(10)['CONCEPTO ECONÓMICO'].tolist()
    
    # Filtra el DataFrame original para incluir solo los 10 conceptos económicos principales
    df_filtrado_conceptos = df[df['CONCEPTO ECONÓMICO'].isin(top_10_conceptos)]
    
    # Agrupa por AÑO y CONCEPTO ECONÓMICO y suma el IMPORTE
    df_agrupado_conceptos = df_filtrado_conceptos.groupby(['AÑO', 'CONCEPTO ECONÓMICO'])['IMPORTE'].sum().reset_index()
    
    # Crear gráfico dinámico para Conceptos Económicos
    fig_conceptos = px.line(
        df_agrupado_conceptos,
        x="AÑO",
        y="IMPORTE",
        color="CONCEPTO ECONÓMICO",
        title="Evolución del gasto total por Concepto Económico (Top 10)",
        markers=True
    )
    
    fig_conceptos.update_layout(
        xaxis_title="Año",
        yaxis_title="Importe total",
        legend_title="Concepto Económico",
        hovermode="x unified",  # Hover unificado por año
        template="plotly_white"
    )
    
    st.plotly_chart(fig_conceptos)
    
    st.markdown(""" El primer gráfico muestra la evolución del gasto total asignado a los 10 principales centros directivos a lo largo de los años. Cada línea representa el comportamiento de un centro específico, permitiendo identificar tendencias como aumentos o disminuciones significativas en su presupuesto. Esta información es clave para analizar las prioridades y decisiones estratégicas de la institución en diferentes períodos.

El segundo gráfico presenta la evolución del gasto total por los 10 conceptos económicos más relevantes. Aquí se observa cómo se distribuyen los recursos en función de las categorías de gasto, permitiendo detectar patrones relacionados con áreas específicas como dietas, suministros o transferencias corrientes. Este análisis facilita una comprensión más detallada de las políticas presupuestarias y sus cambios a lo largo del tiempo.

Ambos gráficos complementan el análisis, ofreciendo una perspectiva global sobre cómo se han asignado los recursos en diferentes dimensiones clave de la organización.""")