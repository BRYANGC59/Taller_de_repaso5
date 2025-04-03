import email
from dataclasses import dataclass, field
from datetime import datetime, date, time
from os import system
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error

@dataclass
class Reminder:
    EMAIL: ClassVar[str] = email
    SYSTEM: ClassVar[str] = system
    date_time: datetime = datetime.now()
    type: str = EMAIL

    def __str__(self) -> str:
        return f"Reminder on {self.date_time} of type {self.type}"

@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time
    id:str = field(default_factory=generate_unique_id)
    reminders: ClassVar[list[Reminder]] = field(init=False, default=list)


    def add_reminder(self, email: str, system: str):
        new_reminder = Reminder(email, system)
        self.reminders.append(new_reminder)

    def delete_reminder(self, reminder_index: int):
        if reminder_index in self.reminders:
            self.reminders.pop(reminder_index)
        else:
            reminder_not_found_error()

    def __str__(self) -> str:
        return f"ID: {self.id}Event title: {self.title}Description: {self.description}Time: {self.start_at} - {self.end_at}"

class Day:
    def __init__(self, date_: date):
        self.date_:date = date_
        self.slots: dict[time, str | None] = {}
        self.slots._init_slots(00,00,15)

    def add_event(self, event_id: str, start_at: time, end_at: time):
        self.slots[event_id]


class Calendar:
    def __init__(self):
        self.days: dict[date, Day] = {}
        self.events: dict[str, Event] = {}

    def add_event(self, title: str, description: str, date_: date, start_at: time, and_at: time):


