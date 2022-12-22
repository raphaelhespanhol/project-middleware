#!/usr/bin/env bash
source /etc/environment

# Setup dependencies
echo 'START SETUP'
docker-compose down
docker system prune -f
docker kill $(docker ps -q)
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker-compose up -d azurite mssql
echo -ne 'WAITING DEPENDENCIES SETUP.'
while ! docker-compose logs --tail=10 mssql | grep --line-buffered 'EdgeTelemetry starting up'; do
  # shellcheck disable=SC2006
  if [[ `docker-compose logs --tail=10 mssql | grep --line-buffered 'ERROR'` ]]; then
    docker-compose logs --tail=100 mssql; echo 'BE ATTENTION: THE DEPENDENCIES SHOWS SOME ERRORS: PLEASE VERIFY LOGS ABOVE! ^^^' ; exit 0;
  else
    echo -ne '.'
  fi
done
echo 'DEPENDENCIES LOADED WITH SUCCESS.'

echo 'Cheers!'
docker attach azurite
