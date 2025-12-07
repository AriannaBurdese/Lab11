import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self._id_map = {}



    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        self.G.clear() # svuoto grafo
        lista_rifugi = DAO.get_nodes()
        self._id_map = {}#associa ogni id del rifugio all'oggetto Rifugio corrispondente
        for rifugio in lista_rifugi:
            rifugio_id = getattr(rifugio, 'id',None)
            if rifugio_id is not None:
                self._id_map[rifugio_id] = rifugio

        sentieri = DAO.get_edges(year) #lista dei sentieri filtrata per anno
        for sentiero in sentieri:
            rifugio1 = self._id_map[sentiero.id_rifugio1] # prendo gli id dei due rifugi collegati, con id_map li trasformo negli oggeti RIFUGIO corrispondenti per usarli come nodi nel grafo
            rifugio2 = self._id_map[sentiero.id_rifugio2]

            self.G.add_edge(rifugio1, rifugio2) #networkx controlla se rifugio 1 e 2 sono gia dei nodi, e se non esistono li crea.



    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        rifugi = list(self.G.nodes())
        return rifugi

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """

        return len(list(self.G.neighbors(node)))
    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        return int(nx.number_connected_components(self.G))

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """
        #a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        #return a
        return b
    # metodo1 : bfs_tree()
    """"
    def get_reachable_bfs_tree(self, start):
        albero = nx.bfs_tree(self.G, start)
        nodi = list(albero.nodes())
        nodi.remove(start) #tolgo nodo di partenza
        return nodi"""

    def get_reachable_iterative(self, start):
        visitati = []
        da_visitare = [start]
        while da_visitare:
            for nodo in da_visitare:
                vicini = list(self.G.neighbors(nodo)) #prendo tutti i rifugi vicini
                for vicino in vicini:
                    if vicino not in visitati:
                        da_visitare.append(vicino)
                visitati.append(nodo)
                da_visitare.remove(nodo)
        if start in visitati:
            visitati.remove(start)
        return visitati






