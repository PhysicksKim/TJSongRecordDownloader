import email
import imaplib
import json
import re

from email.header import decode_header
from typing import TypedDict

# imap 정보 불러오기
class ImapInfo(TypedDict):
    imap_server: str
    imap_user_id: str
    imap_user_pw: str
    imap_port: int

with open('imap_info.json', 'r') as f:
    __imap_info = json.load(f)

imap_info: ImapInfo = __imap_info

def extract_song_title(email_body):
    # 정규식을 이용하여 노래 제목 추출
    match = re.search(r'\(업소명 : .+? / 제목 : (.+?) / 가수명 : .+?\)', email_body)
    if match:
        song_title = match.group(1)
        # 공백 제거
        song_title = song_title.replace(" ", "")
        return song_title
    else:
        return None

def save_attachment_with_title(file_payload, file_name, song_title):
    # 파일 이름 가져오기
    print(f"Original file name: {file_name}")

    # 파일명에 노래 제목 추가
    file_name_without_extension, file_extension = file_name.rsplit('.', 1)
    new_file_name = f"{file_name_without_extension}_{song_title}.{file_extension}"
    print(f"New file name: {new_file_name}")

    # 파일 저장
    with open(new_file_name, "wb") as f:
        f.write(file_payload)


def print_email_text(part):
    content_type = part.get_content_type()
    if content_type == "text/html":
        print(part.get_payload(decode=True).decode())


# IMAP 서버에 연결
URL = imap_info["imap_server"]
session = imaplib.IMAP4_SSL(URL)

# 로그인 정보
username = imap_info["imap_user_id"]
password = imap_info["imap_user_pw"]

# 로그인
session.login(username, password)

# INBOX 선택
session.select("inbox")

# 모든 메일의 ID를 검색
status, messages = session.search(None, "ALL")

# 검색 결과에서 메일 ID 목록을 가져옴
mail_ids = messages[0].split()

# 최근 n개의 메일 ID 선택 (여기서는 5개)
last_n_ids = mail_ids[-2:]

# 선택한 메일 ID를 이용하여 각 메일의 내용을 가져옴
for mail_id in last_n_ids:
    status, msg_data = session.fetch(mail_id, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    # 이메일이 여러 부분으로 구성되어 있는 경우
    if msg.is_multipart():
        # 변수 확보
        file_name = ""
        file_payload = ""
        song_title = ""

        # 모든 부분을 순회
        for part in msg.walk():
            # 이메일 본문인 경우
            if part.get_content_type() == "text/html":
                # 노래 제목 추출
                email_body = part.get_payload(decode=True).decode()
                song_title = extract_song_title(email_body)

            # 첨부 파일인 경우
            elif part.get_content_disposition() == "attachment":
                # 파일 제목 추출
                file_name = part.get_filename()
                print(file_name)

                # 파일 내용 추출
                file_payload = part.get_payload(decode=True)

        # 첨부 파일 다운로드
        save_attachment_with_title(file_payload, file_name, song_title)

    else:
        pass

# 로그아웃
session.logout()
