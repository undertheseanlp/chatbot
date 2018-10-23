# Chatbot tiếng Việt

![](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)
![](https://img.shields.io/badge/opensource-vietnamese-blue.svg)
![](https://img.shields.io/badge/build-passing-green.svg)
![](https://img.shields.io/badge/powered%20by-rivescript-blue.svg)

Dự án nghiên cứu về bài toán xây dựng *chatbot tiếng Việt*, được phát triển bởi nhóm nghiên cứu xử lý ngôn ngữ tự nhiên tiếng Việt - [underthesea](https://github.com/undertheseanlp). Chứa mã nguồn các thử nghiệm cho việc xây dựng một chatbot đơn giản, tích hợp với django và có thể triển khai dưới dạng một ứng dụng Web.

**Nhóm tác giả**

* Vũ Anh ([anhv.ict91@gmail.com](anhv.ict91@gmail.com))
* Cao Thanh Tùng ([caothanhtungst@gmail.com](caothanhtungst@gmail.com))
* Hồ Thanh Luân ([hothanhluan1996@gmail.com](hothanhluan1996@gmail.com))
* Nguyễn Thị Hậu ([nguyenhau1996mta@gmail.com](nguyenhau1996mta@gmail.com))

**Live Demo**: [http://undertheseanlp.com:8000](http://undertheseanlp.com:8000/#!/)

**Tham gia đóng góp**

 Mọi ý kiến đóng góp hoặc yêu cầu trợ giúp xin gửi vào mục [Issues](../../issues) của dự án. Các thảo luận được khuyến khích **sử dụng tiếng Việt** để dễ dàng trong quá trình trao đổi. 
 
Nếu bạn có kinh nghiệm trong bài toán này, muốn tham gia vào nhóm phát triển với vai trò là [Developer](https://github.com/undertheseanlp/underthesea/wiki/H%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-%C4%91%C3%B3ng-g%C3%B3p#developercontributor), xin hãy đọc kỹ [Hướng dẫn tham gia đóng góp](https://github.com/undertheseanlp/underthesea/wiki/H%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-%C4%91%C3%B3ng-g%C3%B3p#developercontributor).

## Mục lục

* [Giới thiệu về Hoài An](#giới-thiệu-về-hoài-an)
* [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
* [Thiết lập môi trường](#thiết-lập-môi-trường)
* [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
* [Bản quyền](#bản-quyền)

## Giới thiệu về Hoài An 

Sản phẩm đầu tiên của dự án là chatbot Hoài An. Với mục tiêu là một chat-chit bot (bot để trò chuyện tán ngẫu), Hoài An được xây dựng như là một cô gái 20 tuổi, sống ở Hà Nội, thích trò chuyện với mọi người. Cùng chat với Hoàn An tại [đường dẫn]((http://undertheseanlp.com:8000/#!/)) này nhé.

![](images/chatlog.png)

## Yêu cầu hệ thống

* `Operating Systems: Linux (Ubuntu, CentOS), Mac`
* `Python 3.5+`
* `conda 4+`
* `Django==1.11.1`
* `rivescript==1.14.9`

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

Để chạy chatbot, gõ các câu lệnh 

```
cd chatbot
source activate chatbot
python manage.py runserver 0.0.0.0:8000
```

Sau đó, mở trình duyệt, vào đường dẫn http://localhost:8000 để bắt đầu chat với bot 

## Bản quyền

Mã nguồn của dự án được phân phối theo giấy phép [GPL-3.0](LICENSE.txt).