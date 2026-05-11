#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    is_valid = False
    for i in allowed:
        if i in ingredients.lower():
            is_valid = True
            break
    if is_valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
