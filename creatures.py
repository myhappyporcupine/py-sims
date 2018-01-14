import random

class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.creatures = []

    def __str__(self):
        world_str = 'World' + ':' + str(self.width) + 'X' + str(self.height)
        for current_creature in self.creatures:
            world_str += '\n' + str(current_creature)
        return world_str
    
    def birth(self):
        new_creature = Creature(random.randint(0, self.width-1), random.randint(0, self.height-1))
        self.creatures.append(new_creature)

    def step(self):
        for current_creature in self.creatures:
            if current_creature.live:
                current_creature.move(self.width-1, self.height-1)
                current_creature.grow()

    # look for collision with a naive algorithm, if print_collision then print the collision, if kill then make the creature earlier in the list kill the creature later in the list upon collision
    def collisions(self, print_collision=False, kill=True):
        for i in range(len(self.creatures)):
            for j in range(i+1, len(self.creatures)):
                if self.creatures[i].x == self.creatures[j].x and self.creatures[i].y == self.creatures[j].y:
                    if print_collision:
                        print('collision->' + str(self.creatures[i]) + '&' + str(self.creatures[j]))
                    if kill and self.creatures[j].live:
                        self.creatures[j].die()

class Creature:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.live = True
        self.age = 0

    def __str__(self):
        if (self.live):
            return 'live:' + str(self.age) + '@(' + str(self.x) + ',' + str(self.y) + ')'
        else:
            return 'dead:' + str(self.age) + '@(' + str(self.x) + ',' + str(self.y) + ')'

    def grow(self):
        self.age += 1

    def die(self):
        self.live = False

    def revive(self):
        self.live = True

    def move(self, max_x, max_y):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        if self.x < 0:
            self.x = 0
        elif self.x > max_x:
            self.x = max_x
        if self.y < 0:
            self.y = 0
        elif self.y > max_y:
            self.y = max_y

world = World(10, 10)

for i in range(5):
    world.birth()

print(world)

def step():
    world.step()
    print(world)
    world.collisions()
    print()
