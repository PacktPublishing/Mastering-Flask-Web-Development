from modules.equations import eqn_bp
from flask import render_template, request
import gladiator as gl

from sympy import symbols, sympify
from sympy.plotting import plot 
import matplotlib

import base64
from io import BytesIO
from PIL import Image

@eqn_bp.route('/eqn/single/plot', methods = ['GET', 'POST'])
async def plot_equation():
    if request.method == 'GET':
        data = None
    else:
        field_validations = (
            ('equation', gl.required, gl.type_(str)),
            ('maxval', gl.required, gl.type_(str), gl.regex_('[0-9]+')),
            ('minval', gl.required, gl.type_(str), gl.regex_('[0-9]+')) 
        )
        form_data = request.form.to_dict()
        result = gl.validate(field_validations, form_data )
        upperbound = float(form_data['maxval'])
        lowerbound = float(form_data['minval'])
        data = None
        
        if bool(result) and lowerbound <= upperbound:
            matplotlib.use('agg')
            x = symbols('x')
            eqn = sympify(form_data['equation'])
            graph = plot(eqn, (x, lowerbound, upperbound), line_color='red', show=False)
            filename = "./files/img/simple_plot.png"
            graph.save(filename)
            
            img = Image.open(filename)
            image_io = BytesIO()
            img.save(image_io, 'PNG')
            data = base64.b64encode(image_io.getbuffer()).decode("ascii")
    return render_template('plot_eqn_form.html', data=data), 200

@eqn_bp.route('/eqn/multi/plot', methods = ['GET', 'POST'])
async def plot_two_equations():
    if request.method == 'GET':
        data = None
    else:
        field_validations = (
            ('equation1', gl.required, gl.type_(str)),
            ('equation2', gl.required, gl.type_(str)),
            ('eqn1_maxval', gl.required, gl.type_(str), gl.regex_('[0-9]+')),
            ('eqn1_minval', gl.required, gl.type_(str), gl.regex_('[0-9]+')),
            ('eqn2_maxval', gl.required, gl.type_(str), gl.regex_('[0-9]+')),
            ('eqn2_minval', gl.required, gl.type_(str), gl.regex_('[0-9]+')), 
        )
        form_data = request.form.to_dict()
        result = gl.validate(field_validations, form_data )
        eqn1_upper = float(form_data['eqn1_maxval'])
        eqn1_lower = float(form_data['eqn1_minval'])
        eqn2_upper = float(form_data['eqn2_maxval'])
        eqn2_lower = float(form_data['eqn2_minval'])
        data = None
        if bool(result) and (eqn1_lower <= eqn1_upper) and (eqn2_lower <= eqn2_upper):
            matplotlib.use('agg')
            x = symbols('x')
            eqn1 = sympify(form_data['equation1'])
            eqn2 = sympify(form_data['equation2'])
            graph = plot(eqn1, (x, eqn1_lower, eqn1_upper), line_color='red', show=False)
            graph.extend(plot(eqn2, (x, eqn2_lower, eqn2_upper), line_color='blue', show=False))
            filename = "./files/img/multi_plot.png"
            graph.save(filename)
           
            img = Image.open(filename)
            image_io = BytesIO()
            img.save(image_io, 'PNG')
            
            data = base64.b64encode(image_io.getbuffer()).decode("ascii")
    return render_template('plot_two_eqns_form.html', data=data), 200