
# Requirements

First, you need to ensure you have [Python3.10](https://www.python.org/downloads/release/python-31010/) and
[Rust](https://www.rust-lang.org/tools/install) installed on your computer and available on the PATH.

# Running the application

To run the app, use [make](https://gnuwin32.sourceforge.net/packages/make.htm) 
```shell
python -m venv venv
. venv/bin/activate
make
```
> **NOTE:** If you have your python configured as python3, use `alias python=python3`

Or run in manually

```shell
python -m venv venv
. venv/bin/activate
pip install -Ur requirements.txt --quiet
cargo install maturin --locked
maturin build -i python --release
pip install --force-reinstall --no-index --find-links=./target/wheels/ py_ltl_engine
python ./app/main.py
```

##### Tested platforms: Windows 10, Ubuntu 20.04  

# Development mode

To run in development mode, use `make develop`

# Linting

To run linters, use `make lint`.

# Formatting

To run formatters, use `make format`.

# Testing

To run tests, use `make test`.

# Test Coverage

To generate test coverage in HTML, use `make coverage` (grcov required)
