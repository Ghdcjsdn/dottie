from pydub import AudioSegment
import os

# 변환할 파일 리스트
files = [
    "/Users/hongcheonu/Desktop/개웃겨서도티낳음/짜잇호.m4a",
    "/Users/hongcheonu/Desktop/개웃겨서도티낳음/호잇짜.m4a",
]

for file_path in files:
    # 파일 이름과 폴더
    folder, file_name = os.path.split(file_path)
    name, ext = os.path.splitext(file_name)
    
    # 출력 파일 경로
    out_path = os.path.join(folder, f"{name}.mp3")
    
    # M4A 불러오기
    audio = AudioSegment.from_file(file_path, format="m4a")
    
    # WAV로 내보내기
    audio.export(out_path, format="mp3")
    print(f"변환 완료: {out_path}")
