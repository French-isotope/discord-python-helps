pokebase = {
    "baby_trigger_item": None,
    "chain": {
        "evolution_details": [

        ],
        "evolves_to": [
            {
                "evolution_details": [
                    {
                        "gender": None,
                        "held_item": None,
                        "item": None,
                        "known_move": None,
                        "known_move_type": None,
                        "location": None,
                        "min_affection": None,
                        "min_beauty": None,
                        "min_happiness": None,
                        "min_level": 16,
                        "needs_overworld_rain": False,
                        "party_species": None,
                        "party_type": None,
                        "relative_physical_stats": None,
                        "time_of_day": "",
                        "trade_species": None,
                        "trigger": {
                            "name": "level-up",
                            "url": "https://pokeapi.co/api/v2/evolution-trigger/1/"
                        },
                        "turn_upside_down": False
                    }
                ],
                "evolves_to": [
                    {
                        "evolution_details": [
                            {
                                "gender": None,
                                "held_item": None,
                                "item": None,
                                "known_move": None,
                                "known_move_type": None,
                                "location": None,
                                "min_affection": None,
                                "min_beauty": None,
                                "min_happiness": None,
                                "min_level": 36,
                                "needs_overworld_rain": False,
                                "party_species": None,
                                "party_type": None,
                                "relative_physical_stats": None,
                                "time_of_day": "",
                                "trade_species": None,
                                "trigger": {
                                    "name": "level-up",
                                    "url": "https://pokeapi.co/api/v2/evolution-trigger/1/"
                                },
                                "turn_upside_down": False
                            }
                        ],
                        "evolves_to": [

                        ],
                        "is_baby": False,
                        "species": {
                            "name": "charizard",
                            "url": "https://pokeapi.co/api/v2/pokemon-species/6/"
                        }
                    }
                ],
                "is_baby": False,
                "species": {
                    "name": "charmeleon",
                    "url": "https://pokeapi.co/api/v2/pokemon-species/5/"
                }
            }
        ],
        "is_baby": False,
        "species": {
            "name": "charmander",
            "url": "https://pokeapi.co/api/v2/pokemon-species/4/"
        }
    },
    "id": 2
}

print(pokebase["chain"]["species"]["name"])
print(pokebase["chain"]["evolves_to"][0]["evolution_details"][0]["min_level"])