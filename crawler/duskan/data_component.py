class DataComponent:
    pass


class ChosunData(DataComponent):
    def __init__(self, **kwargs):
        title = kwargs["title"] if "title" in kwargs else ""
        content = kwargs["content"] if "content" in kwargs else ""
        category = kwargs["category"] if "category" in kwargs else ""
        date = kwargs["date"] if "date" in kwargs else ""
        url = kwargs["url"] if "url" in kwargs else ""
        id = "noid"
        if not url == "":
            id = url.split("/")[-1].split(".")[0]

        
        self.contents={
            "id": id,
            "url": url,
            "title": title,
            "content": content,
            "date": date,
            "category": category,
        }

    def export_to_str(self):
        order_content = ["id", "url", "title", "date", "category", "date"]
        export_text = ""
        export_format = "{}: {}".format
        for key in order_content:
            text = export_format(key, self.contents[key])
            export_text += text

        return export_text
        
