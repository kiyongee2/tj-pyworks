# QR 코드 생성기
import qrcode

data = "http://giyong.info"

# QR 코드 생성
img = qrcode.make(data)

# 이미지 파일로 저장
img.save('qrcode.png')
print("QR 코드가 'qrcode.png' 파일로 저장되었습니다.")
