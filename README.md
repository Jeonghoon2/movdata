# Movie Data

![LGTM](https://i.lgtm.fun/2t2c.png)

영화 진흥 위원원에서 제공하는 API를 이용하여 다양한 조건들을 적용하여 **데이터를 조작** 해보기 위한 목적

### 📖 API Ref
- [영화 진흥 위원회](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)

### 🎁 Versions
- v0.2
    - 영화 진흥 위원회에서 제공하는 [영화 목록 API](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)을 사용하여 년도별 영화 추출 후 저장
    - 이미 다운 받은 영화 데이터가 있을 경우 중복 저장 되지 않게 Skip

- v0.3 
    - 영화 진흥 위원회에서 제공하는 [영화 상세 정보 API](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)를 사용하여 저장된 저장된 영화 목록에서 movieCd를 사용하여 해당 movieCd의 상세 영화 정보를 추출 후 저장

- v0.4
    - 영화 진흥 위원회에서 제공하는 [영화사 목록 API](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)을 사용하여 년도별 영화 추출 후 저장
    - 이미 다운 받은 영화 데이터가 있을 경우 중복 저장 되지 않게 Skip