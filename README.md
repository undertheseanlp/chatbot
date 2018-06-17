# Vietnamese Chatbot

![](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)

This repository contains starter code for creating a simple *Vietnamese Chatbot*. It is a part of [underthesea](https://github.com/magizbox/underthesea) project. The code gives an end-to-end working example for creating simple chatbot engine, integrating with django and deploying as a web application. It can easily be extended to create your own custom-defined application. 

## Table of contents

* [1. Installation](#1-installation)
  * [1.1 Requirements](#11-requirements)
  * [1.2 Download and Setup Environment](#12-download-and-setup-environment)
* [2. Usage](#2-usage)
* [3. References](#3-references)

## 1. Installation

### 1.1 Requirements

This code is writen in python. The dependencies are:

* `Operating Systems: Linux (Ubuntu, CentOS), Mac`
* `Python 3.5+`
* `conda 4+`

Python Packages

```
Django==1.11.1
rivescript==1.14.9
```

### 1.2 Download and Setup Environment


Clone project using git

```
$ git clone https://github.com/undertheseanlp/chatbot.git
```

Create environment and install requirements

```
cd chatbot
conda create -n chatbot python=3.6
source activate chatbot
pip install -r requirements.txt
```

## 2. Usage

To run chatbot

```
cd chatbot
source activate chatbot
python manage.py runserver 0.0.0.0:8000
```

## 3. References

To be updated

Last update: 06/2018