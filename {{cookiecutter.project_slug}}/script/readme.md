# FAQ

## What are these scripts?

These scripts are a set of boilerplate scripts new developers can run to quickly get started with this project. It tries to follow the [Scripts To Rule Them All](https://github.com/github/scripts-to-rule-them-all) pattern.

### I am a new developer. In what order should I run these scripts?

Welcome aboard! 🎉🎊

The correct order is:

1. `./script/bootstrap`
2. `./script/setup`

You can find more information about these scripts below.

### <a name="bootstrap">Bootstrap</a>

[`script/bootstrap`](bootstrap) is used to install all project dependencies.

You typically have to run this only once.

### <a name="setup">Setup</a>

[`script/setup`](setup) is used to recreate the database and migrate it for you.

This depends on the `createdb` and `dropdb` exectubles having access to your Postgres installation.

#### <a name="setup-troubleshooting">Troubleshooting</a>

In case you get a message similar to this:

```sh
createdb: could not connect to database my_database: FATAL:  role "my_username" does not exist
```

This means you likely have a fresh installation of Postgres. You will need to create Postgres superuser account for yourself. Please replace `<my-user>` with your exact username.

```sh
sudo su - postgres -c "createuser <my-user> --superuser"
```

### <a name="update">Update</a>

[`script/update`](update) is useful to update the project after a fresh pull.

This may be helpful if you have not worked on the project in a while. This script will execute the `bootstrap` script again to make sure dependencies are installed and up-to-date.

### <a name="lint">Lint</a>

[`script/lint`](lint) is used to check the application source code for coding style problems.

If any problems are found some problems can be automatically resolved by running the `script/format` script.

### <a name="format">Format</a>

[`script/format`](format) is used to automatically resolve some coding style problems in the application.

### <a name="test">Test</a>

[`script/test`](test) is used to run the test suite of the application.

You can optionally supply an argument that is a file path. This allows you to run single tests.

### <a name="clean">Clean</a>

[`script/clean`](clean) is used to clean temporary files.

Sometimes under rare conditions you may experience weird issues. Running this cleaning script may help in these cases.
