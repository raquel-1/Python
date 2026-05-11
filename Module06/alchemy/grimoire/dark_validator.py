#!/usr/bin/env python3
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    is_valid = False
    for i in allowed:
        if i in ingredients.lower():
            is_valid = True
            break
    if is_valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
