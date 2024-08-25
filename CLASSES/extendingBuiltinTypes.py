class Text(str):
    def duplicate(self):
        return self + self

# text=Text("python")

# print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")
