import base64
import os
import re
import gradio as gr
import modules.scripts as scripts

from datetime import datetime
from io import BytesIO
from modules.processing import process_images, Processed


aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', '')

boto3_session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

s3_client = boto3_session.client('s3')

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
        if not checkbox_create_cross_ref_prompts:
            return True
        print(f"process {p}")
        print(f"cross ref prompts checkbox {checkbox_create_cross_ref_prompts}")
        # print(f"*args {args}")
        print(f"*kwargs {kwargs}")
        pass