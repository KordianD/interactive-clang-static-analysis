from src.parser.scm_parser import extract_person_from_git_blame_output

GIT_BLAME_EXAMPLE: str = r"4d1d5c39 (JohnPaul 2019-02-02 15:18:20 +0100 10)  " \
                         r" url='https://github.com/invalid/interactive-clang-static-analysis',\n"


def test_extract_person_from_git_blame():
    found_person = extract_person_from_git_blame_output(GIT_BLAME_EXAMPLE)
    assert found_person == "JohnPaul"
