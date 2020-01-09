

class DisplayVideo:

    def __init__(self, video):
        self.type = video.type
        self.url = video.video.url
        self.size = int(int(video.video.size) / 1000000)
        self.owner = video.owner
        self.date_uploaded = video.date_uploaded.date()
        self.name = video.name
        self.id = video.id


class DisplayDocument:

    def __init__(self, document):
        self.owner = document.owner
        self.name = document.name
        self.date_uploaded = document.date_uploaded
        self.document = document.document
        self.group = document.group
        self.private = document.private
        self.size = int(int(document.document.size) / 1000000)
        self.id = document.id




