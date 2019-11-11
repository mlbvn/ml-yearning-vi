# Đóng góp vào dự án

**Dự án không thể thành công nếu không có sự đóng góp của cộng đồng. Nếu bạn muốn đóng góp một phần vào dự án, bạn vui lòng xem các công việc cần thực hiện [tại đây](https://github.com/aivivn/Machine-Learning-Yearning-Vietnamese-Translation/issues). Các công việc được gán nhãn [high priority](https://github.com/aivivn/Machine-Learning-Yearning-Vietnamese-Translation/issues?q=is%3Aissue+is%3Aopen+label%3A"high+priority") là các công việc cần được hoàn thành trước.**

Việc đóng góp được thực hiện qua các Pull Request (PR). Đây là bài [hướng dẫn tạo pull request](https://codetot.net/contribute-github/) khá chi tiết, các bạn có thể tham khảo.

Lưu ý khi tạo một PR:

* Kiểm tra trong tab [Issues](https://github.com/aivivn/Machine-Learning-Yearning-Vietnamese-Translation/issues) và [Pull Requests](https://github.com/aivivn/Machine-Learning-Yearning-Vietnamese-Translation/pulls) xem đã có ai đề cập hoặc làm việc đó chưa, tránh dẫm chân lên nhau.

* Khi bạn bắt đầu làm một việc mới, bạn để lại một comment ở issue tương ứng, hoặc tạo issue mới, hoặc tạo một PR mới với tiêu đề tương ứng để những người làm sau không làm trùng công việc của bạn.


# Hai giai đoạn để dịch môt chương
## 1. Giai đoạn 1
Đây là giai đoạn dịch từ bản tiếng Anh sang bản tiếng Việt lần đầu tiên. Bản dịch này phải đảm bảo ý nghĩa của bản dịch sát với bản gốc, việc trau chuốt ngôn từ sẽ được làm kỹ hơn ở giai đoạn 2. Nếu trong quá trình dịch, bạn gặp một thuật ngữ chưa có trong bảng thuật ngữ, bạn có thể tạo một PR riêng cho việc thêm thuật ngữ mới vào bảng. Bản dịch thô chỉ được chấp nhận nếu tất cả các thuật ngữ đã có trong Bảng thuật ngữ.

Một vài lưu ý:
1. Bản dịch tiếng Việt phải bắt đầu từ dòng **ngay** dưới dấu `->`. Việc này để đảm bảo khi hiển thị những thay đổi trong mỗi PR, github cũng hiển thị phần nghĩa gốc tiếng Anh ngay trên dấu `->`, giúp cho quá trình review thuận tiện hơn. Chẳng hạn:

```
Machine learning is the foundation of countless important applications, including web search, email anti-spam, speech recognition, product recommendations, and more. I assume that you or your team is working on a machine learning application, and that you want to make rapid progress. This book will help you do so.
->
Học máy là nền tảng cho nhiều ững dụng quan trọng, ...
```

2. Định dạng của bản gốc cần được giữ nguyên. Ví dụ:
```
# 1. Why Machine Learning Strategy
->
# 1. Tại sao cần chiến lược Học Máy

**supervised learning**
->
**học có giám sát**
```

## Giai đoạn 2
Trong giai đoạn này, các chương sẽ được trau chuốt hơn về mặt ngôn từ, cách diễn đạt. Giai đoạn này chỉ được thực hiện sau khi giai đoạn 1 đã hoàn thành.

# Bổ sung thuật ngữ
Các thuật ngữ tiếng Anh xuất hiện trong sách nếu chưa có trong [Bảng thuật ngữ](glossary.md) cần được thêm vào bảng này thông qua các PR. Vì mỗi PR chỉ được chấp nhận sau khi review nhiều vòng và trải qua nhiều thảo luận, bạn không nên thay đổi quá nhiều thuật ngữ cùng lúc trong một PR.

# Các lưu ý chung khi tạo Pull Request
1. Mỗi PR chỉ nên thực hiện một nhiệm vụ có tên duy nhất. Ví dụ "Dịch chương 1", "Thêm supervised learning vào bảng thuật ngữ". Không nên gộp chung nhiều công việc vào một PR. Việc review nhiều công việc sẽ tốn thời gian hơn và khiến PR được merge chậm hơn.

2. Mỗi PR chỉ nên thay đổi một file duy nhất để tránh xung đột (conflict). Nếu PR của bạn vừa chỉnh sửa file `ch11.md` vừa chỉnh sửa file `glossary.md`, nhiều khả năng trong quá trình review file `ch11.md`, file `glossary.md` đã được merge ở một PR khác. Việc này sẽ dẫn đến xung đột, việc giải quyết xung đột sẽ tốn nhiều công sức, đặc biệt với các bạn chưa quen dùng git.

3. Sự thay đổi trong mỗi PR càng ít càng tốt. Bạn không nên thêm nhiều dòng trắng không cần thiết vào trong file, cũng không nên thay đội nội dung phần tiếng Anh vì rất có thể bạn xóa, thêm một từ nào đó vào bản gốc mà ngưởi review không nhìn ra.


# Review
Review là một việc rất quan trọng trước khi merge một PR. Nếu bạn chưa quen với việc tạo PR, bạn có thể đóng góp bằng cách review các PR hiện tại.

**Mọi đóng góp của các bạn đều được lưu lại trong lịch sử của repo này.**
