class OpenJob:
    def __init__(self, id, name, dep_name):
        self.id = id
        self.name = name
        self.dep_name = dep_name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.dep_name == other.dep_name

    def __hash__(self):
        return hash((self.id, self.name, self.dep_name))

    def __str__(self) -> str:
        return f"('{self.id}','{self.name}','{self.dep_name}')"

    def __repr__(self) -> str:
        return f"({self.id},{self.name},{self.dep_name})"
