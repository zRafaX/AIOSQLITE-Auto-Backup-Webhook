# AIOSQLITE Auto Backup Webhook

Este projeto permite realizar backups automáticos do seu banco de dados `aiosqlite` para uma webhook. É uma solução simples e eficiente para garantir que seus dados estejam sempre seguros em backups externos.

## Funcionalidades

- Backup automático do banco de dados `aiosqlite`.
- Envio do backup para uma URL de webhook especificada.
- Configuração simples por meio de um arquivo `.env`.

## Estrutura do Projeto

- `backup.py`: O script principal que realiza o backup e envia os dados para a webhook.
- `exemplo.env`: Um exemplo de arquivo de configuração com as variáveis necessárias.

## Como Usar

### 1. Clone o Repositório

```bash
git clone https://github.com/seuusuario/aiosqlite-auto-backup-webhook.git
```

### 2. Instale as Dependências

Certifique-se de que você tem o Python instalado e execute:

```bash
pip install -r requirements.txt
```

### 3. Configure o Arquivo `.env`

Renomeie o arquivo `exemplo.env` para `.env` e preencha as informações:

```env
WEBHOOK= https://sua-webhook.url
```

- **WEBHOOK**: URL da webhook para onde o backup será enviado.

### 4. Execute o Script

Inicie o processo de backup:

```bash
python backup.py
```

O script irá compactar o banco de dados e enviar o arquivo para a URL configurada no `.env`.

## Exemplo de Configuração

O arquivo `exemplo.env` mostra um exemplo de como configurar as variáveis necessárias:

```env
WEBHOOK= https://example.com/webhook
```

## Contribuindo

Contribuições são bem-vindas! Se você tiver sugestões ou encontrar problemas, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
