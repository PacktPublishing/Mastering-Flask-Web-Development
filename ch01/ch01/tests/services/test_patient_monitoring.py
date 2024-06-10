import pytest
from services.patient_monitoring import record_patient_exam

@pytest.fixture
def exam_details():
     params = dict()
     params['pid'] = 1111
     params['qid'] = 568
     params['score'] = 87
     params['total'] = 100
     yield params
     
def test_record_patient_exam(exam_details):
    result = record_patient_exam(exam_details)
    assert result is True