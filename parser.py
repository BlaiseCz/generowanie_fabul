import os

from runner import HSPHOME
from world import World

if __name__ == "__main__":
    world = World()
    world.read_from_xml('./geneticquest_db.xml')
    world.add_random_goal()
    world.add_random_goal()
    world.add_random_goal()
    save_path = dir_path = os.path.abspath(HSPHOME) + '/pddl/story/'
    world.save_to_pddl_no_typing( save_path + 'domainM.pddl', save_path +'problemM.pddl')
