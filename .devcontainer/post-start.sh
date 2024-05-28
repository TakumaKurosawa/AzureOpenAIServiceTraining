#!/bin/bash

echo "Running post-start.sh"

echo "Installing python dependencies..."
make dep/install

echo "Lefthook setup..."
lefthook install
