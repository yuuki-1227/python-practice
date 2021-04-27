import streamlit as st
import pandas as pd
import numpy as np

st.title('My 1st App!!!')

st.write('データフレーム')
# pd.DataFrame() Pandasのデータフレーム型を書くことができる
st.write(
    pd.DataFrame({
        '1st column': [1, 2, 3, 4],
        '2nd column': [10, 20, 30, 40]
    })
)
