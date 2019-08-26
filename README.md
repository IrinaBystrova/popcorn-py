# popcorn-py
`site with links for TV series torrents`

### launch with docker
```
docker-compose build && docker-compose up -d && 
docker-compose run --rm web python manage.py migrate && 
docker-compose run --rm web python manage.py crawl_series &&
docker-compose run --rm web python manage.py crawl_new_items &&
docker-compose run --rm web python manage.py createsuperuser &&
docker-compose up
```
