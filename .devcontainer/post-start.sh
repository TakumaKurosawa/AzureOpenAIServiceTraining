#!/bin/bash

echo "Running post-start.sh"

echo "Installing python dependencies..."
make dep/ai

echo "Lefthook setup..."
lefthook install
