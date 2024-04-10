from invite_code.aes import AESCipher
from invite_code.exceptions import InvalidInviteCode
from invite_code.schemas import InviteCode, Person


def get_encrypted_invite_code(invite_code: InviteCode) -> str:
    aes_cipher = AESCipher(invite_code.person.model_dump_json())
    return aes_cipher.encrypt(invite_code.model_dump_json())


def validate_invite_code(encrypted_invite_code: str, person: Person) -> InviteCode:
    aes_cipher = AESCipher(person.model_dump_json())
    try:
        data = aes_cipher.decrypt(encrypted_invite_code)
    except:
        raise InvalidInviteCode
    return InviteCode.model_validate_json(data)
