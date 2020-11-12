class DocumentStore():
    docs = dict() #int, Document

    def add(self, doc):
        self.docs[doc.getDocId()] = doc

    def getAllValues(self):
        return self.docs.values()

    def getDoc(self, id):
        return self.docs[id]


