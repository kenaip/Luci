from random import random


class EmotionHourglass:
    """
    Returns the emotional corresponding status based on a value
    between -20 and 20.
    """
    @staticmethod
    def get_pleasantness(value):
        """
        Returns a pleasantness emotion based on inputed value.

        param : value : <int>
        returns: <str>
        """
        if value > 0:
            if 10 <= value < 20:
                return 'serenity'
            elif value >= 20:
                return 'joy'
            else:
                return 'neutral'

        elif value < 0:
            if -20 < value <= -10:
                return 'pensiveness' 
            elif value <= -20:
                return 'grief'
            else:
                return 'neutral'

        return 'neutral'

    @staticmethod
    def get_attention(value):
        """
        Returns a attention emotion based on inputed value.

        param : value : <int>
        returns: <str>
        """
        if value > 0:
            if 1 <= value < 20:
                return 'interest'
            elif value >= 20:
                return 'anticipation'
            else:
                return 'neutral'

        elif value < 0:
            if -20 < value <= -10:
                return 'distraction' 
            elif value <= -20:
                return 'amazement'
            else:
                return 'neutral'

        return 'neutral'

    @staticmethod
    def get_sensitivity(value):
        """
        Returns a sensitivity emotion based on inputed value.

        param : value : <int>
        returns: <str>
        """
        if value > 0:
            if 10 <= value < 20:
                return 'annoyance'
            elif value >= 20:
                return 'anger'
            else:
                return 'neutral'

        elif value < 0:
            if -20 < value <= -10:
                return 'apprehension' 
            elif value <= -20:
                return 'terror'
            else:
                return 'neutral'

        return 'neutral'

    @staticmethod
    def get_aptitude(value):
        """
        Returns a aptitude emotion based on inputed value.

        param : value : <int>
        returns: <str>
        """
        if value > 0:
            if 10 <= value < 20:
                return 'acceptance'
            elif value >= 20:
                return 'trust'
            else:
                return 'neutral'

        elif value < 0:
            if -20 < value <= -10:
                return 'boredom' 
            elif value <= -20:
                return 'loathing'
            else:
                return 'neutral'

        return 'neutral'


def change_humor_values(text_pol, is_offensive):
    
    pleasantness = 0
    attention = 0
    aptitude = 0.01
    sensitivity = 0

    if text_pol > 0:
        pleasantness += text_pol + random()
        attention += text_pol + random()

    elif text_pol < 0:
        pleasantness -= text_pol + random()
        attention -= text_pol + random()

    if is_offensive:
        pleasantness -= text_pol + random()
        sensitivity -= text_pol + random()

    return {
        'pleasantness': pleasantness,
        'attention': attention,
        'aptitude': aptitude,
        'sensitivity': sensitivity
    }
