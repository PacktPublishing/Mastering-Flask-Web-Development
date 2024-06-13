from modules.rendition import rendition_bp, environ
from flask import send_from_directory, request, render_template, current_app
from datetime import datetime

from jinja2 import Template


from pylatex import Document, Section, Command, NoEscape, Subsection, Tabular, Center
from pylatex.utils import italic
from pylatex.basic import NewLine

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os
from pandas import read_excel # install rlrd

from exceptions.custom import(NoneFilenameException, InvalidTypeException, 
                MissingFileException, FileSavingException)



@rendition_bp.route('/create/hpi/desc/latex', methods = ['GET', 'POST'])
async def create_latex_pdf():
    
    if request.method == 'GET':
          return render_template("hpi_latex_form.html"), 200 
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
            df = read_excel(uploaded_file, sheet_name=2, skiprows=[1])
            hpi_data = df.loc[: , 'Australia':'US'].describe().to_dict()
                     
            hpi_filename = os.path.join('./files/latex','hpi_analysis')
            geometry_options = {
                "landscape": True,
                "margin": "0.5in",
                "headheight": "20pt",
                "headsep": "10pt",
                "includeheadfoot": True
            }
            doc = Document(page_numbers=True, geometry_options=geometry_options, document_options=['10pt','legalpaper'])
            doc.preamble.append(Command('title', 'Mean HPI per Country'))
            doc.preamble.append(Command('author', 'Sherwin John C. Tragura'))
            doc.preamble.append(Command('date', NoEscape(r'\today')))
            doc.append(NoEscape(r'\maketitle'))
            
            # creating a pdf with title "the simple stuff"
            with doc.create(Section('The Data Analysis')):
                doc.append('Here are the statistical anaysis derived from the upladed excel data.')
                
               
                # creating subsection of a pdf
                with doc.create(Subsection('Statistical analysis generated by Pandas')):
                    with doc.create(Tabular('| c | c | c | c | c | c | c | c | c |')) as table:
                        table.add_hline()
                        table.add_row(("Country", "Count", "Mean", "Std Dev", "Min", "25%", "50%", "75%", "Max"))
                        table.add_empty_row()
                    
                        for key, value in hpi_data.items():
                            table.add_hline()
                            print(key, value['count'], value['mean'], value['std'], value['min'], value['25%'], value['50%'], value['75%'], value['max'])
                            table.add_row((key, value['count'], value['mean'], value['std'], value['min'], value['25%'], value['50%'], value['75%'], value['max']))
                        table.add_empty_row()
                        table.add_hline()
        except:
            raise FileSavingException()
        
        doc.generate_pdf(hpi_filename, clean_tex=False, compiler="pdflatex")
        return send_from_directory('./files/latex', 'hpi_analysis.pdf')

@rendition_bp.route('/render/hpi/plot/eqns', methods = ['GET', 'POST'])
async def convert_latex():
    tpl:Template = environ.get_template('/latex/hpi_plot.tex')
    outpath=os.path.join('./files/latex','hpi_plot.pdf')
    outfile=open(outpath,'w')
    outfile.write(await tpl.render_async(author='Sherwin John Tragura', title="Rendering HPI Plot with LaTeX", date=datetime.now().strftime("%B %d, %Y"), renderTbl=True))
    outfile.close()
    os.system("pdflatex -output-directory=" + './files/latex' + " " + outpath)
    return send_from_directory('./files/latex', 'hpi_plot.pdf')