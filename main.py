import streamlit as st
import speedtest

# Título de la aplicación
st.title("Prueba de Velocidad de Internet")


if st.button("Iniciar prueba de velocidad"):
    st.text("Midiendo... por favor espera unos momentos.")
    

    st_test = speedtest.Speedtest()
    st_test.get_best_server()


    download_speed = st_test.download() / 1_000_000  
    st.text(f"Velocidad de descarga: {download_speed:.2f} Mbps")


    upload_speed = st_test.upload() / 1_000_000  
    st.text(f"Velocidad de carga: {upload_speed:.2f} Mbps")


    ping = st_test.results.ping
    st.text(f"Ping: {ping:.2f} ms")
