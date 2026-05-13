#!/usr/bin/env python3

"""
3️⃣ ex1/factory.py — Las nuevas factories
HealingCreatureFactory(CreatureFactory):

create_base → devuelve Sproutling("Sproutling")
create_evolved → devuelve Bloomelle("Bloomelle")

TransformCreatureFactory(CreatureFactory):

create_base → devuelve Shiftling("Shiftling")
create_evolved → devuelve Morphagon("Morphagon")


💡 Importa CreatureFactory desde ex0


4️⃣ ex1/__init__.py
Solo expone las factories:
pythonfrom ex1.factory import HealingCreatureFactory, TransformCreatureFactory

5️⃣ capacitor.py — El script de prueba
Dos bloques:
Bloque healing:
print("Testing Creature with healing capability")
# crea factory → base → describe, attack, heal
# evolved → describe, attack, heal
Bloque transform:
print("Testing Creature with transform capability")
# crea factory → base → describe, attack, transform, attack, revert
# evolved → describe, attack, transform, attack, revert
"""
