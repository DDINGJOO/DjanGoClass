## OOP :  SOLID
from jedi.plugins.stdlib import StaticMethodObject

class SystemMonitor:
    def load_event(self):
        """ 이벤트 로드 """
        # return 외부 -> 파일;

    def indentify_events(self):
        """도메인 이벤트로 변환 """
        # 파일 -> 파일2

    def stream_events(self):
        """도메인 이벤트로 변환 """
        # 파일2 -> 파싱 -> 전송


## OCP  개방/ 폐쇄 원칙

# 확장에대해 열려있고, 변화에대해 닫혀있어야한다.


class Event:
    raw_data : dict
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meet_condition(event_data: dict) -> bool:
        return False


class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data : dict):
        return (
                event_data["before"]["Session"] == 0
                and event_data["after"]["Session"] ==1)

class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data : dict):
        return (
                event_data["before"]["Session"] == 0
                and event_data["after"]["Session"] ==1)

class UK_event(Event):
    @staticmethod
    def meets_condition(event_data : dict):

        return (
                event_data["before"]["Session"] == 0
                and event_data["after"]["Session"] ==1)


class SystemMonitor:

    def __init__(self, event_date):
        self.event_data = event_date

    def indentify_events(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meet_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
            return UK_event(self.event_data)


# LSP
## 상속 <-
class Event:
    raw_data : dict
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meet_condition(event_data: dict) -> bool:
        return False



class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data : dict):
        return (
                event_data["before"]["Session"] == 0
                and event_data["after"]["Session"] ==1)

class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data : dict):
        return (
                event_data["before"]["Session"] == 0
                and event_data["after"]["Session"] ==1)





















