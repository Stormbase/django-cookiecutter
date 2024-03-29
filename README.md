# Stormbase Django Cookiecutter

[![License: MIT](https://img.shields.io/github/license/Stormbase/django-cookiecutter)](https://github.com/Stormbase/django-cookiecutter/blob/master/LICENSE)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The (opinionated) Django [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) template we use at Stormbase for new projects.
This template is a huge time saver for us and we wish to share it with the world ❤️

## Features

- Python 3.9
- Django 3.2
- [Poetry](https://github.com/python-poetry/poetry)
- Pytest
- Black + isort
- Eslint + Stylelint
- Basic webpack config with autoprefixer and SCSS support
- Dockerfile included
- GitLab CI config file
- Deploy to Heroku
- Scripts-to-rule-them-all — A set of scripts to quickly setup the project and to perform certain tasks. Find them in the `script` folder.

## Using this template

Make sure you have cookiecutter installed [Cookiecutter installation guide](https://cookiecutter.readthedocs.io/en/latest/installation.html)

```sh
cookiecutter gh:stormbase/django-cookiecutter
```

Follow the prompts and you're all set!

## Gitlab CI configuration

The default CI config triggers a deployment to staging when the `staging` branch is updated.

Pushing to a branch named `production` will trigger a production deployment. Please note that a production deployment requires manual confirmation from the GitLab UI.

## License

This project is licensed under MIT.

Please see [LICENSE](LICENSE)
