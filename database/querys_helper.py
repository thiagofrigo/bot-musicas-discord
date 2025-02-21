class Querys:
    CREATE_BASE_PLAYLISTS : str = """
        CREATE TABLE IF NOT EXISTS playlists(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """

    CREATE_BASE_SONGS: str = """
        CREATE TABLE IF NOT EXISTS songs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            playlist_id INTEGER,
            url TEXT NOT NULL,
            FOREIGN KEY (playlist_id) REFERENCES playlists(id) ON DELETE CASCADE    
        )
    """

    INSERT_PLAYLIST: str = '''
        INSERT INTO playlists (name) VALUES(?)
    '''

    SELECT_PLAYLIST: str = '''
        SELECT id FROM playlists WHERE name VALUES(?)
    '''

    INSERT_SONG: str = '''
        INSERT INTO songs (playlist_id, url) VALUES(?, ?)
    '''
