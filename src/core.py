from abc import ABC, abstractmethod
from pubsub import pub, core
import pydantic
import pydantic_settings
import typing


class AbstractTask(core.listener.UserListener, ABC):
    config: pydantic_settings.BaseSettings
 
    def __init__(self, *topicNames: typing.Sequence[str], config: pydantic_settings.BaseSettings | None = None) -> None:
        self.config = config

        for topic in topicNames:
            pub.subscribe(self, topic)

    @abstractmethod
    def __call__(self, message: pydantic.BaseModel):
        ...


class SendTaskMessage(object):
    def __init__(self, topicName: str, message: pydantic.BaseModel) -> None:
        pub.sendMessage(topicName, message=message)
