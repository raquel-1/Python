#!/usr/bin/env python3

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    result = validate_ingredients(ingredients)
    status = "recorded" if "VALID" in result else "rejected"
    return f"Spell {status}: {spell_name} ({result})"
