from collections import deque
from torre import Torre 

discos = range(1, 8)

torre_esq = Torre('Torre Esquerda')
torre_central = Torre('Torre Central', sorted(discos, reverse=True))
torre_dir = Torre('Torre Direita')

joga_1 = True
    
class THanoi:
    def torre_apta(self, d, torre):
        if len(torre) == 0:
            return True
        valor = torre[len(torre) - 1]
        if d > valor: 
            return False
        return True
 
    def encaminha_jogada(self, d):
        if d in torre_dir:
            self.melhor_jogada(d, torre_esq, torre_central)
        elif d in torre_central: 
            self.melhor_jogada(d, torre_dir, torre_esq)
        elif d in torre_esq: 
            self.melhor_jogada(d, torre_dir, torre_central)
    
    def torre_completa(self, torre):
        num_elements = len(torre)
        if num_elements == 0:
            return False
        completa = (num_elements == (torre[0] - torre[num_elements - 1]) + 1)
        print 'Torre completa', completa
        return completa
     
    def ciclo_completo(self):
           td_completa = self.torre_completa(torre_dir)
           te_completa = self.torre_completa(torre_esq)
           if(td_completa and te_completa):
               if(len(torre_dir) == 1 and torre_dir[0] == max(torre_esq) + 1):
                   return True
               if(len(torre_esq) == 1 and torre_esq[0] == max(torre_dir) + 1):
                   return True
           return False
    
    def torre_primeiro_mov(self, d):
        torre = self.obter_torre(d)
        length = len(torre)
        if length % 2 == 0:
            return torre_central
        else:
            return self.obter_torre_oposta(torre)
        
    def obter_torre_oposta(self, torre):
        if torre.name == 'Torre Esquerda':
            return torre_dir
        if torre.name == 'Torre Direita':
            return torre_esq
                
    def melhor_jogada(self, d, torreA, torreB):
        if not self.torre_apta(d, torreA):
             self.move_disco(d, torreB)
             return
        if not self.torre_apta(d, torreB):
             self.move_disco(d, torreA)
             return
         
        dA = self.topo(torreA)
        dB = self.topo(torreB)
        
        par_esperando = ((dA - 1) == d) or ((dB - 1) == d)
        
        if dB == 0 and not par_esperando:
            self.move_disco(d, torreB)
        elif dA == 0 and not par_esperando:
            self.move_disco(d, torreA)
        else:
            #two possible moves!
            if (dA - 1) == d:
                self.move_disco(d, torreA)
            elif (dB - 1) == d:
                self.move_disco(d, torreB)
            elif self.ciclo_completo():
                torre = self.torre_primeiro_mov(d)
                self.move_disco(d, torre)
            else:
                self.realiza_jogada_complexa(d, torreA, torreB)
                                                                            
    def realiza_jogada_complexa(self, d, torreA, torreB):
        indiceProxDoAtual = (d + 1)
        indiceProxProx = (d + 2)
        torreAtual = self.obter_torre(d)
        penultimoDisco = torreAtual[len(torreAtual) - 2]
        if d == (penultimoDisco - 1):
            if self.obter_torre(indiceProxProx) == torreA:
                self.move_disco(d, torreB)
            else:
                self.move_disco(d, torreA)
        
    def obter_torre(self, d):
        if d in torre_dir:
            return torre_dir
        elif d in torre_central: 
            return torre_central
        elif d in torre_esq: 
            return torre_esq
        
    def topo(self, torre):
        if len(torre) == 0:
            return 0
        valor = torre[len(torre) - 1]
        return valor
       
    def move_disco(self, d, torre):
        if d in torre_esq:
            torre_esq.pop()
        if d in torre_central:
            torre_central.pop()
        if d in torre_dir:
            torre_dir.pop()
        
        self.escreve_movimento(d, torre)
        torre.append(d)
    
    def escreve_movimento(self, d, torre):
        print d, '=>', torre
            
    def executa_movimento(self):
        global joga_1          
        if joga_1:
            self.encaminha_jogada(1)
            joga_1 = False
        else:
            dE = self.topo(torre_esq)
            dC = self.topo(torre_central)
            dD = self.topo(torre_dir)
            values = [v for v in [dE, dC, dD] if v != 1 and v > 0]
            minValue = min(values)
            self.encaminha_jogada(minValue)
            joga_1 = True
        
th = THanoi()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()
th.executa_movimento()