import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# channel.queue_declare(queue='fila')

run = True
nome = input("Qual o seu nome? ")

print("Digite algo... CTRL+C para sair!")
while(run):
    body = str(input("> "))
    channel.basic_publish(exchange='', routing_key='t', body='> '+'['+nome+']: '+body)
    print(".")

connection.close()
