#!/bin/sh

echo "flake8 test start"
flake8 monarch

if [ "$?" != 0 ]
then
    echo "flake8 test failed!"
    exit 1;
else
    echo "flake8 test success!"
fi
