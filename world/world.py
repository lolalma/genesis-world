import random

class Tile:
    def __init__(self, terrain_type, has_resource=False):
        self.terrain_type = terrain_type
        self.has_resource = has_resource

class Biome:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources

class ProceduralWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.world = [[None for _ in range(width)] for _ in range(height)]
        self.biomes = self.create_biomes()

    def create_biomes(self):
        return [
            Biome("forest", ["wood", "berry"]),
            Biome("desert", ["sand", "cactus"]),
            Biome("mountain", ["stone", "iron"]),
            Biome("ocean", ["fish", "seaweed"])
        ]

    def generate_tile(self):
        biome = random.choice(self.biomes)
        has_resource = random.choice([True, False])
        return Tile(biome.name, has_resource)

    def generate_world(self):
        for y in range(self.height):
            for x in range(self.width):
                self.world[y][x] = self.generate_tile()

    def display_world(self):
        for row in self.world:
            print(" ".join([tile.terrain_type for tile in row]))

# Example usage
if __name__ == "__main__":
    world = ProceduralWorld(10, 10)
    world.generate_world()
    world.display_world()