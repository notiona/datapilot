"""DataAnalyst class for datapilot library"""

from copy import deepcopy

import pandas as pd

from constants.help_message import DATA_ANALYST_HELP_MESSAGE
from constants.dtype_classifier import DTYPE_MAPPING
from constants.suspicious_values import SUSPICIOUS_VALUES
from utils.print_util import print_divider

class DataAnalyst():
    """
    DataAnalyst class for datapilot library
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


    def help(self):
        print(DATA_ANALYST_HELP_MESSAGE)
    

    def get_all_column_info(self, max_col_print=None):
        print(f"Number of columns: {len(self._df.columns)}")
        for idx, col in enumerate(self._df.columns):
            print(f"column {idx+1} name: {col}, type: {self._df_types[col]}")
    

    def column_type_detector(self, col):
        DTYPE_THRESHOLD = 0.1
        value_counts_series = self._df[col].value_counts()
        ratio = len(value_counts_series) / len(self._df)
        return "numerical" if ratio > DTYPE_THRESHOLD else "categorical"


    def inspect_data(self):
        print("Report for dataframe")
        print_divider()
        print("pandas dataframe report:")
        self._df.info()
        print_divider()
        print("column type detection report:")
        for col in self._df.columns:
            print(f"column: {col}: ")
            pd_type = DTYPE_MAPPING[str(self._df.dtypes[col])]
            dp_type = self.column_type_detector(col)
            if pd_type == dp_type:
                print(f"\tdetected type: {pd_type}")
            else:
                print(
                    "Warning! Detected type different! "
                    "Please assign numerical/categorical manually."
                )
                print(f"\tpandas detected type: {pd_type}")
                print(f"\tdatapilot detected type: {dp_type}")
        print_divider()


    def detect_suspicious(self):
        df = self._df
        for susp in SUSPICIOUS_VALUES:
            if len(df[df.eq(susp).any(axis=1)]):
                print(f"Suspicious value {susp} detected!")
                print_divider()
                print(df[df.eq(susp).any(axis=1)])
                print_divider()


    def detect_missing(self):
        df = self._df
        if len(df[df.isna().any(axis=1)]):
            print("Missing rows detected")
            print_divider()
            print(df[df.isna().any(axis=1)])
            print_divider()
        else:
            print("No missing value detected")


    def detect_duplicate(self):
        df = self._df
        if len(df[df.duplicated(keep=False)]):
            print("Duplicate rows detected")
            print_divider()
            print(df[df.duplicated(keep=False)])
            print_divider()
        else:
            print("No duplicate row detected")


    def custom_feature_engineering(self, func):
        # Get all positional args which are existing column names
        col_names = func.__code__.co_varnames
        for col_name in col_names:
            if col_name not in self._df.columns:
                raise ValueError(f"column {col_name} not in df columns")
        # create new column with given function name, using unpack syntax
        self._df[func.__name__] = \
            func(*(self._df[col_name] for col_name in col_names))
        print(self._df)


    def analyze_merge_ability(self):
        pass    
