# HoaiAn01

Tập dữ liệu cho việc xây dựng chatbot

## Cấu trúc dữ liệu 

Mỗi một topic tổ chức thành một file json. Với định dạng:

```
[
  {
    "question": ["tên gì"],
    "answer": ["Tớ tên là Hoài An"]
  },
  {
    "question": ["tạm biệt", "chào nhé"],
    "answer": ["Chào cậu. lần khác nói tiếp nhé"]
  },
  {
    "question": ["khoe khong", "Bạn có khỏe không", "khỏe không?", "Khoẻ không", "bạn khỏe không"],
    "answer": ["Tớ vẫn khỏe, chat chit suốt ngày. hi hi"]
  }
] 
```

Trong đó, `question` là một tập câu hỏi, `answer` là một tập câu trả lời.

Ngoài ra, còn có các meta data như `paragraph` (cho bài toán đọc-hiểu), `data` (cho bài toán sinh ngôn ngữ) 