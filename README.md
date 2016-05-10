# WORK IN PROGRESS #

Sadly we could not create a finished project within the timeframe of the API Challenge, so far the python scripts can fill the database correctly by using the API but have to be started by hand as of now. The frontend is mainly static and mocked, but we are looking forward to finishing it as it has been a lot of fun so far.

# League Unlock Challenge #

League Unlock Challenge uses data about your League of Legend games provided by the Riot Developer API to give you points for several kinds of achievements. You can form a league with friends for a fun competition to be the best at the League Unlock Challenge!

## Dependencies ##

1. PostgreSQL
2. PostgREST
3. Python 3
4. Virtualenv
5. Node.JS
6. Bower

If you are using MacOSX you should install homebrew by opening the terminal and running

``` bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Install PostgreSQL ###

PostgreSQL is a open source database that is used in this project to store the data we receive from the API. You can get more information on http://www.postgresql.org/

**Ubuntu:**

``` bash
sudo apt-get install postgresql postgresql-contrib
```

**MacOSX with homebrew:**

``` bash
brew install postgres
```

**Windows:**

Download and install binary from http://www.postgresql.org/download/

### Get PostgREST ###

> PostgREST serves a fully RESTful API from any existing PostgreSQL database. It provides a cleaner, more standards-compliant, faster API than you are likely to write from scratch.

You can get more information on http://postgrest.com/

To use PostgREST you can download the release for you platform from https://github.com/begriffs/postgrest/releases/tag/v0.3.1.1 and extract it with
``` bash
tar zxf postgrest-[version]-[platform].tar.xz
```

### Install Python ###

**Linux:**

Linux distribution usually come with python 3 preinstalled. If both python 2 and 3 are installed, you might need to run it as `python3`. You can make sure you have the right version with `python -v`.

**MacOSX with homebrew:**

Install it with

```
brew install python
```

**Windows:**

Download the official release here and execute to install: https://www.python.org/downloads/release/python-351/

This will come with pip automatically. If your installation does not have it read here https://pip.pypa.io/en/latest/installing/

### Install virtualenv & python dependencies ###

To install virtualenv, run `pip install virtualenv`.

Create virtualenv and install the dependencies for the python scripts:

Bash:
``` bash
virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r db_scripts/requirements.txt
```

Fish:
``` bash
virtualenv --no-site-packages --distribute .env; and source .env/bin/activate.fish; and pip install -r db_scripts/requirements.txt
```

To deactivate the virtualenv again:

``` bash
deactivate
```

### Install Node.JS ###

**Linux:**

``` bash
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**MacOsX with homebrew:**

``` bash
brew install node
```

**Windows:**

Download and install the binary: https://nodejs.org/en/download/

**After installing:**

Once Node.JS and NPM are installed you can run
```
npm install
```
to install the required javascript packages.

### Install Bower ###

``` bash
npm install -g bower
bower install
```

## Setup ##

### Start PostgreSQL server ###

Read how to start the database server: http://www.postgresql.org/docs/current/static/server-start.html

Once the server is started, create a database

``` bash
createdb luc
```

### Database scripts ###

Once you have a database created, run the DatabaseCreation.sql script to create the table schema

``` bash
psql -d luc -a -f db_scripts/DatabaseCreation.sql
```

### Start PostgREST server ###

Start PostgREST server on default port 3000
```
postgrest postgres://localhost:5432/luc -a postgres -j <secret>
```
For more information read http://postgrest.com/install/server/

### Python scripts ###

Too use the python scripts, you will need to create key-file with your Riot API Key first.

``` bash
echo ENTER-YOUR-KEY-HERE > KEY
```

To use the python scripts that are updating/filling your database, you will need to create a db_config file with your hostadress of your postgresql server, the name of your db, the user_name for your database and your password for this user.
All this information should each be stored per line.

``` bash
echo HOSTADRESS >> DB_CONFIG
echo DB_NAME >> DB_CONFIG
echo USER_NAME >> DB_CONFIG
echo PASSWORD >> DB_CONFIG
```
<TODO>

## Deployment ##

#### Local Deployment for Development

You can use the serve gulp task to deploy locally.

```sh
gulp serve
```

This outputs an IP address you can use to locally test and another that can be used on devices connected to your network.

### Github Pages ###

1. In app.js change `app.baseUrl = '/';` to `app.baseUrl = '/league-unlock-challenge/';`
2. Run `gulp build-deploy-gh-pages` from command line
3. To see changes wait 1-2 minutes then load Github pages for your app (ex: https://fidge123.github.io/league-unlock-challenge/)
