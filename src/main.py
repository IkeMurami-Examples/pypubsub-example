from playground_task import PlaygroundTask
from _tasks import Task
from core import SendTaskMessage
from models import Data

# Register all tasks
tasks = [
    PlaygroundTask(Task.TEST),
]

if __name__ == '__main__':
    # Send some message
    SendTaskMessage(Task.TEST, Data(some='test'))
