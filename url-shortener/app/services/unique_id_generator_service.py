from random import randint
from fastapi import Depends
from threading import Thread, Lock
from time import sleep, time

from app.services.i_unique_id_generator import IUniqueIdGenerator
from app.config.settings import LocationSettings, get_location_settings


class UniqueIdGeneratorService(IUniqueIdGenerator):
    sequence: int = 0
    PATACOING_TIMESTAMP: int = 1738967643000
    mutex = Lock()

    def __init__(
        self, location_settings: LocationSettings = Depends(get_location_settings)
    ):
        self.datacenter_id = location_settings.datacenter_id
        self.machine_id = location_settings.machine_id

        thread = Thread(target=UniqueIdGeneratorService.sequence_thread, args=(100,))
        thread.start()

    @staticmethod
    def sequence_thread(interval: int):
        while True:
            sleep(interval / 1000)
            UniqueIdGeneratorService.reset_sequence()

    def generate_unique_id(self) -> int:
        if self.timestamp.bit_length() > 41:
            raise ValueError("Timestamp value is too high")

        if self.datacenter_id.bit_length() > 5:
            raise ValueError("Datacenter id value is too high")

        if self.machine_id.bit_length() > 5:
            raise ValueError("Machine id value is too high")

        machine_id_shift = 12
        datacenter_id_shift = machine_id_shift + 5
        timestamp_shift = datacenter_id_shift + 5

        with self.mutex:
            number = (
                (self.timestamp << timestamp_shift)
                | (self.datacenter_id << datacenter_id_shift)
                | (self.machine_id << machine_id_shift)
                | self.sequence
            )
            self.increment_sequence()

        return number

    @classmethod
    def increment_sequence(cls, number: int = 1):
        cls.sequence += number

    @classmethod
    def reset_sequence(cls):
        with cls.mutex:
            cls.sequence = 0

    @property
    def timestamp(self) -> int:
        return int(time() * 1000) - self.PATACOING_TIMESTAMP
