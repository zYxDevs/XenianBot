from telegram import Bot, User

from . import MWT

__all__ = ['get_self', 'get_user_link', 'get_option_from_string']


@MWT(timeout=60 * 60)
def get_self(bot: Bot) -> User:
    """Get User object of this bot

    Args:
        bot (:obj:`Bot`): Telegram Api Bot Object

    Returns:
        :obj:`User`: The user object of this bot
    """
    return bot.get_me()


def get_user_link(user: User) -> str:
    """Get the link to a user

    Either the @Username or [First Name](tg://user?id=123456)

    Args:
        user (:obj:`telegram.user.User`): A Telegram User Object

    Returns:
        :obj:`str`: The link to a user
    """
    if user.username:
        return '@{}'.format(user.username)
    else:
        return '[{}](tg://user?id={})'.format(user.first_name, user.id)


def get_option_from_string(option_short: str, string: str) -> tuple:
    """Extract option from a string

    Examples:
        >>> string = 'This is some user message -echo_it Yes'
        >>> result = get_option_from_string('echo_it', string)
        >>> print(result)
        >>> # ('Yes', 'This is some user message')

        >>> string = 'This is some user message'
        >>> result = get_option_from_string('echo_it', string)
        >>> print(result)
        >>> # (None, None)

    Args:
        option_short (:obj:`str`): The name of the option
        string (:obj:`str`): Whole string from where to extract from

    Returns:
        :obj:`tuple`: A Tuple of the found option and the string without the option or a tuple of two None's
    """
    splitted_text = string.split(' ')
    option_short = option_short if option_short.startswith('-') else '-' + option_short
    if option_short in splitted_text:
        in_list_position = splitted_text.index(option_short)
        if len(splitted_text) > in_list_position + 1:
            option = splitted_text[in_list_position + 1]
            for index in range(2):
                del splitted_text[in_list_position]
            string = ' '.join(splitted_text)
            return option, string
    return None, None
