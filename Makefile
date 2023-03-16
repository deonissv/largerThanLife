all: install build run

install: requirements
	rustup component add clippy-preview
	cargo install maturin --locked

requirements:
	python -m pip install -Ur requirements.txt --quiet

build:
	maturin build -i python --release
	python -m pip install --force-reinstall --no-index --find-links=./target/wheels/ py_ltl_engine

develop:
	maturin develop
	python ./app/main.py

run:
	python ./app/main.py

test:
	cargo test
	pytest ./app/tests/test.py

coverage:
	find ./target/coverage/ -name '*.profraw' -delete
	CARGO_INCREMENTAL=0 RUSTFLAGS='-C instrument-coverage' LLVM_PROFILE_FILE='./target/coverage/cargo-test-%p-%m.profraw' cargo test
	grcov . --binary-path . -s . -t html --branch --ignore-not-existing --ignore '../' --ignore "/" -o target/coverage/html

format:
	cargo fmt
	black ./app/

lint:
	cargo clippy
	flake8 ./app/main.py
