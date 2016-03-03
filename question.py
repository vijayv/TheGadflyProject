class Question:
    """ Understands: question generated by vandalizer algorithm
    """
    def __init__(self, source_sentence, question, answer, question_type):
        self.source_sentence = source_sentence
        self.question = question
        self.answer = answer
        self._type = question_type