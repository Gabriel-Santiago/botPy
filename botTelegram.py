import requests
import json
import os


class TelegramBot:

    def __init__(self):
        token = '1851770995:AAF6OGen2zPAXATtPrv5b779MrkCkxeoOzY'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    # Iniciar o bot
    def Iniciar(self):

        update_id = None
        while True:
            atualizacao = self.obter_mensagens(update_id)
            dados = atualizacao['result']

            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado['message']['text'])
                    chat_id = dado['message']['from']['id']
                    eh_primeira_mensagem = int(dado['message']['message_id']) == 1
                    resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_mensagens(self, update_id):

        link_requisicao = f'{self.url_base}getUpdates?timeout=108'

        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma reposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):

        if eh_primeira_mensagem == True or mensagem.lower() == 'lista':
            return f'''Olá, Bem vindo ao Bot Musical! 
            Escolha a opção que mais se encaixa em você
            {os.linesep}1 - Felicidade{os.linesep}2 - Tristeza{os.linesep}3 - Raiva
            {os.linesep}4 - Realizar atividade física{os.linesep}5 - Estudar / Trabalhar'''

        if mensagem == '1':
            return f'''Bora se animar ainda mais com essas playlist iiihuuuuuuuuuuu!!!!!
            {os.linesep}https://open.spotify.com/playlist/0yPwtaPEqn7mqjzkZjY5zD?si=2670491d4e914cab
            {os.linesep}https://open.spotify.com/playlist/37i9dQZF1DWUIDYTCle9M9?si=77ce222485f941c4
            {os.linesep}https://open.spotify.com/playlist/0D2ZwgWjaFexMNB7asMfr1?si=d88d1806ff794e0f'''

        elif mensagem == '2':
            return f'''Escolha uma das playlist!\nA meta é 'chô' tristeza!\nCaso não se sinta confortável, procure alguém para conversar.
            {os.linesep}https://open.spotify.com/playlist/3uYC45loQSzbizKb042Asr?si=b4b89648bd454108
            {os.linesep}https://open.spotify.com/playlist/2kfCDjiXLdwmpdHCQsuDH6?si=80fd68fab2c14baf
            {os.linesep}https://open.spotify.com/playlist/7K3MAASWVZWUDDbxp6QWdP?si=7c6882c7aeb94ad5'''

        elif mensagem == '3':
            return f'''A escolha foi feita para que você possa relaxar...\nEvite fazer coisas que exigem atenção!
            {os.linesep}https://open.spotify.com/playlist/37i9dQZF1DWTo2LqahHGYj?si=e84eac0e4b8b4d31
            {os.linesep}https://open.spotify.com/episode/5jNhsKenfGXzyadjfNnacC?si=DYiLQezsRmizD4LkrMsrhQ
            {os.linesep}https://open.spotify.com/artist/3nZ3ed6p4CKc1McTLypr6H?si=Ea4LPOxkTgOZVkIPHIS5uQ'''

        elif mensagem == '4':
            return f'''Aproveite seu momento fazendo exercícios!\nE não se esqueça do alongamento e da água!
            {os.linesep}https://open.spotify.com/artist/6AQ3Ju0aclkVXTivkO1vFG?si=cktDmFqhTP-uITZfXIB8sg
            {os.linesep}https://open.spotify.com/playlist/6Qr9v4bM1rEpqv4eTZ4nrW?si=64a4163e48c1433a
            {os.linesep}https://open.spotify.com/playlist/49QcGrGUaLZrknsDbaaG8r?si=257e75ba853b4e11'''

        elif mensagem == '5':
            return f'''Escolha uma das playlist!\nA escolha é feita para que você aproveite a música e não se distraia!
            {os.linesep}https://open.spotify.com/playlist/1OwNtZAeTU9eokrsd0Cwc6?si=d900ac483c504e4b
            {os.linesep}https://open.spotify.com/playlist/1uIbp48oZiEuY8CYT06sSR?si=c97f359241a6477e
            {os.linesep}https://open.spotify.com/artist/2wOqMjp9TyABvtHdOSOTUS?si=ScDNSG0DQ8WN0ov-mZCscA'''

        else:
            return 'Gostaria de acessar as opções novamente? Digite "lista"'

    # Responder
    def responder(self, resposta, chat_id):

        link_requisiao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisiao)


bot = TelegramBot()
bot.Iniciar()
