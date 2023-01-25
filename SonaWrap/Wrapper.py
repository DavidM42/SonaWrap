import requests
import shutil
from pprint import pprint

#TODO package with top level here for import
from SonaWrap.schemas.Schedule import ScheduleSchema
from SonaWrap.schemas.MainMenuInfo import MainMenuInfoSchema
from SonaWrap.schemas.StudyPage import StudyPageSchema
from SonaWrap.schemas.StudyInfo import StudyInfoSchema

from SonaWrap.SonaApiError import SonaApiError

class SonaWrap:
    def __init__(self, token:str=None, username:str = None, password:str = None, base_host:str="https://psywue.sona-systems.com"):
        self._host = base_host
        self._token = token if token else self._authenticate(username,password)
        print("Initialized SonaWrap with token "+ self._token)

    def get_token(self):
        return self._token

    def _request_invalidator(self, r):
        if r.status_code != 200 or r.json()["ErrorCode"] != 0:
            print(r.text)
            print(r.json()["Errors"])
            print(r.json())
            #TODO own exception here
            raise SonaApiError("Request to SoNA api failed", r.json())
        return r.json()["Result"]

    def test_connection(self):
        #TODO export cause unused
        url = self._host + "/services/SonaMobileAPI.svc/TestConnection"
        r = requests.post(url)
        # r_json = r.json()

        # print(r.text)
        #TODO schema
        #TODO better way to invalidate errored
        r = self._request_invalidator(r)
        return r
        #TODO return type

    def _login_page(self):
        #TODO export cause unused
        url = self._host + "/services/SonaMobileAPI.svc/GetLoginPageInfoV2"
        r = requests.post(url)
        r = self._request_invalidator(r)
        #TODO schema
        # print(r.text)
        return r
        #TODO return type


    def custom_icon(self):
        url = self._host + "/custom/customlogo.png"

        r = requests.get(url,stream=True)
        # print(r.status_code)
        with open('logo.png', 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
        del r
        #TODO return image here as object instead of saving at all

    def _authenticate(self, username:str, password:str) -> str: #TODO return type token given here
        # r_login_page = self._login_page()

        url = self._host + "/services/SonaMobileAPI.svc/AuthenticateV2"

        body = {
            "p_username": username,
            "p_password": password,
            "p_language_pref":"DE",
            "p_mobile_version":"2.8.8"
        }

        print("Authenticasting")
        r = requests.post(url, json=body)

        #TODO own authorize exception
        token = self._request_invalidator(r)['sona_auth']

        # print(r.text)
        return token

    #TODO nextLogin Page request but no useful info in capture

    def my_schedule(self):
        url = self._host + "/services/SonaMobileAPI.svc/GetMyScheduleInfo"

        body = {
            "p_sessionToken": self._token
        }

        r = requests.post(url, json=body)
        result = self._request_invalidator(r)

        schema = ScheduleSchema()
        resultObj = schema.load(result)

        return resultObj


    def main_menu_info(self):
        url = self._host + "/services/SonaMobileAPI.svc/GetMainMenuInfo"

        body = {
            "p_sessionToken": self._token
        }

        r = requests.post(url, json=body)
        result = self._request_invalidator(r)

        schema = MainMenuInfoSchema()
        resultObj = schema.load(result)

        return resultObj


    def study_page_info(self) -> StudyPageSchema:
        url = self._host + "/services/SonaMobileAPI.svc/GetStudiesPageInfo"

        body = {
            "p_sessionToken": self._token
        }

        r = requests.post(url, json=body)
        result = self._request_invalidator(r)

        schema = StudyPageSchema()
        resultObj = schema.load(result)

        return resultObj

    def study_info(self, experiment_id:int) -> StudyInfoSchema:
        url = self._host + "/services/SonaMobileAPI.svc/GetStudyInfo"

        body = {
            "p_sessionToken": self._token,
            "p_experiment_id": experiment_id
        }

        r = requests.post(url, json=body)
        result = self._request_invalidator(r)

        schema = StudyInfoSchema()
        resultObj = schema.load(result)

        return resultObj