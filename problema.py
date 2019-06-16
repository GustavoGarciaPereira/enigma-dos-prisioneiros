"""
por gustavo garcia pereira!
"""

import random

class ClassProblema(object):
    controle = 0
    cont = 0
    lampada = False
    pri_visitou = [0,1,2,3,4,5,6,7,8,9,10]
    print("problema!!")

    def popula_vetor(self, indi):
        self.pri_visitou.append(indi)

    def eleger_controle(self):
        self.controle = random.randrange(10)+1

    def visitar_sala(self):
        na_sala = random.randrange(10)+1
        if self.pri_visitou[na_sala] == self.controle:
            print("<<<<<<<<<<<  Controle na sala! >>>>>>>>>>>>>>>")
            if self.lampada:
                self.cont += 1
                self.lampada = False
        else:
            print("<<<<<<<<<<<<<<<<< Outro prisioneiro na sala! >>>>>>>>>>>>>>>>>")
            if not self.lampada:
                self.popula_vetor(na_sala)
                self.lampada = True

    def pergunta(self):
        print("@ numero de prisioneiros que sivitaraom a sala! ",self.cont)
        if self.cont == 10:
            print("todos já passarao na sala [S/N]: S")
            return False
        else:
            print("todos já passarao na sala [S/N]: N")
            return True



p = ClassProblema()
p.eleger_controle()
flag = True

while flag:
    p.visitar_sala()
    flag = p.pergunta()
