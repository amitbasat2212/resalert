class Status:
    def __init__(self, s_name: str, s_order: int) -> None:
        self.s_name = s_name
        self.s_order = s_order

    def __eq__(self, other):
        return self.s_name == other.s_name and self.s_order == other.s_order

    def __hash__(self):
        return hash((self.s_name, self.s_order))

    def __str__(self) -> str:
        return f"({self.s_name},{self.s_order})"

    def __repr__(self) -> str:
        return f"<Status> ({self.s_name}, {self.s_order})"
