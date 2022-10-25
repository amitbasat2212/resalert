class Candidate:
    def __init__(self, f_name, l_name, mail, cv, Gender):
        self.f_name = f_name
        self.l_name = l_name
        self.mail = mail
        self.cv = cv
        self.Gender = Gender

    def __eq__(self, other):
        return self.f_name == other.f_name and self.l_name == other.l_name and self.mail == other.mail and self.cv == other.cv and other.mail and self.Gender == other.Gender

    def __hash__(self):
        return hash((self.f_name, self.l_name))

    def __str__(self) -> str:
        return f"('{self.f_name}','{self.l_name}','{self.mail}','{self.cv}','{self.Gender}')"

    def __repr__(self) -> str:
        return f"<Candidate>  ({self.first_name},{self.last_name},{self.mail},{self.cv},{self.Gender})"
