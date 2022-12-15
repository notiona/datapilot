"""Annotator class for datapilot library"""

from copy import deepcopy
import os

import ipywidgets as widgets
from IPython.display import display

from constants.help_message import ANNOTATOR_HELP_MESSAGE

class Annotator():
    """
    Annotator class for datapilot library
    """

    def __init__(self, path):
        self.configure_current_annotation(path)


    @property
    def annotation_project_path(self):
        # defensive copy
        return deepcopy(self._annotation_project_path)


    @annotation_project_path.setter
    def annotation_project_path(self, path):
        self._annotation_project_path = path


    def configure_current_annotation(self, path):
        self._annotation_project_path = path
        full_annot_path = os.path.join(
            self.annotation_project_path, "_datapilot_annotations"
        )
        os.makedirs(full_annot_path,exist_ok=True)


    def help(self):
        print(ANNOTATOR_HELP_MESSAGE)


    def create_annotation(self):
        # choose file format
        # input title, or filename
        title = input("Enter title of new annotation")
        print(title)
        # input content
        text_area = widgets.Textarea()
        submit_button=widgets.Button(description='Save content',button_style='success')
        def on_button_clicked(b):
            print(text_area.value)
        display(text_area,submit_button)
        submit_button.on_click(on_button_clicked)
        

    def get_all_annotation(self):
        full_annot_path = os.path.join(
            self.annotation_project_path, "_datapilot_annotations"
        )
        if not os.path.isdir(full_annot_path):
            raise FileNotFoundError(f"{full_annot_path} does not exist")
        else:
            print("List of all annotations")
            for filename in os.listdir(full_annot_path):
                print(os.path.splitext(filename)[0])


    def edit_annotation(self):
        print("edit annotation")


    def remove_annotation(self):
        print("remove annotation")


    def view_annotation(self):
        print("view annotation")


    def load_annotation(self, path):
        print("load annotation")
    

    def search_annotation(self):
        print("search annotation")
