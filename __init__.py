from mycroft import MycroftSkill, intent_file_handler


class ResearchAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.research.intent')
    def handle_assistant_research(self, message):
        self.speak_dialog('assistant.research')


def create_skill():
    return ResearchAssistant()

