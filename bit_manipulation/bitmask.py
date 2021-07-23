class BitMask:
  def get_bit(num: int, index: int) -> int:
    return (num >> index) & 1

  def set_bit(num: int, index: int) -> int:
    return num | (1 << index)

  def clear_bit(num: int, index: int) -> int:
    return num & ~(1 << index)

  def update_bit(num: int, index: int, value: int):
    mask = 1 << index
    return (num | mask) & (value << index)