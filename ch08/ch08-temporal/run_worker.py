from temporalio.client import Client
from temporalio.worker import Worker, UnsandboxedWorkflowRunner
import asyncio

from modules.admin.activities.workflow import reserve_schedule, close_schedule
from modules.models.workflow import appt_queue_id
from modules.workflows.transactions import ReserveAppointmentWorkflow
  

async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue=appt_queue_id,
        workflows=[ReserveAppointmentWorkflow],
        activities=[reserve_schedule, close_schedule],
        workflow_runner=UnsandboxedWorkflowRunner,   
    )
    await worker.run()


if __name__ == "__main__":
    print("Temporal worker started...")
    asyncio.run(main())