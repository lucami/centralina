# https://blog.streamlit.io/how-to-build-a-real-time-live-dashboard-with-streamlit/
import math
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import streamlit as st  # 🎈 data web app development
import random


def add_new_pm10sample(np_array_pm10, pm10_socket):
    a = np.delete(np_array_pm10, 0)
    r = int(random.random() * 10)
    a = np.append(a, r)
    return a


def add_new_pm2p5sample(np_array_2p5, pm10_socket):
    # print(np_array_2p5)
    a = np.delete(np_array_2p5, 0)
    # print(a)
    r = int(random.random() * 10)
    a = np.append(a, r)
    # print(a)
    return a


if __name__ == "__main__":
    st.set_page_config(
        page_title="Real-Time Data Science Dashboard",
        #page_icon="✅",
        layout="wide",
    )

    # dashboard title
    st.title("Real-Time Live Data")

    # creating a single-element container
    placeholder_time = st.empty()
    placeholder_pm = st.empty()

    pm10 = np.zeros(300)
    pm2p5 = np.ones(300)
    t = time.time()
    # near real-time / live feed simulation
    while True:
        with placeholder_time.container():
            st.write(f"Chart rfresh time: {math.ceil((time.time() - t)*100)/100}[s]")
            t = time.time()
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
        aggregate = []
        for i in range(len(pm10)):
            d = [pm10[i], pm2p5[i]]
            aggregate.append(d)
        chart_data2 = pd.DataFrame(aggregate, columns=['pm10', 'pm2.5'])
        # print(chart_data)
        # print(chart_data2)
        with placeholder_pm.container():
            st.line_chart(chart_data2)
            time.sleep(2)

        pm10 = add_new_pm10sample(pm10, 0)
        pm2p5 = add_new_pm2p5sample(pm2p5, 0)
