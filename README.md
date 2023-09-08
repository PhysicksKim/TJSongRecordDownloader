# TJ Song Record Downloader  
This script automatically downloads TJ Karaoke song recordings sent via email and saves them with a specific filename format.  
    
---  
  
# TJ 노래 녹음 다운로드 스크립트   
이메일로 받은 TJ 노래 녹음 파일을 자동으로 다운로드 해줍니다.   
  
  
### 첨부 파일 이름 저장 방식      
파일 이름은 아래와 같은 형식으로 저장됩니다.    
노래 제목에서 공백은 제거된다.  
  
```
첨부파일이름_노래제목.mp3
```
  
```
20230908180002534_22852_LoveYourself.mp3  
```
   
<br>   
   
### 동작 방식   
1. 최신순 100개 이메일을 순차적으로 탐색해서 제목이 "TJ 미디어 고품질 녹음곡을 전해드립니다." 인 이메일을 찾습니다.   
2. 제목이 "TJ 미디어 고품질 녹음곡을 전해드립니다."인 메일들을 연속으로 읽고 첨부파일을 저장한다.   
3. 제목이 "TJ 미디어 고품질 녹음곡을 전해드립니다."가 아닌 메일을 만나면 스크립트를 마무리하고 종료한다.  

