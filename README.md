# keysafe.software

## For OS X

```
$ brew install pyqt
```

## For Ubuntu/Debian

```
$ sudo apt-get install python-qt4 pyqt4-dev-tools qt4-designer
```

## Install PostgreSQL
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

in postgresql.conf setup:
client_encoding = utf8
```

### Create a database and user

```
psql -d postgres
CREATE DATABASE cad_keysafe;
CREATE USER cad_root WITH PASSWORD 'root_pass';
GRANT ALL PRIVILEGES ON DATABASE cad_keysafe to cad_root;
```

### TODO:

- [x] Create requirements for Linux system
- [x] Create simple UI design
- [x] Connect windows
- [x] Folder structure
- [ ] Setup UnitTesting with Nose
- [x] Setup Database (PostgreSQL(prefer) or Mongo)
- [ ] Spawn windows for timers(e.g. with gevents)
- [ ] Make a runner
- [ ] Build as a python package
- [ ] It's not all :)
