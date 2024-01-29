import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def gaussian_distribution(x, mean, std_dev):
    return 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))

def main():
    st.title('Gaussian Distribution Generator')

    st.sidebar.header('Adjust Parameters')
    mean = st.sidebar.slider('Mean', -10.0, 10.0, 0.0, 0.1)
    std_dev = st.sidebar.slider('Standard Deviation', 0.1, 10.0, 1.0, 0.1)

    x = np.linspace(-10, 10, 1000)

    y = gaussian_distribution(x, mean, std_dev)

    fig, ax = plt.subplots()
    ax.plot(x, y, color='blue')
    ax.fill_between(x, 0, y, color='skyblue', alpha=0.5)
    ax.set_title('Gaussian Distribution')
    ax.set_xlabel('X')
    ax.set_ylabel('Probability Density')
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 0.5)

    st.pyplot(fig)

if __name__ == "__main__":
    main()
