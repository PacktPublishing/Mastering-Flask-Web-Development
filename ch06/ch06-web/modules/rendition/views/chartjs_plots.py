from modules.rendition import rendition_bp
from flask import render_template, request, current_app

from pandas import read_excel
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os

from exceptions.custom import (NoneFilenameException, InvalidTypeException, 
                MissingFileException, FileSavingException)

@rendition_bp.route("/chartjs/hpi/bar", methods = ['GET', 'POST'])
async def create_chartjs_bar():
    if request.method == 'GET':
        bar_labels = []
        bar_values = []
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
            bar_labels=df.loc[: , 'Australia':'US'].columns.to_list()
            bar_values=df.loc[: , 'Australia':'US'].mean().to_list()
    
        except:
            raise FileSavingException()
        
    return render_template('bar_chart.html', title='Bar Graph for HPI values', labels=bar_labels, values=bar_values), 200

@rendition_bp.route("/chartjs/hpi/line", methods = ['GET', 'POST'])
async def create_chartjs_line():
    if request.method == 'GET':
        bar_labels = []
        bar_values = []
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
            bar_labels=df.loc[: , 'Australia':'US'].columns.to_list()
            bar_values=df.loc[: , 'Australia':'US'].mean().to_list()
    
        except:
            raise FileSavingException()
        
    return render_template('line_chart.html', title='Line Graph for HPI values', max=200, labels=bar_labels, values=bar_values), 200 

@rendition_bp.route("/chartjs/hpi/pie", methods = ['GET', 'POST'])
async def create_chartjs_pie():
    if request.method == 'GET':
        values = []
        labels = []
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
            labels=df.loc[: , 'Australia':'US'].columns.to_list()
            values=df.loc[: , 'Australia':'US'].mean().to_list()
    
        except:
            raise FileSavingException()
        
    return render_template('pie_chart.html', title='Bitcoin Monthly Price in USD', max=200, labels=labels, values=values)


    
    
