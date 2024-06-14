from celery import shared_task
import asyncio
from pyzeebe import ZeebeClient, create_insecure_channel

channel = create_insecure_channel(hostname="localhost", port=26500)  # Will use ZEEBE_ADDRESS environment variable or localhost:26500
client = ZeebeClient(channel)

@shared_task(ignore_result=False)
def deploy_zeebe_wf(bpmn_file):
    async def zeebe_wf(bpmn_file):
        try:
            await client.deploy_process(bpmn_file)
            return True
        except Exception as e:
            print(e)
        return False
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(zeebe_wf(bpmn_file))

@shared_task(ignore_result=False)
def run_zeebe_task(docid, patientid):
    async def zeebe_task(docid, patientid):
        try:   
                     # Run a Zeebe instance process
            process_instance_key, result = await client.run_process_with_result(
                         bpmn_process_id="Process_Diagnostics", variables={"docid": docid, "patientid":patientid}, variables_to_fetch =["result"], timeout=10000
            )
            print(process_instance_key)
            return result
        except Exception as e:
            print(e)
            return {}
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(zeebe_task(docid, patientid))