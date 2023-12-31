// Este código conecta ao kafka, e produz uma mensagem com data e hora no tópico.

const kafka_broker = 'broker1:9092';
const kafka_topic = 'meu.topico.aqui';
const message = 'Mensagem enviada do kafkajs em ' + new Date().toLocaleString('pt-br', {
    hour12: false,
    timeZone: 'America/Sao_Paulo'
});

const { Kafka } = require('kafkajs');

(async () => {

    const kafka = new Kafka({
        clientId: 'my-app',
        brokers: [kafka_broker]
    });

    const producer = kafka.producer();

    await producer.connect();

    await producer.send({
        topic: kafka_topic,
        messages: [
            { value: message },
        ],
    });

    await producer.disconnect();

})()
