from dataclasses import dataclass

@dataclass
class Album:
    AlbumId: int
    Title: str
    ArtistId: int
    totD: float

    def __hash__(self):
        return hash(self.AlbumId)

    #def __eq__(self, other):
        #return self.AlbumId == other.AlbumId

    def __str__(self):
        return f"{self.Title} -- {toMinutes(self.totD)}"

def toMinutes(d):
    return d/1000/60
