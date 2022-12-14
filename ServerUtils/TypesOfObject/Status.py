class Status:
    def __init__(self, s_order: int, s_name: str) -> None:
        self.s_order = s_order
        self.s_name = s_name

    def __eq__(self, other):
        return self.s_order == other.s_order and self.s_name == other.s_name

    def __hash__(self):
        return hash((self.s_order, self.s_name))

    def __str__(self) -> str:
        return f"('{self.s_order}','{self.s_name}')"

    def __repr__(self) -> str:
        return f"<Status> ({self.s_order}, {self.s_name})"
