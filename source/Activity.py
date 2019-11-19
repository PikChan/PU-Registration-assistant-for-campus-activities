"""
    摘要：这是一个 活动 对象。

"""


class Activity:
    def __init__(self, name="无名", bao_min_time="2019", start_time="19：00"):
        """

        :type start_time: time
        """
        self.name = name
        self.bao_min_time = bao_min_time
        self.start_time = start_time
