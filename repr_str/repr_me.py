class NTorrent(object):
    def __init__(self, tool_id, path) -> None:
        # type: (int, str) -> None
        self.tool_id = tool_id
        self.path = path


def main():
    ntorrents = [
        NTorrent(287, "/nino"),
        NTorrent(89, "/products"),
        NTorrent(342, "/pasten"),
    ]

    # print with str (print calls str by default)
    for n in ntorrents:
        print(n)

    # print with repr
    for n in ntorrents:
        print(repr(n))


if __name__ == "__main__":
    main()
