import logging

import aiohttp


class BaseAPI:
    def __init__(self, base_link: str, base_token: str = ''):
        self._link = base_link
        self._token = base_token
        if self._token:
            self.headers = {'Authorization': 'Bearer', 'Accept': '*/*'}
        else:
            self.headers = { 'Accept': '*/*'}

    async def get_json(self, route: str, params: dict = None):
        params = {}
        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(url=f'{self._link}{route}', params=params, verify_ssl=False) as resp:
                    logging.info(f'{resp.status}{self._link}{route}')
                    return await resp.json()
        except aiohttp.ClientConnectionError:
            logging.warning('API is unreachable')
        except Exception as e:
            logging.warning(f'API is unreachable {e}')

    async def get_data(self, route: str, params: dict = None):
                params = {}
                try:
                    async with aiohttp.ClientSession(headers=self.headers) as session:
                        async with session.get(url=f'{self._link}{route}', params=params, verify_ssl=False) as resp:
                            logging.info(f'{resp.status}{self._link}{route}')
                            return await resp.read()
                except aiohttp.ClientConnectionError:
                    logging.warning('API is unreachable')
                except Exception as e:
                    logging.warning(f'API is unreachable {e}')











