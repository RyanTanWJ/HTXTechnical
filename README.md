# HTXTecnical

## Linux installation
1. Install SQLite
```zsh
sudo apt install sqlite3
```
2. Apply tables.sql to create tables
```zsh
user@server:~/<workspace>$ sqlite3 backend/default.db
sqlite> <copy commands from tables.sql>
```