from src.parser.GitParser import get_clang_warnings

fo = open("data/one_override_warning.txt", "rw+")

clang_warnings = fo.readlines()


def test_get_clang_warnings():
    returned_clang_warnings = get_clang_warnings(clang_warnings)
    assert returned_clang_warnings[0].check_name == 'modernize-use-override'
