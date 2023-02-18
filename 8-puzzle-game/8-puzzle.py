from queue import Queue 
import copy
import time

endNode = []
nodePocet = 0

def printNode(node):    # funkcia ktora sluzi na vypisanie nodu (uzlu), postupne vypise jednotlive pozicie
    print(node[0],node[1],node[2])
    print(node[3],node[4],node[5])
    print(node[6],node[7],node[8])   
    print('------')

def checkFinal(node_zaciatok,node_koniec): # funkcia ktora porovnava ci sa zhoduju nody (od nultej po 9 poziciu) ak ano tak program nasiel cestu k rieseniu
    if node_zaciatok[:9]==node_koniec[:9]:
        printNode(endNode)       
        return True
    return False

def check_zaciatok(node_zaciatok): # funkcia ktora kontroluje ci uz sa dany uzol vyskitol ak ano vrati iba false ak nie tak ho zapise do zoznamu pozretych uzlov a pomocneho zoznamu
    global nodePocet
    if node_zaciatok[:9] not in visitedList_zaciatok:
        queue_zaciatok.put(node_zaciatok)
        pomocny_zoznam_zaciatok.append(node_zaciatok)
        visitedList_zaciatok.append(node_zaciatok[:9])
    nodePocet+=1
    return False

def check_koniec(node_koniec): # funkcia pracuje na rovnakej baze ako predosla len do nej vstupuje uzol od koncovej strany
    global nodePocet
    if node_koniec[:9] not in visitedList_koniec:
        queue_koniec.put(node_koniec)
        pomocny_zoznam_koniec.append(node_koniec)
        visitedList_koniec.append(node_koniec[:9])
    nodePocet+=1
    return False

pomocny_zoznam_zaciatok = []
pomocny_zoznam_koniec = []
print("pre spustenie hry stlačťe 1 pre ukončenie 0 : ",end="")
vstup = int(input())

while vstup == 1:
    print("Zadajte vstup (čísla od 1 po 8 a na miesto medzery číslo 0)")
    print("Začiatočný stav: ",end="")
    start = str(input()) # pouzivatel zada vstup
    startNode = []
    for x in range(len(start)):
        startNode.append(int(start[x]))  # vytvorenie pola startNode 


    print("Zadajte výstup (čísla od 1 po 8 a na miesto medzery číslo 0)")
    print("Koncový stav: ",end="")
    end=str(input())
    endNode = []
    for x in range(len(end)):
        endNode.append(int(end[x]))
 
    if  len(startNode) == len(endNode) == 9:
        if 1 in startNode and 2 in startNode and 3 in startNode and 4 in startNode and 5 in startNode and 6 in startNode and 7 in startNode and 8 in startNode and 0 in startNode:
            if 1 in endNode and 2 in endNode and 3 in endNode and 4 in endNode and 5 in endNode and 6 in endNode and 7 in endNode and 8 in endNode and 0 in endNode: # ak platia tieto podmienky znamena ze vstup aj vystup su vyhovujuce
                found = False
                visitedList_zaciatok = []
                visitedList_koniec = []
                queue_zaciatok = Queue()
                queue_zaciatok.put(startNode)
                queue_koniec = Queue()
                queue_koniec.put(endNode)
                visitedList_zaciatok.append(startNode)
                printNode(startNode)
                pomocny_zoznam_koniec.append(endNode)

                if startNode == endNode:
                    print("Hlavolam je poskladaný")
                    break

                t1 = time.perf_counter()

                while (not found and not queue_zaciatok.empty()):
                    currentNode_zaciatok = queue_zaciatok.get()
                    blankIndex_zaciatok = currentNode_zaciatok.index(0)  # prazdne policko je na tom mieste ktore je oznacene 0
                    currentNode_koniec = queue_koniec.get()
                    blankIndex_koniec = currentNode_koniec.index(0)

                    if blankIndex_zaciatok!=0 and blankIndex_zaciatok!=1 and blankIndex_zaciatok!=2 and found == False: # ak sa prazdne policko nenachadza na poziciach 0,1,2 a found je false tak sa s prazdnym polickom mozme posunut vyssie
                        upNode_zaciatok = copy.deepcopy(currentNode_zaciatok)
                        upNode_zaciatok[blankIndex_zaciatok] = upNode_zaciatok[blankIndex_zaciatok-3]
                        upNode_zaciatok[blankIndex_zaciatok-3] = 0
                        upNode_zaciatok.append('HORE')
                        found = check_zaciatok(upNode_zaciatok)

                    if blankIndex_zaciatok!=0 and blankIndex_zaciatok!=3 and blankIndex_zaciatok!=6 and found == False: # ak sa prazdne policko nenachadza na poziciach 0,3,3 a found je false tak sa s prazdnym polickom mozme posunut dolava
                        leftNode_zaciatok = copy.deepcopy(currentNode_zaciatok)
                        leftNode_zaciatok[blankIndex_zaciatok] = leftNode_zaciatok[blankIndex_zaciatok-1]
                        leftNode_zaciatok[blankIndex_zaciatok-1] = 0
                        leftNode_zaciatok.append('DOĽAVA')
                        found = check_zaciatok(leftNode_zaciatok)

                    if blankIndex_zaciatok!=6 and blankIndex_zaciatok!=7 and blankIndex_zaciatok!=8 and found == False: # ak sa prazdne policko nenachadza na poziciach 6,7, a found je false tak sa s prazdnym polickom mozme posunut dole
                        downNode_zaciatok = copy.deepcopy(currentNode_zaciatok)
                        downNode_zaciatok[blankIndex_zaciatok] = downNode_zaciatok[blankIndex_zaciatok+3]
                        downNode_zaciatok[blankIndex_zaciatok+3] = 0
                        downNode_zaciatok.append('DOLE')
                        found = check_zaciatok(downNode_zaciatok)

                    if blankIndex_zaciatok!=2 and blankIndex_zaciatok!=5 and blankIndex_zaciatok!=8 and found == False: # ak sa prazdne policko nenachadza na poziciach 2,5,8 a found je false tak sa s prazdnym polickom mozme posunut doprava
                        rightNode_zaciatok = copy.deepcopy(currentNode_zaciatok)
                        rightNode_zaciatok[blankIndex_zaciatok] = rightNode_zaciatok[blankIndex_zaciatok+1]
                        rightNode_zaciatok[blankIndex_zaciatok+1] = 0
                        rightNode_zaciatok.append('DOPRAVA')
                        found = check_zaciatok(rightNode_zaciatok)
        
                    ###

                    if blankIndex_koniec!=0 and blankIndex_koniec!=1 and blankIndex_koniec!=2 and found == False: # kedze ideme od konca tak pri tychto podmienkach postupujeme opacne 
                        upNode_koniec = copy.deepcopy(currentNode_koniec)
                        upNode_koniec[blankIndex_koniec] = upNode_koniec[blankIndex_koniec-3]
                        upNode_koniec[blankIndex_koniec-3] = 0
                        upNode_koniec.append('DOLE')
                        found = check_koniec(upNode_koniec)

                    if blankIndex_koniec!=0 and blankIndex_koniec!=3 and blankIndex_koniec!=6 and found == False:
                        leftNode_koniec = copy.deepcopy(currentNode_koniec)
                        leftNode_koniec[blankIndex_koniec] = leftNode_koniec[blankIndex_koniec-1]
                        leftNode_koniec[blankIndex_koniec-1] = 0
                        leftNode_koniec.append('DOPRAVA')
                        found = check_koniec(leftNode_koniec)

                    if blankIndex_koniec!=6 and blankIndex_koniec!=7 and blankIndex_koniec!=8 and found == False:
                        downNode_koniec = copy.deepcopy(currentNode_koniec)
                        downNode_koniec[blankIndex_koniec] = downNode_koniec[blankIndex_koniec+3]
                        downNode_koniec[blankIndex_koniec+3] = 0
                        downNode_koniec.append('HORE')
                        found = check_koniec(downNode_koniec)

                    if blankIndex_koniec!=2 and blankIndex_koniec!=5 and blankIndex_koniec!=8 and found == False:
                        rightNode_koniec = copy.deepcopy(currentNode_koniec)
                        rightNode_koniec[blankIndex_koniec] = rightNode_koniec[blankIndex_koniec+1]
                        rightNode_koniec[blankIndex_koniec+1] = 0
                        rightNode_koniec.append('DOĽAVA')
                        found = check_koniec(rightNode_koniec)

                    ###

                    for x in range(len(pomocny_zoznam_zaciatok)):  # vo for cykloch sa porovnavaju jednotlive uzli ak sa nejake dvojice zhoduju tak progrmam nasiel cestu
                        for y in range(len(pomocny_zoznam_koniec)):
                             a = pomocny_zoznam_zaciatok[x]
                             b = pomocny_zoznam_koniec[y]  
                             found = checkFinal(a[:9],b[:9]) #pomocny_zoznam_zaciatok[x],pomocny_zoznam_koniec[y])
                             if found == True:
                                 a = pomocny_zoznam_zaciatok[x]
                                 b = pomocny_zoznam_koniec[y]  
                                 b.reverse() # kedze druha polovica krokov je v zlom smere je potrebne tento zoznam obratit 
                                 print(a[9:],b[0:-9])   # vypis cesty
                                 hlbka_z = len(a)-9
                                 hlbka_k = len(b)-9
                                 print("Hlbka stromu od začiatku :", hlbka_z)
                                 print("Hlbka stromu od konca :", hlbka_k)
                                 print("Pocet uzlov: ",nodePocet)
                                 print("Počet ťahov potrebných na vyriešenie: ", len(a)+len(b)-18) # -18 preto lebo v kazdom zozname je 9 cislic ktore nepredstavuju tak 
                                 break
                        if found == True:
                            break

                    
                t2 = time.perf_counter()
                print('čas riešenia:', t2-t1)
                print('------')      
                if queue_zaciatok.empty():
                    print("Hlavolam nieje riešiteľný !")
                    break
                print("pre spustenie hry stlačťe 1 pre ukončenie 0 : ",end="")
                pomocny_zoznam_zaciatok = []
                pomocny_zoznam_koniec = []
                nodePocet=0
                vstup = int(input())
                
            else:  # ak vstup nebol vyhovujuci pouzivatel je upozorneny
                print("Zlý vstup")
                print("pre spustenie hry stlačťe 1 pre ukončenie 0 : ",end="")
                vstup = int(input())
                pomocny_zoznam_zaciatok = []
                pomocny_zoznam_koniec = []
        else:
            print("Zlý vstup")
            print("pre spustenie hry stlačťe 1 pre ukončenie 0 : ",end="")
            vstup = int(input())
            pomocny_zoznam_zaciatok = []
            pomocny_zoznam_koniec = []
    else:
        print("Zlý vstup")
        print("pre spustenie hry stlačťe 1 pre ukončenie 0 : ",end="")
        vstup = int(input())
        pomocny_zoznam_zaciatok = []
        pomocny_zoznam_koniec = []
        
    
