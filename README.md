# TJ Song Record Downloader / TJ 노래 녹음 다운로더
This python script automatically downloads TJ Karaoke song recordings sent via email and saves them with a specific filename format.  

<br><br>  
  
# 개요  
이메일로 받은 TJ 노래 녹음 파일 다운로드를 자동화 해줍니다.     
  
![image](https://github.com/PhysicksKim/TJSongRecordDownloader/assets/101965836/0fdc569b-d25b-4693-a575-e3350acf4174)    
   
<br>  
  
### 불편사항  
TJ 노래 녹음 파일을 이메일로 전송시, 위와 같이 메일 하나에 파일 하나씩 전송됩니다.  
  
### 매크로 기능   
1. 여러 메일로 나눠 전송된 노래 녹음 파일을 자동으로 다운로드 해줍니다.         
2. 파일명에 노래 제목을 덧붙이도록 해줍니다. (파일 제목 포맷팅)    
    
### 파일 제목 포맷팅          
파일 이름은 아래와 같은 형식으로 저장됩니다.    
노래 제목에서 공백은 제거됩니다.  
  
```
첨부파일이름_노래제목.mp3
```
  
```
20230908180002534_22852_LoveYourself.mp3  
```
   
<br>   
  
# How to Run  
  
## 주의사항  
- 네이버 메일만 지원합니다.  
- 메일 시스템이 추가 인증을 요구하는 경우는 지원하지 않습니다.  
- 최신순 30개 메일 내에 제목이 "TJ 미디어 고품질 녹음곡을 전해드립니다." 인 메일의 
  
<br>  
  
## 실행 방법  
0. python 3.8 이상 버전을 필요로 합니다.  
1. main.py 파일을 다운로드 합니다.  
2. 동일한 폴더에 imap_info.json 파일을 생성하고 아래와 같이 json 데이터를 적습니다.    
```json
{
  "imap_server": "imap.naver.com",
  "imap_user_id": "네이버이메일주소",
  "imap_user_pw": "네이버비밀번호",
  "imap_port": 993
}
```
3. python 실행 환경(IDE, 명령 프롬프트 등)에서 main.py 파일을 실행합니다.  
  
<br>  
   
## 매크로 동작 방식   
1. 최신순 30개 이메일을 읽습니다.   
2. 제목이 "TJ 미디어 고품질 녹음곡을 전해드립니다."인 메일을 읽고 첨부파일을 저장한다.   
   
