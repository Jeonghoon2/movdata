import requests
import os
import json
import time
from tqdm import tqdm

class ListDataSave:

    def __init__(self) -> None:
        
        """ 초기 데이터 셋팅 """
        self.read_url : str = f"" # request에 읽어 들일 URL
        self.write_path : str = os.path.expanduser('~/mov/datas') # 읽어들인 모든 데이터를 저장할 경로
        self.per_page : int = 10 # 페이지당 읽어 들일 개수
        self.cur_page : int = 1 # 읽어들일 현재 페이지 번호
        self.req_intervar : int = 1 # request를 읽어 들일 인터벌
        self.params: dict = {} # URL에 추가할 params
        self.partition_cols = {} # wirte할 때 경로에 추가할 파티션

        self.item_result, self.item_list = None, None # Json Key

        # 하위 Class
        self.set = self.set(self)
        self.get = self.get(self)

    def run(self):
        # total 페이지 개수 구하기
        tot_cnt = self.read_data()[self.item_result]['totCnt']
        total_page = (tot_cnt // self.per_page) + 1

        # # 모든 데이터 호출
        all_data = []

        for page in tqdm(range(1, total_page + 1)):
            self.cur_page = page
            all_data.extend(self.read_data()[self.item_result][self.item_list])
            time.sleep(self.req_intervar) 

        self.save_data(all_data)

        return True


    """ 메인 Function """
    def read_data(self) -> json:
        param_str = f"&page={self.cur_page}"

        for key, value in self.params.items():
            param_str += f"&{key}={value}"

        response = requests.get(f"{self.read_url}{param_str}")

        return response.json()

    def save_data(self, data):
        # 데이터 저장 로직
        self.change_write_path()

        write_path = str(self.write_path) + "/data.json"

        os.makedirs(os.path.dirname(write_path), exist_ok=True)

        with open(write_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        

    """ 서브 Function """
    def get_home_path():
        user_path = os.path.expanduser('~/')
        return os.path.join(user_path,'mov','data')


    def change_url(self):
        for k,v in self.params.items():
                self.read_url += f"&{k}={v}"

    def change_write_path(self):
        # 저장 경로 변경 로직
        path_components = [self.write_path]
        for key, value in self.partition_cols.items():
            path_components.append(f"{key}={value}")
        self.write_path = os.path.join(*path_components)


    """ Sub Class"""
    class get:
        
        def __init__(self, outer) -> None:
            self.outer = outer

        def url(self):
            return self.outer.read_url
        
        def write_path(self):
            return self.outer.write_path
        

    class set:

        def __init__(self, outer) -> None:
            self.outer = outer

        def base_url(self, url : str):
            self.outer.read_url = f"{url}?key={os.getenv('MOVIE_API_KEY')}"
            return self.outer.read_url

        def params(self, new_params: dict):
            self.outer.params = new_params
            return self.outer.read_url
        
        def partition(self, **cols):
            self.outer.partition_cols.update(cols)

        def per_page(self, new_per_page: int):
            self.outer.per_page = new_per_page
            return self.outer.per_page
        
        def req_interval(self, new_interval):
            self.outer.req_intervar = new_interval
            return self.outer.req_intervar
        
        def json_col_name(self, item_result_name : str, item_list_name : str):
            self.outer.item_result, self.outer.item_list = item_result_name, item_list_name
            return self.outer.item_result, self.outer.item_list