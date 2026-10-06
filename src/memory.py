class ShortTerm:
    """短期记忆
    保存对话历史
    """

    def __init__(self):
        self._messages = []

    def add(self, message) -> None:
        self._messages.append(message)

    def get_messages(self):
        return list(self._messages)

    def clear(self) -> None:
        """清空全部历史
        开始新对话时使用
        """
        self._messages = []
