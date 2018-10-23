# Chatbot tiếng Việt

![](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)
![](https://img.shields.io/badge/opensource-vietnamese-blue.svg)
![](https://img.shields.io/badge/build-passing-green.svg)
![](https://img.shields.io/badge/powered%20by-rivescript-blue.svg)

Dự án nghiên cứu về bài toán xây dựng *chatbot tiếng Việt*, được phát triển bởi nhóm nghiên cứu xử lý ngôn ngữ tự nhiên tiếng Việt - [underthesea](https://github.com/undertheseanlp). Chứa mã nguồn các thử nghiệm cho việc xây dựng một chatbot đơn giản, tích hợp với django và có thể triển khai dưới dạng một ứng dụng Web.

Live Demo: [http://undertheseanlp.com:8000/#!/](http://undertheseanlp.com:8000/#!/)

**Nhóm tác giả**

* Vũ Anh ([anhv.ict91@gmail.com](anhv.ict91@gmail.com))
* Cao Thanh Tùng ([caothanhtungst@gmail.com](caothanhtungst@gmail.com))
* Hồ Thanh Luân ([hothanhluan1996@gmail.com](hothanhluan1996@gmail.com))
* Nguyễn Thị Hậu ([nguyenhau1996mta@gmail.com](nguyenhau1996mta@gmail.com))

**Tham gia đóng góp**

 Mọi ý kiến đóng góp hoặc yêu cầu trợ giúp xin gửi vào mục [Issues](../../issues) của dự án. Các thảo luận được khuyến khích **sử dụng tiếng Việt** để dễ dàng trong quá trình trao đổi. 
 
Nếu bạn có kinh nghiệm trong bài toán này, muốn tham gia vào nhóm phát triển với vai trò là [Developer](https://github.com/undertheseanlp/underthesea/wiki/H%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-%C4%91%C3%B3ng-g%C3%B3p#developercontributor), xin hãy đọc kỹ [Hướng dẫn tham gia đóng góp](https://github.com/undertheseanlp/underthesea/wiki/H%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-%C4%91%C3%B3ng-g%C3%B3p#developercontributor).

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

Then go to http://localhost:8000 to start chat with bot

## 3. References

To be updated

Last update: 06/2018
