class JobByPerson:
    def __init__(self, mail, job, status, stage):
        self.mail = mail
        self.job = job
        self.status = status
        self.stage = stage

    def __eq__(self, other):
        return self.mail == other.mail and self.job == other.job and self.status == other.status and self.stage == other.stage

    def __hash__(self):
        return hash((self.mail, self.job, self.status, self.stage))

    def __str__(self) -> str:
        return f"('{self.mail}','{self.job}','{self.status}','{self.stage}')"

    def __repr__(self) -> str:
        return f"<JobByPerson>  ({self.mail},{self.job},{self.status},{self.stage})"
