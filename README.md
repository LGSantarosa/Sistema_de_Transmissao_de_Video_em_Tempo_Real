# Sistema de Transmissão de Vídeo em Tempo Real

Disciplina: CSC — Avaliação Somativa 2

Integrantes: Carla Ferraz de Araujo, Gabriella Tavares Pedroso, Luiz Gustavo Santarosa

## Descrição
Servidor que transmite "vídeo ao vivo" (frames simulados em texto) para múltiplos
clientes via **Multicast sobre UDP**. Cada canal possui um endereço de grupo
multicast e o servidor envia um pacote por frame, uma única vez, independente do
número de espectadores.

- Protocolo de transporte: **UDP**
- Modelo de comunicação: **Multicast**
- Bibliotecas: `socket`, `threading`, `time`, `struct`

## Como executar

1. Inicie o servidor:
   ```
   python3 servidor.py
   ```

2. Em outro terminal, inicie um cliente e escolha o canal (1, 2 ou 3):
   ```
   python3 cliente.py
   ```

3. Abra vários clientes (em terminais diferentes) para testar a recepção
   simultânea. Clientes no mesmo canal recebem os mesmos frames sincronizados.

## Canais
| Canal | Endereço Multicast | Porta |
|-------|--------------------|-------|
| 1     | 224.1.1.1          | 5007  |
| 2     | 224.1.1.2          | 5007  |
| 3     | 224.1.1.3          | 5007  |
