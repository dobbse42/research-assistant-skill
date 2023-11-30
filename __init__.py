from mycroft import MycroftSkill, intent_file_handler

import Paper

class ResearchAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.log.info("assistant has loaded")

    @intent_file_handler('assistant.research.intent')
    def handle_assistant_research(self, message):
        self.log.info("assistant has entered intent handler")
        self.speak_dialog('assistant.research')
        my_paper = Paper.Paper("1904.12956")
        self.speak(str(my_paper.arxiv_id))

    def converse(self, utterances, lang):
        if utterances and self.voc_match(utterances[0], 'wait'):
            self.speak_dialog('waiting')
            return True
        else:
            return False

# Might need this:
#    def shutdown(self):
#        pass (would be needed to close filepointers and finish any file operations).


def create_skill():
    return ResearchAssistant()

