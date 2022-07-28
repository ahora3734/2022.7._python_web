# (터미널에)"pip install bs4"로 beautifulsoup 라이브러리 설치
# (터미널) "pip install requests"

from bs4 import BeautifulSoup #beautifulsoup을 불러옴 그럼 아래에서는 포함된 기능을 사용할 수 있음
from urllib.request import urlopen #urllib.request라는 곳에서 urlopen 기능을 가져와 아래에서 사용하겠다.

with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#주소를 열어서 response에 담겠다.
# response = urlopen('https://en.wikipedia.org/wiki/Main_Page') #과 동일


    soup = BeautifulSoup(response, 'html.parser') 
#위에서 담은 response를 가져와서 html.parser로 분석해서 soup에 담는다.

    for anchor in soup.find_all('a'): #soup중에 find_all('a') 모든 a태그를 찾아서 anchor에 담는다.
        print(anchor.get('href', '/')) #anchor에서 href(주소)를 get해서 출력
        