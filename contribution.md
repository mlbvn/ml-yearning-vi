# Đóng góp vào dự án

# Các bước dịch một chương
Một chương được hoàn thành khi nó trải qua các công đoạn:

## 1. Copy + format từ bản gốc
Để tiện cho việc dịch và review, mỗi chương bắt đầu với việc copy bản gốc và định dạng. Ví dụ như [ở đây](https://github.com/aivivn/Machine-Learning-Yearning-Vietnamese-Translation/pull/24/files).

Một vài lưu ý:
1. Tên chương để ở heading 1, ví dụ:

```
# Why Machine Learning Strategy
->

```
2. Một đoạn trong bản gốc đưa về một dòng, ví dụ:
```
Machine learning is the foundation of countless important applications, including web search, email anti-spam, speech recognition, product recommendations, and more. I assume that you or your team is working on a machine learning application, and that you want to make rapid progress. This book will help you do so.
->

```

3. Sau mỗi dòng là một dấu mũi tên (`->`) và một dòng trắng để người dịch điền về sau. Người dịch bắt đầu ở dòng **dưới dấu mũi tên**.

4. Các chữ in đậm, in nghiêng cần được định dạng như bản gốc, ví dụ:
```
**in đậm**
*in nghiêng*
```

## 2.Bổ sung bảng thuật ngữ
Sau khi copy từ bản gốc của một chương cần kiểm tra xem những từ nào trong chương đó chưa có trong [Bảng thuật ngữ](glossary.md). Nếu chưa có thì bổ sung bằng cách tạo một Pull Request.

## 3. Dịch
Sau khi đã có bản gốc và đầy đủ thuật ngữ, bạn có thể tạo một Pull Request mới để bắt đầu dịch. Chú ý, bạn chỉ dịch khi một thuật ngữ đã có trong [Bảng thuật ngữ](glossary.md) để hạn chế số lượng biến thể của một từ. Nếu một thuật ngữ chưa có trong Bảng thuật ngữ, bạn có thể tạo riêng một Pull Request để bổ sung.

## 4. Review
Khi có Pull Request mới, sẽ cần rất nhiều bình luận và kiểm tra trước khi Pull Request đó được approved.


## 5. Hoàn thành
Sau khi một Pull Request được approve, nhóm điều hành sẽ xóa phần tiếng Anh và các dấu `->`, chỉ để phần tiếng Việt trước khi merge và master branch.

# Làm thế nào để đóng góp vào việc dịch?
Trong năm bước bên trên, bạn có thể đóng góp ở bất cứ bước nào ngoại trừ bước cuối chỉ có nhóm điều hành mới được thực hiện.

Ngoài ra việc lấy các ảnh trong sách đưa vào thư mục [imgs](../imgs) cũng rất cần thiết.