from flask_script import Manager
from songbase import app, db, Artist, Song

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    coldplay = Artist(name='Coldplay', about='Coldplay is a British rock band.')
    maroon5 = Artist(name='Maroon 5', about='Maroon 5 is an American pop rock band.')
    song1 = Song(name = 'yellow', year=2004, lyrics='and it was all yellow', artist=coldplay)
    song2 = Song(name = 'yellow 2', year=2004, lyrics='and it was all yellow 2', artist=coldplay)
    db.session.add(coldplay)
    db.session.add(maroon5)
    db.session.add(song1)
    db.session.add(song2)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
