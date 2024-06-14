from temporalio import activity

from modules.models.workflow import EmailDetails


@activity.defn
async def send_email(details: EmailDetails) -> str:
        print(f"Sending email to {details.email} with message: {details.message}, count: {details.count}")
        return "success"



