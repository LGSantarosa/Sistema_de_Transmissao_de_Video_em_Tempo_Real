import socket
import struct

CANAIS = {
    1: "224.1.1.1",
    2: "224.1.1.2",
    3: "224.1.1.3",
}
PORTA = 5007


def main():
    print("Canais disponiveis:", list(CANAIS.keys()))
    canal = int(input("Escolha o canal que deseja assistir: "))
    grupo = CANAIS[canal]

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
