# spaceship-you

## To Run in development on your local server

### Execution
```
./cloud_sql_proxy -instances=spaceship-you:us-west1:spaceship-db=tcp:3306
python3 manage.py runserver
```