# keysafe.software

```
git clone https://github.com/VolVoz/keysafe.software.git
```

## For OS X

```
$ brew install pyqt
```

## For Ubuntu

```
sudo apt-get update
sudo apt-get install python-qt4 pyqt4-dev-tools qt4-designer
```

## For Debian/Raspbian

```
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
```

## Install PostgreSQL
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib libpq-dev python-dev
```

#### Install requirements
```
pip install --upgrade pip
pip install -r requirements/requirements.txt
```

#### Create a database and user from psql

```
sudo -u postgres psql
CREATE DATABASE cad_keysafe;
CREATE USER cad_root WITH PASSWORD 'root_pass';
CREATE USER cad_django WITH PASSWORD 'root_pass';
GRANT ALL PRIVILEGES ON DATABASE cad_keysafe to cad_root;
GRANT ALL PRIVILEGES ON DATABASE cad_keysafe to cad_django;


python database/createdb.py
```

#### Check created database:
```
sudo -u postgres psql -d cad_keysafe
cad_keysafe=# \dt
 Schema |     Name      | Type  |  Owner
--------+---------------+-------+----------
 public | key           | table | cad_root
 public | user          | table | cad_root
 public | user_key_link | table | cad_root
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
