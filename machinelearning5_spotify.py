import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("data science/netflix_titles.csv")
print(data.head(10))
# print(data.info())
# print(data.describe())
# print(data.shape)