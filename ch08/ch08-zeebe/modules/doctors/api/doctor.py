import os
from flask import request, jsonify
from modules.doctors import doc_bp
from modules.doctors.services.diagnosis_tasks import run_zeebe_task, deploy_zeebe_wf
from modules.settings import Zeebe


@doc_bp.get("/diagnosis/bpmn/deploy")
async def deploy_diagnosis_analysis_bpmn():
    try:
        filepath = os.path.join(Zeebe.BPMN_DUMP_PATH, "dams_diagnosis.bpmn")
        print(filepath)
        task = deploy_zeebe_wf.apply_async(args=[filepath])
        result = task.get()
        return jsonify(data=result), 201
    except Exception as e:
            print(e)
    return jsonify(data="error"), 500
    
@doc_bp.post("/diagnosis/analysis/text")
async def extract_analysis_text(): 
        try:
            data = request.get_json()
            docid = data['docid']
            patientid = int(data['patientid'])
            task = run_zeebe_task.apply_async(args=[docid, patientid])
            result = task.get()
            return jsonify(result), 201
        except Exception as e:
            print(e)
        return jsonify(data="error"), 500
    
    


