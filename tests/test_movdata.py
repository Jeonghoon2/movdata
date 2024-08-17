from movdata.cli import save_movies
from movdata.get_mov_detail import load_movie_list, make_movie_info_data
from movdata.get_mov_companies import load_movie_companies
from movdata.get_list_data import ListDataSave

# 영화 목록 저장 테스트
def test_load_movie_list():

    ild = ListDataSave()

    params = {
        "openStartDt": "2015",
        "openEndDt": "2015"
    }

    ild.set.base_url("https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json")
    ild.set.params(params)
    ild.set.json_col_name('movieListResult','movieList')
    ild.set.partition(type='movies', year='2015')

    assert ild.run()
    

# 영화사 목록 저장 테스트
def test_load_company_list():
    ild = ListDataSave()
    ild.set.base_url("http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json")
    ild.set.json_col_name('companyListResult','companyList')
    ild.set.partition(type='companies')

    assert ild.run()

# 영화인 목록 저장 테스트
def test_load_people_list():
    ild = ListDataSave()
    ild.set.base_url("http://kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json")
    ild.set.json_col_name('peopleListResult','peopleList')
    ild.set.partition(type='peoples')

    assert ild.run()