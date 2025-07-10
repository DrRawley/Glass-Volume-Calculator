import streamlit as st
import math

def page_2():
    st.title("Page 2")

pages = {
    "Calculators": [
    st.Page("calc_sphere_diam.py", title="Calculate Sphere Diameter"),
    st.Page(page_2, title="Page 2")
    ]
}

pg = st.navigation(pages)
pg.run()


