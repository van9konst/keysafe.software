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
$ sudo apt-get install python-qt4 pyqt4-dev-tools qt4-designer
```

## Install PostgreSQL
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

in postgresql.conf setup:
```

### Setup database by make file(old way,need renew)

```
virtualenv venv
./makedb.sh
pip install -r requirements/requirements_db.txt
python database/createdb.py
```

### or Create a database and user from psql

```
sudo -u postgres psql
=#CREATE DATABASE cad_keysafe;
=#CREATE USER cad_root WITH PASSWORD 'root_pass';
=#GRANT ALL PRIVILEGES ON DATABASE cad_keysafe to cad_root;

virtualenv venv
pip install -r requirements/requirements_db.txt
python database/createdb.py
```

## For Debian/Raspbian

```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib libpq-dev python-dev
```

#### Install pyenv
```
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
```

#### Update pyenv and install python 2.7.11
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
pyenv install 2.7.11
pyenv global 2.7.11
```

#### Install requirements
```
pip install --upgrade pip
pip install -r requirements/requirements.txt
```

### Check created database:
```
sudo -u postgres psql -d cad_keysafe
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
