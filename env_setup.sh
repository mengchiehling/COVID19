#!/bin/bash
conda create --name cosnova-covid19 python=3.7 -y
conda env update --name cosnova-covid19 --file imported_packages.yml

