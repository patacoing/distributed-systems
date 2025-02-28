from pydantic import AnyHttpUrl

from app.services.i_hasher_service import IHasherService


class HasherService(IHasherService):
    def __init__(self):
        pass

    def hash(self, id: int) -> str:
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if id == 0:
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while id:
            id, rem = divmod(id, base)
            arr.append(alphabet[rem])
        arr.reverse()
        return "".join(arr)
