from modules.equations import eqn_bp
from flask import render_template, request
from sympy import sympify
import gladiator as gl

@eqn_bp.route('/eqn/simple/singlevar', methods = ['GET', 'POST'])
async def solve_univariate_linear():
    if request.method == 'GET':
        soln = None
    else:
        field_validations = (
            ('lineqn', gl.required, gl.type_(str), gl.regex_('[+\-]?(([0-9]+\.[0-9]+)|([0-9]+\.?)|(\.?[0-9]+))[+\-/*][x]([+\-/*](([0-9]+\.[0-9]+)|([0-9]+\.?)|(\.?[0-9]+))[+\-/*][x])*([+\-/*](([0-9]+\.[0-9]+)|([0-9]+\.?)|(\.?[0-9]+)))*')),
            ('xvar', gl.required, gl.type_(str), gl.regex_('[0-9]+'))
        )
        form_data = request.form.to_dict()
        result = gl.validate(field_validations, form_data )
        
        if result:
            xval = float(form_data['xvar'])
            eqn = sympify(form_data['lineqn'], {'x': xval})
            soln = eqn.evalf()
        else:
            soln = None
       
    return render_template('simple_linear_sv_form.html', soln=soln), 200

@eqn_bp.route('/eqn/simple/bivar', methods = ['GET', 'POST'])
async def solve_multivariate_linear():
    if request.method == 'GET':
        soln = None
    else:
        field_validations = (
            ('lineqn', gl.required, gl.type_(str), gl.regex_('[+\-]?(([0-9]+\.[0-9]+)|([0-9]+\.?)|(\.?[0-9]+))[+\-/*][xy]([+\-/*](([0-9]+\.[0-9]+)|([0-9]+\.?)|(\.?[0-9]+))[+\-/*][xy])*([+\-/*](([0-9]+\.[0-9]+)|([0-9]+\.?)|(\.?[0-9]+)))*')),
            ('xvar', gl.required, gl.type_(str), gl.regex_('[0-9]+')),
            ('yvar', gl.required, gl.type_(str), gl.regex_('[0-9]+')) 
        )
        form_data = request.form.to_dict()
        result = gl.validate(field_validations, form_data )
        
        if bool(result):
            xval = float(form_data['xvar'])
            yval = float(form_data['yvar'])
            eqn = sympify(form_data['lineqn'], {'x': xval, 'y': yval})
            soln = eqn.evalf()
        else:
            soln = None
       
    return render_template('simple_linear_mv_form.html', soln=soln), 200

@eqn_bp.route('/eqn/nonlinear/svar', methods = ['GET', 'POST'])
async def solve_nonlinear_model():
    if request.method == 'GET':
        soln = None
    else:
        field_validations = (
            ('nonlineqn', gl.required, gl.type_(str)),
            ('xvar', gl.required, gl.type_(str), gl.regex_('[0-9]+')) 
        )
        form_data = request.form.to_dict()
        result = gl.validate(field_validations, form_data )
        
        if bool(result):
            xval = float(form_data['xvar'])
            try:
                eqn = sympify(form_data['nonlineqn'], {'x': xval})
                soln = eqn.evalf()
            except:
                soln = None
        else:
            soln = None
    return render_template('simple_nonlinear_form.html', soln=soln), 200
