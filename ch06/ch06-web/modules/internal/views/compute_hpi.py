from modules.internal import internal_bp
from flask import render_template, request, current_app

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os

from exceptions.custom import (NoneFilenameException, InvalidTypeException, 
                MissingFileException, FileSavingException)
from pandas import read_excel # install rlrd
from json import dumps

from modules.internal.services.hpi_formula import compute_hpi_laspeyre


@internal_bp.route("/upload/xlsx/house/prices", methods = ['GET', 'POST'])
async def compute_laspeyre_hpi():
    if request.method == 'GET':
        hpi_value = None
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
             df_prices = read_excel(uploaded_file, sheet_name=0, skiprows=[1])
             df_json = dumps(df_prices.to_dict())
             task = compute_hpi_laspeyre.apply_async(args=[df_json])
             hpi_value = task.get()
        except Exception as e:
            print(e)
            raise FileSavingException()
        
    return render_template("compute_hpi_form.html", hpi=hpi_value), 200 


