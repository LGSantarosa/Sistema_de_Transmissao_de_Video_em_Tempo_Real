import socket
import struct
PORTA = 5007
PORTA_TCP = 5005
IP_SERVIDOR = "127.0.0.1"


def buscar_canais():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_SERVIDOR, PORTA_TCP))
    dados = b""
    while True:
        parte = sock.recv(1024)
        if not parte:
            break
        dados += parte
    sock.close()
    canais = {}
    for linha in dados.decode("utf-8").splitlines():
        k, v = linha.split(",")
        canais[int(k)] = v
    return canais


def main():
    canais = buscar_canais()
    print("Canais disponiveis:", list(canais.keys()))
    canal = int(input("Escolha o canal que deseja assistir: "))
    grupo = canais[canal]

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((grupo, PORTA))

    grupo_bin = socket.inet_aton(grupo)
    mreq = struct.pack("4sL", grupo_bin, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print(f"Assistindo o CANAL {canal} ({grupo}). Aguardando frames...\n")
    while True:
        dados, _ = sock.recvfrom(1024)
        print(dados.decode("utf-8"))


if __name__ == "__main__":
    main()
