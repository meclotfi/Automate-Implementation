class Automate(object):
    def __init__(self, X, So, S, F, I):
        self.X = X
        self.So = So
        self.S = S
        self.F = F
        self.I = I

    def __str__(self):
        st = ""
        for s in range(len(self.S)):
            st = st+"\n "+self.S[s]+":"
            for i in self.I:
                if(s == i[0]):
                    st = st+"----"+i[1]+'---->'+self.S[i[2]]+"\n    "
        return st

    def succ(self, s, m):
        l = []
        for i in self.I:
            if((i[0] == s) & (i[1] == m)):
                l.append(i)
        return l

    def reconnaissance(self, word):
        """retourne vrai si word est reconnus par l automate A et faux sinon"""
        actu = self.So
        j = 0
        list = []
        aprt = True
        pile = []
        trace = [w for w in word]
        trace[0] = self.So
        while((j < len(word)) & (aprt)):
            list = self.succ(actu, word[j])
            if(len(list) == 0):
                if(len(pile) == 0):
                    aprt = False
                else:
                    elt = pile.pop()
                    actu = elt[0][0][2]
                    j = elt[1]
                    trace[j] = actu
                    if(len(elt[0]) > 0):
                        pile.append((elt[0][1:], elt[1]))
            else:
                if(len(list) == 1):
                    trace[j] = actu
                    j = j+1
                    actu = list[0][2]
                else:
                    j = j+1
                    pile.append((list[1:], j))
                    actu = list[0][2]
                    trace[j-1] = actu
        if((j == len(word)) & (actu in self.F)):
            aprt = True
        else:
            aprt = False
        return aprt, trace

    def afficher_trace(self, word):
        st = ''
        apt, trace = self.reconnaissance(word)
        if(apt == True):
            st = "le mot <<"+word+">>  est reconnus par l'automate A=" + \
                self.__str__()+"et son trace est: \n"
            j = 0
            for i in trace:
                st = st+self.S[trace[i]]+" "+word[:j]+"---->"
                j = j+1
            st = st+word
        else:
            st = st = "le mot <<"+word+">>  n'est pas reconnus par l'automate A=" + \
                self.__str__()
        return st


# Automate(alphabet , l'etat initial  , tous les etats ,  liste des etats final,
# list des instruction)
A = Automate(["a", "b"], 0, ["S0", "S1"], [1], [
    (0, "a", 0), (0, "a", 1), (1, "b", 1), (1, "b", 0)])
print(A.afficher_trace("abaabab"))
