import json
from datetime import datetime
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from common.loggingManeger.logConfig import log_message


T = TypeVar("T", bound=BaseModel)

class DataSerializer:
    """ 범용 직렬화/역직렬화 클래스 """

    @staticmethod
    def serialize(obj: Any) -> str:
        """
        객체를 JSON 문자열로 직렬화
        """
        try:
            return json.dumps(obj, default=DataSerializer._default_encoder, ensure_ascii=False)
        except (TypeError, ValueError) as e:
            log_message("error", f"[DataSerializer.serialize] object={obj}", f"error={e}")
            return None

    @staticmethod
    def deserialize(data: str, clazz: Type[T]) -> T | None:
        """
        JSON 문자열을 객체로 변환 (Pydantic 모델 활용)
        """
        try:
            return clazz.parse_raw(data)
        except (json.JSONDecodeError, ValueError) as e:
            log_message("error", f"[DataSerializer.deserialize] data={data},class={clazz}" , f"error={e}")
            return None

    @staticmethod
    def deserialize_object(data: dict, clazz: Type[T]) -> T:
        """
        딕셔너리를 객체로 변환
        """
        try:
            return clazz(**data)
        except (ValueError, TypeError) as e:
            log_message("error", f"[DataSerializer.deserialize_object] data={data}, class={clazz}" , f"error={e}")
            return None

    @staticmethod
    def _default_encoder(obj):
        """
        JSON 직렬화할 수 없는 객체 변환기
        """
        if isinstance(obj, datetime):
            return obj.isoformat()  # '2025-02-08T12:34:56.789'
        raise TypeError(f"Type {type(obj)} not serializable")

