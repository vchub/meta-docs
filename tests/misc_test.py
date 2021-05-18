from dataclasses import dataclass

# from src.main import Headers, Mail


def test_dataclass():
    @dataclass
    class B:
        x: int
        y: int = None

        def to_dict(self):
            return {k: v for k, v in self.__dict__.items() if v is not None}

    a = B(1, 2)
    assert a.__dict__ == {"x": 1, "y": 2}
    a = B(y=2, x=1)
    assert a.__dict__ == {"x": 1, "y": 2}
    a = B(x=1)
    assert a.__dict__ == {"x": 1, "y": None}
    assert a.to_dict() == {"x": 1}

    b = B(**a.to_dict())
    assert b.x == 1 and b.y is None
