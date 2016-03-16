class Lesson:
    """
    Class to represent a Lesson
    """
    def __init__(self, ID, topic, module, content):
        self.lesson_ID = ID
        self.topic = topic
        self.module = module
        self.content = content

    def view_lesson():
        pass

    def is_available():
        pass

    def __str__(self):
        """
        For testing purposes
        """
        # return "{}, {}: {} paragraphs".format(self.content.title, self.module,
        #                                       len(self.content.paragraphs))
        title = "{}, {}, {}".format(self.content.title, self.topic, self.module)
        o = title + "\n"
        o += "-" * len(title) + "\n"
        o += self.content.introduction + "\n"
        for i in self.content.paragraphs:
            o += i.body + "\n"
            o += "[Image: {}, Link: {}]".format(i.image, i.link)
            o += "\n\n"
        o += self.content.summary + "\n"
        return o


class Content:
    def __init__(self, title, introduction, paragraphs, summary):
        self.title = title
        self.introduction = introduction
        self.paragraphs = paragraphs
        self.summary = summary


class Paragraph:
    def __init__(self, body, image=None, link=None):
        """
        A class to represent a paragraph with an optional image and link
        """
        self.body = body
        self.image = image
        self.link = link
