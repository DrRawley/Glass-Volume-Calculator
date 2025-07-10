import streamlit as st
import math

st.title("Calculate Rod Length from Sphere Diameter")

sphere_diam = st.number_input('Sphere Diameter (mm): ', min_value=0.0, max_value=1000.0, step=0.1, value=10.0)
sphere_vol = math.pi / 6 * sphere_diam ** 3
st.write(f"Sphere volume = {sphere_vol:.1f} mm^3")
st.divider()

#Rod row
col_diam, col_len = st.columns([0.3,0.7], vertical_alignment="bottom")
rod_diameter = col_diam.number_input('Rod Diamter (mm): ', min_value=0.01, max_value=1000.0, value=7.0) #, key=f"num_{i}")

rod_length = sphere_vol / ( math.pi / 4 * rod_diameter ** 2 )
col_len.subheader(f"Rod length = {rod_length:.1f} mm")
#End Rod row