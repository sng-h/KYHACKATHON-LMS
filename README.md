git clone [GitHub 저장소 주소]
cd KYHACKATHON_project

# 1. 가상 환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate

# 2. 필요한 라이브러리 설치
pip install -r requirements.txt

# 3. 서버 실행
python3 manage.py runserver
