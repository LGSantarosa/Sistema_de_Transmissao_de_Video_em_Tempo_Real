import socket
import threading
import time
CANAIS = {
    1: "224.1.1.1",
    2: "224.1.1.2",
    3: "224.1.1.3",
}
PORTA = 5007
PORTA_TCP = 5005
TTL = 2 


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


def servir_lista_canais():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", PORTA_TCP))
    sock.listen()
    print(f"[TCP] Aguardando clientes na porta {PORTA_TCP}...")
    while True:
        conn, endereco = sock.accept()
        lista = "\n".join(f"{k},{v}" for k, v in CANAIS.items()).encode("utf-8")
        conn.sendall(lista)
        conn.close()
        print(f"[TCP] Lista de canais enviada para {endereco[0]}")


def main():
    print("Servidor de streaming iniciado. Canais ativos:", list(CANAIS.keys()))

    threading.Thread(target=servir_lista_canais, daemon=True).start()

    for numero_canal, grupo in CANAIS.items():
        t = threading.Thread(target=transmitir_canal, args=(numero_canal, grupo), daemon=True)
        t.start()

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
