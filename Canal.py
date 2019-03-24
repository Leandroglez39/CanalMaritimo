import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from binarytree import heapq

heap = heapq
Time = 0
body_heap = []

class lock:

    def __init__(self, id):
        self.id = id
        self.name = 'lock' + str(id)
        self.free = True
        self.capacity = 12
        self.list_ship = []
        self.down = True


class Channel:

    def __init__(self):
        self.lockslist = initlocks()

    def insert_ship_in_first_locks(self, id, ship):
        lockx = self.lockslist[id]

        if lockx.free:
            if lockx.capacity >= ship.range:
                lockx.list_ship.append(ship)
                lockx.capacity = lockx.capacity - ship.range
                if lockx.capacity == 0:
                    lockx.free = False
                    lockx.down = False
                    # Comenzar flujo de agua
                    return 0
            lockx.free = False
            # Comenzar flujo de agua
            lockx.down = False

    def free_lock(self, id_of_lock):
        self.lockslist[id_of_lock].free = True
        self.lockslist[id_of_lock].capacity = 12
        self.lockslist[id_of_lock].list_ship = []
        ######Chekear el tiempo que demora en volver a bajar el agua
        self.lockslist[id_of_lock].down = True

    def move_into_locks(self, id_lock_orgin, id_lock_destiny):

        lis = self.lockslist[id_lock_orgin].list_ship
        self.free_lock(id_lock_orgin)
        # Ver q las compuertas esten abiertas
        self.lockslist[id_lock_destiny].free = False
        self.lockslist[id_lock_destiny].capacity = self.lockslist[id_lock_orgin].capacity
        self.lockslist[id_lock_destiny].list_ship = lis
        # comenzar el flujo de agua



    def manager(self):

        list_of_ships = generate_list_of_ship()
        build_heap(list_of_ships)

        while Time <= 780:
            pass


        return 0


    def run_locks(self):
        for x in reversed(self.lockslist):
            if not x.free:
                for y in x.list_ship:
                    pass
            else:
                continue



class ship:

    def __init__(self, id, range):
        self.id = id;
        self.tarrive = 0
        self.tbegining = 0
        self.texit = 0
        self.texcusa1 = 0
        self.texcusa2 = 0
        self.texcusa3 = 0
        self.texcusa4 = 0
        self.texcusa5 = 0
        self.range = range


def initlocks():
    list = []
    for x in range(1, 6):
        list.append(lock(x))







def distnorm(x, mu, sigma):
    return int(((1 / (sigma*np.sqrt(2*np.pi))) * (np.e ** (((-1) / 2)) * ((x-mu) / sigma) ** 2))/10)



def disexp(x,alpha):
    return int(((1/alpha)*np.e**(-x/alpha))*70)


def generate_list_of_ship() -> list:
    list = []
    for x in range(1,50):
        ran = np.random.randint(0,781)
        if ran < 240:
            list.append((distnorm(ran,5,2),2))
            continue
        if ran < 600:
            list.append((distnorm(ran,3,1),2))
            continue
        list.append((distnorm(ran,10,2),2))

    for x in range(1,50):
        ran = np.random.randint(0,781)
        if ran < 240:
            list.append((distnorm(ran,15,3),4))
            continue
        if ran < 600:
            list.append((distnorm(ran,10,5),4))
            continue
        list.append((distnorm(ran,20,5),4))

    for x in range(1,50):
        ran = np.random.randint(0,781)
        if ran < 240:
            list.append((distnorm(ran,45,3),8))
            continue
        if ran < 600:
            list.append((distnorm(ran,35,7),8))
            continue
        list.append((distnorm(ran,60,9),8))

    return list

def build_heap(lis):
    for x in lis:
        if x <= 780:
            heap.heappush(body_heap,x)
        else:
            continue

#normal = distnorm(5,2)


#normal = stats.norm(60, 9)
#x = np.linspace(normal.ppf(0.01),normal.ppf(0.99), 100)
#num = np.random.randint(0,780)
#print(num)
#fp = normal.pdf(num) # Función de Probabil
#print(x)
#print(fp)

#print(np.random.rand(4))
#print(number)
#print(distnorm(1,60,9))
#print(generate_list_of_ship())
#print(stats.norm(60,9).)
print(disexp(np.random.uniform(),4))
print(disexp(np.random.uniform(),2))
print(disexp(np.random.uniform(),7))


