import gladiator as gl
from modules.equations import eqn_bp
from flask import render_template, request
from sympy import symbols, sympify, solve

@eqn_bp.route('/eqn/eqnsystem/solve', methods = ['GET', 'POST'])
async def solve_multiple_eqns():
    if request.method == 'GET':
        soln = None
    else:
        field_validations = (
            ('polyeqn1', gl.required, gl.type_(str)),
            ('polyeqn2', gl.required, gl.type_(str))
        )
        form_data = request.form.to_dict()
        result = gl.validate(field_validations, form_data )
        print(bool(result))
        if bool(result):
            x, y = symbols('x y')
            eqn1 = sympify(form_data['polyeqn1'])
            eqn2 = sympify(form_data['polyeqn2'])
            soln = solve((eqn1, eqn2),(x, y))
        else:
            soln = None
       
    return render_template('complex_multiple_eqns_form.html', soln=soln), 200

