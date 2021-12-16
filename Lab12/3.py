from ChainingHashTableMap import ChainingHashTableMap
from DoublyLinkedList import DoublyLinkedList
class PlayList:
    def __init__(self):
        self.song_table = ChainingHashTableMap()
        self.song_list = DoublyLinkedList()

    def add_song(self,new_song_name):
        self.song_list.add_last(new_song_name)
        self.song_table.__setitem__(new_song_name,self.song_list.trailer.prev)

    def add_song_after(self, song_name, new_song_name ):
        try:
            index_node = self.song_table[song_name]
            self.song_list.add_after(index_node,new_song_name)
            self.song_table.__setitem__(new_song_name,index_node.next)
        except KeyError:
            raise KeyError('this song not in PlayList')

    def play_song(self,song_name):
        if song_name in self.song_table:
            print('Playing'+ ' ' +song_name)
        else:
            raise KeyError ('this song not in PlayList')

    def play_list(self):
        for i in self.song_list:
            print( 'Playing'+ ' ' + i )

p1 = PlayList( )
p1.add_song("Jana Gana Mana")
p1.add_song("Kimi Ga Yo")
p1.add_song("The Star-Spangled Banner")
p1.add_song("March of the Volunteers")
p1.add_song_after("The Star-Spangled Banner", "La Marcha Real")
p1.add_song_after("Kimi Ga Yo", "Aegukga")
p1.add_song("Arise, O Compatriots")
p1.add_song("Chant de Ralliement")
p1.add_song_after("Chant de Ralliement", "Himno Nacional Mexicano")
p1.add_song_after("Jana Gana Mana", "God Save The Queen")
p1.play_song("The Star-Spangled Banner")
p1.play_song("Jana Gana Mana")
p1.play_list( )


