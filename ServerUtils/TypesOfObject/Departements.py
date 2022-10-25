class Departements:
    def __init__(self, dep_name: str) -> None:
        self.dep_name = dep_name

    def __eq__(self, other):
        return self.dep_name == other.dep_name

    def __hash__(self):
        return hash(self.dep_name)

    def __str__(self) -> str:
        return f"('{self.dep_name}')"

    def __repr__(self) -> str:
        return f"<Departements>  {self.dep_name}"
