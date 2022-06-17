import math
import os

from ae import init_pop, mutate_member, remove_worst_from_pop, add_new_members, assign_fitness, print_pop_stats

HSPHOME = os.path.join("hsp-planners/hsp-1.12")
POP_SIZE = 100
ITERATIONS = 140


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
    Initializing PROBLEMS file with 
    problems and domains list which go to planners 
"""


def init_problems_file() -> None:
    with open('hsp-planners/hsp-1.12/pddl/story/PROBLEMS', 'a') as myfile:
        for i in range(POP_SIZE):
            myfile.write(f'problem_{i}.pddl domain_{i}.pddl')
            myfile.write('\n')


def clear_problems_file() -> None:
    open('hsp-planners/hsp-1.12/pddl/story/PROBLEMS', 'w').close()


"""
    ae loop -> runs population ae algorithm in loop with mutation
"""
if __name__ == "__main__":
    # TEST
    # run_hsp_planner(f'/pddl/story')
    save_path = dir_path = os.path.abspath(HSPHOME) + '/pddl/story/'
    pop = init_pop(POP_SIZE)
    init_problems_file()

    for _ in range(ITERATIONS):
        for member in pop:
            mut = mutate_member(member)
            mut.save_to_pddl(f'{save_path}domain_{mut.id}.pddl', f'{save_path}problem_{mut.id}.pddl')

        run_hsp_planner(f'/pddl/story')
        assign_fitness(population=pop, desired_story_arc=[1, 2, 3, 1])
        remove_worst_from_pop(last=10)
        add_new_members(population=pop, pop_size=POP_SIZE)
        print_pop_stats(pop)
    clear_problems_file()
