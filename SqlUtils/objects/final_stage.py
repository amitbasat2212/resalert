class Final_Stage:
    def __init__(self, fs_name: str) -> None:
        self.fs_name = fs_name
    def __eq__(self, other):
        return self.fs_name == other.fs_name

    def __hash__(self):
        return hash(self.fs_name)

    def __str__(self) -> str:
        return f"('{self.fs_name}')"

    def __repr__(self) -> str:
        return f"<Type>  {self.fs_name}"
