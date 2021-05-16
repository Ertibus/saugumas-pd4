class Utilities:
    @classmethod
    def clear_layout(cls, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                cls.clear_layout(child.layout())
