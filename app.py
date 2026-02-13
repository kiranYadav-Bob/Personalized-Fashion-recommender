import streamlit as st
import os
import pickle
import numpy as np
from sklearn.neighbors import NearestNeighbors
from PIL import Image

# Load the saved "fingerprints"
feature_list = np.array(pickle.load(open('embeddings.pkl', 'rb')))
filenames = pickle.load(open('filenames.pkl', 'rb'))

# Define the KNN Recommender
neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
neighbors.fit(feature_list)

st.title('👗 Personalized Fashion Recommender')

uploaded_file = st.file_uploader("Upload a fashion item image...")

if uploaded_file is not None:
    # 1. Display uploaded image
    display_image = Image.open(uploaded_file)
    st.image(display_image, caption='Your Upload', width=200)
    
    # 2. Extract features of uploaded image (using same logic as Step A)
    # [Insert feature extraction code here for the single uploaded image]
    
    # 3. Find Neighbors
    distances, indices = neighbors.kneighbors([query_feature])
    
    # 4. Show Recommendations
    st.header("Recommended for You:")
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.image(filenames[indices[0][i+1]]) # i+1 to skip the original image