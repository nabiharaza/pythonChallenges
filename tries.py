class node:
    def __init__(self, value, child):
        self.value = value
        self.end = False
        self.child = {}
        if child is not None:
            self.child[child.value] = child

    def addToken(self, token):
        if len(token) == 0:
            self.end = True
            return
        if token[0] not in self.child:
            self.child[token[0]] = node(token[0], None)
        self.child[token[0]].addToken(token[1:])

    def searchToken(self, token):
        if len(token) == 0:
            return True
        if token[0] in self.child:
            return self.child[token[0]].searchToken(token[1:])
        else:
            return False

    def printMe(self):
        print (self.value, self.child.keys(), self.end)
        for i in self.child.values():
            i.printMe()

    def countLeaves(self):
        return sum(list(map(lambda x: x.countLeaves(), self.child.values()))) + (1 if self.end else 0)

    def getSubtree(self, token):
        if len(token) == 0:
            return self
        if token[0] in self.child:
            return self.child[token[0]].getSubtree(token[1:])
        else:
            return None

    def countOccurrences(self, token):
        subtree = self.getSubtree(token)
        return 0 if (subtree is None) else subtree.countLeaves()

root = node("*", None)
root.addToken("A")
root.addToken("a")
root.addToken("Vaffa")
root.addToken("Vaffrensdfsdfedfsdfsdfssfs")
root.addToken("Vaffrensdfefssfs")
root.addToken("Vaffrensdfsdfsdfssfs")
root.addToken("Vaffrensdfsdfsdxxfs")
root.addToken("Vaffrensxxfssfs")
root.addToken("Vaffrefsdfsdfssfs")
root.addToken("Vaffrefsdfsdfssfsc")
root.addToken("Vaffrefsdfsdfssfsd")
root.addToken("Vaffrefsdfsdfssfse")
root.addToken("Vaffrefsdfsdfssfsr")
root.addToken("Vaffrefsdfsdfssfsgg")
root.addToken("Vaffrefsdfsdfssfscc")
root.addToken("Vaffrefsdfsdfssfsxxx")
root.addToken("Vaffin")
root.addToken("Vaffend")
root.addToken("Bast")
root.addToken("Baste")
root.addToken("Basto")
root.addToken("Baston")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Basqweqweqweqweqwetone")
root.addToken("Basqweqweqweqweqwetone")
root.addToken("Basqweqweqweqweqwetosdfsdfe")
root.addToken("Bastone")
root.addToken("Bastdasdasdasdne")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Bastoner")
root.addToken("Bastonerro")
root.addToken("Abac")
root.addToken("Abbondanzi")
root.addToken("Abbondi")
root.addToken("Abdone")
root.addToken("Abelardo")
root.addToken("Abele")
root.addToken("Abenzio")
root.addToken("Abibo")
root.addToken("Abramio")
root.addToken("Abramo")
root.addToken("Acacio")
root.addToken("Acario")
root.addToken("Accursio")
root.addToken("Achille")
root.addToken("Acilio")
root.addToken("Aciscolo")
root.addToken("Acrisio")
root.addToken("Adalardo")
root.addToken("Adalberto")
root.addToken("Adalfredo")
root.addToken("Adalgiso")
root.addToken("Adalrico")
root.addToken("Adamo")
root.addToken("Addo")
root.addToken("Adelardo")
root.addToken("Adelberto")
root.addToken("Adelchi")
root.addToken("Adelfo")
root.addToken("Adelgardo")
root.addToken("Adelmo")
root.addToken("Adeodato")
root.addToken("Adolfo")
root.addToken("Adone")
root.addToken("Adriano")
root.addToken("Adrione")
root.addToken("Afro")
root.addToken("Agabio")
root.addToken("Agamennone")
root.addToken("Agape")
root.addToken("Agapito")
root.addToken("Agazio")
root.addToken("Agenore")
root.addToken("Agesilao")
root.addToken("Agostino")
root.addToken("Agrippa")
root.addToken("Aiace")
root.addToken("Aidano")
root.addToken("Aimone")
root.addToken("Aladino")
root.addToken("Alamanno")
root.addToken("Alano")
root.addToken("Alarico")
root.addToken("Albano")
root.addToken("Alberico")
root.addToken("Alberto")
root.addToken("Albino")
root.addToken("Alboino")
root.addToken("Albrico")
root.addToken("Alceo")
root.addToken("Alceste")
root.addToken("Alcibiade")
root.addToken("Alcide")
root.addToken("Alcino")
root.addToken("Aldo")
root.addToken("Aldobrando")
root.addToken("Aleandro")
root.addToken("Aleardo")
root.addToken("Aleramo")
root.addToken("Alessandro")
root.addToken("Alessio")
root.addToken("Alfio")
root.addToken("Alfonso")
root.addToken("Alfredo")
root.addToken("Algiso")
root.addToken("Alighiero")
root.addToken("Almerigo")
root.addToken("Almiro")
root.addToken("Aloisio")
root.addToken("Alvaro")
root.addToken("Alviero")
root.addToken("Alvise")
root.addToken("Amabile")
root.addToken("Amadeo")
root.addToken("Amando")
root.addToken("Amanzio")
root.addToken("Amaranto")
root.addToken("Amato")
root.addToken("Amatore")
root.addToken("Amauri")
root.addToken("Ambrogio")
root.addToken("Ambrosiano")
root.addToken("Amedeo")
root.addToken("Amelio")
root.addToken("Amerigo")
root.addToken("Amico")
root.addToken("Amilcare")
root.addToken("Amintore")
root.addToken("Amleto")
root.addToken("Amone")
root.addToken("Amore")
root.addToken("Amos")
root.addToken("Ampelio")
root.addToken("Anacleto")
root.addToken("Andrea")
root.addToken("Angelo")
root.addToken("Aniceto")
root.addToken("Aniello")
root.addToken("Annibale")
root.addToken("Ansaldo")
root.addToken("Anselmo")
root.addToken("Ansovino")
root.addToken("Antelmo")
root.addToken("Antero")
root.addToken("Antimo")
root.addToken("Antino")
root.addToken("Antioco")
root.addToken("Antonello")
root.addToken("Antonio")
root.addToken("Apollinare")
root.addToken("Apollo")
root.addToken("Apuleio")
root.addToken("Aquilino")
root.addToken("Araldo")
root.addToken("Aratone")
root.addToken("Arcadio")
root.addToken("Archimede")
root.addToken("Archippo")
root.addToken("Arcibaldo")
root.addToken("Ardito")
root.addToken("Arduino")
root.addToken("Aresio")
root.addToken("Argimiro")
root.addToken("Argo")
root.addToken("Arialdo")
root.addToken("Ariberto")
root.addToken("Ariele")
root.addToken("Ariosto")
root.addToken("Aris")
root.addToken("Aristarco")
root.addToken("Aristeo")
root.addToken("Aristide")
root.addToken("Aristione")
root.addToken("Aristo")
root.addToken("Aristofane")
root.addToken("Aristotele")
root.addToken("Armando")
root.addToken("Arminio")
root.addToken("Arnaldo")
root.addToken("Aronne")
root.addToken("Arrigo")
root.addToken("Arturo")
root.addToken("Ascanio")
root.addToken("Asdrubale")
root.addToken("Asimodeo")
root.addToken("Assunto")
root.addToken("Asterio")
root.addToken("Astianatte")
root.addToken("Ataleo")
root.addToken("Atanasio")
root.addToken("Athos")
root.addToken("Attila")
root.addToken("Attilano")
root.addToken("Attilio")
root.addToken("Auberto")
root.addToken("Audace")
root.addToken("Augusto")
root.addToken("Aureliano")
root.addToken("Aurelio")
root.addToken("Auro")
root.addToken("Ausilio")
root.addToken("Averardo")
root.addToken("Azeglio")
root.addToken("Azeli")

print root.countOccurrences("Ar")