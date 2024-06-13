from modules.rendition import rendition_bp
from flask import  render_template, request, current_app

import json
import plotly
import plotly.express as px

from pandas import read_csv
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os

from exceptions.custom import (NoneFilenameException, InvalidTypeException, 
                MissingFileException, FileSavingException)

@rendition_bp.route("/plotly/csv/bedprice", methods = ['GET', 'POST'])
async def create_plotly_stacked_bar():
    if request.method == 'GET':
        graphJSON = '{}'
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
            df_csv = read_csv(uploaded_file)
            fig = px.bar(df_csv, x='Bedrooms', y='Price', color='FurnishingStatus', barmode='group')
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
        except:
            raise FileSavingException()
        
    return render_template('plotly.html', graphJSON=graphJSON, title="Stacked Bar Graph of Bedroom vs Price per Furnishing Status")

