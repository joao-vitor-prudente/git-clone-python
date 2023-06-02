"""Entry point for program"""

import sys
from src.classes.actions import Actions
from src.actions.git_add import git_add
from src.actions.git_commit import git_commit
from src.actions.git_init import git_init
from src.actions.git_log import git_log
from src.actions.git_show import git_show
from src.actions.git_rebase import git_rebase
from src.validations.command_validation import validate_arguments


def main():
    """Parses comands and arguments and executes the corresponding action."""

    arguments = sys.argv[1:]
    if len(arguments) == 0:
        return
    validate_arguments(arguments)
    action = Actions(arguments[0])

    match (action):
        case Actions.INIT:
            git_init()
        case Actions.ADD:
            git_add(file_path=arguments[1])
        case Actions.COMMIT:
            git_commit(message=arguments[2])
        case Actions.LOG:
            if len(arguments) == 1:
                git_log()
            else:
                git_log(log_content=True)
        case Actions.SHOW:
            git_show(commit_id=arguments[1])
        case Actions.REBASE:
            git_rebase(commit_id=arguments[1])


if __name__ == "__main__":
    main()
