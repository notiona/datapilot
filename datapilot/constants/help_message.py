"""List of help messages"""

ANNOTATOR_HELP_MESSAGE = \
"""
help():
    List all functions of Annotator
configure_current_annotation():
    Configure current annotation path
create_annotation():
    Create and save markdown or txt from jupyter to local
get_all_annotation():
    Get list of annotations of current project
edit_annotation():
    Edit annotation
remove_annotation():
    Delete annotation
view_annotation():
    Load markdown syntax from local to jupyter
load_annotation():
    Given path, merge syntax file from other project
search_annotation():
    Search by title and content of annotation
"""

DATA_ANALYST_HELP_MESSAGE = \
"""
help():
    List all functions of DataAnalyst
"""

VISUALIZER_HELP_MESSAGE = \
"""
help():
    List all functions of Visualizer
get_all_column_info():
    Get column name and type of self.df
visualize_one_column():
    Column-wise quick visualization
visualize_two_columns():
    Inter column quick visualization, depending on input type
visualize_pca_2d():
    Low-code PCA + 2d visualization
visualize_pca_3d():
    Low-code PCA + 3d visualization
"""

VISUALIZER_TWO_COLUMNS_HELP_MESSAGE = \
"""
column_names: List[str]
enforce_column_type: str
"""
