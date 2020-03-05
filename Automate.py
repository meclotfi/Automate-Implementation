class Automate(object):
    def __init__(self, X, So, S, F, I):
        self.X = X
        self.So = int(So)
        self.S = S
        self.F = F
        self.I = I
        # verification de l'alphabet
        if not all(len(s) == 1 for s in X):
            raise Exception("alphabet est fausse")
        # conformite de l'etat initiale et fineaux
        if (So >= len(S)):
            raise Exception("etat initiale non existant")
        for f in F:
            if f >= len(S):
                raise Exception("etat finale non existant")
        # verification des instructions
        for i in I:
            if((i[0] >= len(S)) | (i[2] >= len(S)) | (not (i[1] in X))):
                raise Exception("Instruction "+str(i)+"est fausse")

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
        trace = [w for w in word+"s"]
        trace[0] = self.So
        back = False
        while((j < len(word)) & (aprt)):
            if(back == False):
                list = self.succ(actu, word[j])
            else:
                back = False
            print("j=="+str(j)+"  on a "+str(len(list))+" choix " +
                  str([self.S[l[2]] for l in list]))
            if(len(list) == 0):
                if(len(pile) == 0):
                    aprt = False
                else:
                    elt = pile.pop()
                    print(elt)
                    actu = elt[0][0][2]
                    j = elt[1]
                    trace[j+1] = actu
                    list = elt[0]
                    back = True
                    if(len(elt[0]) > 1):
                        pile.append((elt[0][1:], elt[1]))
            else:
                if(len(list) == 1):
                    j = j+1
                    actu = list[0][2]
                    trace[j] = actu
                else:
                    pile.append((list[1:], j))
                    actu = list[0][2]
                    j = j+1
                    trace[j] = actu
                    if((j == len(word)) & (len(list[1:]) > 0) & (not(actu in self.F))):
                        j = j-1
                        list = list[1:]
                        back = True

        if((j == len(word)) & (actu in self.F)):
            aprt = True
        else:
            aprt = False
        return aprt, trace

    def afficher_trace(self, word):
        st = ''
        apt, trace = self.reconnaissance(word)

        if(apt == True):
            st = "le mot <<"+word+">>  est reconnus par l'automate A=" + self.__str__() +\
                "et son trace est: \n"

            j = 0
            for i in trace:
                st = st+word[:j]+" "+self.S[i]+"---->"
                j = j+1
            st = st+word
        else:
            st = st + "le mot <<"+word+">>  n'est pas reconnus par l'automate A=" + self.__str__()
        return st

    def Type(self):
        s = [len(s[1]) == 1 for s in self.I]
        simp = any(v == False for v in s)
        typ1 = ["simple" if not simp else "general"]

        m = any((val1[0] == val2[0]) & (val1[1] == val2[1]) & (
            val1[2] != val2[2]) for val1 in self.I for val2 in self.I)
        type2 = ["deterministe" if not m else "non deterministe"]
        return "l'automate est :"+str(typ1[0])+" "+str(type2[0])


# Automate(alphabet , l'etat initial  , tous les etats ,  liste des etats final,
# list des instruction)
A = Automate(["a", "b", "c"], 0, ["S0", "S1", "S2"], [2], [
    (0, "a", 0), (0, "a", 1), (0, "c", 2), (1, "b", 1), (1, "b", 0), (1, "b", 2), (2, "c", 2), (2, "c", 1), (2, "c", 0)])
#
print(A.Type())
# print(A.afficher_trace("accaccabc"))
