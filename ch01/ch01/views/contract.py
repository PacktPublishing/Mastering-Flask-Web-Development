from flask.views import MethodView, View
from flask import render_template, request
from repository.patient_contract import ( insert_patient_contract, select_all_patient_contract, 
                                         delete_patient_contract_pid, select_all_unpaid_patient)
from services.utility import list_pid

class ContractView(MethodView):
    def __init__(self):
        pass 

    def get(self):
        return render_template("contract/add_patient_contract.html")

    def post(self):
        pid = request.form['pid']
        approver = request.form['approver']
        approved_date = request.form['approved_date']
        hcp = request.form['hcp']
        payment_mode = request.form['payment_mode']
        amount_paid = request.form['amount_paid']
        amount_due = request.form['amount_due']
        result = insert_patient_contract(pid=int(pid), approved_by=approver, approved_date=approved_date, hcp=hcp, payment_mode=payment_mode,
                                amount_paid=float(amount_paid), amount_due=float(amount_due))
        if result == False:
            return render_template("contract/add_patient_contract.html")
        
        contracts = select_all_patient_contract()
        return render_template("contract/list_patient_contract.html", contracts=contracts)

class ListUnpaidContractView(View):
    def dispatch_request(self):
        contracts = select_all_unpaid_patient()
        return render_template("contract/list_patient_contract.html", contracts=contracts) 
    
class DeleteContractByPIDView(View):
    methods = ['GET', 'POST']
    
    def __init__(self):
        pass
    
    def dispatch_request(self):
        if request.method == "GET": 
            pids = list_pid()
            return render_template("contract/delete_patient_contract.html", pids=pids)
        else:
            pid = int(request.form['pid'])
            result = delete_patient_contract_pid(pid)
            if result == False:
                pids = list_pid()
                return render_template("contract/delete_patient_contract.html", pids=pids)
            
            contracts = select_all_patient_contract()
            return render_template("contract/list_patient_contract.html", contracts=contracts)
    