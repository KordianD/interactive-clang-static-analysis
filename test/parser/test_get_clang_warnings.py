from src.parser.git_parser import get_clang_warnings

clang_warning = [line.rstrip('\n') for line in open(
    'test/parser/data/one_override_warning.txt')]


def test_get_clang_warnings():
    returned_clang_warnings = get_clang_warnings(clang_warning)
    print('RETURNED')
    print(returned_clang_warnings[0].check_name)
    assert returned_clang_warnings[0].check_name == 'modernize-use-override'
