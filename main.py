import streamlit as st
import speedtest

# Título de la aplicación
st.title("Prueba de Velocidad de Internet")

# Botón para iniciar la prueba
if st.button("Iniciar prueba de velocidad"):
    st.text("Midiendo... por favor espera unos momentos.")
    
    # Crear una instancia de Speedtest
    st_test = speedtest.Speedtest()
    st_test.get_best_server()

    # Medir la velocidad de descarga
    download_speed = st_test.download() / 1_000_000  
    st.text(f"Velocidad de descarga: {download_speed:.2f} Mbps")

    # Medir la velocidad de carga
    upload_speed = st_test.upload() / 1_000_000  
    st.text(f"Velocidad de carga: {upload_speed:.2f} Mbps")

    # Medir el ping (latencia)
    ping = st_test.results.ping
    st.text(f"Ping: {ping:.2f} ms")
