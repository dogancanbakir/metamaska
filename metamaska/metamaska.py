from metamaska.payload_classifier import PayloadClassifier


class Metamaska:
    def __init__(self):
        self.payload_cls = PayloadClassifier()

    def form(self, meta):
        if not meta:
            raise ValueError("meta is required.")

        return self.payload_cls.predict(meta)[0]
