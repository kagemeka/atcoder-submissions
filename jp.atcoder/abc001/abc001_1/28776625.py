import asyncio


async def subtract(lhs: int, rhs: int) -> int:
    return lhs - rhs


async def main() -> None:
    h1 = int(input())
    h2 = int(input())
    print(await subtract(h1, h2))


if __name__ == "__main__":
    asyncio.run(main())
