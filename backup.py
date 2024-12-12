import requests
import shutil
import os
import tempfile
from datetime import datetime
import time

def send_backup_to_webhook(backup_path):
    webhook_url = os.getenv('WEBHOOK')

    restart_message = {
        'content': '🔄️ Backup:',
        'username': 'Backup'
    }

    files = {'file': (f'MINHA_DATABASE_{datetime.now().strftime("%Y%m%d%H%M%S")}.zip', open(backup_path, 'rb'))}

    response = requests.post(webhook_url, data=restart_message, files=files)

    if response.status_code == 200:
        print('✅ Backup enviado!')
    else:
        print(f'Erro ao enviar o backup. Código de status: {response.status_code}')

def create_backup():
    # Defina o caminho da pasta que você deseja fazer backup
    folder_path = './'

    # Crie um nome de arquivo para o backup com base na data e hora
    backup_filename = f'MINHA_DATABASE_{datetime.now().strftime("%Y%m%d%H%M%S")}.zip'

    # Caminho completo para a pasta de backup
    backup_folder_path = './Backup'

    # Remova a pasta de backup existente, se existir
    if os.path.exists(backup_folder_path):
        shutil.rmtree(backup_folder_path)

    # Crie um diretório temporário para armazenar os arquivos de backup
    temp_dir = tempfile.mkdtemp()

    # Copie todo o conteúdo do diretório principal para o diretório temporário, excluindo as pastas a serem ignoradas
    for root, dirs, files in os.walk(folder_path, topdown=True):
        # Ignorar as pastas .cache e .local
        dirs[:] = [d for d in dirs if d not in ['.cache', '.local']]

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(temp_dir, os.path.relpath(src_file, folder_path))
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            shutil.copy2(src_file, dest_file)

    # Crie o arquivo de backup .zip
    backup_path = os.path.join(backup_folder_path, backup_filename)
    shutil.make_archive(backup_path[:-4], 'zip', temp_dir)

    # Remova o diretório temporário
    shutil.rmtree(temp_dir)

    return backup_path

if __name__ == '__main__':
    while True:
        backup_path = create_backup()
        send_backup_to_webhook(backup_path)
        time.sleep(3600)  # Aguarde 3600 segundos antes de fazer o próximo backup
