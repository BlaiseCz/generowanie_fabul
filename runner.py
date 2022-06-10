import os

from ae import init_pop, mutate_member, remove_worst_from_pop, add_new_members, assign_fitness

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
    ae loop -> runs population ae algorithm in loop with mutation
"""


if __name__ == "__main__":
    # TEST
    # run_hsp_planner(f'/pddl/story')
    pop = init_pop(POP_SIZE)

    for _ in range(ITERATIONS):
        for member in pop():
            mut = mutate_member(member)
            mut.save_to_pddl()
            save_path = dir_path = os.path.abspath(HSPHOME) + '/pddl/story/'
            mut.save_to_pddl(save_path + 'domain' + mut.id + '.pddl', save_path + 'problem' + mut.id + '.pddl')

        run_hsp_planner(f'/pddl/story')
        assign_fitness(pop)
        remove_worst_from_pop(last=10)
        add_new_members(pop) # TODO with crossover
