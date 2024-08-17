# Movie Data

![LGTM](https://i.lgtm.fun/2t2c.png)

영화 진흥 위원원에서 제공하는 API를 이용하여 다양한 조건들을 적용하여 **데이터를 조작** 해보기 위한 목적

### 📖 API Ref
- [영화 진흥 위원회](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)

### 🔥 Usage
- **import**

    ```
    from movdata.get_list_data import ListDataSave
    ```

- **get_list_data**

    **Example : 영화 목록**

    ```python
    ild = ListDataSave()

    params = {
        "openStartDt": "2015",
        "openEndDt": "2015"
    }

    ild.set.base_url("https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json")
    ild.set.params(params)
    ild.set.json_col_name('movieListResult','movieList')
    ild.set.partition(type='movies', year='2015')

    ild.run()
    ```

    **Example : 영화사 목록**
    ```python
    ild = ListDataSave()
    ild.set.base_url("http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json")
    ild.set.json_col_name('companyListResult','companyList')
    ild.set.partition(type='companies')

    ild.run()
    ```
    영화인 목록을 추출도 영화사 목록과 동일한 방법으로 가능

- get_list_data Result 

    <img width="226" alt="image" src="https://github.com/user-attachments/assets/8f12d468-74f3-470a-baa7-620a598bba0d">

### 🎁 Versions
- v0.2
    - 영화 진흥 위원회에서 제공하는 [영화 목록 API](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)을 사용하여 년도별 영화 추출 후 저장
    - 이미 다운 받은 영화 데이터가 있을 경우 중복 저장 되지 않게 Skip

- v0.3 
    - 영화 진흥 위원회에서 제공하는 [영화 상세 정보 API](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)를 사용하여 저장된 저장된 영화 목록에서 movieCd를 사용하여 해당 movieCd의 상세 영화 정보를 추출 후 저장

- v0.4
    - 영화 진흥 위원회에서 제공하는 [영화사 목록 API](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)을 사용하여 년도별 영화 추출 후 저장
    - 이미 다운 받은 영화 데이터가 있을 경우 중복 저장 되지 않게 Skip

- v0.5
    - 아이템 목록을 저장하는 기능의 코드들의 다들 각각 분리되어 같은 동작을 여러 코드에서 실행되는 중복 제거
    - set 함수를 통해 필수 데이터를 직접 입력 받도록 함수 구현 
    - get_list_data의 가능한 API 참조 사이트[[영화 목록 API](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do), [영화사 목록 API](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do), [영화인 목록 API](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)]