> # 1. Why Machine Learning Strategy

# 1. Tại sao cần chiến lược Machine Learning 

> Machine learning is the foundation of countless important applications, including web search, email anti-spam, speech recognition, product recommendations, and more. I assume that you or your team is working on a machine learning application, and that you want to make rapid progress. This book will help you do so.

Machine Learning là nền tảng cho hàng loạt ứng dụng quan trọng như tìm kiếm trang web, lọc thư điện tử spam, nhận dạng giọng nói, gợi ý sản phẩm, và nhiều ứng dụng khác nữa. Nếu bạn cùng các thành viên trong nhóm đang làm một dự án machine learning và rất muốn tiến triển nhanh chóng, thì quyển sách này là dành cho bạn.

> **Example: Building a cat picture startup**

 **Ví dụ: Xây dựng Startup về ảnh mèo** 

> Say you’re building a startup that will provide an endless stream of cat pictures to cat lovers.

Giả sử bạn xây dựng công ty khởi nghiệp cung cấp không giới hạn ảnh mèo cho những người yêu thích. 


![img](../imgs/C01_01.png)

> You use a neural network to build a computer vision system for detecting cats in pictures. But tragically, your learning algorithm’s accuracy is not yet good enough. You are under tremendous pressure to improve your cat detector. What do you do?

Bạn dùng mạng neural cho hệ thống thị giác máy nhận biết ảnh có hình mèo. Nhưng dở một cái là thuật toán bạn dùng chưa đủ độ chính xác. Bạn đang chịu rất nhiều áp lực để tăng chất lượng dự đoán tìm ảnh mèo. Bạn sẽ làm thế nào?


> Your team has a lot of ideas, such as:

Nhóm bạn có thể đưa ra rất nhiều ý tưởng như:

> * Get more data: Collect more pictures of cats.

* Lấy thêm dữ liệu: Sưu tầm thêm nhiều ảnh mèo.

> * Collect a more diverse training set. For example, pictures of cats in unusual positions; cats with unusual coloration; pictures shot with a variety of camera settings; ...

* Lấy tập huấn luyện đa dạng hơn. Ví dụ như: ảnh mèo ở vị trí độc lạ, ảnh mèo với màu sắc khác thường, ảnh mèo được chụp với cấu hình máy ảnh khác nhau .v.v.

> * Train the algorithm longer, by running more gradient descent iterations.

* Huấn luyện thuật toán lâu hơn bằng cách chạy nhiều vòng lặp gradient descent hơn. 
 
> * Try a bigger neural network, with more layers/hidden units/parameters.

* Thử nghiệm mạng neural lớn hơn với nhiều lớp/nút ẩn/tham số hơn.

> * Try a smaller neural network.

* Thử nghiệm mạng neural nhỏ hơn.

> * Try adding regularization (such as L2 regularization).

*  Thử nghiệm kỹ thuật regularization (ví dụ như L2 regularization)

> * Change the neural network architecture (activation function, number of hidden units, etc.)

*  Thay đổi kiến trúc mạng neural (ví dụ: hàm activation, số lượng nút ẩn, .v.v)

* ...

> If you choose well among these possible directions, you’ll build the leading cat picture platform, and lead your company to success. If you choose poorly, you might waste months. How do you proceed?

Nếu chọn đúng một trong những hướng kể trên, có thể bạn sẽ xây dựng nên một nền tảng ảnh mèo và startup thành công. Ngược lại, nếu chọn nhầm hướng, bạn có thể đánh mất cả tháng trời. Vậy phải làm như thế nào? 

> This book will tell you how. Most machine learning problems leave clues that tell you what’s useful to try, and what’s not useful to try. Learning to read those clues will save you months or years of development time.

Cuốn sách này sẽ giúp bạn trả lời câu hỏi đó. Phần lớn các vấn đề về machine learning đều có những dấu hiệu riêng ẩn chứa gợi ý về phương hướng giải quyết. Việc học để phát hiện ra những dấu hiệu đó sẽ giúp bạn tiết kiệm hàng tháng hay thậm chí hàng năm trời phát triển sản phẩm. 



> # 2. How to use this book to help your team

# 2. Cách sử dụng cuốn sách khi làm việc nhóm

> After finishing this book, you will have a deep understanding of how to set technical direction for a machine learning project.

Sau khi đọc xong cuốn sách này, bạn sẽ hiểu sâu hơn về cách lựa chọn hướng giải quyết kỹ thuật cho đề tài machine learning. 

> But your teammates might not understand why you’re recommending a particular direction. Perhaps you want your team to define a single-number evaluation metric, but they aren’t convinced. How do you persuade them?

Nhưng có thể cộng sự của bạn không hiểu tại sao bạn lại chọn hướng đi như vậy. Có thể bạn muốn cả đội xác định và dùng một phép đo đơn trị, nhưng liệu tất cả thành viên đều đồng tình với quyết định đó? Và bạn sẽ làm gì để thuyết phục họ?

> That’s why I made the chapters short: So that you can print them out and get your teammates to read just the 1-2 pages you need them to know.

Đó là lý do tại sao tôi chủ tâm viết những chương rất ngắn. Bạn có thể dễ dàng thuyết phục quý đồng nghiệp bằng cách chia sẻ 1-2 trang bản in của chương liên quan.

> A few changes in prioritization can have a huge effect on your team’s productivity. By helping your team with a few such changes, I hope that you can become the superhero of your team!

Chỉ với một vài thay đổi nhỏ về thứ tự ưu tiên có thể tác động lớn tới năng suất công việc của cả nhóm. Và bằng những thay đổi đó, tôi hi vọng bạn sẽ sớm trở thành siêu nhân Machine Learning của cả đội!

![img](../imgs/C02_01.png)



># 3. Prerequisites and Notation

# 3. Điều kiện tiên quyết và Ký hiệu

> If you have taken a Machine Learning course such as my machine learning MOOC on Coursera, or if you have experience applying supervised learning, you will be able to understand this text.

Nếu bạn đã từng học một lớp về Machine Learning ví dụ như lớp MOOC của tôi trên Coursera, hoặc bạn có kinh nghiệm áp dụng học có giám sát thì cuốn sách này sẽ dễ hiểu đối với bạn.

> I assume you are familiar with **supervised learning**: learning a function that maps from x to y, using labeled training examples (x,y). Supervised learning algorithms include linear regression, logistic regression, and neural networks. There are many forms of machine learning, but the majority of Machine Learning’s practical value today comes from supervised learning.

Tôi giả định rằng bạn đã quen thuộc với **học có giám sát**: học một hàm ánh xạ từ x tới y, sử dụng các cặp dữ liệu có nhãn (x,y). Các thuật toán học có giám sát bao gồm hồi quy tuyến tính, hồi quy logistic và mạng neural. Machine Learning có rất nhiều dạng tuy nhiên phần lớn các giá trị thực tiễn của nó hiện nay đến từ học có giám sát.

> I will frequently refer to neural networks (also known as “deep learning”). You’ll only need a basic understanding of what they are to follow this text.

Tôi sẽ thường xuyên đề cập đến mạng neural (còn được biết đến là "deep learning"). Bạn chỉ cần nắm được một số khái niệm cơ bản về mạng neural là có thể hiểu được nội dung cuốn sách.


> If you are not familiar with the concepts mentioned here, watch the first three weeks of videos in the Machine Learning course on Coursera at http://ml-class.org

Nếu những khái niệm nêu trên còn mới với bạn thì bạn hãy xem các video ba tuần đầu tiên của khóa học Machine Learning trên Coursera tại http://ml-class.org

![img](../imgs/C03_01.png)



> # 4. Scale drives machine learning progress

# 4. Quy mô quyết định mô hình machine learning

> Many of the ideas of deep learning (neural networks) have been around for decades. Why are these ideas taking off now?

Rất nhiều những ý tưởng của deep learning (mạng neural) đã xuất hiện từ hàng thập kỷ trước. Vậy tại sao tới bây giờ chúng mới bùng nổ như vậy?  

> Two of the biggest drivers of recent progress have been:

Có hai nguyên nhân mang tính quyết định tới những phát triển gần đây của deep learning là:

> * **Data availability.** People are now spending more time on digital devices (laptops, mobile devices). Their digital activities generate huge amounts of data that we can feed to our learning algorithms.

* **Dữ liệu sẵn có**. Ngày nay, mọi người dành nhiều thời gian hơn bên những thiết bị số như máy tính xách tay, thiết bị di động, .v.v. Chính những thiết bị số này là nguồn tạo ra lượng dữ liệu cực lớn -- dữ liệu vẫn dùng cho những thuật toán học ngày nay.

> * **Computational scale.** We started just a few years ago to be able to train neural networks that are big enough to take advantage of the huge datasets we now have.

* **Quy mô năng lực tính toán**. Cho tới một vài năm gần đây chúng ta mới có thể huấn luyện mạng neural đủ lớn để tận dụng những bộ dữ liệu khổng lồ này. 

> In detail, even as you accumulate more data, usually the performance of older learning algorithms, such as logistic regression, “plateaus.” This means its learning curve “flattens out,” and the algorithm stops improving even as you give it more data:

Cho dù có thêm nhiều nhiều dữ liệu nữa, hiệu quả của thuật toán machine learning thế hệ cũ như hồi quy logistic cũng không tăng. Nghĩa là đồ thị quá trình học chững lại và thuật toán ngừng cải thiện cho dù có thêm dữ liệu: 

![img](../imgs/C04_01.png)

> It was as if the older algorithms didn’t know what to do with all the data we now have.

Như thể thuật toán cổ điển không biết xử lý thế nào với tất cả lượng dữ liệu đang có. 

> If you train a small neutral network (NN) on the same supervised learning task, you might get slightly better performance:

Nếu bạn huấn luyện một mạng neural nhỏ cho cùng một tác vụ học có giám sát thì có thể đạt chất lượng cao hơn một chút:

![img](../imgs/C04_02.png)

> Here, by “Small NN” we mean a neural network with only a small number of hidden units/layers/parameters. Finally, if you train larger and larger neural networks, you can obtain even better performance [1]:

"Mạng neural nhỏ" ở đây có nghĩa là mạng neural với ít nút ẩn/tầng/tham số. Sau cùng, bạn có thể cải thiện chất lượng thêm nữa nếu dùng các mạng neural lớn hơn [1]: 

![img](../imgs/C04_03.png)

> Thus, you obtain the best performance when you (i) Train a very large neural network, so that you are on the green curve above; (ii) Have a huge amount of data.

Vì thế bạn có thể đạt được kết quả tốt nhất khi (i) huấn luyện mạng neural rất lớn - tương ứng với đường chất lượng màu xanh lục và (ii) có lượng dữ liệu lớn. 

> Many other details such as neural network architecture are also important, and there has been much innovation here. But one of the more reliable ways to improve an algorithm’s performance today is still to (i) train a bigger network and (ii) get more data.

Còn nhiều chủ đề quan trọng khác, như kiến trúc mạng neural, với rất nhiều sáng tạo và công trình nghiên cứu. Nhưng suy cho cùng, một trong những cách đơn giản hơn để tăng chất lượng thuật toán vẫn là (i) huấn luyện mạng lớn hơn và (ii) lấy thêm dữ liệu.

> **FOOTNOTE:**

**Chú Thích**

> [1] This diagram shows NNs doing better in the regime of small datasets. This effect is less consistent than the effect of NNs doing well in the regime of huge datasets. In the small data regime, depending on how the features are hand-engineered, traditional algorithms may or may not do better. For example, if you have 20 training examples, it might not matter much whether you use logistic regression or a neural network; the hand-engineering of features will have a bigger effect than the choice of algorithm. But if you have 1 million examples, I would favor the neural network.

[1] Mặc dù hình vẽ thể hiện mạng neural cho kết quả tốt hơn với tập dữ liệu nhỏ, nhưng nhận định này ít nhất quán hơn so với nhận định về mạng neural với dữ liệu lớn. Vì đối với dữ liệu nhỏ, chất lượng thuật toán truyền thống có thể hoặc không cho kết quả tốt hơn mạng neural và bị phụ thuộc rất nhiều vào cách tạo đặc trưng thủ công. Nếu ta chỉ có 20 mẫu huấn luyện thì việc dùng hồi quy logistic hay mạng neural không khác biệt nhiều và lựa chọn đặc trưng thủ công sẽ có ý nghĩa hơn. Còn nếu có một triệu mẫu, thì tôi sẽ chọn dùng mạng neural. 

> The process of how to accomplish (i) and (ii) are surprisingly complex. This book will discuss the details at length. We will start with general strategies that are useful for both traditional learning algorithms and neural networks, and build up to the most modern strategies for building deep learning systems.

Quá trình đạt được (i) huấn luyện mạng lớn trên (ii) tập dữ liệu lớn có thể phức tạp hơn bạn tưởng. Nhưng đừng lo, vấn đề này sẽ được thảo luận đầy đủ và chi tiết trong cuốn sách này. Chúng ta sẽ bắt đầu với các chiến thuật chung, hữu ích cho cả thuật toán truyền thống lẫn mạng neural, và từ từ xây dựng chiến thuật mới cho việc xây dựng các hệ thống deep learning. 


> # 5. Your development and test sets

# 5. Tập phát triển và tập kiểm tra

> Let’s return to our earlier cat pictures example: You run a mobile app, and users are uploading pictures of many different things to your app. You want to automatically find the cat pictures.

Trở lại với ví dụ bức ảnh mèo ở phần trước: khi bạn có một ứng dụng di động, và người dùng đang tải nhiều loại ảnh lên ứng dụng của bạn. Bạn muốn tự động tìm ra đâu là các bức ảnh mèo.

> Your team gets a large training set by downloading pictures of cats (positive examples) and non-cats (negative examples) off of different websites. They split the dataset 70%/30% into training and test sets. Using this data, they build a cat detector that works well on the training and test sets.

Nhóm của bạn có một tập dữ liệu lớn bằng cách tải các bức ảnh mèo (các mẫu dương) và các bức ảnh không có mèo (các mẫu âm) từ nhiều nguồn khác nhau. Tập dữ liệu này sau đó được chia 70%/30% thành tập huấn luyện và tập kiểm tra. Sử dụng tập dữ liệu này, bạn tạo ra một bộ nhận dạng mèo có thể hoạt động tốt ở cả tập huấn luyện và tập kiểm tra.

> But when you deploy this classifier into the mobile app, you find that the performance is really poor!

Tuy nhiên, khi triển khai bộ nhận dạng mèo này lên một ứng dụng di động, bạn lại thấy rằng kết quả rất tệ!

![img](../imgs/C05_01.png)

> ## What happened?

## Điều gì đã xảy ra?

> You figure out that the pictures users are uploading have a different look than the website images that make up your training set: Users are uploading pictures taken with mobile phones, which tend to be lower resolution, blurrier, and poorly lit. Since your training/test sets were made of website images, your algorithm did not generalize well to the actual distribution you care about: mobile phone pictures.

Bạn nhận ra rằng các bức ảnh được người dùng tải lên nhìn khác các bức ảnh mà bạn tải về từ trên mạng mà được dùng để xây dựng tập dữ liệu: do các bức ảnh được chụp bằng điện thoại thường có độ phân giải thấp hơn, bị nhòe (mờ) hoặc tối hơn. Do bộ nhận dạng được huấn luyện trên tập dữ liệu từ ảnh trên mạng nên nó không khái quát hóa tốt đến phân phối thực tế mà bạn cần nhắm đến: ảnh chụp từ điện thoại.

> Before the modern era of big data, it was a common rule in machine learning to use a random 70%/30% split to form your training and test sets. This practice can work, but it’s a bad idea in more and more applications where the training distribution (website images in our example above) is different from the distribution you ultimately care about (mobile phone images).

Trước kỷ nguyên big data, có một nguyên tắc chung trong machine learing là chia tập huấn luyện và kiểm tra ngẫu nhiên theo tỉ lệ 70%/30%. Cách chia này có thể hiệu quả, nhưng không phải là một ý tưởng tốt trong ngày càng nhiều ứng dụng nơi mà phân phối của tập huấn luyện (ảnh trên mạng trong ví dụ trên đây) khác với phân phối của dữ liệu bạn thực sự quan tậm (ảnh chụp từ điện thoại).

> We usually define:

Chúng ta thường định nghĩa như sau:

> * **Training set** — Which you run your learning algorithm on.

* **Tập huấn luyện** — Là tập dữ liệu để chạy thuật toán học.

> * **Dev (development) set** — Which you use to tune parameters, select features, and make other decisions regarding the learning algorithm. Sometimes also called the hold-out cross validation set.

* **Tập phát triển** — Là tập dữ liệu được dùng để điều chỉnh lại các tham số, lựa chọn đặc trưng và quyết định các thay đổi liên quan đến thuật toán học. Đôi khi, nó còn được gọi là tập kiểm định chéo.

> * **Test set** — which you use to evaluate the performance of the algorithm, but not to make any decisions regarding what learning algorithm or parameters to use.

* **Tập kiểm tra** — Là tập dữ liệu dùng để đánh giá chất lượng của thuật toán học, nhưng không được dùng để quyết định các thay đổi liên quan đến thuật toán học hay các tham số.

> Once you define a dev set (development set) and test set, your team will try a lot of ideas, such as different learning algorithm parameters, to see what works best. The dev and test sets allow your team to quickly see how well your algorithm is doing.

Sau khi định nghĩa tập phát triển và tập kiểm tra, nhóm của bạn có thể thử nhiều ý tưởng khác nhau, ví dụ như các tham số khác nhau cho thuật toán học, để tìm ra ý tưởng tốt nhất. Tập phát triển và tập kiểm tra cho phép nhóm của bạn có thể đánh giá khả năng hoạt động của thuật toán một cách nhanh chóng.

> In other words, **the purpose of the dev and test sets are to direct your team toward the most important changes to make to the machine learning system**.

Nói cách khác, **mục đích của tập phát triển và tập kiểm tra là hướng nhóm bạn tơí những thay đổi quan trọng nhất trong hệ thống machine learning**.

> So, you should do the following:

Vậy nên, bạn nên làm những điều sau đây:

> Choose dev and test sets to reflect data you expect to get in the future and want to do well on.

Lựa chọn tập phát triển và tập kiểm tra sao cho có thể phản ánh dữ liệu bạn gặp phải trong tương lai và muốn hoạt động tốt trên nó.

> In other words, your test set should not simply be 30% of the available data, especially if you expect your future data (mobile phone images) to be different in nature from your training set (website images).

Nói cách khác, tập kiểm tra không nên chỉ đơn thuần là 30% dữ liệu hiện có, đặc biệt là khi bạn mong đợi dữ liệu tương lai (ảnh chụp từ điện thoại) về bản chất sẽ khác với dữ liệu trong tập huấn luyện (ảnh từ trên mạng).

> If you have not yet launched your mobile app, you might not have any users yet, and thus might not be able to get data that accurately reflects what you have to do well on in the future. But you might still try to approximate this. For example, ask your friends to take mobile phone pictures of cats and send them to you. Once your app is launched, you can update your dev/test sets using actual user data.

Khi ứng dụng di động chưa được triển khai thì bạn có thể chưa có người dùng nào cả, nên việc có thể có được dữ liệu phản ánh chính xác dữ liệu tương lai là rất khó. Nhưng bạn vẫn có thể thử làm gần giống dữ liệu đó. Ví dụ, bạn có thể nhờ bạn bè chụp những bức ảnh mèo bằng điện thoại và gửi cho bạn. Một khi ứng dụng được triển khai, bạn có thể cập nhật tập phát triển/kiểm tra bằng dữ liệu người dùng thực tế.

> If you really don’t have any way of getting data that approximates what you expect to get in the future, perhaps you can start by using website images. But you should be aware of the risk of this leading to a system that doesn’t generalize well.

Nếu bạn thực sự không có cách nào để có được dữ liệu gần giống với dữ liệu tương lai thì bạn có thể sử dụng ảnh từ các trang web. Nhưng bạn nên nhận thức nguy cơ dẫn đến một hệ thống khái quát hóa không tốt.

> It requires judgment to decide how much to invest in developing great dev and test sets. But don’t assume your training distribution is the same as your test distribution. Try to pick test examples that reflect what you ultimately want to perform well on, rather than whatever data you happen to have for training.

Ta cần thẩm định để quyết định được cần phải tập trung bao nhiêu cho việc phát triển tập phát triển và tập kiểm tra. Tuy nhiên đừng đánh đồng phân phối giữa tập huấn luyện và tập kiểm tra. Hãy chọn ra những mẫu kiểm tra phản ánh cái mà bạn muốn thực hiện tốt, hơn là bất kì dữ liệu nào bạn tình cờ có được cho tập huấn luyện.



**Chương này đã được merge nhưng cần một lần chỉnh sửa văn phong nữa. Mong các bạn đóng góp bằng cách tạo Pull Request mới.**
-----------

> # Your dev and test sets should come from the same distribution

# Tập phát triển và tập kiểm tra nên có cùng phân phối

<img src="../imgs/C06_01.png" width=300 align=center>

> You have your cat app image data segmented into four regions, based on your largest markets: (i) US, (ii) China, (iii) India, and (iv) Other. To come up with a dev set and a test set, say we put US and India in the dev set; China and Other in the test set. In other words, we can randomly assign two of these segments to the dev set, and the other two to the test set, right?

Dựa trên vị trí người dùng ứng dụng di động của bạn, tập dữ liệu ảnh mèo được tải lên từ bốn khu vực chính: (i) Hoa Kỳ, (ii) Trung Quốc, (iii) Ấn Độ, và (iv) Khu vực khác. Để tạo tập phát triển và tập kiểm tra, giả định như chúng ta lấy dữ liệu từ Hoa Kỳ và Ấn Độ để tạo tập phát triển; Trung Quốc và Khu vực khác để tạo tập kiểm tra. Nói cách khác, chúng ta có thể chọn ngẫu nhiên dữ liệu ảnh từ hai trong bốn khu vực trên làm tập phát triển, dữ liệu ảnh từ hai khu vực còn lại làm tập kiểm tra. Phân chia vậy liệu có đúng hay không?

> Once you define the dev and test sets, your team will be focused on improving dev set performance. Thus, the dev set should reflect the task you want to improve on the most: To do well on all four geographies, and not only two.

Một khi bạn đã phân loại tập phát triển và tập kiểm tra, nhóm của bạn sẽ tập trung cải thiện kết quả trên tập phát triển. Bởi vậy, tập phát triển nên đại diện nhiệm vụ bạn muốn cải thiện nhiều nhất: hoạt động tốt trên dữ liệu không chỉ hai mà cả bốn thị trường.

> There is a second problem with having different dev and test set distributions: There is a chance that your team will build something that works well on the dev set, only to find that it does poorly on the test set. I’ve seen this result in much frustration and wasted effort. Avoid letting this happen to you.

Vấn đề thứ hai với việc tập phát triển và tập kiểm tra có phân phối khác nhau: Có khả năng nhóm của bạn xây dựng được một mô hình hoạt động tốt trên tập phát triển nhưng lại kém trên tập kiểm tra. Tôi đã từng thấy việc này (việc có phân phối khác nhau của hai tập dữ liệu) dẫn đến những kết quả đáng thất vọng và sự lãng phí về công sức. Hãy tránh để điều này xảy ra.

> As an example, suppose your team develops a system that works well on the dev set but not the test set. If your dev and test sets had come from the same distribution, then you would have a very clear diagnosis of what went wrong: You have overfit the dev set. The obvious cure is to get more dev set data.

Ví dụ, nhóm của bạn phát triển một hệ thống hoạt động tốt trên tập phát triển nhưng kém trên tập kiểm tra. Nếu tập phát triển và tập kiểm tra có cùng một phân phối thì bạn có thể xác định ngay vấn đề: Mô hình của bạn đã overfit tập phát triển. Cách xử lý hiển nhiên nhất đó là bổ sung thêm dữ liệu cho tập phát triển.

> But if the dev and test sets come from different distributions, then your options are less clear. Several things could have gone wrong:

Nhưng nếu tập phát triển và tập kiểm tra được tạo từ các phân phối khác nhau thì việc xác định vấn đề sẽ phức tạp hơn. Rất nhiều vấn đề có thể xảy ra:   

> 1. You had overfit to the dev set.

1. Bạn đã overfit tập phát triển.

> 2. The test set is harder than the dev set. So your algorithm might be doing as well as could be expected, and no further significant improvement is possible.

2. Dữ liệu tập kiểm tra đa dạng (phức tạp) hơn tập phát triển. Thuật toán của bạn có thể đã hoạt động tốt trên tập phát triển, và không thể có thêm cải thiện đáng kể.

> 3. The test set is not necessarily harder, but just different, from the dev set. So what works well on the dev set just does not work well on the test set. In this case, a lot of your work to improve dev set performance might be wasted effort.

3. Tập kiểm tra có thể không khó hơn nhưng lại khác so với tập phát triển. Do đó mô hình có thể hoạt động tốt trên tập phát triển nhưng lại kém trên tập kiểm tra. Trong trường hợp này, việc cố gắng cải thiện mô hình để hoạt động tốt trên tập phát triển có thể trở nên vô nghĩa.

> Working on machine learning applications is hard enough. Having mismatched dev and test sets introduces additional uncertainty about whether improving on the dev set distribution also improves test set performance. Having mismatched dev and test sets makes it harder to figure out what is and isn’t working, and thus makes it harder to prioritize what to work on.

Nhiều vấn đề phức tạp có thể xảy ra khi làm việc với các ứng dụng machine learning. Tập phát triển và kiểm tra không nhất quán dẫn đến sự không chắc chắn về việc liệu rằng cải thiện hiệu quả trên tập phát triển có giúp cải thiện hiệu quả trên tập kiểm tra. Sự không nhất quán này khiến việc tìm ra nguyên nhân và sắp xếp hướng giải quyết trở nên khó khăn hơn vì không biết mô hình gặp vấn đề ở đâu. Tập phát triển và tập kiểm tra khác nhau cũng khiến cho việc xác định vấn đề trở nên khó khăn hơn, nhất là trong việc lựa chọn các công việc ưu tiên cần thiết để cải thiện mô hình.

> If you are working on a 3rd party benchmark problem, their creator might have specified dev and test sets that come from different distributions. Luck, rather than skill, will have a greater impact on your performance on such benchmarks compared to if the dev and test sets come from the same distribution. It is an important research problem to develop learning algorithms that are trained on one distribution and generalize well to another. But if your goal is to make progress on a specific machine learning application rather than make research progress, I recommend trying to choose dev and test sets that are drawn from the same distribution. This will make your team more efficient.

Nếu bạn đang làm việc với một bài toán đánh giá xếp hạng của bên thứ ba, họ có thể cung cấp tập phát triển và tập kiểm tra có phân phối khác nhau. Nếu so sánh với bài toán có tập phát triển và tập kiểm tra đến từ cùng phân phối, bài toán này có kết quả phụ thuộc nhiều vào may mắn hơn là kỹ năng của bạn. Việc phát triển các thuật toán mà mô hình được huấn luyện trên một phân phối để khái quát hóa tốt trên một phân phối khác là một vấn đề quan trọng trong nghiên cứu. Tuy nhiên, nếu mục tiêu của bạn là cải thiện một ứng dụng machine learning cụ thể thay vì tạo ra tiến triển trong nghiên cứu, tôi khuyên bạn chọn tập phát triển và tập kiểm tra đến từ cùng phân phối. Điều này sẽ khiến nhóm bạn làm việc hiệu quả hơn.



> # 7. How large do the dev/test sets need to be?

# 7. Tập phát triển/kiểm tra cần lớn đến mức nào?

> The dev set should be large enough to detect differences between algorithms that you are trying out. For example, if classifier A has an accuracy of 90.0% and classifier B has an accuracy of 90.1%, then a dev set of 100 examples would not be able to detect this 0.1% difference. Compared to other machine learning problems I’ve seen, a 100 example dev set is small. Dev sets with sizes from 1,000 to 10,000 examples are common. With 10,000 examples, you will have a good chance of detecting an improvement of 0.1%. [2]

Tập phát triển phải đủ lớn để nhận ra sự khác biệt giữa các thuật toán đang thử nghiệm. Ví dụ, nếu bộ phân loại A có độ chính xác 90,0% và bộ phân loại B có độ chính xác 90,1%, thì một tập phát thiển có 100 mẫu sẽ không thể phát hiện sự khác biệt 0,1% này. So với các vấn đề khác trong machine learning mà tôi đã thấy, một tập phát triển chỉ với 100 mẫu là nhỏ. Các tập phát triển thường có từ 1.000 tới 10.000 mẫu. Với 10.000 mẫu, bạn sẽ có thể thấy sự cải thiện ở mức 0,1%. [2]

> For mature and important applications—for example, advertising, web search, and product recommendations—I have also seen teams that are highly motivated to eke out even a 0.01% improvement, since it has a direct impact on the company’s profits. In this case, the dev set could be much larger than 10,000, in order to detect even smaller improvements.

Trong các ứng dụng quan trọng và đã đã đưa vào khai thác -- ví dụ như quảng cáo, tìm kiếm trên web và gợi ý sản phẩm -- tôi đã thấy nhiều nhóm rất muốn cải thiện chất lượng thuật toán dù chỉ là 0,01%, vì nó có ảnh hưởng trực tiếp đến lợi nhuận của công ty. Trong trường hợp này, tập phát triển có thể lớn hơn 10.000 mẫu rất nhiều để có thể phát hiện ra những cải tiến thậm chí nhỏ hơn.

> How about the size of the test set? It should be large enough to give high confidence in the overall performance of your system. One popular heuristic had been to use 30% of your data for your test set. This works well when you have a modest number of examples—say 100 to 10,000 examples. But in the era of big data where we now have machine learning problems with sometimes more than a billion examples, the fraction of data allocated to dev/test sets has been shrinking, even as the absolute number of examples in the dev/test sets has been growing. There is no need to have excessively large dev/test sets beyond what is needed to evaluate the performance of your algorithms.

Vậy còn kích thước của tập kiểm tra thì sao? Nó cần đủ lớn để mang lại độ tin cậy cao về hiệu quả tổng thể của hệ thống. Một công thức thực nghiệm phổ biến là sử dụng 30% dữ liệu làm tập kiểm tra. Cách làm này hiệu quả với những tập dữ liệu với lượng mẫu khiêm tốn từ 100 tới 10.000. Tuy nhiên, trong kỷ nguyên big data với những bài toán machine learning đôi khi có nhiều hơn một tỷ mẫu, tỉ lệ dữ liệu dùng cho tập phất triển và tập kiểm tra đã giảm xuống đáng kể, mặc dù số lượng mẫu trong hai tập này vẫn tăng lên. Thực sự không cần có tập phát triển/kiểm tra lớn quá mức để đánh giá hiệu quả của các thuật toán.


> **FOOTNOTE:**

> [2] In theory, one could also test if a change to an algorithm makes a statistically significant difference on the dev set. In practice, most teams don’t bother with this (unless they are publishing academic research papers), and I usually do not find statistical significance tests useful for measuring interim progress.

**CHÚ THÍCH:**

[2] Trên lý thuyết, ta cũng có thể kiểm tra xem một thay đổi trong thuật toán có tạo ra sự khác biệt có ý nghĩa thống kê trên tập phát triển hay không. Trong thực tế, hầu hết mọi người đều không quan tâm đến điều này (trừ khi họ muốn công bố các các bài báo khoa học). Tôi thường thấy các bài kiểm định thống kê không mấy hữu ích trong việc đánh giá tiến độ phát triển.



> # 8. Establish a single-number evaluation metric for your team to optimize

# 8. Thiết lập một phép đo đơn trị làm mục tiêu tối ưu

> Classification accuracy is an example of a **single-number evaluation metric**: You run your classifier on the dev set (or test set), and get back a single number about what fraction of examples it classified correctly. According to this metric, if classifier A obtains 97% accuracy, and classifier B obtains 90% accuracy, then we judge classifier A to be superior.

Độ chính xác trong phân loại là ví dụ của **phép đo đơn trị** -- phép đo được biểu diễn bằng chỉ một con số. Khi chạy bộ phân loại trên một tập phát triển (hoặc tập kiểm tra), độ chính xác được tính bằng chỉ số thể hiện tỉ lệ mẫu được phân loại chính xác trên tổng số mẫu trong tập đó. Theo phép đo này, nếu độ chính xác của bộ phân loại A là 97% và của bộ phân loại B là 90% thì ta kết luận rằng bộ phân loại A cho kết quả tốt hơn.

> In contrast, Precision and Recall[3] is not a single-number evaluation metric: It gives two numbers for assessing your classifier. Having multiple-number evaluation metrics makes it harder to compare algorithms. Suppose your algorithms perform as follows:

Ngược lại, Precision và Recall[3] không phải là một phép đo đơn trị: có hai chỉ số được sử dụng để đánh giá bộ phân loại. Việc so sánh các thuật toán với nhau sẽ trở nên khó hơn với những phép đo đa trị -- những phép đo được biểu diễn bằng nhiều hơn một số. Giả sử thuật toán trả về kết quả như sau:


> Here, neither classifier is obviously superior, so it doesn’t immediately guide you toward picking one.

Ở đây, không bộ phân loại nào tốt hơn một cách rõ ràng, vì vậy dựa vào kết quả trên ta không thể ngay lập tức chọn ra một bộ phân loại tốt hơn.

| Bộ Phân Loại  | Precision | Recall |
| ----- | -------: | -------: |
| A  | 95%  | 90% |
| B  | 98%  | 85% |


> During development, your team will try a lot of ideas about algorithm architecture, model parameters, choice of features, etc. Having a **single-number evaluation metric** such as accuracy allows you to sort all your models according to their performance on this metric, and quickly decide what is working best.

Trong quá trình phát triển, nhóm bạn sẽ thử rất nhiều ý tưởng liên quan đến cấu trúc thuật toán, tham số mô hình, lựa chọn các đặc trưng, v.v.. Việc có một **phép đo đơn trị** như độ chính xác sẽ giúp xếp hạng các mô mình dựa theo những kết quả trả về qua phép đo đó, từ đó nhanh chóng quyết định mô hình nào hoạt động tốt nhất.

> If you really care about both Precision and Recall, I recommend using one of the standard ways to combine them into a single number. For example, one could take the average of precision and recall, to end up with a single number. Alternatively, you can compute the “F1 score,” which is a modified way of computing their average, and works better than simply taking the mean.[4]

Nếu bạn thực sự quan tâm đến cả Precision lẫn Recall. Tôi gợi ý sử dụng một trong những cách tiêu chuẩn để kết hợp các chỉ số đó thành một chỉ số duy nhất. Ví dụ, một người có thể lấy giá trị trung bình của Precision và Recall rồi thu về một phép đo đơn trị. Hoặc thay vào đó, bạn có thể tính "chỉ số F1", một biến thể của trung bình cộng, thường hoạt động tốt hơn việc chỉ lấy giá trị trung bình.

> Having a single-number evaluation metric speeds up your ability to make a decision when you are selecting among a large number of classifiers. It gives a clear preference ranking among all of them, and therefore a clear direction for progress.

Việc có một phép đo đơn trị sẽ giúp tăng tốc khả năng đưa ra quyết định của bạn khi bạn phải lựa chọn trong một số lượng lớn bộ phân loại. Phép đo đơn trị đưa ra ưu tiên rõ ràng trong việc phân hạng những thuật toán đó, tạo ra những đường hướng rõ ràng để phát triển. 

| Bộ Phân Loại | Precision | Recall | Chỉ số F1 |
| ----- | -------: | -------: | -----: |
| A  | 95%  | 90% | 92.4% |
| B  | 98%  | 85% | 91.0% |

> As a final example, suppose you are separately tracking the accuracy of your cat classifier in four key markets: (i) US, (ii) China, (iii) India, and (iv) Other. This gives four metrics. By taking an average or weighted average of these four numbers, you end up with a single number metric. Taking an average or weighted average is one of the most common ways to combine multiple metrics into one.

Một ví dụ cuối cùng, giả sử bạn đang theo dõi riêng biệt về độ chính xác của bộ phân loại mèo trong bốn thị trường trọng điểm: (i) Mĩ, (ii) Trung Quốc, (iii) Ấn Độ, và (iv) những nước khác. Bạn sẽ thu về bốn phép đo. Bằng cách lấy giá trị trung bình hoặc giá trị trung bình có trọng số của bốn chỉ số này, bạn sẽ thu được một phép đo đơn trị. Tính toán giá trị trung bình hoặc giá trị trung bình có trọng số là một trong những cách phổ biển nhất để kết hợp nhiều phép đo thành một.

> **FOOTNOTE:**

**CHÚ THÍCH:**
> [3] The Precision of a cat classifier is the fraction of images in the dev (or test) set it labeled as cats that really are cats. Its Recall is the percentage of all cat images in the dev (or test) set that it correctly labeled as a cat. There is often a tradeoff between having high precision and high recall.

[3] Precision của một bộ phân loại mèo là tỉ lệ những ảnh được phân nhãn chính xác là mèo trong tập phát triển (hoặc tập kiểm tra) trên tổng số những ảnh được bộ phân loại phân nhãn mèo trong cùng tập đó. Recall của bộ phân loại đó là số phần trăm của tất cả ảnh mèo ở trong tập phát triển (hoặc tập kiểm tra) được phân loại chính xác là mèo trong cùng tập đó. Thường có một sự đánh đổi giữa việc có chỉ số precision cao và chỉ số recall cao.

> [4] If you want to learn more about the F1 score, see [https://en.wikipedia.org/wiki/F1_score](https://en.wikipedia.org/wiki/F1_score). It is the “harmonic mean” between Precision and Recall, and is calculated as 2/((1/Precision)+(1/Recall)).

[4] Nếu bạn muốn đọc thêm về chỉ số F1, xem [https://en.wikipedia.org/wiki/F1_score](https://en.wikipedia.org/wiki/F1_score). Chỉ số F1 là trung bình điều hoà của Precision và Recall, được tính bằng 2/((1/Precision) + (1/Recall))



> # 9. Optimizing and satisficing metrics

# 9. Phép đo tối ưu và phép đo thỏa mãn

> Here’s another way to combine multiple evaluation metrics.

Đây là một cách khác để kết hợp nhiều phép đo.

> Suppose you care about both the accuracy and the running time of a learning algorithm. You need to choose from these three classifiers:

Giả sử bạn quan tâm đến cả độ chính xác lẫn thời gian chạy của một thuật toán học nào đó. Bạn cần phải chọn trong ba bộ phân loại sau:

| Bộ phân loại  | Độ chính xác | Thời gian chạy |
| ----- | -------: | -------: |
| A  | 90%  | 80ms |
| B  | 92%  | 95ms |
| C  | 95%  | 1,500ms |

> It seems unnatural to derive a single metric by putting accuracy and running time into a single formula, such as:

Việc tạo ra một phép đo đơn trị bằng cách đưa cả độ chính xác và thời gian chạy vào trong một công thức có vẻ không tự nhiên, ví dụ như:

> Accuracy - 0.5*RunningTime

Độ chính xác - 0.5*(Thời gian chạy)

> Here’s what you can do instead: First, define what is an “acceptable” running time. Lets say anything that runs in 100ms is acceptable. Then, maximize accuracy, subject to your classifier meeting the running time criteria. Here, running time is a “satisficing metric”—your classifier just has to be “good enough” on this metric, in the sense that it should take at most 100ms. Accuracy is the “optimizing metric.”

Thay vào đó, bạn có thể làm như sau: Trước hết định nghĩa thế nào là một mốc thời gian chạy "chấp nhận được". Giả sử mốc dưới 100ms là chấp nhận được. Sau đó, hãy cực đại hóa độ chính xác, với ràng buộc là bộ phân loại đó vẫn đảm bảo yêu cầu về thời gian chạy. Ở đây, thời gian chạy là một "phép đo thỏa mãn" - bộ phân loại của bạn chỉ cần "đủ tốt" về mặt này (thời gian), theo nghĩa nó chỉ được phép chạy trong thời gian ít hơn 100ms. Độ chính xác mới là "phép đo tối ưu".

> If you are trading off N different criteria, such as binary file size of the model (which is important for mobile apps, since users don’t want to download large apps), running time, and accuracy, you might consider setting N-1 of the criteria as “satisficing” metrics. I.e., you simply require that they meet a certain value. Then define the final one as the “optimizing” metric. For example, set a threshold for what is acceptable for binary file size and running time, and try to optimize accuracy given those constraints.

Nếu bạn phải cân bằng giữa N tiêu chí khác nhau, ví dụ như kích thước file nhị phân của mô hình (điều này quan trọng với các ứng dụng di động, vì người dùng không muốn tải về những ứng dụng có kích thước lớn), thời gian chạy, và độ chính xác, bạn có thể cân nhắc đặt N-1 trong số các tiêu chí là các phép đo "thỏa mãn". Có nghĩa là bạn chỉ cần yêu cầu chúng đạt giá trị nào đó. Sau đó coi tiêu chí còn lại là phép đo "tối ưu". Ví dụ như đặt mức ngưỡng chấp nhận được cho kích thước file nhị phân và thời gian chạy, sau đó tối ưu độ chính xác với điều kiện các ràng buộc trên vẫn được thỏa mãn.

> As a final example, suppose you are building a hardware device that uses a microphone to listen for the user saying a particular “wakeword,” that then causes the system to wake up. Examples include Amazon Echo listening for “Alexa”; Apple Siri listening for “Hey Siri”; Android listening for “Okay Google”; and Baidu apps listening for “Hello Baidu.” You care about both the false positive rate—the frequency with which the system wakes up even when no one said the wakeword—as well as the false negative rate—how often it fails to wake up when someone says the wakeword. One reasonable goal for the performance of this system is to minimize the false negative rate (optimizing metric), subject to there being no more than one false positive every 24 hours of operation (satisficing metric).

Ví dụ cuối cùng, giả sử bạn cần xây dựng một thiết bị phần cứng có sử dụng microphone để nghe người dùng nói một từ "đánh thức" đặc biệt nào đó để đánh thức hệ thống. Ví dụ về từ đánh thức như Amazon Echo với "Alexa"; Apple Siri với "Hey Siri"; Android với "Hey Google" hay các ứng dụng của Baidu với "Hello Baidu". Bạn quan tâm đến cả tần suất dương tính giả (hay báo động nhầm) - tần suất mà hệ thống thức dậy khi không ai nói cụm đánh thức - cũng như tần suất âm tính giả (hay bỏ sót) - tần suất hệ thống không thức dậy khi có người nói cụm đánh thức. Một mục tiêu khả dĩ cho hệ thống này là tối thiểu hóa tần suất âm tính giả (phép đo tối ưu), trong ràng buộc rằng không có nhiều hơn một báo động nhầm cho mỗi 24 giờ hoạt động (phép đo thỏa mãn).

> Once your team is aligned on the evaluation metric to optimize, they will be able to make faster progress.

Một khi nhóm của bạn thống nhất về việc phép đo nào cần được tối ưu, cả nhóm sẽ đạt tiến độ nhanh hơn.



# 12. Takeaways: Setting up development and test sets
->
# 12. Điều cần nhớ: Thiết lập các tập phát triển và kiểm tra

* Choose dev and test sets from a distribution that reflects what data you expect to get in the future and want to do well on. This may not be the same as your training data’s distribution.
->
* Chọn tập phát triển và tập kiểm tra từ một phân phối phản ánh dữ liệu bạn dự tính nhận được trong tương lai và muốn hoạt động tốt trên nó. Phân phối này có thể không giống phân phối dữ liệu huấn luyện của bạn.

* Choose dev and test sets from the same distribution if possible.
->
* Chọn tập phát triển và kiểm tra từ cùng một phân phối xác suất nếu có thể.

* Choose a single-number evaluation metric for your team to optimize. If there are multiple goals that you care about, consider combining them into a single formula (such as averaging multiple error metrics) or defining satisficing and optimizing metrics.
->
* Chọn một phép đo đơn trị để tối ưu hóa. Nếu có nhiều thông số cần quan tâm, hãy kết hợp chúng thành một công thức duy nhất (chẳng hạn như lấy trung bình của các phép đo) hoặc định nghĩa phép đo thỏa mãn và phép đo để tối ưu.

* Machine learning is a highly iterative process: You may try many dozens of ideas before finding one that you’re satisfied with.
->
* Machine learning là một quá trình lặp đi lặp lại: Bạn có thể phải thử hàng tá ý tưởng trước khi tìm thấy một ý tưởng mà bạn hài lòng.

* Having dev/test sets and a single-number evaluation metric helps you quickly evaluate algorithms, and therefore iterate faster.
->
* Có tập phát triển/kiểm tra và một phép đo đơn trị giúp bạn nhanh chóng đánh giá các thuật toán và do đó lặp lại nhanh hơn.

* When starting out on a brand new application, try to establish dev/test sets and a metric quickly, say in less than a week. It might be okay to take longer on mature applications.
->
* Khi bắt đầu trên một ứng dụng hoàn toàn mới, cố gắng thiết lập tập phát triển/kiểm tra và một phép đo một cách nhanh chóng, trong vòng chưa đầy một tuần. Với các ứng dụng đã được phát triển, quá trình này có thể kéo dài hơn.

* The old heuristic of a 70%/30% train/test split does not apply for problems where you have a lot of data; the dev and test sets can be much less than 30% of the data.
->
* Việc chia dữ liệu huấn luyện/kiểm tra theo tỉ lệ 70%/30% không áp dụng cho các bài toán với nhiều dữ liệu; tập phát triển và kiểm tra có thể chiếm ít hơn con số 30% rất nhiều.

* Your dev set should be large enough to detect meaningful changes in the accuracy of your algorithm, but not necessarily much larger. Your test set should be big enough to give you a confident estimate of the final performance of your system.
->
* Tập phát triển của bạn phải đủ lớn để phát hiện các thay đổi có ý nghĩa đối với độ chính xác của thuật toán, nhưng không nhất thiết phải lớn hơn nhiều. Tập kiểm tra phải đủ lớn để cung cấp cho bạn ước lượng đáng tin cậy về hiệu quả cuối cùng của hệ thống.

* If your dev set and metric are no longer pointing your team in the right direction, quickly change them: (i) If you had overfit the dev set, get more dev set data. (ii) If the actual distribution you care about is different from the dev/test set distribution, get new dev/test set data. (iii) If your metric is no longer measuring what is most important to you, change the metric.
->
* Nếu tập phát triển và phép đo không còn chỉ cho nhóm của bạn đi đúng hướng, hãy nhanh chóng thay đổi chúng: (i) Nếu thuật toán đã overfit tập phát triển, hãy thu thập thêm dữ liệu cho tập này. (ii) Nếu phân phối xác suất thực tế mà bạn quan tâm khác với phân phối xác suất của tập phát triển/kiểm tra, hãy tạo tập phát triển và kiểm tra mới. (iii) Nếu phép đo không còn đo lường được điều quan trọng nhất với bạn, hãy thay đổi phép đo.



> # 14. Error analysis: Look at dev set examples to evaluate ideas
# 14. Phân tích lỗi: đánh giá ý tưởng dựa trên tập phát triển 

![img](../imgs/C14_01.png)

> When you play with your cat app, you notice several examples where it mistakes dogs for cats. Some dogs do look like cats!

Khi kiểm thử ứng dụng nhận dạng mèo, bạn thấy rẳng một số bức ảnh chó bị nhận nhầm. Nhìn chúng tương đối giống mèo!

> A team member proposes incorporating 3rd party software that will make the system do better on dog images. These changes will take a month, and the team member is enthusiastic. Should you ask them to go ahead?

Một thành viên trong nhóm đề xuất tích hợp vào hệ thống phần mềm của bên thứ ba. Việc kết hợp này có thể giúp hệ thống phân biệt tốt hơn các bức ảnh chó. Có thể mất một tháng để hoàn thành quá trình tích hợp và người đề xuất ý tưởng rất hào hứng. Liệu bạn có nên yêu cầu thành viên đó bắt đầu công việc? 

> Before investing a month on this task, I recommend that you first estimate how much it will actually improve the system’s accuracy. Then you can more rationally decide if this is worth the month of development time, or if you’re better off using that time on other tasks.

Trước khi bỏ ra một tháng thực hiện, bạn nên ước lượng công việc này có thể cải thiện độ chính xác của hệ thống tới mức nào. Từ đó,bạn sẽ có thể quyết định xem có đáng bỏ ra chừng đó thời gian vào việc phát triển hay là dành nó cho những việc khác. 

> In detail, here’s what you can do:

Cụ thể, bạn có thể làm theo các bước sau:
> 1. Gather a sample of 100 dev set examples that your system ​misclassified​. I.e., examples that your system made an error on.
1. Thu thập 100 mẫu trong tập phát triển mà ứng dụng của bạn phân loại nhầm — không phải mèo nhưng được phân loại là mèo và ngược lại.
> 2. Look at these examples manually, and count what fraction of them are dog images.
2. Nhìn vào những mẫu trên và đếm xem bao nhiêu trong số đó là ảnh chó.

> The process of looking at misclassified examples is called ​**error analysis​**. In this example, if you find that only 5% of the misclassified images are dogs, then no matter how much you improve your algorithm’s performance on dog images, you won’t get rid of more than 5% of your errors. In other words, 5% is a “ceiling” (meaning maximum possible amount) for how much the proposed project could help. Thus, if your overall system is currently 90% accurate (10% error), this improvement is likely to result in at best 90.5% accuracy (or 9.5% error, which is 5% less error than the original 10% error).

Quá trình nhìn vào những mẫu bị phân loại nhầm được gọi là **phân tích lỗi**. Trong ví dụ này, nếu bạn nhận thấy rằng chỉ 5% lỗi là chó nhầm thành mèo thì cho dù cải thiện thuật toán theo hướng tích hợp phần mềm nhận dạng chó vào ứng dụng, bạn không thể loại bỏ quá 5% số ảnh bị nhận dạng sai. Nói cách khác, 5% là “cận trên” (số lượng tối đa có thể đạt được) cho mức độ cải thiện mà hướng đi trên có thể giúp cho hệ thống. Nếu như độ chính xác ban đầu của ứng dụng là 90% (10% lỗi), việc cải thiện chỉ làm cho hệ thống của bạn đạt được độ chính xác mới là 90.5% (9.5% lỗi, ít hơn 5% so với số lượng lỗi ban đầu). 

> In contrast, if you find that 50% of the mistakes are dogs, then you can be more confident that the proposed project will have a big impact. It could boost accuracy from 90% to 95% (a 50% relative reduction in error, from 10% down to 5%).

Ngược lại, nếu bạn nhận thấy rằng 50% lỗi là do chó bị nhầm thành mèo thì bạn có thể tự tin rằng phương án được đề xuất sẽ có tác động lớn. Nó có thể cải thiện đáng kể độ chính xác của hệ thống từ 90% lên 95% (giảm 50% tổng số lỗi, từ 10% xuống 5%). 

> This simple counting procedure of error analysis gives you a quick way to estimate the possible value of incorporating the 3rd party software for dog images. It provides a quantitative basis on which to decide whether to make this investment.

Cách phân tích lỗi đơn giản ở trên giúp bạn ước lượng nhanh hiệu quả của việc tích hợp phần mềm nhận dạng chó của bên thứ ba vào hệ thống nhận dạng mèo. Đây cũng là cơ sở định lượng để bạn lựa chọn xem có nên đi theo hướng này hay không.

> **Error analysis** can often help you figure out how promising different directions are. I’ve seen many engineers reluctant to carry out error analysis. It often feels more exciting to just jump in and implement some idea, rather than question if the idea is worth the time investment. This is a common mistake: It might result in your team spending a month only to realize afterward that it resulted in little benefit.

Việc **phân tích lỗi** thường giúp bạn nhìn thấy được triển vọng của những hướng giải quyết khác nhau. Tôi thấy nhiều kỹ sư tiến hành phân tích lỗi môt cách miễn cưỡng. Dường như đối với họ ngay lập tức thực hiện một số ý tưởng sẽ thú vị hơn là tự hỏi xem ý tưởng đó có thật sự đáng để bạn bỏ thời gian thực hiện. Đây là một lỗi phổ biến: nó có thể gây lãng phí hàng tháng chỉ để nhận ra rằng sự cải thiện là không đáng kể.

> Manually examining 100 examples does not take long. Even if you take one minute per image, you’d be done in under two hours. These two hours could save you a month of wasted effort.

Quan sát 100 mẫu để phân tích lỗi không tốn nhiều thời gian. Kể cả khi bạn bỏ ra một phút để kiểm tra từng ảnh, thời gian tổng cộng vẫn nhỏ hơn hai giờ. Nếu như ý tưởng kia không tốt, bỏ ra hai giờ phân tích lỗi này có thể giúp bạn tiết kiệm được một tháng.  

> Error Analysis refers to the process of examining dev set examples that your algorithm misclassified, so that you can understand the underlying causes of the errors. This can help you prioritize projects—as in this example—and inspire new directions, which we will discuss next. The next few chapters will also present best practices for carrying out error analyses.

Việc phân tích lỗi là quá trình kiểm tra các mẫu trong tập phát triển bị phân loại nhầm, từ đó bạn có thể hiểu được nguyên nhân.  Hiểu rõ nguyên nhân tạo ra lỗi sẽ giúp bạn nhìn ra những hướng giải quyết mới mà chúng ta sẽ thảo luận ở phần sau. Một số chương tiếp theo sẽ trình bày những "best practices" được dùng để phân tích lỗi. 
