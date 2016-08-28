#!/bin/sh

echo "сreate a new database"

if psql -lqt | cut -d \| -f 1 | grep -qw cad_keysafe; then
    # database exists
    echo -n "DATABASE ALREADY CREATED, DO YOU WANT TO -DELETE- EXISTING DATABASE AND CREATE NEW ONE? (y/n)"
    read answer
    if echo "$answer" | grep -iq "^y" ;then
        dropdb cad_keysafe
        echo "database was removed"
        createdb cad_keysafe
        # run python script for create dabase by models
        echo "database created"
        psql -d postgres -c "CREATE USER cad_root WITH PASSWORD 'root_pass';"
        psql -d postgres -c "GRANT ALL PRIVILEGES ON DATABASE cad_keysafe to cad_root;"
        echo "done"
    else
        echo "aborded"
    fi
else
    createdb cad_keysafe
    # run python script for create dabase by models
    echo "database created"
    psql -d postgres -c "CREATE USER cad_root WITH PASSWORD 'root_pass';"
    psql -d postgres -c "GRANT ALL PRIVILEGES ON DATABASE cad_keysafe to cad_root;"
    echo "user 'cad_root' with password 'root_pass' created"
    echo "done"
fi