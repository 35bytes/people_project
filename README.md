<div align="center">
  <h1>Vaccination System</h1>
</div>

<div align="center">
  <img src="readme-img/vaccination.png" width="80%">
</div>

# Content
- [Introduction](#Introduction)
- [Prerequisites](#Prerequisites)
    - [Windows](#Windows)
    - [macOS](#macOS)
    - [Linux](#Linux)

# Introduction

This project was developed with `Django REST Framework` to keep track of _vaccinations_ and _drugs_ used through an API service. Here you can __consult, create, modify__ and __delete__ drugs and vaccinations.

# Prerequisites

It's necesary install `MySQL` drivers and `Python>=3.6` to run this project.

## Windows

The easiest way to do in windows is installing `MySQL`, but there are some binary wheels you can install easily.

To install `Python` you can go to the [official page](https://www.python.org/).

## macOS

Install MySQL:

```
$ brew install mysql
```

To install `Python` you can go to the [official page](https://www.python.org/).

## Linux

__Note that this is a basic step. I can not support complete step for build for all environment. If you can see some error, you should fix it by yourself, or ask for support in some user forum. Don't file a issue on the issue tracker.__

You may need to install the Python 3 and MySQL development headers and libraries:

Debian / Ubuntu
```
$ sudo apt update
$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential mysql-server
```

Red Hat / CentOS
```
% sudo yum install python3-devel mysql-devel
```