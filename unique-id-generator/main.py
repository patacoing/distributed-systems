from threading import Thread, Lock
from time import sleep, time


mutex = Lock()


def sequence_thread(interval: int):
    while True:
        sleep(interval / 1000)
        print("-----resetting sequence")
        UniqueIdGenerator.reset_sequence()


class UniqueIdGenerator:
    sequence: int = 0
    PATACOING_TIMESTAMP: int = 1738967643000

    def __init__(self, datacenter_id: int, machine_id: int):
        self.datacenter_id = datacenter_id
        self.machine_id = machine_id

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

        with mutex:
            number = (
                (self.timestamp << timestamp_shift)
                | (self.datacenter_id << datacenter_id_shift)
                | (self.machine_id << machine_id_shift)
                | self.sequence
            )
            print(f"{number=}")
            self.increment_sequence()

        return number

    @classmethod
    def increment_sequence(cls, number: int = 1):
        cls.sequence += number

    @classmethod
    def reset_sequence(cls):
        with mutex:
            cls.sequence = 0

    @property
    def timestamp(self) -> int:
        return int(time() * 1000) - self.PATACOING_TIMESTAMP


if __name__ == "__main__":
    datacenter_id = 1
    machine_id = 1

    thread = Thread(target=sequence_thread, args=(100,))
    thread.start()

    unique_id_generator = UniqueIdGenerator(
        datacenter_id=datacenter_id, machine_id=machine_id
    )
    ids = set()
    for _ in range(1000000000):
        id = unique_id_generator.generate_unique_id()
        if id in ids:
            raise ValueError(f"{id=} is in ids")
        ids.add(id)

    print(f"{len(ids)=}")
