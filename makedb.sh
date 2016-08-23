#!/bin/sh

echo "сreate a new database"

if psql -lqt | cut -d \| -f 1 | grep -qw test1; then
    # database exists
    echo -n "DATABASE ALREADY CREATED, DO YOU WANT TO -DELETE- EXISTING DATABASE AND CREATE NEW ONE? (y/n)"
    read answer
    if echo "$answer" | grep -iq "^y" ;then
        dropdb test1
        echo "database was removed"
        createdb test1
        # run python script for create dabase by models
        echo "database created"
        echo "done"
    else
        echo "aborded"
    fi
else
    createdb test1
    # run python script for create dabase by models
    echo "database created"
    echo "done"
fi