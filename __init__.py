from mycroft import MycroftSkill, intent_file_handler


class Radioplayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('radioplayer.intent')
    def handle_radioplayer(self, message):
        self.speak_dialog('radioplayer')


def create_skill():
    return Radioplayer()

