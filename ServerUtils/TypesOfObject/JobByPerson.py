class JobByPerson:
    def __init__(self, mail, job, status, stage):
        self.mail = mail
        self.job = job
        self.status = status
        self.stage = stage

    def __repr__(self) -> str:
        return f"<JobByPerson>  ({self.mail},{self.job},{self.status},{self.stage})"
