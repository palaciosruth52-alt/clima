import streamlit as st
import requests
import pandas as pd

# Configuración de página
st.set_page_config(page_title="Clima de Honduras", page_icon="🇭🇳")

# Diccionario de departamentos de Honduras con coordenadas de sus cabeceras
departamentos = {
    "Atlántida": {"lat": 15.77, "lon": -86.79},
    "Choluteca": {"lat": 13.30, "lon": -87.18},
    "Colón": {"lat": 15.92, "lon": -86.08},
    "Comayagua": {"lat": 14.46, "lon": -87.64},
    "Copán": {"lat": 14.93, "lon": -88.76},
    "Cortés": {"lat": 15.50, "lon": -88.02},
    "El Paraíso": {"lat": 13.84, "lon": -86.57},
    "Francisco Morazán": {"lat": 14.08, "lon": -87.21},
    "Gracias a Dios": {"lat": 15.26, "lon": -84.58},
    "Intibucá": {"lat": 14.30, "lon": -88.18},
    "Islas de la Bahía": {"lat": 16.33, "lon": -86.48},
    "La Paz": {"lat": 14.32, "lon": -87.68},
    "Lempira": {"lat": 14.33, "lon": -88.58},
    "Ocotepeque": {"lat": 14.43, "lon": -88.93},
    "Olancho": {"lat": 14.67, "lon": -85.91},
    "Santa Bárbara": {"lat": 15.11, "lon": -88.24},
    "Valle": {"lat": 13.45, "lon": -87.56},
    "Yoro": {"lat": 15.38, "lon": -87.13}
}

# Selector en la barra lateral
depto = st.sidebar.selectbox("Selecciona un departamento:", sorted(list(departamentos.keys())))

# Obtener datos de la API
lat, lon = departamentos[depto]["lat"], departamentos[depto]["lon"]
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()["current_weather"]
    temp = data["temperature"]
    
    # Lógica de fondo e información
    if temp < 20:
        mensaje = "Clima fresco."
    elif 20 <= temp < 30:
        mensaje = "Clima agradable."
    else:
        mensaje = "Clima caluroso."

    # Aplicar fondo
   

    st.title(f"🇭🇳 Clima en {depto}")
    st.info(mensaje)
    
    col1, col2 = st.columns(2)
    col1.metric("Temperatura", f"{temp} °C")
    col2.metric("Viento", f"{data['windspeed']} km/h")
    
    st.subheader("Ubicación")
    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}), zoom=7)
    
else:
    st.error("Error al conectar con la API.")