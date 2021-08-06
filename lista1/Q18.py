#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade 
#de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo 
#usando este link (em minutos).

dl = float(input("Informe o tamanho do arquivo(em MB): "))
net = int(input("Informe a velocidade da sua internet(em MBs): "))

dlArq = dl*1000
velDl = ((net*1024) / 8)*1000
time=(dlArq/velDl)*1000

min=int(time/60)
sec=time%60

if(sec != 0):
    print("O arquivo sera baixado em %.0f minutos e %.0f segundos"%(min,sec))
else:
    print("O arquivo sera baixado em %.0f minutos")