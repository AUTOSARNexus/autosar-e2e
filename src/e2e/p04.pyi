from _typeshed import WriteableBuffer, ReadableBuffer

def e2e_p04_protect(
    data: WriteableBuffer,
    length: int,
    data_id: int,
    *,
    offset: int = 0,
    increment_counter: bool = True,
) -> None: ...
def e2e_p04_check(
    data: ReadableBuffer,
    length: int,
    data_id: int,
    *,
    offset: int = 0,
) -> bool: ...
