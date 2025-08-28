class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for letra in strs:
            encoded += str(len(letra)) + "#" + letra
        return encoded
            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 1. Encontra o separador #
            j = i
            while s[j] != "#":
                j += 1
            tamanho = int(s[i:j])      # número antes do #
            # 2. Pega a substring com base no tamanho
            palavra = s[j+1 : j+1+tamanho]
            res.append(palavra)
            # 3. Atualiza índice para próxima leitura
            i = j + 1 + tamanho
        return res
