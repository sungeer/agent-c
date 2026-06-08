from langchain_core.messages import BaseMessage, SystemMessage


class ShortTerm:
    """保存对话历史，控制上限，防止超过 token 限制。
    system 消息永远保留，超出上限时删除最旧的非 system 消息。
    """

    def __init__(self, max_messages: int = 20) -> None:
        self.max_messages = max_messages
        self._messages: list[BaseMessage] = []

    def add(self, message: BaseMessage) -> None:
        self._messages.append(message)
        self._trim()

    def _trim(self) -> None:
        """超过上限时，删除最旧的非 system 消息。"""
        non_system_count = sum(1 for m in self._messages if not isinstance(m, SystemMessage))
        if non_system_count <= self.max_messages:
            return
        for i, msg in enumerate(self._messages):
            if not isinstance(msg, SystemMessage):
                self._messages.pop(i)
                return

    def get_messages(self) -> list[BaseMessage]:
        return list(self._messages)

    def clear(self) -> None:
        """清空全部历史（开始新对话时使用）。"""
        self._messages = []
