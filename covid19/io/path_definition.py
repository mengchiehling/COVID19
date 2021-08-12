import os


def get_project_dir():

    """
    Get the full path to the repository
    """

    dir_as_list = os.path.dirname(__file__).split("/")
    index = dir_as_list.index("cosnova")
    project_directory = f"/{os.path.join(*dir_as_list[:index + 1])}"

    return project_directory


def get_file(relative_path: str) -> str:

    """
    Given the relative path to the repository, return the full path
    """

    return os.path.join(get_project_dir(), relative_path)
