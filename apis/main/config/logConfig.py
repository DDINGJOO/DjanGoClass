import logging
from datetime import datetime


# 로그 설정
logging.basicConfig(
    level=logging.INFO,  # 기본 로그 레벨 설정
    format="%(levelname)-8s - %(message)s",
    datefmt="%Y-%m-%d",
)


def log_formatter(code, name, message):
    """
    로그 메시지를 정해진 형식으로 포맷하는 함수
    """
    return f" [{name}] : {message}"


def log_message(level, name, message):
    """
    log_formatter를 사용하여 로그 메시지를 포맷한 후, 해당 level에 맞게 logging 수행
    """
    formatted_message = log_formatter(level, name, message)

    log_levels = {
        "info": logging.info,
        "error": logging.error,
        "warning": logging.warning,
        "debug": logging.debug,
        "critical": logging.critical
    }

    # 정의되지 않은 레벨이 들어오면 info로 처리
    log_func = log_levels.get(level.lower(), logging.info)
    log_func(formatted_message)


# TESTING
if __name__ == "__main__":
    log_message("info", "MainFunction", "프로그램이 시작되었습니다.")
    log_message("debug", "DataProcessor", "데이터를 처리하는 중입니다.")
    log_message("warning", "APIHandler", "API 응답이 느립니다.")
    log_message("error", "Database", "데이터베이스 연결 오류 발생.")
    log_message("critical", "System", "시스템에 치명적인 오류가 발생했습니다.")
