import os
import subprocess
from airflow.exceptions import AirflowException
from airflow.models import BaseOperator
from airflow.utils import apply_defaults

class MyCustomOperator(BaseOperator):
    
    ui_color = '#7A97BF'
    ui_color_fg = '#7A97BF'
    
    template_fields = ()
    
    @apply_defaults
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)


    def my_task(self):
        # Your code here
        pass
       

    def execute(self, context):
        self.my_task()
