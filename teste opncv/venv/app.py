from flask import Flask, render_template, redirect, request, jsonify
from supabase import create_client, Client
from datetime import datetime
import base64

app = Flask(__name__)

url = 'https://vrpiaeclyujvozcbahqb.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZycGlhZWNseXVqdm96Y2JhaHFiIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NzIyNDk1NSwiZXhwIjoyMDAyODAwOTU1fQ.PCtf2Ps69fvjW4frFHG7STKU-F6LGw7Engg8_fOki0A'
client: Client = create_client(url, key)

#declaração do banco  no supabase
bancoImagem = 'saveImagem'

@app.route('/')
def index():
    # Renderiza o template 'index.html' na página inicial
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def receber():
    # Obtém os dados enviados na solicitação POST
    data = request.get_json()
    image = data['image']
    
    # Decodifica a imagem a partir da base64
    img_by = base64.b64decode(image)
    
    # Define um novo nome para a imagem usando a data e hora atual
    novoNome = datetime.now().strftime("%Y-%m-%d  %H:%M:%S") #importação data da imagem
    
    # Faz o upload da imagem para o banco de dados Supabase
    client.storage.from_(bancoImagem).upload(novoNome, img_by)
    print('enviou!')

    # Retorna uma resposta JSON informando que a imagem foi recebida com sucesso
    return jsonify({'message': 'Imagem recebida com sucesso!'})

# Inicia a execução do aplicativo Flask
if __name__ == '__main__':
    app.run()
