import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("Generador de formato BBVA")

texto = st.text_area("Pega aquí el texto")

if st.button("Generar imagen"):
    # Datos simulados (puedes extraerlos del texto con regex)
    concepto = "036240900640"
    nombre = "Monasterio Vazquez, Ma Guadalupe de"
    monto = "$10,600.00"

    # Crear imagen
    img = Image.new("RGB", (800, 400), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    draw.text((50, 30), "Formato para cobrar ordenes de pago BBVA (Cobro de SIT)", font=font, fill="black")
    draw.text((50, 80), f"Nombre: {nombre}", font=font, fill="black")
    draw.text((50, 120), "Convenio SIT: 1215442", font=font, fill="black")
    draw.text((50, 160), f"Referencia: {concepto}", font=font, fill="black")
    draw.text((50, 200), "TEF", font=font, fill="black")
    draw.text((50, 240), f"{monto}", font=font, fill="black")
    draw.text((50, 280), "*Favor de llevar su identificación oficial*", font=font, fill="black")

    st.image(img)
