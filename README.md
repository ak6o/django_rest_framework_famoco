# Django & Django Rest Framework

## Requirements

- Use Django and Django REST Framework
- Add an endpoint which allows listing and uploading Android applications (GET and POST)
- When an application is uploaded the metadata of that application should be extracted with aapt
- The solution should run inside a docker container, ideally with docker-compose

## Extras

- Allow to modify a record
- Allow to delete a record 

When a file is modified or deleted it remove the file from the "media/" directory and replace it by the new one

## Run the project
Start the server :
```bash
docker-compose up
```
Access the API :

[http://0.0.0.0:8000/application/](http://0.0.0.0:8000/application/)