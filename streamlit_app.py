import streamlit as st
import math

st.title("🎈 Glass Volume Calculator")
#st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

num_rods = st.number_input('Number of rods: ', min_value=1, max_value=8, step=1, value=1)

rod_diam = []
rod_length = []
rod_volume = []


for i in range(num_rods):
    rod_diam.append(st.number_input('Rod Diamter (mm): ', min_value=0.01, value=7.0, key=f"num_{i}"))
    rod_length.append(st.slider('Rod Length (mm): ', min_value=0.0, max_value=100.0, step=0.1, key=f"slider_{i}"))
    rod_volume.append(math.pi / 4 * rod_diam[i] ** 2 * rod_length[i])
    st.write(f"Rod {i + 1} Volume is {rod_volume[i]:.2f} mm^3.")


total_volume = sum(rod_volume)

st.write(f"Total Volume is {total_volume:.2f} mm^3.")
sphere_diameter = 2 * ( 3 * total_volume / ( 4 * math.pi ) ) ** (1/3)
st.write(f"Sphere diameter is {sphere_diameter:.2f} mm.")
