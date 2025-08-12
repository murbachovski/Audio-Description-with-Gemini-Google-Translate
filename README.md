# 프로젝트 제목
```
Audio-Description-with-Gemini-Google-Translate
```

# 프로젝트 설명
```
1. Audio file upload
2. Gemini description
3. translate to ko
```

# 가상환경 설정
```
conda create -n arg python=3.9
```

# API_KEY 설정
```
export GENAI_API_KEY=""
```

# 라이브러리 설치
```
pip install -r requirements.txt
```

# 앱 실행
```
./run.sh
```

# 웹 구성
<p align="center">
  <img src="https://github.com/user-attachments/assets/f0643cdf-3ee5-4a4e-b96e-290090f8ec17" width="700">
  <img src="https://github.com/user-attachments/assets/af35674b-369b-4f5f-878a-2e1378fa4202" width="700">
  <img src="https://github.com/user-attachments/assets/50032f90-d49b-450c-bd1b-b055ebca3626" width="700">
</p>

# Ngrok
(로컬 서버 => 공개 서버로 전환)
```
<Mac M1 설치 기준>
https://ngrok.com/downloads/mac-os
brew install ngrok
ngrok config add-authtoken <token>
ngrok http 80
```

# Ngrok log
<p align="center">
  <img src="https://github.com/user-attachments/assets/5ca755c3-d8f8-4088-b3b4-1b735945d351" width="700">
</p>

# Ngrok(공개 서버 접속)
[Ngrok 공개 서버 접속](https://c83c0967a9dd.ngrok-free.app/)<br>

# Ngrok 참고 문서
[위키독스](https://cordcat.tistory.com/105)<br>

# Make requirements.txt
```
pip install pipreqs
```

# pipreqs 참고 문서
[PyPI pipreqs](https://pypi.org/project/pipreqs/)<br>

# Gemini 참고 문서
[위키독스](https://wikidocs.net/254713)<br>
