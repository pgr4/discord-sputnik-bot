def codeblock(str) -> str:
    return f'```{str}```'

async def send_in_codeblock(command, str):
    await command.channel.send(codeblock(str))
    
def clean_command(command) -> str:
    return command.message.content.replace(command.prefix + command.invoked_with, '').strip()
