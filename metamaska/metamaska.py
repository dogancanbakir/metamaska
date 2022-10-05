from metamaska.payload_classifier import PayloadClassifier


class Metamaska:
    def __init__(self):
        self.payload_cls = PayloadClassifier()

    def form(self, meta, probability=False):
        if not meta:
            raise ValueError("meta is required.")

        if probability:
            y_pred_prob = self.payload_cls.predict_proba(meta)
            index = y_pred_prob.argmax(1).item()
            return (self.payload_cls.classes_[index], y_pred_prob[0, index])
        return self.payload_cls.predict(meta)[0]
