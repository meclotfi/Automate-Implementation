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
        index = 0
        while((j < len(word)) & (aprt)):
            list = self.succ(actu, word[j])
            print(list)
            if(len(list) == 0):
                if(len(pile) == 0):
                    aprt = False
                else:
                    print("phase depilement")
                    elt = pile.pop()
                    print(len(elt))
                    actu = elt[0][0][2]
                    j = elt[1]
                    print((actu, j))
                    if(len(elt[0]) > 0):
                        pile.append((elt[0][1:], elt[1]))
            else:
                if(len(list) == 1):
                    j = j+1
                    actu = list[0][2]
                else:
                    print("phase empilement")
                    j = j+1
                    print((list[1:], j))
                    pile.append((list[1:], j))
                    actu = list[0][2]
        if((j == len(word)) & (actu in self.F)):
            aprt = True
        else:
            aprt = False
        return aprt


# Automate(alphabet , l'etat initial  , tous les etats ,  liste des etats final,
# list des instruction)
A = Automate(["a", "b"], 0, ["S0", "S1"], [1], [
    (0, "a", 0), (0, "a", 1), (1, "b", 1), (1, "b", 0)])
print(A)
print(A.reconnaissance("abaabababababab"))
