### Automated Saloon

##### Setting up Virtual Environment
```
# For Linux / Mac
$ source env/bin/activate

# For Windows
> \env\Scripts\activate.bat
```

##### Create Postgres Database to suite the project
```
> CREATE DATABASE autosaloondb;
> CREATE USER admin1 WITH PASSWORD 'admin1234';
> GRANT ALL PRIVILEGES ON DATABASE autosaloondb TO admin1;
> ALTER USER admin1 CREATEDB;
```
###### All set...