import urllib

def handle_repsonse(message) -> str:
  p_message = str(message.content).lower()
  user_message = str(message.content)
  channel = str(message.channel.name)
  commandPrefix = '!'
  
  if p_message == 'hello':
    return 'heyyyy'
    
  if p_message == f'{commandPrefix}help':
    return 'No help for you muahahahahahah'

    
  
    