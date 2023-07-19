import base64
import os
import re
import requests
import gradio as gr
import modules.scripts as scripts

from datetime import datetime
from io import BytesIO
from modules.processing import process_images, Processed


aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', '')

class CrossPrompter(scripts.Script):
    def title(self):
        return ""

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        checkbox_create_cross_ref_prompts = gr.inputs.Checkbox(label="Create Cross Reference Prompts", default=False)
        # bucket_name = gr.inputs.Textbox(label="Bucket Name", placeholder="Enter Bucket Name")
        # collection_name = gr.inputs.Textbox(label="Bucket Path", placeholder="Enter Bucket path")
        return [checkbox_create_cross_ref_prompts]

    def before_process_batch(self, p, checkbox_create_cross_ref_prompts, **kwargs):
        # curl -L "https://docs.google.com/spreadsheets/d/1k_VNVkeLE0fmNZTlT5quAWXodwgTQUO7GDVUlJ_IKnw/export?exportFormat=csv"
        if not checkbox_create_cross_ref_prompts:
            return True
        cross_ref_csv = requests.get('https://docs.google.com/spreadsheets/d/1k_VNVkeLE0fmNZTlT5quAWXodwgTQUO7GDVUlJ_IKnw/export?exportFormat=csv')
        print(f"Returned Cross Reference CSV file: {cross_ref_csv.json()}")
        print(f"process {p}")
        print(f"cross ref prompts checkbox {checkbox_create_cross_ref_prompts}")
        # print(f"*args {args}")
        print(f"*kwargs {kwargs}")
        pass