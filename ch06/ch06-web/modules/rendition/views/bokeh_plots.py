
from modules.rendition import rendition_bp
from flask import  request, render_template, current_app

from bokeh.plotting import figure
from bokeh.embed import components

from pandas import read_excel
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os

from exceptions.custom import (NoneFilenameException, InvalidTypeException, 
                    MissingFileException, FileSavingException)

@rendition_bp.route('/bokeh/hpi/line', methods = ['GET', 'POST'])
def create_bokeh_line():
    if request.method == 'GET':
        script = None
        div = None
    else:
        uploaded_file:FileStorage = request.files['data_file']
        filename = secure_filename(uploaded_file.filename)
        if filename == '':
            raise NoneFilenameException()
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in current_app.config['UPLOAD_FILE_TYPES']:
            raise InvalidTypeException()
        if  uploaded_file.filename == '' or uploaded_file == None:
            raise MissingFileException()
        try:
            df = read_excel(uploaded_file, sheet_name=1, skiprows=[1])
            x = df.index.values
            y = df['UK']
            plot = figure(max_width=600, max_height=800,title=None, toolbar_location="below", background_fill_color="#FFFFCC", x_axis_label='Period by Quarter ID', y_axis_label='Nominal HPI')
            plot.line(x,y, line_width=4, color="#CC0000")

            script, div = components(plot)
        except:
            raise FileSavingException()
   
    return render_template('bokeh.html', script=script, div=div, title="Line Graph of UK's Nominal HPI") 