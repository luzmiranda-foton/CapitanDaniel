import streamlit as st

# importar módulos (puedes crearlos poco a poco)
from modules import disciplina
from modules import issfam
from modules import deberes
from modules import ascensos
from modules import justicia_militar
from modules import armas

st.title("Legislación")

opcion = st.selectbox("Selecciona una ley:", [
    "Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
    "Ley Federal de Armas de Fuego y Explosivos",
    "Código de Justicia Militar",
    "Reglamento General de Deberes Militares",
    "Ley del Instituto de Seguridad Social para las Fuerzas Armadas Mexicanas",
    "Ley de Ascensos y Recompensas del Ejército y Fuerza Aérea Mexicanos"
])

# --- CONEXIÓN CON MÓDULOS ---

if opcion == "Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos":
    disciplina.show()

elif opcion == "Ley Federal de Armas de Fuego y Explosivos":
    armas.show()

elif opcion == "Código de Justicia Militar":
    justicia_militar.show()

elif opcion == "Reglamento General de Deberes Militares":
    deberes.show()    

elif opcion == "Ley del Instituto de Seguridad Social para las Fuerzas Armadas Mexicanas":
   issfam.show()

elif opcion == "Ley de Ascensos y Recompensas del Ejército y Fuerza Aérea Mexicanos":
    ascensos.show() 
