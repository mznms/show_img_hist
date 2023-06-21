import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread
from PIL import Image


st.set_option('deprecation.showfileUploaderEncoding', False)


# image upload button
uploaded_file = st.file_uploader('Choose a image file')

if uploaded_file is not None:
    image_pil_array = Image.open(uploaded_file)
    st.image(
        image_pil_array, caption='uploaded image',
        use_column_width=True
    )


    im = np.array(image_pil_array)


    # show histgram of all colors
    hist_red, _ = np.histogram(im[:, :, 0], bins=64)
    hist_green, _ = np.histogram(im[:, :, 1], bins=64)
    hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
    hist = np.stack((hist_red, hist_green, hist_blue), axis=1)

    df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
    st.bar_chart(df_hist)


    # choose one color
    color = st.radio(
        "choose R, G, or B",
        ('R', 'G', 'B'))
    if color == 'R':
        df_hist = pd.DataFrame(hist_red)
        st.bar_chart(df_hist)
    if color == 'G':
        df_hist = pd.DataFrame(hist_green)
        st.bar_chart(df_hist)
    if color == 'B':
        df_hist = pd.DataFrame(hist_blue)
        st.bar_chart(df_hist)
