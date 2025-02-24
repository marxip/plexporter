import re
import os
from ytmusicapi import YTMusic

def obtener_playlist_id(url):
    """Extrae la ID de la playlist desde una URL válida de YouTube Music."""
    match = re.search(r"list=([\w-]+)", url)
    return match.group(1) if match else None

def limpiar_nombre(nombre):
    """Limpia el nombre de la playlist eliminando caracteres inválidos para nombres de archivos."""
    nombre = re.sub(r'[\\/:*?"<>|]', "", nombre)  # Solo eliminamos los caracteres no permitidos en nombres de archivo
    return nombre.strip()

def generar_nombre_archivo(base_name):
    """Genera un nombre de archivo único para evitar sobreescritura."""
    base_name = limpiar_nombre(base_name)
    filename = f"{base_name}.csv"
    
    counter = 1
    while os.path.exists(filename):
        filename = f"{base_name} ({counter}).csv"
        counter += 1
    
    return filename

def main():
    url = input("🎵 Ingresa la URL de la playlist de YouTube Music: ").strip()
    
    playlist_id = obtener_playlist_id(url)
    if not playlist_id:
        print("❌ Error: No se pudo extraer la ID de la playlist. Verifica la URL.")
        return

    print(f"✅ Playlist ID extraída: {playlist_id}")

    ytmusic = YTMusic(oauth_credentials="credentials.json")

    playlist = ytmusic.get_playlist(playlist_id)
    if not playlist:
        print("❌ No se encontró la playlist o no tienes acceso.")
        return
    
    playlist_title = playlist["title"]
    print(f"🎶 Exportando playlist: {playlist_title} ({len(playlist['tracks'])} canciones)")

    # Generar nombre de archivo basado en la playlist
    filename = generar_nombre_archivo(playlist_title)

    # Exportar a CSV con codificación UTF-8 y separador ;
    with open(filename, "w", encoding="utf-8-sig") as f:
        f.write("Título;Artista;Álbum;Duración;ID\n")
        for track in playlist["tracks"]:
            title = track["title"]
            artist = track["artists"][0]["name"] if track["artists"] else "Desconocido"
            album_data = track.get("album")
            album = album_data["name"] if album_data else "Desconocido"  # Evita el error
            duration = track.get("duration", "Desconocida")
            video_id = track["videoId"]
            f.write(f'"{title}";"{artist}";"{album}";"{duration}";"{video_id}"\n')

    print(f"✅ Exportación completada: {filename}")

if __name__ == "__main__":
    main()
