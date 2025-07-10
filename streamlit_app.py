import streamlit as st
import math

def page_2():
    st.title("Page 2")


pages = {
    "Sphere Diameter Calculators": [
    st.Page("calc_sphere_diam.py", title="Sphere Diameter"),
    ],
    "Rod Length Calculators": [
    st.Page("calc_rod_len_from_sp_diam.py", title="One Rod From Sphere Diameter"),
    ],
}


pg = st.navigation(pages)
pg.run()


