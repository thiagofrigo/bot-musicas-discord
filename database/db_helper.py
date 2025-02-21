import sqlite3
from querys_helper import Querys

class Db_control:

    def __init__(self):
        # Criando conexao com o banco
        self.connection = sqlite3.connect('playlists.database')
        self.cursor = self.connection.cursor()

    def create_bases(self):
        self.cursor.execute(Querys.CREATE_BASE_PLAYLISTS)
        self.cursor.execute(Querys.CREATE_BASE_SONGS)
        self.connection.commit()

    def add_playlist(self,playlist):
        self.cursor.execute(Querys.INSERT_PLAYLIST,(playlist,))
        self.connection.commit()

    def add_song(self,playlist,url):
        playlist_id = self.get_playlists(playlist)
        self.cursor.execute(Querys.INSERT_SONG,(playlist_id, url))


    def get_playlists(self,playlist):
         playlists_id = self.cursor.execute(Querys.SELECT_PLAYLIST, (playlist,))
         return playlists_id



#teste = Db_control()
#adiciona_playlist = teste.adiciona_playlist('batalha')
#playslists = teste.get_playlists()
#print(playslists)