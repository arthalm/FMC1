tabela_de_criptografia = {
    11: "A",
    12: "B",
    13: "C",
    14: "D",
    15: "E",
    16: "F",
    17: "G",
    18: "H",
    19: "I",
    21: "J",
    22: "K",
    23: "L",
    24: "M",
    25: "N",
    26: "O",
    27: "P",
    28: "Q",
    29: "R",
    31: "S",
    32: "T",
    33: "U",
    34: "V",
    35: "W",
    36: "X",
    37: "Y",
    38: "Z",
    39: " ",
    41: ".",
    42: ",",
    43: "!",
    44: "?"
}

n = 7663
D = 4013

def modulo(b) : 
    return pow(b, D) % n

message = "7627-1016-3367-535-5449-933-3945-240-971-4361-2812-255-825-3975-1667-1016-4302-4265-248-3326-5532-7031-6356-1"

vetor = message.split("-")
msg_semidecr = "" # mensagem semidescriptografada

for i in vetor:
    msg_semidecr = msg_semidecr + str(modulo(int(i)))

tam = len(msg_semidecr)
msg_desc = "" # mensagem descriptografada

for j in range(0, tam, 2):
    par = msg_semidecr[j:j+2]
    msg_desc = msg_desc + tabela_de_criptografia[int(par)]

print(msg_desc)