from funcnodes_bt100_3j.controller import BT100_3J
import asyncio


async def testmain():
    bt100 = BT100_3J()
    # bt100.connect()
    await bt100.set_rpm(80)
    await bt100.set_dir(bt100.COUNTERCLOCKWISE)
    await bt100.start()
    await asyncio.sleep(5)
    # for i in range(2):
    #     await bt100.set_state(
    #         rpm=i * 10 + 50,
    #         dir=bt100.CLOCKWISE if i % 2 == 0 else bt100.COUNTERCLOCKWISE,
    #     )

    # # await bt100._get_pump_state()

    # for i in range(5):
    #     await bt100.stop()
    #     await bt100.start()
    await bt100.stop()
    bt100.disconnect()


if __name__ == "__main__":
    asyncio.run(testmain())
