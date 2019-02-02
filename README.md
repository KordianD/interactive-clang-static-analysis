[![Build Status](https://travis-ci.org/KordianD/interactive-clang-static-analysis.svg?branch=master)](https://travis-ci.com/KordianD/interactive-clang-static-analysis)

# interactive-clang-static-analysis
Showing clang static analysis errors from project.

# Prerequisites
    docker
    docker-compose

# How to run
You need to perform several commands.

    git clone https://github.com/KordianD/interactive-clang-static-analysis

    cd interactive-clang-static-analysis

    docker-compose build

    docker-compose up
    
# General 

This project uses `flask` as a web framework and `mongodb` as a database.

The default port which is mapped is `5000`. You could set different one in file `docker-compose.yml`

# Development

If you want to develop code, you need several packages, simply run:

    pip install -r requirements_dev.txt
    
This packages enable running tests on the local machine.

To run tests:

    make test
