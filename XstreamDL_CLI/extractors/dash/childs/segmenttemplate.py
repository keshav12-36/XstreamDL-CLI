from ..mpditem import MPDItem


class SegmentTemplate(MPDItem):
    '''
    SegmentTemplate没有duration的话 timescale好像没什么用
    '''
    def __init__(self, name: str):
        super(SegmentTemplate, self).__init__(name)
        self.timescale = None # type: int
        self.duration = None # type: int
        self.presentationTimeOffset = None # type: int
        self.initialization = None # type: str
        self.media = None # type: str
        self.startNumber = None # type: int

    def generate(self):
        if self.presentationTimeOffset is None:
            self.presentationTimeOffset = 0
        if self.startNumber is None:
            self.startNumber = 1
        self.to_int()

    def to_int(self):
        self.timescale = int(self.timescale)
        self.duration = int(self.duration)
        self.presentationTimeOffset = int(self.presentationTimeOffset)
        self.startNumber = int(self.startNumber)

    def get_initialization(self) -> str:
        return self.initialization.replace('..', '')

    def get_media(self) -> str:
        return self.media.replace('..', '')