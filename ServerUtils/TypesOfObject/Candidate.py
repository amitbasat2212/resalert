class Candidate:
    def __init__(self, f_name, l_name, mail, cv, Gender):
        self.first_name = f_name
        self.last_name = l_name
        self.mail = mail
        self.cv = cv
        self.Gender = Gender

    def __repr__(self) -> str:
        return f"<Candidate>  ({self.first_name},{self.last_name},{self.mail},{self.cv},{self.Gender})"
