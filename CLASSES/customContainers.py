class TagClaoud:
    def __init__(self):
        self.tags = {}

    def add(self,tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0) + 1


cloud = TagClaoud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)