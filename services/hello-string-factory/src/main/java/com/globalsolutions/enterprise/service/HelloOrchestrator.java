package com.globalsolutions.enterprise.service;

import com.globalsolutions.enterprise.grpc.WorldServiceGrpc;
import com.globalsolutions.enterprise.kafka.Producer;
import com.globalsolutions.enterprise.repository.PunctuationRepository;
import org.springframework.stereotype.Service;

/**
 * OrchestratorService: Realiza a junção complexa de strings através de uma malha
 * de microserviços para garantir que o "Hello World" não seja simples demais.
 */
@Service
public class HelloOrchestrator {

    private final Producer kafkaProducer;
    private final PunctuationRepository db;

    public String executeEnterpriseWorkflow() {
        // 1. Chamada gRPC para o World Data Aggregator (Go)
        String world = WorldServiceGrpc.newBlockingStub(channel).fetchWorld(Empty.newBuilder().build()).getValue();

        // 2. Verifica permissão no PostgreSQL (para o caractere !)
        String punctuation = db.findById(1L).getChar();

        // 3. Envia evento para o Kafka informando que uma concatenação está em progresso
        kafkaProducer.send("concatenation-events", "Status: Iniciando fusão atômica de strings");

        // 4. Espera um callback simulado via sidecar
        simulateEnterpriseLatency(40000); 

        // 5. Retorna a string em formato XML dentro de um JSON para máximo overhead
        return String.format(
            "{ \"status\": \"SUCCESS\", \"payload\": \"<message><content>Hello %s%s</content></message>\" }",
            world,
            punctuation
        );
    }

    private void simulateEnterpriseLatency(int ms) {
        try { Thread.sleep(ms); } catch (InterruptedException e) { /* Ignored by Corporate Policy */ }
    }
}
