import yaml
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as patches


def load_config():
    with open("utils/config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    sns.set(**cfg["general_plotting"])
    return cfg

def plot_trends(df: pd.DataFrame, df_corr: pd.DataFrame, ref_country: str, other_countries: list):
        
    f, ax = plt.subplots()

    # Display trend of the reference country:
    df[ref_country].plot(ax=ax, color="darkorange", label=ref_country, linewidth=3)

    # Display trend of the other countries:
    for country in other_countries:
        # Retrieve the correlation coefficient:
        corr_coefficients = df_corr.loc[country, ref_country]

        if corr_coefficients > 0:
            alpha = 0.2
            color = "teal"

        elif corr_coefficients < 0:
            alpha = 0.2
            color = "red"

        df[country].plot(ax=ax, alpha=alpha, color=color, label=country, linewidth=3)

    ax.set_xlabel("Year")
    ax.legend()
    return ax


def add_rectangle(ax: mpl.axes._axes.Axes, df: pd.DataFrame, country: str, color="#fdc029"):

    # Find country
    country_idx = _find_element_in_df_idx(df, country)

    # Define position and size of rectangle:
    bottom_left_vertex = (0.05, country_idx)
    height = 0.95
    width = country_idx + 0.9

    ax.add_patch(patches.Rectangle(bottom_left_vertex, 
                                   width,
                                   height,
                                   edgecolor=color,
                                   fill=False,
                                   lw=5, zorder=5)
                )
    return ax


def _find_element_in_df_idx(df: pd.DataFrame, element: str):
    return list(df.index).index(element)