"""Predefined mapping of pandas dtype -> {numerical, categorical}"""

DTYPE_MAPPING = {
    "float64": "numerical",
    "int64": "numerical",
    "object": "categorical",
    "bool": "categorical",
    "datetime64": "numerical",
    "timedelta[ns]": "numerical",
    "category": "categorical"
}
