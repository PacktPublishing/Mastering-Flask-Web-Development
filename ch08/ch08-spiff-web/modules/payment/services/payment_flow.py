from SpiffWorkflow.specs.WorkflowSpec import WorkflowSpec
from SpiffWorkflow.specs.ExclusiveChoice import ExclusiveChoice
from SpiffWorkflow.specs.Simple import Simple
from SpiffWorkflow.operators import Equal, Attrib, LessThan
from SpiffWorkflow.workflow import Workflow

from SpiffWorkflow.workflow import Workflow

def tx_patient_pay(wf:Workflow, task:Simple):
    print('patient paying')
    
def tx_patient_release(wf:Workflow, task:Simple):
    print('patient release')
    
def tx_patient_onhold(wf:Workflow, task:Simple):
    print('patient onhold')

class PaymentWorkflowSpec(WorkflowSpec):
    def __init__(self):
        super().__init__()
        patient_pay = Simple(wf_spec=self, name='dams_patient_pay')
        patient_pay.ready_event.connect(callback=tx_patient_pay)
        self.start.connect(taskspec=patient_pay)
        
        payment_verify = ExclusiveChoice(wf_spec=self, name='payment_check')
        patient_pay.connect(taskspec=payment_verify)
               
        patient_release = Simple(wf_spec=self, name='dams_patient_release')
        cond = Equal(Attrib(name='amount'), Attrib(name='charge'))
        payment_verify.connect_if(condition=cond, task_spec=patient_release)
        patient_release.completed_event.connect(callback=tx_patient_release)
        
        patient_hold = Simple(wf_spec=self, name='dams_patient_onhold')
      
        payment_verify.connect(task_spec=patient_hold)
        patient_hold.completed_event.connect(callback=tx_patient_onhold)