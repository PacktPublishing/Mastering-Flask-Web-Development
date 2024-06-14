import logging

from pyzeebe import Job

logger = logging.getLogger()

def log_decorator(job: Job) -> Job:
    if not hasattr(job, "_stat"):
        job._stat = "Initialized"
    else:
        job._stat = "Completed"
    logger.info(
        f"Job Type: {job.type}, Status: {job._stat}, Job key: {job.key}"
    )
    return job


def error_handler(exception: Exception, job: Job) -> None:
    response = f"Job Type: {job.type}, Status: Failed, Instance key: Job key: {job.key}, Error: {str(exception)}"
    logger.error(response, exc_info=True)
    if type(exception).__name__ == "ConnectionError":
        job.set_failure_status(response)
    else:
        job.set_error_status(response)