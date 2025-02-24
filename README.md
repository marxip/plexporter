# Exportador de Playlists de YouTube Music a CSV

Este script permite exportar una playlist de YouTube Music a un archivo CSV con formato UTF-8. Incluye información como título de la canción, artista, álbum, duración e ID del video.

## Características

- Extrae automáticamente la ID de una playlist a partir de su URL.
- Obtiene los datos de cada canción utilizando la API de YouTube Music.
- Guarda la información en un archivo CSV con separación por `;` (punto y coma).
- Manejo de caracteres latinos y signos de puntuación sin pérdida de información.
- Evita sobreescribir archivos generando nombres únicos.

## Requisitos

- Python 3.x
- Paquete `ytmusicapi`
- Archivo `credentials.json` con las credenciales de autenticación de YouTube Music API

## Instalación

1. Clonar el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/ytmusic-playlist-exporter.git
   cd ytmusic-playlist-exporter
   ```
2. Instalar dependencias:
   ```sh
   pip install ytmusicapi
   ```

## Uso

1. Ejecutar el script:
   ```sh
   python script.py
   ```
2. Ingresar la URL de la playlist de YouTube Music cuando se solicite.
3. El archivo CSV se generará en la misma carpeta del script.

## Formato de Salida (CSV)

Cada archivo CSV generado tendrá la siguiente estructura:

```
Título;Artista;Álbum;Duración;ID
"Canción 1";"Artista 1";"Álbum 1";"3:45";"abc123"
"Canción 2";"Artista 2";"Álbum 2";"4:10";"def456"
...
```

## Notas

- Se debe contar con el archivo `credentials.json` configurado correctamente.
- Si el archivo ya existe, se genera una versión numerada para evitar sobrescribirlo.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.

---
