# python-cli-sandbox

Example Python CLI project


## Usage

Install (follow instructions below) and run the example CLI:

    list-buckets --help


## Development

### Install Python3 (global)

Using [homebrew](https://brew.sh/), install `pyenv`:

    brew install pyenv

Then use `pyenv` to install the most Python `3.7.x` version (currently `3.7.4`):

    pyenv install 3.7.4

And switch to using this version by default whenever you use `pyenv`:

    pyenv global 3.7.4


### Install virtualenvwrapper (global)

Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) globally
so you can use it to manage isolated [Python virtualenvs](https://virtualenv.pypa.io/en/latest/) by name:

    $(pyenv which pip) install virtualenv virtualenvwrapper

Update your `~/.bash_profile` so that when you use `virtualenvwrapper` to create a `virtualenv`,
it uses the version of Python you installed above with `pyenv`:

    export VIRTUALENVWRAPPER_PYTHON=$(pyenv which python)
    export VIRTUALENVWRAPPER_VIRTUALENV=$(pyenv which virtualenv)
    source $(pyenv which virtualenvwrapper.sh)

Load these new settings:

    source ~/.bash_profile


### Always work in a virtualenv (global)

Once you've installed `virtualenvwrapper`, you should change your environment to prevent installation
of Python packages outside of a `virtualenv`.

To do so, update your `~/.bash_profile` to contain:

    export PIP_REQUIRE_VIRTUALENV=true

Note that you will need to temporarily unset this variable need to (re)install any global packages, such
as `virtualenvwrapper`.


### Create a virtualenv

Using `virtualenvwrapper`, create a named `virtualenv` for this project:

    mkvirtualenv sandbox

Upon running this command, you will automatically be "inside" of the `virtualenv`.

You can leave the `virtualenv` by running:

    deactivate

You can return to the `virtualenv` by running:

    workon sandbox

You can delete the `virtualenv` by running:

    rmvirtualenv sandbox


### Install dw-reports and its dependencies

From inside the `virtualenv`, instal dependencies in *editable* mode.

    pip install -e .[lint,test,typehinting]


### Validation

To run the linter:

    flake8 sandbox

To run unit tests:

    pytest sandbox

To run unit the type checker:

    mypy sandbox
