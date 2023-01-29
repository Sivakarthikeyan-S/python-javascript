from prime import is_prime

def test_prime(n, excepted):
    if is_prime(n) != excepted:
        print(f"ERROR on is_prime({n}), excepted {excepted}")