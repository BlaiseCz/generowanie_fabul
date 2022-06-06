import os

HSPHOME = os.path.join("hsp-planners/hsp-1.12")


def run_hsp_planner(problem_path: str) -> None:
    """
    Run hsp planner, hsp saves result in solutions.all file
    """
    dir_path = os.path.abspath(HSPHOME)
    abs_problem_path = dir_path + problem_path

    os.system(f"export HSPHOME={dir_path}; "
              f"cd $HSPHOME; "
              f"make compile;"
              f"cd {abs_problem_path};"
              f"make compile;"
              f"make solve;")


if __name__ == "__main__":
    run_hsp_planner(f'/pddl/logistics')
