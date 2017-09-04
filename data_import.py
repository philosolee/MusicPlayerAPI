import os
from DataModels.AlbumModel import Album
from DataModels.ArtistModel import Artist
from DataModels.TrackModel import Track
import eyed3

MUSIC_ROOT = "H:\Media\Music\Core"

Artist.objects().all().delete()
Track.objects().all().delete()
Album.objects().all().delete()


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name)) and name != ".sync"]


def create_artist_in_db(artist):
    new_artist = Artist(name=artist)
    new_artist.location = os.path.join(MUSIC_ROOT, artist)
    new_artist.save()


def create_albums_for_artist(artist):
    album_list = get_immediate_subdirectories(os.path.join(MUSIC_ROOT, artist))

    for album in album_list:
        new_album = Album(title=album)
        new_album.artist = Artist.objects(name=artist).first()
        new_album.location = os.path.join(MUSIC_ROOT, artist, album)
        new_album.save()

    return album_list


def create_tracks_for_album(artist, album):
    track_list = os.listdir(os.path.join(MUSIC_ROOT, artist, album))
    for track in track_list:
        if track.endswith(".mp3"):
            track_path = os.path.join(MUSIC_ROOT, artist, album, track)

            meta_data = eyed3.load(track_path)
            if meta_data.tag.title is not None:
                new_track = Track(meta_data.tag.title)
            else:
                print("no title in ID3 tag for track: {0} in dir: {1}".format(track, track_path))
                continue
            artist_object = Artist.objects(name=artist).first()
            new_track.artist = artist_object
            new_track.album = Album.objects(artist=artist_object, title=album).first()
            if meta_data.tag.genre is not None:
                new_track.genre = meta_data.tag.genre.name
            if meta_data.tag.recording_date is not None:
                new_track.year = str(meta_data.tag.recording_date)
            if meta_data.tag.track_num is not None:
                new_track.track_number = meta_data.tag.track_num[0]
            new_track.location = track_path
            new_track.save()


artists = get_immediate_subdirectories(MUSIC_ROOT)


for a in artists:
    create_artist_in_db(a)
    artist_albums = create_albums_for_artist(a)
    for artist_album in artist_albums:
        create_tracks_for_album(a, artist_album)



