# Некое подобие скрипта, который работает с базой данных
# Пока что база данных - это списки

from dataclasses import dataclass
from datetime import date, datetime
from typing import List


@dataclass
class Record:
    record_id: int
    date: datetime
    is_recorded: bool
    patient_id: int

@dataclass
class Patient:
    patient_id: int
    first_name: str
    middle_name: str
    second_name: str
    birthday: date

# импровизированная база данных
records: List[Record] = []
patients: List[Patient] = []

# сделать запись в бд
def set_patient(p: Patient) -> None:
    p.patient_id = len(patients)
    patients.append(p)

def set_record(r: Record) -> None:
    r.record_id = len(records)
    records.append(record)

# запрос из бд
def get_patient(id: int) -> Patient:
    return patients[id]

def get_record(id:int) -> Record:
    return records[id]
