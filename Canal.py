import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from binarytree import heapq

heap = heapq
Time = 0
body_heap = []
list_times_lock1 = []
list_times_lock2 = []
list_times_lock3 = []
list_times_lock4 = []
list_times_lock5 = []

def Printlistship(list):
    a = []
    for x in list:
        a.append(x.id)
    print('Aqui va la lista')
    print(a)

class lock:

    def __init__(self, id):
        self.id = id
        self.name = 'lock' + str(id)
        self.free = True
        self.capacity = 12
        self.list_ship = []
        self.open = np.infty
        self.ready_ship = np.infty
        self.ready_transp = np.infty
        self.ready_exit = np.infty


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

    def fist_lock(self):
        global Time
        select_ships = self.select_ship_in()

        for x in select_ships:
            Time += x.tarrive

        time_open = self.disexp(np.random.uniform(), 4)

        time_in = self.disexp(np.random.uniform(), 2) * len(select_ships)

        time_trans = self.disexp(np.random.uniform(), 7)

        time_exit = (self.disexp(np.random.uniform(), 1.5)) * len(select_ships)

        Time += time_exit + time_trans + time_in + time_open

        return select_ships

    def Media(self,*args):
        suma = 0
        denominador = 0
        for x in args:
            denominador += len(x)
            for y in x:
                suma += y
        return suma/denominador

    def manager(self):
        global Time
        global body_heap
        list_of_ships = self.generate_list_of_ship()
        self.build_heap(list_of_ships)
        #print(body_heap)


        while Time < 111100:
            var = Time
            list = self.fist_lock()
            list_times_lock1.append(Time-var)
            var = Time
            self.all_steep(list)
            list_times_lock2.append(Time - var)
            var = Time
            self.all_steep(list)
            list_times_lock3.append(Time - var)
            var = Time
            self.all_steep(list)
            list_times_lock4.append(Time - var)
            var = Time
            self.all_steep(list)
            list_times_lock5.append(Time - var)
            var = Time

        print('La media de espera de los barcos es ' + str(
            self.Media(list_times_lock2, list_times_lock1, list_times_lock3, list_times_lock4, list_times_lock5)) + ' minutos')

        #while Time <= 100:
            #flag = self.procces_tails()
            #if flag[0]:
                #self.next_lock(flag[1], 1)
            #else:
                #flag = self.all_steep(1,self.lockslist[1].list_ship)

            #if flag[0]:
            #    self.next_lock(flag[1],2)
            #else:
            #    flag = self.all_steep(2, self.lockslist[1].list_ship)


            #if flag[0]:
            #    self.next_lock(flag[1],3)
            #else:
            #    flag = self.all_steep(3, self.lockslist[1].list_ship)

            #if flag[0]:
            #    self.next_lock(flag[1], 4)
            #else:
            #    flag = self.all_steep(4, self.lockslist[1].list_ship)









    def generate_list_of_ship(self) -> list:
        list = []
        id = 0
        var = 50
        for x in range(1, var):
            id += 1
            ran = np.random.randint(0, 781)
            if ran < 240:
                list.append((self.distnorm(ran, 5, 2), 2, id))
                continue
            if ran < 600:
                list.append((self.distnorm(ran, 3, 1), 2, id))
                continue
            list.append((self.distnorm(ran, 10, 2), 2, id))

        for x in range(1, var):
            id += 1
            ran = np.random.randint(0, 781)
            if ran < 240:
                list.append((self.distnorm(ran, 15, 3), 4, id))
                continue
            if ran < 600:
                list.append((self.distnorm(ran, 10, 5), 4, id))
                continue
            list.append((self.distnorm(ran, 20, 5), 4, id))

        for x in range(1, var):
            id += 1
            ran = np.random.randint(0, 781)
            if ran < 240:
                list.append((self.distnorm(ran, 45, 3), 8, id))
                continue
            if ran < 600:
                list.append((self.distnorm(ran, 35, 7), 8, id))
                continue
            list.append((self.distnorm(ran, 60, 9), 8, id))

        return list

    def build_heap(self,lis):
        for x in lis:
            if x[0] <= 780:
                heap.heappush(body_heap, x)
            else:
                continue

    def distnorm(self, x, mu, sigma):
        return int(((1 / (sigma * np.sqrt(2 * np.pi))) * (np.e ** (((-1) / 2)) * ((x - mu) / sigma) ** 2)) / 10)

    def disexp(self, x, alpha):
        return int(((1 / alpha) * np.e ** (-x / alpha)) * 70)

    def run_locks(self):
        for x in reversed(self.lockslist):
            if not x.free:
                for y in x.list_ship:
                    pass
            else:
                continue


    def procces_tails(self ):
        if self.lockslist[0].free:

            #print('Comienza la primera excluza ')

            #if self.lockslist[0].free:

            if self.lockslist[0].open == np.infty:
                time_open = self.disexp(np.random.uniform(),4)
                self.lockslist[0].open = time_open

            if self.lockslist[0].free:
                if self.lockslist[0].open == 0:
                    #print('Ya pueden entrar los barcos')
                    list = self.select_ship_in()
                    self.lockslist[0].list_ship = list

                    if self.lockslist[0].ready_ship == np.infty:
                        time_in = self.disexp(np.random.uniform(),2)* len(list)
                        self.lockslist[0].ready_ship = time_in
                    if self.lockslist[0].ready_ship == 0:
                        self.lockslist[0].free = False

                        Printlistship(self.lockslist[0].list_ship)
                        return (True,self.lockslist[0].list_ship)

                    if self.lockslist[0].ready_ship > 0:
                        self.lockslist[0].ready_ship -= 1

                else:
                    self.lockslist[0].open -= 1

        if not self.lockslist[0].free and self.lockslist[0].open == 0:
            if self.lockslist[0].ready_transp == np.infty:
                time_trans = self.disexp(np.random.uniform(),7)
                self.lockslist[0].ready_transp = time_trans

        if self.lockslist[0].ready_transp == 0:
            if self.lockslist[0].ready_exit == np.infty:
                time_exit = (self.disexp(np.random.uniform(),1.5))* len(self.lockslist[0].list_ship)
                self.lockslist[0].ready_exit = time_exit

        if self.lockslist[0].ready_transp > 0:
            self.lockslist[0].ready_transp -= 1

        if self.lockslist[0].ready_exit == 0:
            id = self.lockslist[0].id
            list_to_ret = self.lockslist[0].list_ship
            self.lockslist[0] = lock(id)
            return (True,list_to_ret)

        if self.lockslist[0].ready_exit > 0:
            self.lockslist[0].ready_exit -= 1
        return (False,[])

    def next_lock(self,list,lock_id):
        self.all_steep(lock_id,list)



    def all_steep(self, list):
        global Time
        time_open = self.disexp(np.random.uniform(), 4)

        time_in = self.disexp(np.random.uniform(), 2) * len(list)

        time_trans = self.disexp(np.random.uniform(), 7)

        time_exit = (self.disexp(np.random.uniform(), 1.5)) * len(list)

        Time += time_open + time_in +time_trans + time_exit

    def select_ship_in(self) -> list:
        list_aux = []
        while len(body_heap) > 0:
            pop = heap.heappop(body_heap)
            if self.lockslist[0].capacity >= pop[1]:
                self.lockslist[0].list_ship.append(ship(pop[2], pop[1],pop[0]))
                self.lockslist[0].capacity -= pop[1]
                if self.lockslist[0].capacity == 0:
                    return self.lockslist[0].list_ship
            else:
                list_aux.append(pop)
        else:
            for x in list_aux:
                heap.heappush(body_heap,x)
            return self.lockslist[0].list_ship


            # Empezar el poceso sin estar lleno el dique

class ship:

    def __init__(self, id, range ,tarrive):
        self.id = id;
        self.tarrive = tarrive
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
    return list



if __name__ == '__main__':
    canal = Channel()
    canal.manager()







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



