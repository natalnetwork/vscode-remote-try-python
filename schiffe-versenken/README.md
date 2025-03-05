# Schiffe-Versenken Spiel

Dies ist ein einfaches Schiffe-Versenken-Spiel, das in Python mit PyQt5 entwickelt wurde. Der Benutzer spielt gegen eine KI.

## Projektstruktur

```
schiffe-versenken
├── src
│   ├── main.py                # Einstiegspunkt der Anwendung
│   ├── ui
│   │   └── main_window.ui     # Layout des Hauptfensters
│   ├── controllers
│   │   └── game_controller.py  # Spiellogik
│   ├── models
│   │   └── game_model.py      # Spielzustand
│   ├── views
│   │   └── game_view.py       # Darstellung des Spiels
│   └── utils
│       └── ai.py              # KI-Logik
├── requirements.txt           # Abhängigkeiten
└── README.md                  # Dokumentation
```

## Installation

Um das Projekt auszuführen, stellen Sie sicher, dass Sie Python 3 und pip installiert haben. Installieren Sie die erforderlichen Pakete mit folgendem Befehl:

```
pip install -r requirements.txt
```

## Nutzung

Um das Spiel zu starten, führen Sie die `main.py` Datei aus:

```
python src/main.py
```

Viel Spaß beim Spielen!