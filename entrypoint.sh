#!/bin/bash
./wait-for-it.sh db:3306

make migrate-up

flask run --host 0.0.0.0
