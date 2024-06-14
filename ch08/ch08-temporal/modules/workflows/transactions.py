import asyncio
from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from modules.activities.workflow import send_email
    from modules.admin.activities.workflow import reserve_schedule, close_schedule
    from modules.models.workflow  import EmailDetails, WorkflowOptions, AppointmentWf, ReqAppointment
   

@workflow.defn(sandboxed=False)
class SendEmailWorkflow:
    def __init__(self) -> None:
        self.email_details = EmailDetails()
        
    @workflow.query
    def details(self) -> EmailDetails:
        return self.email_details

    @workflow.run
    async def run(self, data: WorkflowOptions) -> None:
        duration = 12
        self.email_details.email = data.email
        self.email_details.message = "Welcome to our Subscription Workflow!"
        self.email_details.subscribed = True
        self.email_details.count = 0

        while self.email_details.subscribed:
            self.email_details.count += 1
            if self.email_details.count > 1:
                self.email_details.message = "Thank you for staying subscribed!"

            try:
                await workflow.execute_activity(
                    send_email,
                    self.email_details,
                    start_to_close_timeout=timedelta(seconds=10),
                )
                await asyncio.sleep(duration)

            except asyncio.CancelledError as err:
                # Cancelled by the user. Send them a goodbye message.
                self.email_details.subscribed = False
                self.email_details.message = "Sorry to see you go"
                await workflow.execute_activity(
                    send_email,
                    self.email_details,
                    start_to_close_timeout=timedelta(seconds=10),
                )
                # raise error so workflow shows as cancelled.
                raise err

@workflow.defn(sandboxed=False)      
class ReserveAppointmentWorkflow():
    def __init__(self) -> None:
        self.appointmentwf = AppointmentWf()
        
    @workflow.query
    def details(self) -> AppointmentWf:
        return self.appointmentwf

    @workflow.run
    async def run(self, data: ReqAppointment) -> None:
        duration = 12
        self.appointmentwf.ticketid = data.ticketid
        self.appointmentwf.patientid = data.patientid
        self.appointmentwf.docid = data.docid
        self.appointmentwf.date_scheduled = data.date_scheduled
        self.appointmentwf.time_scheduled = data.time_scheduled
        self.appointmentwf.status = True

        while self.appointmentwf.status:
            self.appointmentwf.remarks = "Doctor reservation being processed...."

            try:
                await workflow.execute_activity(
                    reserve_schedule,
                    self.appointmentwf,
                    start_to_close_timeout=timedelta(seconds=10),
                )
                await asyncio.sleep(duration)

            except asyncio.CancelledError as err:
                # Cancelled by the user. Send them a goodbye message.
                self.appointmentwf.status = False
                self.appointmentwf.remarks = "Appointment with doctor done."
                await workflow.execute_activity(
                    close_schedule,
                    self.appointmentwf,
                    start_to_close_timeout=timedelta(seconds=10),
                )
                raise err
