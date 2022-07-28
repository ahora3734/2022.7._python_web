#### google_images_download 패키지 설치하기
# (터미널창에) pip install git+https://github.com/Joeclinton1/google-images-download.git

# (주의) 기존 설치한 패키지가 있을 경우 pip uninstall google_images_download

from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

arguments = {"keywords":"고양이","limit":20,"print_urls":True}
paths = response.download(arguments)
print(paths)

# arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True,"format": "jpg"}   
# limit : 키워드 한 개당 100장까지 된다고 알고 있음
# print_urls : 저장되고 있는 과정에서 이미지마다 url print할건지
# format : 확장자 정해주기 (없어도 실행됨)
# downloads폴더에 저장됨