import socket
import threading
import time

CANAIS = {
    1: "224.1.1.1",
    2: "224.1.1.2",
    3: "224.1.1.3",
}
PORTA = 5007
TTL = 2  # alcance dos pacotes na rede


def transmitir_canal(numero_canal, grupo):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, TTL)

    frame = 1
    while True:
        mensagem = f"FRAME DE VIDEO {frame} do CANAL {numero_canal}"
        sock.sendto(mensagem.encode("utf-8"), (grupo, PORTA))
        print(f"[Canal {numero_canal}] enviado: {mensagem}")
        frame += 1
        time.sleep(1)


def main():
    print("Servidor de streaming iniciado. Canais ativos:", list(CANAIS.keys()))
    for numero_canal, grupo in CANAIS.items():
        t = threading.Thread(target=transmitir_canal, args=(numero_canal, grupo), daemon=True)
        t.start()

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
