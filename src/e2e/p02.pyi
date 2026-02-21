from _typeshed import WriteableBuffer, ReadableBuffer

def e2e_p02_protect(
    data: WriteableBuffer,
    length: int,
    data_id_list: bytes,
    *,
    increment_counter: bool = True,
) -> None: ...
def e2e_p02_check(
    data: ReadableBuffer,
    length: int,
    data_id_list: bytes,
) -> bool: ...
