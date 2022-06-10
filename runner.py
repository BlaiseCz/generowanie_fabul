import os

HSPHOME = os.path.join("hsp-planners/hsp-1.12")


def run_hsp_planner(problem_path: str) -> None:
    dir_path = os.path.abspath(HSPHOME)
    abs_problem_path = dir_path + problem_path

    os.system(f"export HSPHOME={dir_path}; "
              f"cd $HSPHOME; "
              f"make compile;"
              f"cd {abs_problem_path};"
              f"make compile;"
              f"make solve;")

"""
    ae loop -> runs population ae algorithm in loop with mutation
"""
if __name__ == "__main__":
    # TEST
    run_hsp_planner(f'/pddl/story')

    # TODO
    # pop = init_pop(100)

    # for member in pop():
    #     mutate_pop(pop)
    #     run_hsp_planner()
    #     calc_fitness(pop)
    #     remove_worst_from_pop(last=10)
    #     add_new_members(pop)