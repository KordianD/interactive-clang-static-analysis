from src.parser.warning_parser import find_clang_warnings
from mock import patch


@patch('src.parser.warning_parser.extract_person')
def test_get_clang_warnings(extract_person_mock):
    extract_person_mock.return_value = "test"

    returned_clang_warnings = find_clang_warnings('test/parser/data/one_override_warning.txt')
    assert returned_clang_warnings[0].check_name == 'modernize-use-override'
    assert returned_clang_warnings[0].path_to_file == '/home/test/CLionProjects/untitled/main.cpp'
    assert returned_clang_warnings[0].line_number == 8
    assert returned_clang_warnings[0].owner == "test"
