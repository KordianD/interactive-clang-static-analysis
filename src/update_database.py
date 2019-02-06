import config
from src.parser.warning_parser import find_clang_warnings
from src.db_schemas.clang_warning import ClangWarning


def translate_clang_warning_to_database(clang_warnings):
    for clang_warning in clang_warnings:
        ClangWarning(
            **{"check_name": clang_warning.check_name, "path_to_file": clang_warning.path_to_file,
               "line_number": clang_warning.line_number,
               "owner": clang_warning.owner}).save()


def update_database(db_collection):
    clang_warnings: list = find_clang_warnings(config.PATH_TO_WARNING_FILE)
    db_collection.drop()
    translate_clang_warning_to_database(clang_warnings)
