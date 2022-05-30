from urllib.error import HTTPError
from zipfile import ZipFile
from jp_prefecture import jp_prefectures as jp

class DatasetError(BaseException):
    pass

class CNScrapper(object):

    _BASE_URL = 'https://www.houjin-bangou.nta.go.jp/download'
    _INDEX_URL = f'{_BASE_URL}/zenken/'
    _DOWNLOAD_URL = f'{_BASE_URL}/zenken/index.html'
    _TOKEN_KEY = ( 'jp.go.nta.houjin_bangou.framework.web.common'
                   '.CNSFWTokenProcessor.request.token' )
    _CSV_UNICODE_TABLE_XPATH = '//*[@id="appForm"]/div[2]/div[2]/table/tbody'
    _ATTACHFILE_PREFIX="attachment; filename*=utf-8'jp'"

    def __init__(self, user_agent=None):
        from requests_html import HTMLSession

        self.session = HTMLSession()
        user_agent and self.ssessions.headers.update({'user-agent': user_agent})
        self.response = self.session.get(self._INDEX_URL)
        self.response.html.render(timeout=0, sleep=10)
        self.fileids = self.gathering_fileids(self.response.html)
        self.token = self.response.html.find(f'input[name="{self._TOKEN_KEY}"]',
                                             first=True)
        try:
            self.post_form = {
               f'{self._TOKEN_KEY}': f'{self.token.attrs["value"]}',
               "event" : 'download',
            }
        except AttributeError:
            raise DatasetError('Could not get token') from None

    def gathering_fileids(self, html):
        fileid_cache = dict()
        htmltable =  html.xpath(self._CSV_UNICODE_TABLE_XPATH, first=True)
        if htmltable is not None:
            atags = htmltable.find('a')
        else:
            atags = []
        for entry in atags:
            for e in entry.element.iterancestors():
                if e.tag == 'dl':
                    dt = e.find('dt')
                    if dt is not None:
                       for ee in e.iterdescendants():
                            if ee is not None and ee.tag == 'a':
                                fileid = ( ee.get('onclick')
                                           .replace('return doDownload(','')
                                           .replace(');', ''))
                                fileid_cache[dt.text] = fileid
        return fileid_cache

    def _get_filename(self, headers):
            try:
                c = headers['Content-Disposition']
                filename =c.replace(self._ATTACHFILE_PREFIX, '')
            except:
                filename = None
            return filenamee

    def download(self, prefecture='all'):
        prefecture = self.name_normalized(prefecture)
        try:
            assert id in self.fileids.keys()
            self.post_form['selDlFileNo'] = f'{id}'
            response = self.session.post( url=self._DOWNLOAD_URL,
                                          data=self.post_from)

        except AssertionError:
            raise DatasetError('id not available') from None

        except HTTPError as err:
            raise DatasetError(err)

        print(response.headers)
        self.filename = self._get_filename(response.headers)
        with open(self.filename, 'wb') as save:
                save.write(response.content)
        return self.filename

    def extract_data(self, filepath):
        with ZipFile(filepath, 'r') as zipobj:
            for innerfile in zipobj.namelist():
                if innerfile.endswith('csv'):
                    csvfile = zipobj.extract(innerfile)
            else:
                csvfile = None
        return csvfile

    def name_normalized(self, name):
        name = jp.alphabet2name(name)
        name = name or name in ['全国', 'all', 'All'] and '全国'
        name = name or name in ['国外', 'outside', 'Outside'] and '国外'
        return name

    def get_fileids(self):
         alphabet_names =  jp.name2alphabet([id for id in self.fileids.keys()])
         alphabet_names[0] = 'All'
         alphabet_names[-1] = 'OutSide'
         return alphabet_names


corporate_numbers = CNScrapper()
