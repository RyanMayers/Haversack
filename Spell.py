class Spell:
    "A spell is a discrete magical effect, a single shaping of the magical energies that suffuse the multiverse into a specific, limited expression. In casting a spell, a character carefully plucks at the invisible strands of raw magic suffusing the world, pins them in place in a particular pattern, sets them vibrating in a specific way, and then releases them to unleash the desired effect—in most cases, all in the span of seconds."
    def __init__(self, level, dndClass, castingTime, spellRange, components, duration, desc):
        self.dclass = dndClass
        self.level = level
        self.time = castingTime
        self.range = spellRange
        self.comp = components
        self.dur = duration
        self.desc = desc