import pytest
from encode_and_decode_strings import Solution
import random
import string

# def test_basic_case():
#     sol = Solution()
#     pytest.fail("Test not implemented yet")


@pytest.fixture()
def codec():
    return Solution()


@pytest.mark.parametrize(
    "strs",
    [
        [],  # empty list
        [""],  # single empty string
        ["", "", ""],  # multiple empty strings
        ["a"],  # single char
        ["hello", "world"],  # basic
        ["hello", "", "world", ""],  # mix empty and non-empty
        [" ", "  ", "\t", "\n"],  # whitespace
        ["#", "##", "###", "a#b#c"],  # delimiter-like chars (even if your scheme uses '#')
        ["1:2", "len:5", ":start", "end:"],  # colon-like chars (even if your scheme uses ':')
        ["\0", "a\0b", "\0\0\0"],  # null bytes inside strings
        ["שלום", "עולם", "יוסף"],  # Hebrew / unicode
        ["🙂", "🙃🙂🙃", "漢字", "e\u0301"],  # emoji + combining marks + CJK
        ["a" * 1000, "b" * 2000],  # long strings
        ["".join(chr(i) for i in range(32, 128))],  # lots of ASCII printable chars
        ["same", "same", "same"],  # duplicates
        ["x", "xy", "xyz", "x" * 10, "x" * 100],  # prefix relationships
    ],
)
def test_roundtrip_cases(codec, strs):
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs


def test_encoded_is_str(codec):
    encoded = codec.encode(["a", "b"])
    assert isinstance(encoded, str)


def test_decode_of_encoded_empty_list(codec):
    encoded = codec.encode([])
    assert codec.decode(encoded) == []


def test_many_strings(codec):
    strs = [f"s{i}" for i in range(10_000)]
    assert codec.decode(codec.encode(strs)) == strs


def test_random_roundtrip(codec):
    # טסט "property-like" עם רנדום דטרמיניסטי כדי לתפוס באגים מוזרים
    rnd = random.Random(1337)

    alphabet = (
        string.ascii_letters
        + string.digits
        + string.punctuation
        + " \t\n"
        + "שלום🙂漢字"
        + "\0"
    )

    for _ in range(200):
        k = rnd.randint(0, 50)  # number of strings
        strs = []
        for _ in range(k):
            n = rnd.randint(0, 200)  # length of each string
            s = "".join(rnd.choice(alphabet) for _ in range(n))
            strs.append(s)

        assert codec.decode(codec.encode(strs)) == strs


def test_encode_decode_idempotent_over_encoded(codec):
    # לוודא ש-encode(decode(encoded)) משמר את התוכן (לא חייב לשמר בדיוק את אותו encoded)
    strs = ["a", "", "b#c", "שלום🙂", "\0x\0"]
    encoded1 = codec.encode(strs)
    decoded = codec.decode(encoded1)
    encoded2 = codec.encode(decoded)
    assert codec.decode(encoded2) == strs
