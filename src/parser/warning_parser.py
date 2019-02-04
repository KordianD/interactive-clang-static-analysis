from src.parser.clang_warning import ClangWarning


def get_clang_warnings(warnings: list) -> list:
    clang_warnings: list = []
    for line in warnings:
        if 'warning:' in line:
            end_of_filepath: str = line.find(':')
            path_to_file: str = line[:end_of_filepath]
            end_of_number: int = line[end_of_filepath+1:].find(':')

            line_number: int = int(line[end_of_filepath+1:][:end_of_number])

            start_of_check_name: int = line.rfind('[')

            check_name: str = line.rstrip()[start_of_check_name + 1:-1]

            clang_warnings.append(ClangWarning(
                check_name, path_to_file, line_number))

    return clang_warnings
