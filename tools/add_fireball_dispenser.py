"""Adds the fireball dispenser to the temple's processor lists: FireballDispenserProcessor turns
orange concrete into an upward dispenser holding a fire charge in the middle slot and, in each
other slot, one time in ten. The slots are independent, so every combination of the eight outer
slots is one pick, weighted by its odds, and the last takes the remainder as the default."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data/betterjungletemples/worldgen/processor_list')
OUTER = [0, 1, 2, 3, 5, 6, 7, 8]
def outcome(slots):
    items = [{'Slot': s, 'id': 'minecraft:fire_charge', 'count': 1} for s in sorted(slots + [4])]
    return {'state': {'id': 'minecraft:dispenser', 'properties': {'facing': 'up'}},
            'nbt': {'id': 'minecraft:dispenser', 'Items': items}}
combos = []
for mask in range(256):
    slots = [s for i, s in enumerate(OUTER) if mask >> i & 1]
    n = len(slots)
    combos.append((0.1 ** n * 0.9 ** (8 - n), slots))
combos.sort(key=lambda c: -c[0])
picks, total = [], 0.0
for p, slots in combos[:-1]:
    total += p
    picks.append(dict(below=round(total, 9), **outcome(slots)))
proc = {'processor_type': 'sunrise:pick', 'block': 'minecraft:orange_concrete', 'picks': picks,
        'default': outcome(combos[-1][1])}
for name in ('main', 'main_waterlog'):
    path = os.path.join(ROOT, name + '.json')
    d = json.load(open(path))
    d['processors'] = [p for p in d['processors'] if p.get('block') != 'minecraft:orange_concrete']
    d['processors'].insert(0, proc)
    with open(path, 'w') as f:
        json.dump(d, f, indent=2); f.write('\n')
