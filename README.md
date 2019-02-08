![Inventarium](/invsystem/user_manager/static/user_manager/images/banner.png)
# Inventarium

This project is a django server inventarization system. It requires docker 
and docker compose as well as the python modules stated in the requirements.txt. It can be used to
 inventarize and document basically everything.
## Setup
### Installation
1. Install `docker` and `docker-compose` from [here](https://www.docker.com/get-started) and [here](https://docs.docker.com/compose/install/)
2. Clone this repository
3. Go into the root directory of the repository (where docker-compose.yml) lives and open 
a terminal
4. Execute the command `docker-compose up`. Container images for a postgresSQL 
database and the django server will be pulled and configured automatically. This step 
requires some disk space and an active internet connection
5. You now need to create a database user
### Creating a database user
In order to access the system you will need to create a database user so django can 
interface with the database and you can log in to interact with the server e.g. create 
additional users or inventarize objects.
1. Run `docker ps` while the containers are running do determine the container ID of the 
web server. Something like this will show up:
```
CONTAINER ID        IMAGE               COMMAND                  CREATED               STATUS               PORTS                    NAMES
f1b377c3700f        invsystem_web       "python3 manage.py r…"   1 minute ago          Up 1 minute          0.0.0.0:8000->8000/tcp   invsystem_web_1
1289f9bcdd04        postgres            "docker-entrypoint.s…"   1 minute ago          Up 1 minute          0.0.0.0:5432->5432/tcp   invsystem_db_1
```

You need to copy the `CONTAINER ID` for the image `invsystem_web`

2. Execute the command `docker exec -i -t <CONTAINER ID> /bin/bash`

3. You are now attatched to the docker container via a shell. <br>

Enter `python3 manage.py makemigrations` and `python3 manage.py migrate`.<br> 
This sets up the database and initializes it. 

4. Create the superuser using `python3 manage.py createsuperuser` and enter the 
requested information

5. Open your browser and visit `localhost:8000` or click [here](http://localhost:8000)

6. Click the "Einloggen" button in the top right corner and log in with the account you 
just created using `createsuperuser`

7. You can now access the server and use all of its features

If you need the django admin panel you can just access `localhost:8000/admin` and log in 
with the same superuser account there as well
