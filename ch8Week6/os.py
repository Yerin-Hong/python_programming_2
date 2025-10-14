# 내 폴더의 경로를 정확히 알고 지정하기 위한 코드
# 내 로컬 안의 사진을 불러오는 경우에 사용

import os

# 현재의 파이썬 파일이 있는 폴더 기준으로 경로 설정 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 디렉토리 지정. 내가 가진 path의 절대주소를 불러옴.
print(BASE_DIR)