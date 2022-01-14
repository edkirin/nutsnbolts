#!/bin/sh

echo "### Performing flyway migration..."
postgres -V
cat /app/flyway.conf
/usr/local/bin/flyway -configFiles="/app/flyway.conf" migrate
echo "##################################"
