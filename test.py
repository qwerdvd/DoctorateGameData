from constants import Excel


async def test():
    await Excel.preload_table()


if __name__ == "__main__":
    import asyncio

    asyncio.run(test())
