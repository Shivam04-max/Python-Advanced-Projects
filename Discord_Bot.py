from discord import Intents, Client
import responses

def run_bot(token: str):
    """Run our Discord Bot with the token provided"""
    
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents = intents)
    knowledge: dict = responses.load_knowledge('knowledge.json')
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):

        if message.author.bot:
            return

        print(f'({message.channel}) {message.author}: {message.content}')

        response = responses.get_response(
            message.content,
            knowledge=knowledge
        )

        await message.channel.send(response)
    client.run(token=token)
        
if __name__ == '__main__':
    run_bot(token='MTUzMjI3NTUzODMwNjAwNzA5MA.G1HDDi.kNk5t0Sdc3GOBrZNz_Xa8srGPBNaRPBxy9UNO8')