from modules.upload import upload_bp

from flask import render_template, request, current_app

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os


from pandas import read_csv, read_excel # install rlrd
from numpy import arange

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import statsmodels.api as sm
import seaborn as sbn
import matplotlib

import base64
from io import BytesIO

from exceptions.custom import (NoneFilenameException, InvalidTypeException, 
                MissingFileException, FileSavingException)


@upload_bp.route("/upload/xlsx/rhpi/plot/belgium", methods = ['GET', 'POST'])
async def upload_xlsx_hpi_belgium_plot():
    if request.method == 'GET':
        data = None
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
            df_rhpi = read_excel(uploaded_file, sheet_name=2, usecols='C', skiprows=[1])
            array_rhpi = df_rhpi.to_numpy().flatten()
            array_hpi_index = arange(0, array_rhpi.size )
            fig = Figure(figsize=(6, 6), dpi=72, edgecolor='r', linewidth=2, facecolor='y')
            axes = fig.subplots()
            
            axes.plot(array_hpi_index, array_rhpi, color='#fc0366')
            axes.set_xlabel('Quarterly Duration')
            axes.set_ylabel('House Price Index')
            axes.set_title("Belgium's HPI versus RHPI")
            axes.set_facecolor('#000000')
            axes.spines['bottom'].set_edgecolor('#fca103')
            axes.spines['bottom'].set_linewidth(3)
            axes.spines['top'].set_edgecolor('#fca103')
            axes.spines['top'].set_linewidth(3)
            axes.spines['right'].set_edgecolor('#fca103')
            axes.spines['right'].set_linewidth(3)
            axes.spines['left'].set_edgecolor('#fca103')
            axes.spines['left'].set_linewidth(3)
            axes.xaxis.label.set_color('#000')
            axes.yaxis.label.set_color('#000')
            axes.tick_params(colors='#000', which='both') 
                
            file_loc = "./files/xlsx/"
            uploaded_file.save(file_loc + uploaded_file.filename)
            output = BytesIO()
            fig.savefig(output, format="png")
            data = base64.b64encode(output.getbuffer()).decode("ascii")
        except:
            raise FileSavingException()
        
    return render_template("file_upload_xlsx_form.html", data=data), 200 


@upload_bp.route("/upload/xlsx/rhpi/hpi/plot/belgium", methods = ['GET', 'POST'])
async def upload_xlsx_belgium_hpi_rhpi_plot():
    if request.method == 'GET':
        data = None
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
            df_hpi = read_excel(uploaded_file, sheet_name=1, usecols='C', skiprows=[1])
            df_rhpi = read_excel(uploaded_file, sheet_name=2, usecols='C', skiprows=[1])
            array_hpi = df_hpi.to_numpy().flatten()
            array_hpi_index = arange(0, df_rhpi.size )
            array_rhpi = df_rhpi.to_numpy().flatten()
            array_rhpi_index = arange(0, df_rhpi.size )
            
            fig = Figure(figsize=(7, 7), dpi=72, edgecolor='#140dde', linewidth=2, facecolor='#b7b6d4')
            axes = fig.subplots()
            
            lbl1, = axes.plot(array_hpi_index ,array_hpi, color="#32a8a2")
            lbl2, = axes.plot(array_rhpi_index ,array_rhpi, color="#bf8a26")
            axes.set_xlabel('Quarterly Duration')
            axes.set_ylabel('House Price Index')
            axes.legend([lbl1, lbl2], ["HPI", "RHPI"])
            axes.set_title("Belgium's HPI versus RHPI")
            axes.set_facecolor('#100f52')
            axes.xaxis.label.set_color('#100f52')
            axes.yaxis.label.set_color('#100f52')
            axes.spines['bottom'].set_edgecolor('#100f52')
            axes.spines['bottom'].set_linewidth(3)
            axes.spines['top'].set_edgecolor('#100f52')
            axes.spines['top'].set_linewidth(3)
            axes.spines['right'].set_edgecolor('#100f52')
            axes.spines['right'].set_linewidth(3)
            axes.spines['left'].set_edgecolor('#100f52')
            axes.spines['left'].set_linewidth(3)
            axes.tick_params(colors='#100f52', which='both') 
           
            file_loc = "./files/xlsx/"
            uploaded_file.save(file_loc + uploaded_file.filename)
            output = BytesIO()
            fig.savefig(output, format="png")
            data = base64.b64encode(output.getbuffer()).decode("ascii")
        except:
            raise FileSavingException()
        
    return render_template("file_upload_xlsx_sheets_form.html", data=data), 200 

@upload_bp.route("/upload/xlsx/multi/subplot", methods = ['GET', 'POST'])
async def upload_xlsx_multi_subplots():
    if request.method == 'GET':
        data = None
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
            matplotlib.use('agg')
            fig = plt.figure(figsize=(12, 12))
            axes1 = fig.add_subplot(2, 2, 1)
            axes2 = fig.add_subplot(2, 2, 2)
            axes3 = fig.add_subplot(2, 2, 3)
            axes4 = fig.add_subplot(2, 2, 4)
            
            axes1.plot(df_xlsx.index.values, df_xlsx['Australia'], 'green', 
                       df_xlsx.index.values, df_xlsx['Belgium'], 'red',)
            axes1.set_xlabel('Quarterly Duration')
            axes1.set_ylabel('House Price Index')
            axes1.set_title('RHPI between Australia and Belgium')
            
            index = arange(df_xlsx.loc[: , 'Australia':'US'].shape[1])
            axes2.bar(index, df_xlsx.loc[: , 'Australia':'US'].mean(), color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
            axes2.set_xlabel('Country ID')
            axes2.set_ylabel('Mean HPI')
            axes2.set_xticks(index)
            axes2.set_title('Mean RHPI among countries')
            
            axes3.plot(df_xlsx.loc[: , 'Australia':'US'])
            axes3.set_xlabel('Quarterly Duration')
            axes3.set_ylabel('House Price Index')
            axes3.set_title('RHPI trend among countries')
            
            width = 0.3
            axes4.bar(df_xlsx.loc[0:3, 'Japan'].index.values-width, df_xlsx.loc[0:3, 'Japan'], width=width, color='#d9182b', label="JP")
            axes4.bar(df_xlsx.loc[0:3, 'S. Korea'].index.values, df_xlsx.loc[0:3, 'S. Korea'], width=width, color='#f09ec1', label="SK")
            axes4.bar(df_xlsx.loc[0:3, 'New Zealand'].index.values+width, df_xlsx.loc[0:3, 'New Zealand'], width=width, color='#000', label="NZ")
            axes4.set_xlabel('Quarterly Duration')
            axes4.set_ylabel('House Price Index')
            axes4.set_title('RHPI of Japan, South Korea, and New Zealand')
            axes4.set_xticks(df_xlsx.loc[0:3, 'New Zealand'].index.values)
            axes4.legend()
            
                
            file_loc = "./files/xlsx/"
            uploaded_file.save(file_loc + uploaded_file.filename)
            output = BytesIO()
            fig.savefig(output, format="png")
            data = base64.b64encode(output.getbuffer()).decode("ascii")
        except:
            raise FileSavingException()
        
    return render_template("file_upload_xlsx_subplots_form.html", data=data), 200 
        

@upload_bp.route("/upload/csv/seaborn", methods = ['GET', 'POST'])
async def upload_csv_seaborn():
    if request.method == 'GET':
        data = None
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
            matplotlib.use('agg') # UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
            fig = plt.figure()
            axes = fig.add_subplot(1, 1, 1)
            sbn.scatterplot(y="Bathrooms", x="Bedrooms", data=df_csv, ax=axes)
           
            axes.set_title("Scatter Plot Bath vs Bed")
            axes.set_xlabel("Bathrooms")
            axes.set_ylabel("Bedrooms")
            axes.set_xticks(arange(10))
            axes.set_yticks(arange(10))
           
            
            file_loc = "./files/csv/"
            uploaded_file.save(file_loc + uploaded_file.filename)
            output = BytesIO()
            fig.savefig(output, format="png")
            data = base64.b64encode(output.getbuffer()).decode("ascii")
        except:
            raise FileSavingException()
        
    return render_template("file_upload_csv_form.html", data=data), 200 


@upload_bp.route("/upload/csv/pie", methods = ['GET', 'POST'])
async def upload_csv_pie():
    if request.method == 'GET':
        data = None
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
            matplotlib.use('agg') # UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
            fig = plt.figure()
            axes = fig.add_subplot(1, 1, 1)
            explode = (0.1, 0, 0)
            axes.pie(df_csv.groupby(['FurnishingStatus'])['Price'].count(), colors=['#bfe089', '#ebd05b', '#e67eab'],
            labels =["Furnished","Semi-Furnished","Unfurnished"], autopct ='% 1.1f %%',
            shadow = True, startangle = 90, explode=explode)
            axes.axis('equal')
            axes.legend(loc='lower right',fontsize=7, bbox_to_anchor = (0.75, -01.0) )
           
            
            file_loc = "./files/csv/"
            uploaded_file.save(file_loc + uploaded_file.filename)
            output = BytesIO()
            fig.savefig(output, format="png")
            data = base64.b64encode(output.getbuffer()).decode("ascii")
        except:
            raise FileSavingException()
        
    return render_template("file_upload_csv_pie_form.html", data=data), 200

@upload_bp.route("/upload/stats/plots", methods = ['GET', 'POST'])
async def stat_plots():
    if request.method == 'GET':
        data = None
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
            model = sm.formula.ols("Price ~ Area", data=df_csv).fit()
            price_pred = model.predict()
            
            fig = plt.figure()
            axes = fig.add_subplot(1, 1, 1)
            axes.scatter(df_csv['Area'], df_csv['Price'])
            axes.plot(df_csv['Area'], price_pred, color='red')
           
           
            
            file_loc = "./files/csv/"
            uploaded_file.save(file_loc + uploaded_file.filename)
            output = BytesIO()
            fig.savefig(output, format="png")
            data = base64.b64encode(output.getbuffer()).decode("ascii")
        except:
            raise FileSavingException()
        
    return render_template("file_upload_csv_stats_form.html", data=data), 200
