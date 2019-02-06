import subprocess
import re


def extract_person(path_to_file: str, line_number: int):
    git_blame_output: str = call_git_blame(path_to_file, line_number)
    return extract_person_from_git_blame_output(git_blame_output)


def extract_person_from_git_blame_output(git_blame_output: str):
    found_name = re.search(r'\((\S*)\s', git_blame_output)
    return found_name.group(1)


def call_git_blame(path_to_file: str, line_number: int):
    output = subprocess.run(["git", "blame", "-L", "{line_number},{line_number}".format(line_number=line_number),
                             r"{path_to_file}".format(path_to_file=path_to_file)], capture_output=True)

    if output.returncode:
        raise ValueError(output.stderr)

    return output
