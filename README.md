# age-gender-and-emotion-detect
可以同時偵測年齡、性別和表情
以深度學習模型辨識人臉資訊	
我們使用網路上預先訓練的不同模型來辨識人臉資訊，並將其經過
適當的修改，並合而為一成為我們辨識系統的主體；年齡和性別模型使
用了OpenCV 提供的人臉檢測模型擷取人臉區域，然後透過年齡和性別
檢測模型進行預測。此外，我們將年齡分為了七個區段，分別是(0-6),(8-
13),(15-20),(25-32),(38-43),(48-53),(60-100)，這樣有助於提高判別年齡的準確
性，以及更有效的分類使用者資訊。	
表情辨識利用OpenCV和Keras實現情緒分類器，透過擷取的人臉區
域，將影像進行卷積以及池化等操作，並將結果中的特徵，映射到不同
情緒的概率分佈，最終選擇概率最高的情緒作為預測結果，而情緒分類
包含了angry、disgust、scared、happy、sad、surprised、neutral，一共七
類。

![image](https://github.com/yanghenry0526/Application-of-Facial-Recognition-1225-and-KNN-in-the-E-commerce-Field/assets/73518739/96b8cf75-fb29-4eb3-a599-3babe5aa919b)
![image](https://github.com/yanghenry0526/Application-of-Facial-Recognition-1225-and-KNN-in-the-E-commerce-Field/assets/73518739/f28f1a87-fb30-4f0b-939b-7e77657b28be)


利用webdriver紀錄網路使用行為	
我們使用Selenium中的Webdriver來模擬瀏覽器，追蹤用戶在購物網
站上的瀏覽行為，包括瀏覽特定商品、類別和搜索結果等。並利用當中
元素查找的功能，可以準確找到網頁原始碼上的元素，以便進行相應的
操作。例如：在momo購物網站中，當中名為tempTcode的value元素分類
了各種商品類別。我們便可藉由讀取該值，進行商品的分類。也可以利
用當中的函式庫，進行網址改變的偵測，並採取特定的操作，如：網址
改變時紀錄當下使用者的情緒、計算網頁停留時間等，並將其與網址和
辨識之人臉資訊一併儲存至excel中。

![image](https://github.com/yanghenry0526/Application-of-Facial-Recognition-1225-and-KNN-in-the-E-commerce-Field/assets/73518739/7f93d949-f0ed-40a5-b61d-d560ffdec96a)

利用KNN推薦其他商品	
我們把人臉辨識所抓取到的資料如年齡、性別、表情、停留時間作
為資料集，並將網頁抓取的資料做簡單的分類後做為預測之目標。意即
當我們把一筆年齡、性別、表情和停留時間的資料傳入KNN模型後，
KNN根據計算會輸出一個他認為和這筆資料相近的分類結果。並以彈出
視窗的方式呈現給使用者觀看。

![image](https://github.com/yanghenry0526/Application-of-Facial-Recognition-1225-and-KNN-in-the-E-commerce-Field/assets/73518739/c7b091c2-65f5-4bcc-9c7d-260c43d30ad4)

