# Marked By Covid (MBC) Web Application

Marked By Covid is a national, grassroots, non-partisan nonprofit that promotes accountability, recognition, justice, and a pandemic-free future.

We are led by people directly harmed by the pandemic. Together, we:
1. Promote accountability, equity, and justice.
2. Amplify the voices of those most impacted.
3. Support survivors & bereaved.

The following sections provides the references to the manuals, guides, and specification documentation of this projects.

## References

| Document                                                        | Doc type    | Description                                                             |
| ----------------------------------------------------------------|-------------|-------------------------------------------------------------------------|
| [Technical Manual](docs/technical%20manual/index.md)            | Reference   | Technical overview of database, workflows, and use cases                |
| [Testing Manual](docs/testing%20manual/index.md)                | Reference   | Guide implemented to automated testing of existing modules              |
| [User Manual](docs/user%20manual/index.md)                      | Reference   | Guide to implemention and usage of the API                              |

## Set up Steps

1. Install Dependencies
```
pip install -r requirements.txt
```

2. Apply migrations
```
python manage.py makemigrations
python manage.py migrate

```

3. In order to run client resources, install vue
```
npm install vue
```
4. For development purpose, To load map and api calls create a .env file in the root directory and add following keys and configure values to the file.
```
VUE_APP_GOOGLE_API_KEY=
VUE_APP_API_ENDPOINT=
```
5. Build Vue component if any changes made to Vue

   - 5a. Build the latest file depending on DEV or PROD environments Check for the folder dist/static (Built vue app files) 
    If not exists then build the vue application 
    ```
    npm run build
    ```
    5b. Optionally For running client-app 
    ```
    npm run serve
    ```
6. Run the below command  for collecting static resources. 
```
python manage.py collectstatic
```
7. Create a superuser to login into Django admin console.
```
python manage.py createsuperuser
```
8. Run the project
```
python manage.py runserver
```
9. Login into admin console at below url with superuser credential.
```
http://localhost:8000/admin/
```
10. Open pgAdmin4 and connect to the postgreSQL database and execute the sql script located at
```
markedbycovid/sql/website_config_parameter.sql
```
