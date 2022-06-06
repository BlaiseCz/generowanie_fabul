from collections import defaultdict
from pprint import pprint
import xml.etree.ElementTree as ET

class Object:
    def __init__(self, type, name) -> None:
        self.type = type
        self.name = name
    def __repr__(self) -> str:
        return f"{self.name} - {self.type}"

class Predicate:
    def __init__(self, name) -> None:
        self.name = name
        self.parameters = [] # just values of the parameters
    def repr_problem(self) -> str:
        return f"({self.name} {' '.join(self.parameters)})"
    def repr_domain(self) -> str:
        return f"({self.name} ?{' ?'.join(self.parameters)})"

class Precondition:
    def __init__(self, name) -> None:
        self.name = name
        self.parameters = [] # list of strings

class Effect:
    def __init__(self, predicate, negation=False) -> None:
        self.predicate = predicate
        self.negation = negation
        self.parameters = [] # list of strings

class Operator:
    def __init__(self) -> None:
        self.objects = [] # list of Objects
        self.preconditions = [] # list of Preconditions
        self.effects = []

############## WCZYTYWANIE ##############
root = ET.parse('geneticquest_db.xml').getroot()

types = defaultdict(list)
for tag in root.findall('objects/object'):
    types[tag.get('type')].append(tag.get('name'))

relations = defaultdict(list)
for tag in root.findall('relations/predicate'):
    parameters = []
    for parameter in tag.findall('parameter'):
        parameters.append(parameter.get('value'))
    relations[tag.get('name')].append(parameters)

predicates = defaultdict(list)
for tag in root.findall('predicates/predicate'):
    parameters = []
    for parameter in tag.findall('parameter'):
        parameters.append(parameter.get('type'))
    predicates[tag.get('name')].append(parameters)

operators = dict()
for tag in root.findall('operators/operator'):
    operator = Operator()
    for parameter in tag.findall('parameters/parameter'):
        operator.parameters.append((
            parameter.get('name'),
            parameter.get('type')
        ))
    for precondition in tag.findall('preconditions/precondition'):
        parameters = []
        for parameter in precondition.findall('parameter'):
            parameters.append(parameter.get('name'))
        operator.preconditions.append((
            precondition.get('predicate'),
            *parameters
        ))
    for effect in tag.findall('effects/effect'):
        parameters = []
        for parameter in effect.findall('parameter'):
            parameters.append(parameter.get('name'))
        operator.effects.append((
            effect.get('predicate'),
            *parameters
        ))
    operators[tag.get('name')] = operator

############## ZAPISYWANIE DO PDDL ##############
start_text = """
(define  (problem marry-princess)
    (:domain castles-witches)
    (:objects
"""
medium_text = """
         )
    (:init
"""
end_text = """
    (:goal

    )
)
"""
with open("problem.pddl", "w") as file:
    file.write(start_text)

    for key, value in types.items():
        file.write(f"\t\t{', '.join(value)} - {key}\n")

    file.write(medium_text)

    for key, value in relations.items():
        for parameters in value:
            file.write(f"\t\t({key} {' '.join(parameters)})\n")

    file.write(end_text)


start_text = """
(define (domain castles-witches)
    (:requirements :strips :typing)
"""
with open("domain.pddl", "w") as file:
    file.write(start_text)
    file.write(f"\t(:types {' '.join(types)})\n")
    for name, operator in operators.items():
        file.write(f"\t(:action {name}\n")
        file.write(f"parameters (")
        for p in operator.parameters:
            file.write(f"?{p[0]} - {p[1]} ")
        file.write(")\n")

