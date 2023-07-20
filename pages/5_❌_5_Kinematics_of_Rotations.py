import streamlit as st
import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import toml


def load_config(config_path):
    with open(config_path, 'r') as f:
        config = toml.load(f)
    return config

config = load_config('config.toml')

st.set_page_config(page_title='Lecture 5', page_icon='\U0001F412')

st.header(':violet[**Lecture 5 ยังไม่ Update น้าาา . . . :sob:**]')