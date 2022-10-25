class OpenJob:
    def __init__(self, id, name, dep_name):
        self.id = id
        self.name = name
        self.dep_name = dep_name

    def __repr__(self) -> str:
        return f"<OpenJob>  ({self.id},{self.name},{self.dep_name})"
