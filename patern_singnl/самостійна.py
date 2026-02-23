from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def send(self) -> None:
        pass


class EmailMessage(Message):
    def send(self) -> None:
        print("Sending Email message...")


class SMSMessage(Message):
    def send(self) -> None:
        print("Sending SMS message...")


class PushMessage(Message):
    def send(self) -> None:
        print("Sending Push notification...")




class MessageFactory:
    @staticmethod
    def create_message(message_type: str) -> Message:
        mt = message_type.strip().lower()

        if mt == "email":
            return EmailMessage()
        if mt == "sms":
            return SMSMessage()
        if mt == "push":
            return PushMessage()

        raise ValueError(f"Unknown message_type: {message_type}")