from utils.logger import log

from redis import Redis, ResponseError


import json
import sys
import os

logges = log(system_handeler=sys.stdout, file_handler="monitor/redish.log")


class RedishAbstration:
    """Redish abstration class"""

    def __init__(self) -> None:
        self.client = Redis(host=os.getenv(
            "LOCALHOST"), port=os.getenv("PORT"), decode_responses=True)

    def post_data(self, user_data: str, ai_data: str) -> None:
        schema = {
            "user_messgae": user_data,
            "ai_message": ai_data
        }
        try:
            data = json.dumps(schema).encode("utf-8")
            self.client.set(name="defult", value=data)
            logges.info("data has been store sucessfully")
        except ResponseError as error:
            logges.exception(
                f"redish data base exception occureed:{str(error)}")
        finally:
            self.client.close()

    def get_data(self):
        try:
            _data = self.client.get(name="defult")
            parsed_Data = json.load(_data)
            logges.info("data parsed sucessfully from the database")
            return parsed_Data
        except ResponseError as error:
            raise RuntimeError(str(error))
        finally:
            self.client.close()

    def delete_object(self):
        try:
            self.client.delete("defult")
            logges.info("db key deleted succesfully")
        except ResponseError as error:
            logges.exception(f"an exception occured{str(error)}")
            raise RuntimeError(str(error))
        finally:
            self.client.close()
