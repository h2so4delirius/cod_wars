class VigenereCipher(object):
    def __init__(self, key :str, alphabet :str):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text :str):
        res, num = "", 0
        for i in text:
            num_res = -1
            for j in range(0, len(self.alphabet)):
                if self.key[num] == self.alphabet[j]:
                    num_res_cop = j                    
                    for k in range(0, len(self.alphabet)):
                        if self.alphabet[k] == i:
                            num_res = num_res_cop + k
                            break
                    break
            num += 1
            if num == len(self.key):
                num = 0
            #print(num_res)
            if num_res == -1:
                res += i
            else:
                #print(num_res," ",i)
                res += self.alphabet[num_res%len(self.alphabet)]
        return res
                
    
    def decode(self, text :str):
        res, num = "", 0
        for i in text:
            num_res = -1
            for j in range(0, len(self.alphabet)):
                if self.key[num] == self.alphabet[j]:
                    num_res_cop = j                    
                    for k in range(0, len(self.alphabet)):
                        if self.alphabet[k] == i:
                            num_res = num_res_cop + k
                            break
                    break
            num += 1
            if num == len(self.key):
                num = 0
            #print(num_res)
            if num_res == -1:
                res += i
            else:
                #print(num_res," ",i)
                res += self.alphabet[num_res%len(self.alphabet)]
        return res



abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

print(c.encode('codewars'))
print(c.decode('rovwsoiv'))