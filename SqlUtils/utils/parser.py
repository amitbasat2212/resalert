import json
from ServerUtils.TypesOfObject.Candidate import Candidate
from ServerUtils.TypesOfObject.Departements import Departements
from ServerUtils.TypesOfObject.FinalStage import FinalStage
from ServerUtils.TypesOfObject.OpenJob import OpenJob
from ServerUtils.TypesOfObject.PersonJobs import PersonJobs
from ServerUtils.TypesOfObject.Status import Status
# from utils.constants import *


def _get_dict_from_json(json_dir: str):
    person_jobs_data_file = open(json_dir)
    person_jobs_data = json.load(person_jobs_data_file)
    person_jobs_data_file.close()
    return person_jobs_data


def _parse_person_jobs_data(person_jobs_data):
    status, pokemons_trainers, pokemons_types = set(), set(), set()

    trainers = dict()  # {trainer: trainerId}
    types = dict()  # {type: trainerId}
    trainer_id, type_id = 1, 1
    for p in person_jobs_data:
        pokemon = Pokemon(p[P_ID], p[P_NAME], p[P_HEIGHT], p[P_WEIGHT])
        pokemons.add(pokemon)
        type = Type(type_id, p[P_TYPE])
        if type not in types:
            types[type] = type_id
            type_id += 1
        pokemons_types.add(P_T_Pair(pokemon.id, types[type]))
        for t in p[P_TRAINER]:
            trainer = Trainer(trainer_id, t[T_NAME], t[T_TOWN])
            if trainer not in trainers:
                trainers[trainer] = trainer_id
                trainer_id += 1
            pokemons_trainers.add(P_T_Pair(pokemon.id, trainers[trainer]))
    return pokemons, trainers, pokemons_trainers, types, pokemons_types


# def parse(json_dir: str):
#     poke_data = _get_dict_from_json(json_dir)
#     return _parse_poke_data(poke_data)
