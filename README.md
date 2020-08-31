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
- [How to use?](#How-to-use?)

# Introduction

This project was developed with `Django REST Framework` to keep track of _vaccinations_ and _drugs_ used through an API service. Here you can __consult, create, modify__ and __delete__ drugs and vaccinations.

The project was deployed publicly on AWS, so anyone can access it.

# How to use?

You can use the URL in your browser to interact with the API, but maybe is more useful do it with [Postman](https://www.postman.com/).

<div>
    <table>
        <tr>
            <th>URL</th>
            <th>Method</th>
            <th>Content Type</th>
            <th>Body values</th>
            <th>Restrictions</th>
            <th>Comment</th>
        </tr>
        <tr>
            <td>ec2-54-232-160-16.sa-east-1.compute.amazonaws.com:8000/drugs</td>
            <td>GET</td>
            <td></td>
            <td></td>
            <td></td>
            <td>List all registered drugs</td>
        </tr>
        <tr>
            <td>ec2-54-232-160-16.sa-east-1.compute.amazonaws.com:8000/drugs/:id</td>
            <td>GET</td>
            <td></td>
            <td></td>
            <td></td>
            <td>You get the detail of a drug.</td>
        </tr>
        <tr>
            <td>ec2-54-232-160-16.sa-east-1.compute.amazonaws.com:8000/drug</td>
            <td>POST</td>
            <td>application/json</td>
            <td>
                <p>name: string</p>
                <p>code: string</p>
                <p>descriptions: string</p>
            </td>
            <td>
                <p>Code can get max 10 chars and it's unique.</p>
                <p>Description can get max 255 chars.</p>
            </td>
            <td>Register a new drug.</td>
        </tr>
        <tr>
            <td>ec2-54-232-160-16.sa-east-1.compute.amazonaws.com:8000/drug/:id</td>
            <td>PUT</td>
            <td>application/json</td>
            <td>
                <p>name: string</p>
                <p>code: string</p>
                <p>descriptions: string</p>
            </td>
            <td>
                <p>Code can get max 10 chars and it's unique.</p>
                <p>Description can get max 255 chars.</p>
            </td>
            <td>Update a drug.</td>
        </tr>
        <tr>
            <td>ec2-54-232-160-16.sa-east-1.compute.amazonaws.com:8000/drug/:id</td>
            <td>DELETE</td>
            <td></td>
            <td></td>
            <td></td>
            <td>Delete a drug.</td>
        </tr>
        <tr>
            <td>ec2-54-232-160-16.sa-east-1.compute.amazonaws.com:8000/vaccinations</td>
            <td>GET</td>
            <td></td>
            <td></td>
            <td></td>
            <td>List all registered vaccinations</td>
        </tr>
        <tr>
            <td>ec2-54-232-160-16.sa-east-1.compute.amazonaws.com:8000/vaccinations/:id</td>
            <td>GET</td>
            <td></td>
            <td></td>
            <td></td>
            <td>You get the detail of a vaccination.</td>
        </tr>
        <tr>
            <td>ec2-54-232-160-16.sa-east-1.compute.amazonaws.com:8000/vaccinations</td>
            <td>POST</td>
            <td>application/json</td>
            <td>
                <p>rut: string</p>
                <p>dose: string</p>
                <p>date: string "yyyy-mm-dd"</p>
                <p>drug: drug id</p>
            </td>
            <td>
                <p>The verification digit will be validated, so need to be a valid rut (Chilean ID).</p>
                <p>Dose need to be 0.15 <= dose <= 1.0</p>
                <p>The drug ID need exist.</p>
            </td>
            <td>Register a new vaccination.</td>
        </tr>
        <tr>
            <td>ec2-54-232-160-16.sa-east-1.compute.amazonaws.com:8000/vaccinations/:id</td>
            <td>PUT</td>
            <td>application/json</td>
            <td>
                <p>rut: string</p>
                <p>dose: string</p>
                <p>date: string "yyyy-mm-dd"</p>
                <p>drug: drug id</p>
            </td>
            <td>
                <p>The verification digit will be validated, so need to be a valid rut (Chilean ID).</p>
                <p>Dose need to be 0.15 <= dose <= 1.0</p>
                <p>The drug ID need exist.</p>
            </td>
            <td>Update a vaccination.</td>
        </tr>
        <tr>
            <td>ec2-54-232-160-16.sa-east-1.compute.amazonaws.com:8000/vaccinations/:id</td>
            <td>DELETE</td>
            <td></td>
            <td></td>
            <td></td>
            <td>Delete a vaccination.</td>
        </tr>
    </table>
</div>
<br>

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