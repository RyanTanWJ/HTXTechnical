# HTXTecnical

## Linux installation
1. Install SQLite
```zsh
sudo apt install sqlite3
```
2. Apply tables.sql to create tables
```zsh
user@server:~/<workspace>$ sqlite3 backend/default.db
sqlite> < copy commands from tables.sql >
```

## High Level Architecture Diagramw
![architecture](./architecture.pdf)

A very simple setup utilising VueJS to create a web application that users can interact with.

The web application communicates with the backend server running on Flask.

Flask then uses the services provided by WhisperAI and SQLite.