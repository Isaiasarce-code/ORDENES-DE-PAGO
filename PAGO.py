import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("Generador de formato BBVA")

# Textarea más grande
texto = st.text_area("Pega aquí el texto", height=230)

# Solo generar si hay texto
if texto.strip():
    lineas = [l.strip() for l in texto.split("\n") if l.strip()]

    if len(lineas) < 4:
        st.error("El texto debe tener al menos 4 líneas.")
    else:
        # EXTRAER LÍNEA 2, 4 Y ÚLTIMA
        concepto = lineas[1]       # Fila 2
        nombre = lineas[3]         # Fila 4
        monto = lineas[-1]         # Última fila

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
else:
    st.info("Pega el texto para generar la imagen automáticamente.")
