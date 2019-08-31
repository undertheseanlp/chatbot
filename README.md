# Chatbot tiếng Việt

![](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)
![](https://img.shields.io/badge/opensource-vietnamese-blue.svg)
![](https://img.shields.io/badge/build-passing-green.svg)
![](https://img.shields.io/badge/powered%20by-chatscript-blue.svg)

Dự án nghiên cứu về bài toán xây dựng *chatbot tiếng Việt*, được phát triển bởi nhóm nghiên cứu xử lý ngôn ngữ tự nhiên tiếng Việt - [underthesea](https://github.com/undertheseanlp). Chứa mã nguồn các thử nghiệm cho việc xây dựng một chatbot đơn giản, tích hợp với django và có thể triển khai dưới dạng một ứng dụng Web.

**Live Demo**: [http://undertheseanlp.com:8000](http://undertheseanlp.com:8000/#!/)

## Mục lục

* [Giới thiệu về Hoài An](#giới-thiệu-về-hoài-an)
* [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
* [Thiết lập môi trường](#thiết-lập-môi-trường)
* [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
* [Bản quyền](#bản-quyền)

## Giới thiệu về Hoài An 

Sản phẩm đầu tiên của dự án là chatbot Hoài An. Với mục tiêu là một chat-chit bot (bot để trò chuyện tán ngẫu), Hoài An được xây dựng như là một cô gái 20 tuổi, sống ở Hà Nội, thích trò chuyện với mọi người.

Cùng chat với Hoài An tại [đường dẫn này](http://undertheseanlp.com:8000/#!/) nhé.

![](images/chatlog.png)

## Yêu cầu hệ thống

* `Operating Systems: Linux (Ubuntu, CentOS), Mac`
* `Python 3.6+`, `Anaconda 4+`

## Thiết lập môi trường

Tải project bằng cách sử dụng lệnh `git clone`

```
$ git clone https://github.com/undertheseanlp/chatbot.git
```

Tạo môi trường mới và cài đặt các gói liên quan

```
cd chatbot
conda create -n chatbot python=3.6
source activate chatbot
pip install -r requirements.txt
```

## Hướng dẫn sử dụng

Cài đặt Rasa 

```
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

Chạy rasa

```
$ rasa shell
2019-08-31 11:58:11 INFO     root  - Connecting to channel 'cmdline' which was specified by the '--connector' argument. Any other channels will be ignored. To connect to all given channels, omit the '--connector' argument.
2019-08-31 11:58:11 INFO     root  - Starting Rasa server on http://localhost:5005
Bot loaded. Type a message and press enter (use '/stop' to exit):
```

Chatbot với Hoài An 

```
Your input ->  hello
Hey! How are you?
Your input ->  i'm good
Great carry on!
Your input ->  bye
Bye 
```

## Bản quyền

Mã nguồn của dự án được phân phối theo giấy phép [GPL-3.0](LICENSE.txt).
