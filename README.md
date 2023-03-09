## How to run this project ?

1. Make sure you have docker and docker-compose installed.

```
https://docs.docker.com/compose/install/
https://docs.docker.com/engine/install/
```
2. Clone repository.

3. Change name of .env.template to .env and fill enviroment variables.

    In order to make sending email works. In this example u need to create gmail account,
    enable two factor authentication and generate password for an app. ` your account -> security -> password for an app.`
    


4. Then in project root directory run:

```
docker-compose up --build
```

Project is up and runnning on `http://localhost/api/v1`


### Creating superuser
In project root.
``` 
make superuser
```

### Running test suite.
In project root.
```
make test
```

### Documentation
Generated documentation is available
`http://localhost/api/v1/schema/swagger-ui/` or `http://localhost/api/v1/schema/redoc/`


### User email notification.
When app is up and running notification for users are sent at 10 am UTC.
