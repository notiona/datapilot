"""Visualizer class for datapilot library"""

from copy import deepcopy

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
from sklearn.decomposition import PCA

from constants.help_message import (
    VISUALIZER_HELP_MESSAGE,
    VISUALIZER_TWO_COLUMNS_HELP_MESSAGE,
)

class Visualizer():
    """
    Visualizer class for datapilot library
    """

    def __init__(self, df):
        if isinstance(df, pd.DataFrame):
            self._df = df
        else:
            raise ValueError(
                f"Expected pandas.DataFrame object. Got {type(df)} instead"
            )
        # Keep track of numerical / categorical type tag for all columns
        self._df_types = {col : str(df.dtypes[col]) for col in df.columns}
        self._df_types = {
            k:('numerical' if v.startswith(("float", "int")) else 'categorical')
            for (k,v) in self._df_types.items()
        }


    @property
    def df(self):
        # defensive copy
        return self._df.copy()


    @df.setter
    def df(self, df):
        self._df = df
    

    @property
    def df_types(self):
        # defensive copy
        return deepcopy(self._df_types)


    @df_types.setter
    def df_types(self, df_types):
        self._df_types = df_types


    def get_all_column_info(self, max_col_print=None):
        print(f"Number of columns: {len(self._df.columns)}")
        for idx, col in enumerate(self._df.columns):
            print(f"column {idx+1} name: {col}, type: {self._df_types[col]}")


    def help(self):
        print(VISUALIZER_HELP_MESSAGE)


    def visualize_one_column_numerical(self, df, column_name):
        """
        Helper function to visualize one column numerical column
        """
        fig, axs = plt.subplots(ncols=2)
        sns.kdeplot(data=df, x=column_name, ax=axs[0])
        sns.histplot(data=df, x=column_name, ax=axs[1])


    def visualize_one_column_categorical(self, df, column_name):
        """
        Helper function to visualize one column categorical column
        """
        fig, axs = plt.subplots(ncols=2)
        sns.histplot(data=df, x=column_name, ax=axs[0])
        plt.pie(
            list(df[column_name].value_counts().array),
            labels = list(df[column_name].value_counts().index),
            autopct='%.0f%%'
        )
        plt.show()


    def visualize_one_column(
        self,
        column_name,
        enforce_column_type=None
    ):
        df = self._df
        try:
            col_type = self._df_types[column_name]
        except KeyError:
            print(f"column name {column_name} not found in DataFrame")
        if enforce_column_type is not None and \
            enforce_column_type not in ("numerical", "categorical"):
            raise ValueError(
                f"enforce_column_type is not in ('numerical', 'categorical')"
            )
        
        if enforce_column_type is not None:
            # reset _df_types
            self._df_types[column_name] = enforce_column_type
            # numerical column visualization
            if enforce_column_type == "numerical":
                self.visualize_one_column_numerical(df, column_name)
            # categorical column visualization
            elif enforce_column_type == "categorical":
                self.visualize_one_column_categorical(df, column_name)
        else:
            if col_type == "numerical":
                self.visualize_one_column_numerical(df, column_name)
            elif col_type == "categorical":
                self.visualize_one_column_categorical(df, column_name)
    

    def visualize_two_columns(
        self,
        column_names,
    ):
        df = self._df
        if len(column_names) != 2:
            raise ValueError(VISUALIZER_TWO_COLUMNS_HELP_MESSAGE)
        col_types = set(column_names)
        if len(col_types) == 1:
            if "numerical" in col_types: # numerical - numerical
                sns.scatterplot(data=df, x=column_names[0], y=column_names[1])
            elif "categorical" in col_types: # categorical - categorical
                # Not tested
                sns.heatmap(data=df[[column_names[0], column_names[1]]], annot=True)
        else: # numerical - categorical
            fig, axs = plt.subplots(nrows=2, ncols=2)
            fig.set_figheight(10)
            fig.set_figwidth(10)
            sns.stripplot(
                data=df,
                x=column_names[0],
                y=column_names[1],
                ax=axs[0,0]
            )
            sns.swarmplot(
                data=df,
                x=column_names[0],
                y=column_names[1],
                ax=axs[0,1]
            )
            sns.boxplot(
                data=df,
                x=column_names[0],
                y=column_names[1],
                ax=axs[1,0]
            )
            sns.violinplot(
                data=df,
                x=column_names[0],
                y=column_names[1],
                ax=axs[1,1]
            )


    def visualize_pca_nd(self, hue_column, dimension):
        """
        Helper function to visualize n-dimensional PCA result
        """
        # hue column must be categorical and should exist
        df = self._df
        RANDOM_STATE = 42
        pca = PCA(n_components=dimension, random_state=RANDOM_STATE)
        components = pca.fit_transform(df.loc[:, ~df.columns.isin([hue_column])])
        total_var = pca.explained_variance_ratio_.sum() * 100
        y = df[hue_column]
        if dimension == 2:
            labels = {'0': 'PC 1', '1': 'PC 2'}
            fig = px.scatter(
            components, x=0, y=1,color=y,
            title=f'Total Explained Variance: {total_var:.2f}%',
            labels=labels,
            width=800, height=800,
            )
        elif dimension == 3:
            labels = {'0': 'PC 1', '1': 'PC 2', '2': 'PC 3'}
            fig = px.scatter_3d(
                components, x=0, y=1, z=2, color=y,
                title=f'Total Explained Variance: {total_var:.2f}%',
                labels=labels,
                width=800, height=800,
            )
        fig.show()


    def visualize_pca_2d(self, hue_column):
        self.visualize_pca_nd(hue_column, dimension=2)
    

    def visualize_pca_3d(self, hue_column):
        self.visualize_pca_nd(hue_column, dimension=3)
