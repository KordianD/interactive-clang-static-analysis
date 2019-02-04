from src.parser.warning_parser import get_clang_warnings

clang_warning = [line.rstrip('\n') for line in open(
    'test/parser/data/one_override_warning.txt')]


def test_get_clang_warnings():
    returned_clang_warnings = get_clang_warnings(clang_warning)
    assert returned_clang_warnings[0].check_name == 'modernize-use-override'
    assert returned_clang_warnings[0].path_to_file == '/home/test/CLionProjects/untitled/main.cpp'
    assert returned_clang_warnings[0].line_number == 8
