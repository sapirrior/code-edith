from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

# Minimalist Style: Just Orangex for the symbol
style = Style.from_dict({
    'symbol': '#d97757',
    '': '#a0a0a0'
})

def get_input():
    # The symbol is 3 characters: ">", ">", " "
    message = [('class:symbol', '>> ')]

    # Continuation creates the indent for wrapped lines (3 spaces)
    def continuation(width, line_number, is_soft_wrap):
        return [('class:symbol', '   ')]

    return prompt(
        message,
        style=style,
        prompt_continuation=continuation,
        wrap_lines=True
    ).strip()