"""Annotator class for datapilot library"""

from copy import deepcopy
import os

import ipywidgets as widgets
from IPython.display import display, Markdown
import markdown

from constants.help_message import ANNOTATOR_HELP_MESSAGE
from constants.markdown_template import MARKDOWN_TEMPLATE
from utils.print_util import print_divider


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

    def get_all_annotation(self):
        full_annot_path = os.path.join(
            self.annotation_project_path, "_datapilot_annotations"
        )
        if not os.path.isdir(full_annot_path):
            raise FileNotFoundError(f"{full_annot_path} does not exist")
        else:
            print("List of all annotations")
            print_divider()
            for filename in os.listdir(full_annot_path):
                print(os.path.splitext(filename)[0])
            print_divider()


    def create_annotation(self):
        # choose file format
        # input title, or filename
        title = input("Enter title of new annotation")
        # input content
        layout=widgets.Layout(height="auto", width="auto")
        text_area = widgets.Textarea(
            value=MARKDOWN_TEMPLATE,
            layout=layout,
            rows=10
        )
        submit_button=widgets.Button(description='Save content',button_style='success')
        def on_button_clicked(b):
            if b.button_style == 'success':
                with open(f"./_datapilot_annotations/{title}.md", "w", encoding="utf-8") as output_file:
                    output_file.write(text_area.value)
            text_area.value = ""
            text_area.disabled=True
            b.description="Saved"
            b.button_style="info"
            b.disabled=True
        display(text_area,submit_button)
        submit_button.on_click(on_button_clicked)


    def view_annotation(self, title):
        try:
            print_divider()
            display(Markdown(f"./_datapilot_annotations/{title}.md"))
            print_divider()
        except FileNotFoundError:
            print(f"Annotation with title={title} not found")


    def edit_annotation(self, title):
        try:
            # plain text
            with open(f"./_datapilot_annotations/{title}.md", 'r') as f:
                md_content = f.read()
            # read as html
            # f = open(f"./_datapilot_annotations/{title}.md", 'r')
            # htmlmarkdown=markdown.markdown(f.read())
            layout=widgets.Layout(height="auto", width="auto")
            text_area = widgets.Textarea(
                value=md_content,
                layout=layout,
                rows=10
            )
            submit_button=widgets.Button(description='Save content',button_style='success')
            def on_button_clicked(b):
                if b.button_style == 'success':
                    with open(f"./_datapilot_annotations/{title}.md", "w", encoding="utf-8") as output_file:
                        output_file.write(text_area.value)
                text_area.value = ""
                text_area.disabled=True
                b.description="Saved"
                b.button_style="info"
                b.disabled=True
            display(text_area,submit_button)
            submit_button.on_click(on_button_clicked)
        except FileNotFoundError:
            print(f"Annotation with title={title} not found")


    def remove_annotation(self):
        print("remove annotation")


    def load_annotation(self, path):
        print("load annotation")
    

    def search_annotation(self):
        print("search annotation")
