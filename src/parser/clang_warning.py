class ClangWarning:
    def __init__(self, check_name: str, path_to_file: str, line_number: int):
        self.check_name = check_name
        self.path_to_file = path_to_file
        self.line_number = line_number
