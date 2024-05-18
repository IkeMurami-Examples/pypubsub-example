from core import AbstractTask
from models import Data


class PlaygroundTask(AbstractTask):
    def __call__(self, message: Data):
        print('Message', self.config, message)
