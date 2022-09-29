"""Escreva código capaz de acessar a chave ‘history’ no dicionário abaixo"""


sampleDict = {
   "class":{
  	"student":{
     	"name":"Mike",
     	"marks":{
        	"physics":70,
        	"history":80
     	}
  	}
   }
}

print(sampleDict["class"]["student"]["marks"]["history"])
