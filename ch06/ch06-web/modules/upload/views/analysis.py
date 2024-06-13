from modules.upload import upload_bp
from flask import render_template, request, current_app
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os
from pandas import read_excel
from exceptions.custom import (NoneFilenameException, InvalidTypeException, 
                MissingFileException, FileSavingException)

@upload_bp.route('/upload/xlsx/analysis', methods = ["GET", "POST"])
async def show_analysis():
    if request.method == 'GET':
        df_tbl = None 
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
            df_xlsx = read_excel(uploaded_file, sheet_name=2, skiprows=[1])
            df_tbl = df_xlsx.loc[: , 'Australia':'US'].describe().to_html()
        except:
            raise FileSavingException()
        
    return render_template("file_upload_pandas_xlsx.html", table=df_tbl), 200 