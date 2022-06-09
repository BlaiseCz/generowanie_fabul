from collections import defaultdict
from pprint import pprint
from random import randrange, sample
import xml.etree.ElementTree as ET

class Operator:
    def __init__(self) -> None:
        self.parameters = defaultdict(list) # objects (name: type)
        self.preconditions = [] # predicates [name, param1, param2, ...]
        self.effects = [] # predicates [name, param1, param2, ...]

"""

Objects are in form of defaultdict (type: [name1, name2, ...]).

All predicates (relations, preconditions) are a list,
the first element is the name [name, param1, param2, ...].

In genetic search we only add/remove parameters to/from goals list.
"""
class World:
    def __init__(self):
        self.objects = defaultdict(list) # objects that the world contains
        self.start = [] # predicates that the world starts with
        self.predicates = [] # predicates available for goal
        self.operators = defaultdict(Operator) # actions available in the world
        self.goal = []

    def add_random_goal(self):
        predicate = self.predicates[randrange(len(self.predicates))]
        result = [predicate[0]] # name is the same
        for type in predicate[1:]:
            result.append(self.objects[type][randrange(len(self.objects[type]))])
        self.goal.append(result)

    def remove_random_goal(self):
        self.goal.pop(randrange(len(self.goal)))

    def __mul__(self, other):
        """
        Crossovers self.goal set. ! In-place !

        Usage:
            w = World()
            w2 = World()
            ...
            w.goal = w * w2
        """
        result = set(sample(self.goal, len(self.goal)//2) + \
                     sample(other.goal, len(other.goal)//2) )
        return result


    def read_from_xml(self, path: str):

        root = ET.parse(path).getroot()

        # objects into a dictionary with type as key
        for tag in root.findall('objects/object'):
            self.objects[tag.get('type')].append(tag.get('name'))

        for tag in root.findall('relations/predicate'):
            self.start.append([tag.get('name')])
            for parameter in tag.findall('parameter'):
                self.start[-1].append(parameter.get('value'))

        for tag in root.findall('predicates/predicate'):
            self.predicates.append([tag.get('name')])
            for parameter in tag.findall('parameter'):
                self.predicates[-1].append(parameter.get('type'))

        for tag in root.findall('operators/operator'):
            for parameter in tag.findall('parameters/parameter'):
                self.operators[tag.get('name')].parameters[parameter.get('type')].append(parameter.get('name'))
            for precondition in tag.findall('preconditions/precondition'):
                self.operators[tag.get('name')].preconditions.append([precondition.get('predicate')])
                for parameter in precondition.findall('parameter'):
                    self.operators[tag.get('name')].preconditions[-1].append(parameter.get('name'))
            for effect in tag.findall('effects/effect'):
                self.operators[tag.get('name')].effects.append([effect.get('predicate')])
                for parameter in effect.findall('parameter'):
                    self.operators[tag.get('name')].preconditions[-1].append(parameter.get('name'))

    def save_to_pddl(self, path_domain: str, path_problem: str):
        start_text = """
(define (domain castles-witches)
   (:requirements :strips :typing)
"""
        with open(path_domain, "w") as file:
            file.write(start_text)
            file.write(f"   (:types {' '.join(self.objects.keys())})\n")
            for name, operator in self.operators.items():
                file.write(f"   (:action {name}\n")
                file.write(f"\t:parameters (")
                for type, names in operator.parameters.items():
                    for name in names:
                        file.write(f"?{name} - {type} ")
                file.write(")\n")
                file.write(f"\t:precondition (and")
                for predicate in operator.preconditions:
                    file.write(f" ({predicate[0] }")
                    for name in predicate[1:]:
                        file.write(f"?{name} ")
                    file.write(")")
                file.write(")\n")
                file.write(f"\t:effect (and")
                for effect in operator.preconditions:
                    file.write(f" ({effect[0] }")
                    for name in effect[1:]:
                        file.write(f"?{name} ")
                    file.write(")")
                file.write(")\n")
                file.write("\n   )\n")
                file.write(")")

        #TODO: write predicates list at the end

        start_text = """
(define  (problem marry-princess)
    (:domain castles-witches)
    (:objects
"""
        medium_text = """
    )
    (:init
"""
        goal_text = """
    )
    (:goal
"""
        end_text = """
    )
)
"""
        with open(path_problem, "w") as file:
            file.write(start_text)

            for type, names in self.objects.items():
                file.write(f"\t\t{', '.join(names)} - {type}\n")

            file.write(medium_text)

            for predicate in self.start:
                file.write(f"\t\t({' '.join(predicate)})\n")

            file.write(goal_text)

            for predicate in self.goal:
                file.write(f"\t\t({' '.join(predicate)})\n")

            file.write(end_text)


if __name__ == "__main__":
    world = World()
    world.read_from_xml('./geneticquest_db.xml')
    world.add_random_goal()
    world.add_random_goal()
    world.add_random_goal()
    world.save_to_pddl('domain.pddl', 'problem.pddl')
