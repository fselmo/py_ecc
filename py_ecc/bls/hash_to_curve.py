from typing import List
from py_ecc.fields import (
    optimized_bls12_381_FQ2 as FQ2,
)
from py_ecc.optimized_bls12_381 import (
    add,
    iso_map_G2,
    field_modulus,
    multiply_clear_cofactor_G2,
    optimized_swu_G2,
)

from .constants import HASH_TO_FIELD_L
from .hash import expand_message_xmd
from .typing import G2Uncompressed


# Hash to G2
def hash_to_G2(message: bytes, DST: bytes) -> G2Uncompressed:
    """
    Convert a message to a point on G2 as defined here:
    https://tools.ietf.org/html/draft-irtf-cfrg-hash-to-curve-05#section-3

    Contants and inputs follow the ciphersuite ``BLS12381G2-SHA256-SSWU-RO-`` defined here:
    https://tools.ietf.org/html/draft-irtf-cfrg-hash-to-curve-05#section-8.9.2
    """
    u0, u1 = hash_to_field_FQ2(message, 2, DST)
    q0 = map_to_curve_G2(u0)
    q1 = map_to_curve_G2(u1)
    r = add(q0, q1)
    p = clear_cofactor_G2(r)
    return p


def hash_to_field_FQ2(message: bytes, count: int, DST: bytes) -> List[FQ2]:
    """
    Hash To Base Field for FQ2

    Convert a message to a point in the finite field as defined here:
    https://tools.ietf.org/html/draft-irtf-cfrg-hash-to-curve-05#section-5
    """
    M = 2  # m is the extension degree of FQ2
    len_in_bytes = count * M * HASH_TO_FIELD_L
    pseudo_random_bytes = expand_message_xmd(message, DST, len_in_bytes)
    u = []
    for i in range(0, count):
        e: List[int] = []
        for j in range(0, M):
            elem_offset = HASH_TO_FIELD_L * (j + i * M)
            tv = pseudo_random_bytes[elem_offset: elem_offset + HASH_TO_FIELD_L]
            e.append(int.from_bytes(tv, 'big') % field_modulus)
        u.append(FQ2(e))

    return u


def map_to_curve_G2(u: FQ2) -> G2Uncompressed:
    """
    Map To Curve for G2

    First, convert FQ2 point to a point on the 3-Isogeny curve.
    SWU Map: https://tools.ietf.org/html/draft-irtf-cfrg-hash-to-curve-05#section-6.6.2

    Second, map 3-Isogeny curve to BLS12-381-G2 curve.
    3-Isogeny Map: https://tools.ietf.org/html/draft-irtf-cfrg-hash-to-curve-05#appendix-C.3
    """
    (x, y, z) = optimized_swu_G2(u)
    return iso_map_G2(x, y, z)


def clear_cofactor_G2(p: G2Uncompressed) -> G2Uncompressed:
    """
    Clear Cofactor via Multiplication

    Ensure a point falls in the correct sub group of the curve.
    """
    return multiply_clear_cofactor_G2(p)
