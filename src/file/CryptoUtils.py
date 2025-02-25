import base64


class CryptoUtils:
    @staticmethod
    def simple_encrypt_decrypt(text: str, key: str) -> str:
        """
        使用 Base64 和 XOR 操作进行简单的加密和解密。
        :param text: 需要加密或解密的文本
        :param key: 作为加密和解密的密钥（字符串）
        :return: 加密后的字符串（或解密后的原始字符串）
        """
        key_bytes = key.encode()
        text_bytes = text.encode()
        encrypted_bytes = bytearray(
            text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes))
        )
        return base64.urlsafe_b64encode(encrypted_bytes).decode()

    @staticmethod
    def decrypt(encrypted_text: str, key: str) -> str:
        """
        解密 Base64 和 XOR 加密的字符串。
        :param encrypted_text: 加密后的字符串
        :param key: 作为解密的密钥（字符串）
        :return: 解密后的原始字符串
        """
        key_bytes = key.encode()
        encrypted_bytes = base64.urlsafe_b64decode(encrypted_text)
        decrypted_bytes = bytearray(
            encrypted_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(encrypted_bytes))
        )
        return decrypted_bytes.decode()


# 示例用法
if __name__ == "__main__":
    key = "mysecretkey"  # 选择一个密钥
    original_text = "HelloWorld"

    encrypted_text = CryptoUtils.simple_encrypt_decrypt(original_text, key)
    decrypted_text = CryptoUtils.decrypt(encrypted_text, key)

    print(f"原文本: {original_text}")
    print(f"加密后: {encrypted_text}")
    print(f"解密后: {decrypted_text}")  # 应该与原文本相同
