## Initial Project

#### Step 1 modify environment file

- Change filename "application/.env-sample" to "application/.env" 
- Modify variable in .env file

#### Step 2 Start postgres database with docker compose

> sudo docker-compose up -d

#### Step 3 migrate database

> cd application
>
> python manage.py migrate

#### Step 4 load fake data

$ python manage.py generate_fake_data [number of student]

Example
> python manage.py generate_fake_data 10

#### Step 5 create super user

> python manage.py createsuperuser

## Starting Project

#### Step 1 Start postgres database with docker compose

> sudo docker-compose up -d

#### Step 2 Start project

> cd application

> python manage runserver

## URL information

##### list all school
> GET,POST: /schools 

Params for GET
>- page (default=0)
>- page_size (default=10)
>- search (search in name of school)

example
>/schools?page=2&page_size=5&search=kim


##### get/update/delete specific school with id
> GET,PUT,PATCH,DELETE /schools/:id

##### list students who belong to school
> GET: /schools/:id/students

Params for GET
>- page (default=0)
>- page_size (default=10)
>- search (search in firstname and lastname of student)

example
>/schools/1/students?page=2&page_size=5&search=kim

##### creation student in the school
> POST: /schools/:id/students

##### get/update/delete specific student in school with id
> GET,PUT,PATCH,DELETE /schools/:id/students/:id

##### list all student
> GET, POST: /students

Params for GET
>- page (default=0)
>- page_size (default=10)
>- search (search in firstname and lastname of student)

example
>/students?page=2&page_size=5&search=kim

##### get/update/delete specific student with id
> GET,PUT,PATCH,DELETE /students/:id