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
```

### Setup database by make file

```
virtualenv venv
./makedb.sh
pip install -r requirements/requirements_db.txt
python database/createdb.py
```

### or Create a database and user from psql

```
psql
=#CREATE DATABASE cad_keysafe;
=#CREATE USER cad_root WITH PASSWORD 'root_pass';
=#GRANT ALL PRIVILEGES ON DATABASE cad_keysafe to cad_root;
virtualenv venv
pip install -r requirements/requirements_db.txt
python database/createdb.py
```

### Check created database:
```
psql -d cad_keysafe
cad_keysafe=# \dt
 Schema |     Name      | Type  |  Owner   
--------+---------------+-------+----------
 public | key           | table | cad_root
 public | user          | table | cad_root
 public | user_key_link | table | cad_root
 
if you see this shit, all is ok! :smiley:

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
