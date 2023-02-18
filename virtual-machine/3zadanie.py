import numpy
import random
from operator import attrgetter, pos



starting_position = [0, 0]  #pole v ktorom su suradice startu
pom = 0                     #pomocna premenna pri selekcii najuspesnejsieho hladaca pokladov
best_way = []               #najlepsia najdena cesta v pripade ze neboli najdene vsetky poklady
found = 0                   #premenna ktora urcuje ci boli najdene vsetky poklady
population = []             #pole ktore v sebe ma vsetkych jedincov prvej generacie
treasure_position = []      #pole obsahujuce suradnice pokladov
given = 1

class Individual():                                                         #jedinec z populacie a nastavenie jeho hodnot
    def __init__(self, memory, path, treasures, fitness):

        self.memory = []
        self.memory.extend(memory)
        self.path = path
        self.treasures = treasures
        self.fitness = fitness


def mutate(member):                                                          #funkcia v ktorej mutuju jedinci
    for i in range(64):
        random_num = random.randint(1, 100)
        if random_num <= 1:
            member.memory[i] = random.randint(0, 255)


def crossover(individual_1, individual_2):                                    #funkcia na krizenie jedincov
    lucky = random.randint(1, len(individual_1.memory) - 1)
    memory1 = []
    memory2 = []
    for i in range(len(individual_1.memory)):
        if i >= lucky:
            memory1.append(individual_2.memory[i])
            memory2.append(individual_1.memory[i])
        else:
            memory1.append(individual_1.memory[i])
            memory2.append(individual_2.memory[i])
    final_individual_1 = Individual(memory1, get_path(memory1[:]), 0, 0)
    final_individual_2 = Individual(memory2, get_path(memory2[:]), 0, 0)
    return final_individual_1, final_individual_2


def tournament(generation, amount):                                          #funkcia na vybratie jedincov 
    competitors = []
    for i in range(amount):
       competitors.append(random.choice(generation))
    return max(competitors, key=attrgetter('fitness'))


def configure_fitness(individual):                                                #funkcia pocitajuca fitness jedincov

    if individual.treasures != 0:
        individual.fitness = 100*int(individual.treasures) - len(individual.path)
    else:
        individual.fitness -= len(individual.path)


def count_treasures(individual, board, treasures, size):                    #funkcia pocitajuca najdene poklady

    if board[0] < size:
        if board[1] < size:                                 
            for one in treasures:                                             
                if board[0] == one[0]:
                    if board[1] == one[1]:
                        individual.treasures += 1
                        treasures.remove(one)
            return True
    return False


def find_treasures(starting_position, treasure_position, individual, size):              #funkcia sluzi na pohyb po mape
    for move in individual.path:
        if move == 'H':
            starting_position[1] -= 1
            if not count_treasures(individual, starting_position, treasure_position, size):
                break
        if move == 'D':
            starting_position[1] += 1
            if not count_treasures(individual, starting_position, treasure_position, size):
                break
        if move == 'P':
            starting_position[0] += 1
            if not count_treasures(individual, starting_position, treasure_position, size):
                break
        if move == 'L':
            starting_position[0] -= 1
            if not count_treasures(individual, starting_position, treasure_position, size):
                break
        
###
def get_size():                                                 #funkcia ktora ziska rozmer mriezky/mapy
    file = open("size.txt", "r")
    size = int(file.readline())
    return size


def get_starting_position(starting_position):                             #funkcia vracajuca suradnice startu
    file = open("start.txt", "r")
    for line in file:
        starting_position[0], starting_position[1] = (int(line.split()[0]), int(line.split()[1]))
    return starting_position


def get_treasure_position(treasure_position):                       #funkcia vracajuca suradnice vsetkych pokladov
   file = open("treasures.txt", "r")
   for line in file:
      treasure_position.append((int(line.split()[0]), int(line.split()[1])))
###

def get_movement(number):                             #funkcia urcuje symboly podla poctu jednotiek v bunke
    counter = 0
    while number != 0:
        if number & 1:
            counter += 1

        number = number >> 1

    if 0 <= counter <= 2:
        return 'H'
    if 2 < counter <= 4:
        return 'D'
    if 4 < counter <= 6:
        return 'P'
    if 6 < counter <= 8:
        return 'L'


def get_path(tape):                                               #funkcia pomocou ktorej ziskame cestu kazdeho jedinca
    memoryIndex = 0
    moves = []
    for i in range(500):
        instruction = tape[memoryIndex] >> 6
        address = tape[memoryIndex] & 63

        if instruction == 0:
            tape[address] += 1

        if instruction == 1:
            tape[address] -= 1

        if instruction == 2:
            memoryIndex = address

        if instruction == 3:
            moves.append(get_movement(tape[memoryIndex]))      #tato funkcia nam naplna pole symbolov pohybu

        if instruction != 2:
            memoryIndex += 1

            if memoryIndex > 63:
                memoryIndex = 0
    return moves                                                  #funkcia nam vrati pole so symbolmi pohybu(P, D,...)


def create_individual():                                                #funkcia na vytvorenie pamatovych buniek
    memory = [int(random.randint(0, 255)) for i in range(64)]             #pamatove bunky obsahujuce instrukcii
    return memory                                                         #nastavenie nahodnych hodnot pre 64 bitov


fitnes_zoz = []
pocet=0

number_of_generations = input('Zadajte pocet generacii: ')
population_size = input('Zadajte pocet jedincov pre populaciu: ')
size = get_size()                                   #rozmer mapy
starting_position = get_starting_position(starting_position)            #startovna pozicia jedincov
get_treasure_position(treasure_position)                #funkcia ktora naplni pole dvojicami suradnic pokladov
number_of_treasures = len(treasure_position)               #pocet pokladov 

for member in range(int(population_size)):

    memory = create_individual()
    individual = Individual(memory, get_path(memory[:]), 0, 0)
    population.append(individual)

for i in range(int(number_of_generations)):

    #print('Generacia cislo: ',i)
    for member in population:

        find_treasures(starting_position[:], treasure_position[:], member, size)
        if member.treasures == number_of_treasures:

            print('Jedinec z ',i,'. generacie nasiel vsetky poklady: ', member.path)
            found = 1
            break
        else:
            configure_fitness(member)
            fitnes_zoz.append(member.fitness)
            pocet+=1

    if found == 1:
        break
    new_generation = []

    for pair in range(int(len(population) / 2)):

        while True:
            individual1 = tournament(population, 3)
            individual2 = tournament(population, 3)
            if not individual1 is individual2:
                break

        new_individual = crossover(individual1, individual2)
        mutate(new_individual[0])
        mutate(new_individual[1])
        new_generation.append(new_individual[0])
        new_generation.append(new_individual[1])
    population.clear()
    population.extend(new_generation)

if found != 1:
    fit = -10000   
    for member in population:
        
        find_treasures(starting_position[:], treasure_position[:], member, size)
        poklady = member.treasures
        if poklady > pom:
            pom = poklady
            best_way = member.path
            fit = member.fitness

        if poklady == pom:
            fit2 = member.fitness
            if fit2>fit:
                best_way=member.path

    print("Vsetky poklady neboli najdene.\ncesta najuspesnejsieho jedinca: ",best_way,"\nnasiel : ",pom,"poklady")