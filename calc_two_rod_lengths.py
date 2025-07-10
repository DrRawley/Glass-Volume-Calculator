import streamlit as st
import math

st.title("Calculate Rod Length from Sphere Diameter")

sphere_diam = st.number_input('Sphere Diameter (mm): ', min_value=0.0, max_value=1000.0, step=0.1, value=10.0)
sphere_vol = math.pi / 6 * sphere_diam ** 3
st.write(f"Sphere volume = {sphere_vol:.1f} mm^3")

st.divider()
#Rod 1 input row
col_diam, col_len = st.columns([0.3,0.7])
rod_1_diam = col_diam.number_input('Rod 1 Diamter (mm): ', min_value=0.01, value=7.0, key=f"num_rod1")

#Calculate maximum rod length based on the sphere volume and rod 1 diameter
max_rod_1_length = sphere_vol / ( math.pi / 4 * rod_1_diam ** 2 )

rod_1_length = col_len.slider('Rod Length (mm): ', min_value=0.0, max_value=max_rod_1_length, step=0.1, key=f"slider_rod1", format="%0.1f")
#End Rod 1 input row

rod_1_volume = math.pi / 4 * rod_1_diam ** 2 * rod_1_length
st.write(f"Rod 1 volume = {rod_1_volume:.2f} mm^3")

rod_2_volume = sphere_vol - rod_1_volume
st.write(f"Rod 2 volume = {rod_2_volume:.2f} mm^3")

st.divider()
#Rod 2 row
col_diam, col_len = st.columns([0.3,0.7], vertical_alignment="bottom")
rod_2_diam = col_diam.number_input('Rod 2 Diamter (mm): ', min_value=0.01, value=7.0, key=f"num_rod2")

rod_2_length = rod_2_volume / ( math.pi / 4 * rod_2_diam ** 2 )

col_len.subheader(f"Rod 2 Length = {rod_2_length:.1f} mm")
#End rod 2 row