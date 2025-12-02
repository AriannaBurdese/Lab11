from dataclasses import dataclass
@dataclass
class Rifugio:
    id: int
    nome: str
    localita: str
    altitutide: int
    capienza : int
    aperto: int


    def __str__(self):
        return f"{self.id, self.nome, self.localita, self.altitutide, self.capienza, self.aperto }"
    def __repr__(self):
        return f"{self.id, self.nome, self.localita, self.altitutide, self.capienza, self.aperto }"


