# GlobantPokeberriesStatisticsAPI
Pokeberries Statistics API required by Globant as part of Python technical evaluation process.

## Local Development

### First Build Only
1. `cp .env.example .env`
2. `docker build -t globantpokeberryimage . `
3. `docker run -d --name globantpokeberry -p 80:80 globantpokeberryimage`

### Tests
Run tests within Docker container shell
```shell
coverage run -m pytest
```

See coverage report
```shell
coverage report -m
```
