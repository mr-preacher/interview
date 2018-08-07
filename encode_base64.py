class Base64Transformer:
    dictionary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o',
                  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '+', '/']

    # 1 byte is 8 bit, base64 code is 6 bit
    @staticmethod
    def get_symbol(val):
        return Base64Transformer.dictionary[val]

    def encode(self, arr):
        result = []

        for j in range(0, int(len(arr) / 3)):
            offset = 3 * j
            result.append(self.get_symbol(ord(arr[offset]) >> 2))
            result.append(self.get_symbol((ord(arr[offset]) & 3) << 4 | ord(arr[offset + 1]) >> 4))
            result.append(self.get_symbol((ord(arr[offset + 1]) & 15) << 2 | ord(arr[offset + 2]) >> 6))
            result.append(self.get_symbol(ord(arr[offset + 2]) & 63))

        offset = len(arr) - len(arr) % 3
        if len(arr) % 3 == 2:
            result.append(self.get_symbol(ord(arr[offset]) >> 2))
            result.append(self.get_symbol((ord(arr[offset]) & 3) << 4 | ord(arr[offset + 1]) >> 4))
            result.append(self.get_symbol((ord(arr[offset + 1]) & 15) << 2))
            result.append("=")
        elif len(arr) % 3 == 1:
            result.append(self.get_symbol(ord(arr[offset]) >> 2))
            result.append(self.get_symbol((ord(arr[offset]) & 3) << 4))
            result.append("==")
        return result


o = Base64Transformer()

print(o.encode(['M', 'a', 'n']))
print(o.encode(['M', 'a']))
print(o.encode(['M']))
