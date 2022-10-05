import os
import joblib
from metamaska.utils import remove_new_line, remove_whitespace, unquote

DEFAULT_LOCATION = os.path.join(os.path.dirname(__file__), 'models', 'payload_clf.joblib')


class PayloadClassifier:
    def __init__(self, payload_clf_filename=DEFAULT_LOCATION):

        if os.path.isfile(payload_clf_filename) is False:
            raise ValueError("payload clf model file doesn't exist")

        self.payload_clf = joblib.load(payload_clf_filename)
        self.classes_ = self.payload_clf.classes_

    def _transform(self, payload):
        if not payload:
            raise ValueError("payload is required.")

        payload = unquote(payload)
        payload = remove_new_line(payload)
        payload = payload.lower()
        payload = remove_whitespace(payload)

        return payload

    def predict(self, payload):
        payload = self._transform(payload)
        return self.payload_clf.predict([payload])

    def predict_proba(self, payload):
        payload = self._transform(payload)
        return self.payload_clf.predict_proba([payload])
