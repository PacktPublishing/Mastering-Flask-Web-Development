from flask import Blueprint
from jinja2 import FileSystemLoader, Environment
from latex.jinja2 import make_env

rendition_bp = Blueprint("rendition_bp", __name__, template_folder="pages", static_folder="resources", 
                       static_url_path="static", url_prefix="/ch06")

environ:Environment = make_env(loader=FileSystemLoader('files'), enable_async=True,
                block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = 'VAR{',
    variable_end_string = '}',
    comment_start_string = '#{',
    comment_end_string = '}',
    line_statement_prefix = '%-',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,)

import modules.rendition.views.plotly_plots
import modules.rendition.views.chartjs_plots
import modules.rendition.views.bokeh_plots
import modules.rendition.views.pdf_latex_transformation



