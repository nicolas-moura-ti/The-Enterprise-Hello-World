import time
import requests
import psycopg2
import os

def run_orchestrator():
    print("\n🚀 INICIANDO FLUXO DE SINERGIA GLOBAL 'HELLO WORLD'...")
    
    # 1. Auth Step
    print("Step 1: Solicitando autorização ao auth-gate-provider...")
    auth = requests.get("http://auth-gate-provider:9001").json()
    print(f"Status: {auth['status']}")

    # 2. Hello Factory
    print("Step 2: Obtendo string primária do hello-string-factory...")
    hello = requests.get("http://hello-string-factory:9002").json()['value']

    # 3. World Aggregator
    print("Step 3: Obtendo string secundária do world-data-aggregator...")
    world = requests.get("http://world-data-aggregator:9003").json()['value']

    # 4. Database for Punctuation
    print("Step 4: Conectando ao punctuation-relational-db para buscar integridade do '!'...")
    conn = psycopg2.connect(
        host="punctuation-relational-db",
        database="punctuation_db",
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "password_too_weak_for_enterprise")
    )
    cur = conn.cursor()
    cur.execute("SELECT char FROM punctuation WHERE id = 1;")
    punctuation = cur.fetchone()[0]
    cur.close()
    conn.close()

    # 5. Enterprise Latency
    print(f"Step 5: Iniciando Latência Estratégica de 40 segundos (Simulando processamento em Cloud)...")
    for i in range(40, 0, -10):
        print(f"Aguardando... {i}s restantes para conformidade total.")
        time.sleep(10)

    # 6. Final Output (The Overengineered Way)
    final_string = f"{hello} {world}{punctuation}"
    output = {
        "status": "SUCCESS",
        "timestamp": time.time(),
        "payload": f"<message><content>{final_string}</content><anonymized>False</anonymized></message>",
        "metadata": {
            "hops": 15,
            "cost_per_char": "$0.42",
            "compliance": "TOTAL"
        }
    }
    
    print("\n--- OUTPUT FINAL (NÍVEL EXECUTIVO) ---")
    print(output)
    print("--------------------------------------\n")

if __name__ == "__main__":
    # Esperar os outros serviços subirem
    time.sleep(10)
    while True:
        try:
            run_orchestrator()
            break
        except Exception as e:
            print(f"Aguardando infraestrutura... Error: {e}")
            time.sleep(5)
    
    # Manter o container vivo para análise de logs
    print("Fluxo finalizado. Mantendo container ativo para auditoria.")
    while True: time.sleep(100)
