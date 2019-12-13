import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()


fila = ''

escolher = True
while(escolher):
    res = raw_input("Ver mensagens do grupo Pessoal [p] ou do Trabalho [t] ? ")
    if(res == 't'):
        escolher = False
        fila = res
    elif(res == 'p'):
        escolher = False
        fila = res

channel.queue_declare(queue = fila)

def callback(ch, method, properties, body):
    print(body)

channel.basic_consume(
    queue=fila, on_message_callback=callback, auto_ack=True)

print(' Esperando ... CTRL+C para sair!')
channel.start_consuming()
