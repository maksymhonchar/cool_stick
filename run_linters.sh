#!/bin/bash

echo "Running mypy..."
mypy --exclude __pycache__,venv,_docs --show-error-codes .
echo ""

echo "Running flake8..."
flake8 --exclude=venv,__pycache__,docs .
echo ""

echo "Running bandit..."
bandit -r controllers/ models/ views/ main.py
echo ""

echo "Fin!"