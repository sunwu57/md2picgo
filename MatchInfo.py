# 图片匹配信息对象
class MatchInfo:
    def __init__(self, filepath, picUrls, absolutePicUrls=None):
        # md文件路径
        self.filepath = filepath
        # 文件中所有匹配到的图片url
        self.picUrls = picUrls
        self.absolutePicUrls = absolutePicUrls if absolutePicUrls is not None else picUrls

    def toString(self):
        s="======================\n"
        s+=self.filepath+":\n"
        s+="\n".join(map(str, self.picUrls))
        return s
    def to_dict(self):
        return {
            "filepath": self.filepath,
            "picUrls": self.picUrls,
            "absolutePicUrls": self.absolutePicUrls
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["filepath"],
            data["picUrls"],
            data.get("absolutePicUrls", data["picUrls"])
        )
