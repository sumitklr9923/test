name: Auto Click on Document

on:
  push:
    branches:
      - main

jobs:
  auto-click:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2  # Update to the latest version that supports Node.js 16

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install Dependencies
      run: |
        pip install -r requirements.txt  # If you have any dependencies

    - name: Run Auto Click Script
      run: python auto_click.py
